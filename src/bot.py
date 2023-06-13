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
    auth_token_input,
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
    account_token_input,
    account_update_button,
    account_name_input,
    account_name_invalid,
    account_name_update_success,
    account_name_button,
    account_view,
    account_embed,
)

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

        auth_token_input.on_submit = MethodType(on_login, auth_token_input)

        # opens the token modal
        async def auth_token_modal(interaction: Interaction):
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

        account_token_input.on_submit = MethodType(on_update, account_token_input)

        # opens token modal for sync
        async def account_token_modal(interaction: Interaction):
            await interaction.response.send_modal(account_token_input)

        account_update_button.callback = account_token_modal

        # renames the user on the server
        async def on_rename(input: AccountNameInput, interaction: Interaction):
            await update_name(str(input.name), interaction)

        account_name_input.on_submit = MethodType(on_rename, account_name_input)

        # opens name modal for new name
        async def account_name_modal(interaction: Interaction):
            await interaction.response.send_modal(account_name_input)

        account_name_button.callback = account_name_modal

        await message.edit(content="", embed=account_embed, view=account_view())

    async def voice(self, member: Member, before: VoiceState, after: VoiceState):
        create = utils.get(member.guild.voice_channels, name="create")
        category = utils.get(member.guild.categories, name="voice")

        # user joined #create
        if before.channel != after.channel and after.channel == create:
            # create channel with permissions
            channel = await member.guild.create_voice_channel(
                name=f"{member.display_name}",
                overwrites={
                    member: PermissionOverwrite(
                        manage_channels=True
                    ),
                    utils.get(
                        member.guild.roles, name="@everyone"
                    ) : PermissionOverwrite(
                        view_channel=False,
                    ),
                    utils.get(
                        member.guild.roles, name="Authenticated"
                    ): PermissionOverwrite(
                        add_reactions=True,
                        attach_files=True,
                        connect=True,
                        embed_links=True,
                        external_emoji=True,
                        external_stickers=True,
                        read_message_history=True,
                        read_message=True,
                        send_message=True,
                        speak=True,
                        stream=True,
                        view_channel=True,
                    ),
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
            and before.channel.name != "create"
        ):
            # delete empty channels except #create
            await before.channel.delete()

    async def channels(self):
        pass


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
    matches = re.findall(r"^\[[a-z0-9]+\]", interaction.user.nick)
    if len(matches) != 1:
        await send_response_message(account_name_invalid)
        return
    try:
        await interaction.user.edit(nick=f"{matches[0]} {name}")
    except Forbidden:
        # user is server owner
        pass
    await send_response_message(account_name_update_success)


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
