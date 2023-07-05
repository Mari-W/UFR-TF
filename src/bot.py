from multiprocessing import Manager
from random import randint
import re
from types import MethodType
from typing import Any
from discord import (
    Client,
    Colour,
    Forbidden,
    Intents,
    Interaction,
    InteractionResponse,
    Member,
    Message,
    NotFound,
    PermissionOverwrite,
    Role,
    TextChannel,
    VoiceState,
    utils,
)

from .data import degrees
from .ui import (
    about_embed,
    AuthTokenInput,
    auth_token_button,
    auth_view,
    auth_embed,
    auth_logout_success,
    auth_login_success,
    auth_login_failure,
    AccountTokenInput,
    AccountNameInput,
    account_logout_button,
    account_update_success,
    account_update_button,
    account_name_invalid,
    account_name_update_success,
    account_name_button,
    account_view,
    account_embed,
    ChannelRequestInput,
    channels_request_button,
    channel_request_send,
    channel_view,
    channel_embed,
    ChannelRequestAcceptInput,
    create_channel_request_accept_embed,
    accept_channel_request_send,
    accept_channel_send,
    ChannelRequestDeclineInput,
    decline_channel_send
)
from .env import env

# thread shared state between fastapi and discord bot
state = Manager().dict()

## Bot ##################################################################################


class Bot(Client):
    def __init__(self, **options) -> None:
        # get admin permissions
        intents = Intents.all()
        super().__init__(intents=intents, **options)

    async def on_ready(self):
        # create #about message
        await self.about()
        # create #authenticate message
        await self.authenticate()
        # create #accounts message
        await self.account()
        # create #channels message
        await self.channels()

    async def about(self):
        # get about channel
        message = await last_channel_message(channel_by_name(self, "about"))
        # update message
        await message.edit(content="", embed=about_embed)

    async def authenticate(self):
        # get authenticate channel
        message = await last_channel_message(channel_by_name(self, "authenticate"))

        # try logging in on token input
        async def on_login(input: AuthTokenInput, interaction: Interaction):
            await login(str(input.token), interaction)

        # opens the token modal
        async def auth_token_modal(interaction: Interaction):
            auth_token_input = AuthTokenInput()
            auth_token_input.on_submit = MethodType(on_login, auth_token_input)
            await interaction.response.send_modal(auth_token_input)

        auth_token_button.callback = auth_token_modal

        await message.edit(content="", embed=auth_embed, view=auth_view())

    async def account(self):
        message = await last_channel_message(channel_by_name(self, "account"))

        account_logout_button.callback = logout

        # try logging out and in on token input
        async def on_update(input: AccountTokenInput, interaction: Interaction):
            if await logout(interaction, message=False) and await login(
                str(input.token), interaction, message=False
            ):
                await send_response_message(
                    interaction.response, account_update_success
                )

        # opens token modal for sync
        async def account_token_modal(interaction: Interaction):
            account_token_input = AccountTokenInput()
            account_token_input.on_submit = MethodType(on_update, account_token_input)
            await interaction.response.send_modal(account_token_input)

        account_update_button.callback = account_token_modal

        # renames the user on the server
        async def on_rename(input: AccountNameInput, interaction: Interaction):
            await update_name(input.name.value, interaction)

        # opens name modal for new name
        async def account_name_modal(interaction: Interaction):
            account_name_input = AccountNameInput()
            account_name_input.on_submit = MethodType(on_rename, account_name_input)
            await interaction.response.send_modal(account_name_input)

        account_name_button.callback = account_name_modal

        await message.edit(content="", embed=account_embed, view=account_view())

    async def channels(self):
        # get channels channel
        message = await last_channel_message(channel_by_name(self, "channels"))

        # opens the request modal
        async def channel_request_modal(interaction: Interaction):
            channel_request_input = ChannelRequestInput()
            channel_request_input.on_submit = MethodType(on_request, channel_request_input)
            await interaction.response.send_modal(channel_request_input)

        # sends the rquest to admin channel
        async def on_request(input: ChannelRequestInput, interaction: Interaction):
            await forward_request(input, interaction)

        channels_request_button.callback = channel_request_modal

        await message.edit(content="", embed=channel_embed, view=channel_view())

    async def voice(self, member: Member, before: VoiceState, after: VoiceState):
        create = utils.get(member.guild.voice_channels, name="create")
        category = utils.get(member.guild.categories, name="voice")

        # user joined #create
        if before.channel != after.channel and after.channel == create:
            # create channel with permissions
            channel = await member.guild.create_voice_channel(
                name=f"{member.display_name}",
                overwrites={
                    utils.get(
                        member.guild.roles, name="@everyone"
                    ): PermissionOverwrite(
                        view_channel=False,
                    ),
                    utils.get(
                        member.guild.roles, name="Authenticated"
                    ): PermissionOverwrite(
                        add_reactions=True,
                        attach_files=True,
                        connect=True,
                        create_instant_invite=True,
                        create_public_threads=True,
                        embed_links=True,
                        external_emojis=True,
                        external_stickers=True,
                        read_message_history=True,
                        read_messages=True,
                        send_messages=True,
                        send_messages_in_threads=True,
                        send_voice_messages=True,
                        speak=True,
                        stream=True,
                        use_application_commands=True,
                        use_embedded_activities=True,
                        use_external_emojis=True,
                        use_external_sounds=True,
                        use_external_stickers=True,
                        use_soundboard=True,
                        use_voice_activation=True,
                    ),
                    member: PermissionOverwrite(manage_channels=True),
                },
                category=category,
                position=1,
            )
            # move user to channel
            await member.move_to(channel)
        if (
            before.channel != after.channel
            and before.channel.category == category
            and not before.channel.members
            and before.channel.id != int(env.create_voice_channel_id)
        ):
            # delete empty channels except #create
            await before.channel.delete()


## Functionality ########################################################################


async def login(token: str, interaction: Interaction, message=True) -> bool:
    # token is valid
    if token in state:
        # get user information
        user = state[token]

        # assign according roles
        studies = (
            degrees.get(user["studies"], user["studies"])
            if user["studies"] is not None
            else "Employee"
        )

        await interaction.user.add_roles(
            utils.get(interaction.guild.roles, name="Authenticated"),
            await get_or_create_role(interaction.guild, studies),
        )

        # remove account from name before
        name = re.sub(r"^\[[a-z0-9]+\]", "", interaction.user.display_name)
        try:
            await interaction.user.edit(nick=f"[{user['sub']}] {name}")
        except Forbidden:
            # user is server owner
            pass

        # send success message
        if message:
            await send_response_message(interaction.response, auth_login_success)
        return True

    # token is invalid
    else:
        # send failure message
        await send_response_message(interaction.response, auth_login_failure)
        return False


async def logout(interaction: Interaction, message=True) -> bool:
    # get all roles to remove
    roles = list(
        filter(
            lambda role: role.name != "Admin" and role.name != "@everyone",
            interaction.user.roles,
        )
    )

    await interaction.user.remove_roles(*roles)

    # reset username
    try:
        await interaction.user.edit(nick=None)
    except Forbidden:
        # user is server owner
        pass

    if message:
        await send_response_message(interaction.response, auth_logout_success)
    return True


async def update_name(name: str, interaction: Interaction):
    matches = re.findall(r"^\[[a-z0-9]+\]", str(interaction.user.nick))
    if len(matches) != 1:
        await send_response_message(interaction.response, account_name_invalid)
    else:
        try:
            await interaction.user.edit(nick=f"{matches[0]} {name}")
        except Forbidden:
            # user is server owner
            pass
        await send_response_message(interaction.response, account_name_update_success)


async def forward_request(input: ChannelRequestInput, request_interaction: Interaction):
    async def on_accept(channel_request_accept_input: ChannelRequestAcceptInput, accept_interaction: Interaction):
        await accept_interaction.user.guild.create_text_channel(
            name=channel_request_accept_input.name_of_channel.value,
            overwrites={
                utils.get(
                    accept_interaction.user.guild.roles, name="@everyone"
                ): PermissionOverwrite(
                    view_channel=False,
                ),
                utils.get(
                    accept_interaction.user.guild.roles, name="Authenticated"
                ): PermissionOverwrite(
                    add_reactions=True,
                    attach_files=True,
                    create_instant_invite=True,
                    create_public_threads=True,
                    embed_links=True,
                    external_emojis=True,
                    external_stickers=True,
                    read_message_history=True,
                    read_messages=True,
                    send_messages=True,
                    send_messages_in_threads=True,
                    send_voice_messages=True,
                    use_application_commands=True,
                    use_embedded_activities=True,
                    use_external_emojis=True,
                    use_external_stickers=True
                )
            },
            category=utils.get(accept_interaction.user.guild.categories, name="channels"),
            topic=f"**[{channel_request_accept_input.kind_of_lecture}]**{channel_request_accept_input.name_of_lecture}"
        )

        await request_interaction.user.send(f"Your channel request for {channel_request_accept_input.name_of_channel} is accepted")

        await accept_interaction.message.edit(view=None)
        await send_response_message(accept_interaction.response, accept_channel_send)
        
    async def on_decline(channel_request_decline_input: ChannelRequestDeclineInput, decline_interaction: Interaction):

        decline_message = channel_request_decline_input.declined_massage.value
        await request_interaction.user.send(decline_message)

        await decline_interaction.message.edit(view=None)
        await send_response_message(decline_interaction.response, decline_channel_send)

    view, embed = create_channel_request_accept_embed(input, request_interaction, on_accept, on_decline)

    channel = utils.get(request_interaction.user.guild.channels, name="accept")
    await channel.send(embed=embed, view=view)

    await send_response_message(request_interaction.response, accept_channel_request_send)


## Utils ################################################################################


async def get_or_create_role(guild: Any, name: str) -> Role:
    role = utils.get(guild.roles, name=name)
    if role is None:
        role = await guild.create_role(
            name=name,
            colour=Colour.from_rgb(randint(0, 255), randint(0, 255), randint(0, 255)),
            hoist=True,
        )
        await role.edit(position=2)

    return role


async def send_response_message(response: InteractionResponse, message: str):
    await response.send_message(message, ephemeral=True, delete_after=10)


async def last_channel_message(channel: TextChannel) -> Message:
    try:
        message = await channel.fetch_message(channel.last_message_id)
    except NotFound:
        message = await channel.send(content="...", silent=True)
    return message


def channel_by_name(bot: Bot, name: str, category: str | None = None):
    def find(channel: TextChannel) -> bool:
        return channel.name == name and (
            category == None or channel.category.name == category
        )

    return utils.find(find, bot.guilds[0].text_channels)
