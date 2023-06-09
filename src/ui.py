from datetime import datetime
from typing import Callable
from discord import ButtonStyle, Colour, Embed, Interaction
from discord.ui import View, Button, Modal, TextInput

from types import MethodType

from .env import env

## #about ###############################################################################

about_embed_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."
about_embed_auth = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."
about_embed_rules = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."

about_embed = Embed(
    type="rich",
    title="About this Discord Server",
    colour=Colour.blurple(),
    timestamp=datetime.now(),
    description=about_embed_description,
)

about_embed.add_field(name="Authentication", value=about_embed_auth, inline=False)
about_embed.add_field(name="Rules", value=about_embed_rules, inline=False)

## #auth ###############################################################################

auth_login_success = "Login successful."
auth_login_failure = "Invalid Token. A token is valid only for 5 Minutes. You might want to generate a new token by reloading the website."
auth_logout_success = "Logout successful."

auth_embed_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."
auth_embed_get_token = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."
auth_embed_enter_token = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."


class AuthTokenInput(Modal, title="Enter Authentication Token"):
    token = TextInput(label="Token", placeholder="Authentication Token")


auth_token_button = Button(label="Enter Auth Token", style=ButtonStyle.primary)
auth_link_button = Button(label="Get Auth Token", url=env.url + "token")
auth_view = (
    lambda: View(timeout=None).add_item(auth_link_button).add_item(auth_token_button)
)

auth_embed = Embed(
    type="rich",
    title="Authenticate using University Account",
    url=env.url + "token",
    colour=Colour.blurple(),
    timestamp=datetime.now(),
    description=auth_embed_description,
)

auth_embed.add_field(name="Get Token", value=auth_embed_get_token, inline=False)
auth_embed.add_field(name="Enter Token", value=auth_embed_enter_token, inline=False)
auth_embed.set_footer(text="Powered by Laurel")

## #account #############################################################################

account_update_success = "Sync successful."
account_name_invalid = "Your name does not follow the naming guidelines. Please contact a server administrator."
account_name_update_success = "Name update successful."
account_embed_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."
account_embed_disconnect = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."
account_embed_sync = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."
account_embed_name = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."


class AccountTokenInput(Modal, title="Enter Authentication Token"):
    token = TextInput(label="Token", placeholder="Paste Authentication Token Here")


class AccountNameInput(Modal, title="Change Nickname"):
    name = TextInput(label="New Nickname")


account_logout_button = Button(label="Disconnect", style=ButtonStyle.danger)
account_name_button = Button(label="Update Nickname", style=ButtonStyle.secondary)
account_token_button = Button(label="Get Sync Token", url=env.url + "token")
account_update_button = Button(label="Enter Sync Token", style=ButtonStyle.primary)

account_view = lambda: (
    View(timeout=None)
    .add_item(account_logout_button)
    .add_item(account_token_button)
    .add_item(account_update_button)
    .add_item(account_name_button)
)

account_embed = Embed(
    type="rich",
    title="Manage Your Connected Account",
    colour=Colour.blurple(),
    timestamp=datetime.now(),
    description=account_embed_description,
)

account_embed.add_field(
    name="1. Disconnect University Account",
    value=account_embed_disconnect,
    inline=False,
)
account_embed.add_field(
    name="2. Sync University Account",
    value=account_embed_sync,
    inline=False,
)
account_embed.add_field(
    name="3. Sync Discord Name",
    value=account_embed_name,
    inline=False,
)
account_embed.set_footer(text="Powered by Laurel")

## #channels #############################################################################

channel_request_send = "Request sent successfully"
channel_request_accepted = (
    lambda channel: f"Your channel request for {channel} was accepted."
)


channels_embed_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."


class ChannelRequestInput(Modal, title="Text Channel Request"):
    name_of_lecture = TextInput(label="Name of Lecture", placeholder="eg. SAT solving")
    kind_of_event = TextInput(
        label="Kind of Event", placeholder="Lecture / Seminar / BOK / Lab / ..."
    )
    name_of_channel = TextInput(
        label="Suggested Name of Channel", placeholder="eg. sat-solving", required=False
    )


class OffTopicChannelRequestInput(Modal, title="Offtopic Channel Request"):
    name_of_channel = TextInput(label="Name of Channel", placeholder="Volleyball")
    description = TextInput(
        label="Description",
        placeholder="A place to find people for playing volleyball",
    )


channels_request_button = Button(label="Request Channel", style=ButtonStyle.danger)
offtopic_request_button = Button(
    label="Request Offtopic Channel", style=ButtonStyle.blurple
)

channel_view = lambda: (
    View(timeout=None)
    .add_item(channels_request_button)
    .add_item(offtopic_request_button)
)

channel_embed = Embed(
    type="rich",
    title="Request a Text Channel",
    colour=Colour.blurple(),
    timestamp=datetime.now(),
    description=channels_embed_description,
)

channel_embed.set_footer(text="Powered by Laurel")

## #accept channels #############################################################################

accept_channel_send = "Accepted channel request"
decline_channel_send = "Declined channel request"

accept_channel_request_send = "Request submitted"


class ChannelRequestAcceptInput(Modal, title="Accept Text Channel Request"):
    name_of_lecture = TextInput(label="Name of Lecture")
    kind_of_event = TextInput(label="Kind of Event")
    name_of_channel = TextInput(label="Name of Channel")


class ChannelRequestDeclineInput(Modal, title="Decline Text Channel Request"):
    declined_massage = TextInput(label="Reason")


def create_channel_request_accept_embed(
    input: ChannelRequestInput,
    interaction: Interaction,
    on_accept: Callable[[ChannelRequestAcceptInput, Interaction], None],
    on_decline: Callable[[ChannelRequestDeclineInput, Interaction], None],
) -> tuple[View, Embed]:
    async def channel_request_accept_modal(modal_interaction: Interaction):
        channel_request_accept_input = ChannelRequestAcceptInput()

        channel_request_accept_input.name_of_channel.default = (
            input.name_of_channel.value
        )
        channel_request_accept_input.kind_of_event.default = input.kind_of_event.value
        channel_request_accept_input.name_of_lecture.default = (
            input.name_of_lecture.value
        )

        channel_request_accept_input.on_submit = MethodType(
            on_accept, channel_request_accept_input
        )

        await modal_interaction.response.send_modal(channel_request_accept_input)

    async def channel_request_decline_modal(modal_interaction: Interaction):
        channel_request_decline_input = ChannelRequestDeclineInput()

        channel_request_decline_input.declined_massage.default = (
            f"The channel '{input.name_of_channel.value}' already exists. [..]"
        )

        channel_request_decline_input.on_submit = MethodType(
            on_decline, channel_request_decline_input
        )

        await modal_interaction.response.send_modal(channel_request_decline_input)

    accept_channel_request_button = Button(label="Accept", style=ButtonStyle.green)
    decline_channel_request_button = Button(label="Decline", style=ButtonStyle.danger)

    accept_channel_request_button.callback = channel_request_accept_modal
    decline_channel_request_button.callback = channel_request_decline_modal

    accept_channel_request_view = (
        View(timeout=None)
        .add_item(accept_channel_request_button)
        .add_item(decline_channel_request_button)
    )

    accept_channel_request_embed = Embed(
        type="rich",
        title="Text Channel Request",
        colour=Colour.blurple(),
        timestamp=datetime.now(),
    )
    accept_channel_request_embed.add_field(
        name="Name of Lecture",
        value=input.name_of_lecture.value,
        inline=False
    )
    accept_channel_request_embed.add_field(
        name="Kind of Lecture",
        value=input.kind_of_event.value,
        inline=False
    )
    accept_channel_request_embed.add_field(
        name="Name of Channel",
        value=input.name_of_channel.value,
        inline=False
    )
    accept_channel_request_embed.set_author(
        name=interaction.user.nick, icon_url=interaction.user.avatar.url
    )

    return accept_channel_request_view, accept_channel_request_embed


# offtopic channel request #############################################################################

accept_offtopic_channel_send = "Accepted offtopic channel request"
decline_offtopic_channel_send = "Declined offtopic channel request"

class OffTopicChannelRequestAcceptInput(Modal, title="Accept Offtopic Channel Request"):
    name_of_channel = TextInput(label="Name of Channel")
    description = TextInput(label="Description")


class OffTopicChannelRequestDeclineInput(
    Modal, title="Decline Offtopic Channel Request"
):
    declined_massage = TextInput(label="Reason")


def create_offtopic_channel_request_accept_embed(
    input: OffTopicChannelRequestInput,
    interaction: Interaction,
    on_accept: Callable[[ChannelRequestAcceptInput, Interaction], None],
    on_decline: Callable[[ChannelRequestDeclineInput, Interaction], None],
) -> tuple[View, Embed]:
    async def offtopic_channel_request_accept_modal(modal_interaction: Interaction):
        offtopic_channel_request_accept_input = OffTopicChannelRequestAcceptInput()

        offtopic_channel_request_accept_input.name_of_channel.default = (
            input.name_of_channel.value
        )
        offtopic_channel_request_accept_input.description.default = (
            input.description.value
        )

        offtopic_channel_request_accept_input.on_submit = MethodType(
            on_accept, offtopic_channel_request_accept_input
        )

        await modal_interaction.response.send_modal(
            offtopic_channel_request_accept_input
        )

    async def offtopic_channel_request_decline_modal(modal_interaction: Interaction):
        offtopic_channel_request_decline_input = OffTopicChannelRequestDeclineInput()

        offtopic_channel_request_decline_input.declined_massage.default = (
            f"The channel '{input.name_of_channel.value}' already exists.  [..]"
        )

        offtopic_channel_request_decline_input.on_submit = MethodType(
            on_decline, offtopic_channel_request_decline_input
        )

        await modal_interaction.response.send_modal(
            offtopic_channel_request_decline_input
        )

    accept_offtopic_channel_request_button = Button(
        label="Accept", style=ButtonStyle.green
    )
    decline_offtopic_channel_request_button = Button(
        label="Decline", style=ButtonStyle.danger
    )

    accept_offtopic_channel_request_button.callback = (
        offtopic_channel_request_accept_modal
    )
    decline_offtopic_channel_request_button.callback = (
        offtopic_channel_request_decline_modal
    )

    accept_offtopic_channel_request_view = (
        View(timeout=None)
        .add_item(accept_offtopic_channel_request_button)
        .add_item(decline_offtopic_channel_request_button)
    )

    accept_offtopic_channel_request_embed = Embed(
        type="rich",
        title="Offtopic Channel Request",
        colour=Colour.blurple(),
        timestamp=datetime.now(),
    )
    accept_offtopic_channel_request_embed.add_field(
        name="Name of Channel",
        value=input.name_of_channel.value,
        inline=False
    )
    accept_offtopic_channel_request_embed.add_field(
        name="Description",
        value=input.description.value,
        inline=False
    )

    accept_offtopic_channel_request_embed.set_author(
        name=interaction.user.nick, icon_url=interaction.user.avatar.url
    )

    return accept_offtopic_channel_request_view, accept_offtopic_channel_request_embed

# support request #############################################################################


support_request_send = "Request sent successfully"
support_request_accepted = (
    lambda nick, invite: f"A moderator is now ready to help you in the {nick}'s support channel. {invite}"
)


support_embed_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."


class SupportRequestInput(Modal, title="Support request"):
    topic = TextInput(label="Topic", placeholder="eg. Authenticate")
    description = TextInput(
        label="Description", placeholder="eg. My generated token isn't valid."
    )


support_request_button = Button(label="Request Support", style=ButtonStyle.green)

support_view = lambda: (
    View(timeout=None)
    .add_item(support_request_button)
)

support_embed = Embed(
    type="rich",
    title="Support",
    colour=Colour.blurple(),
    timestamp=datetime.now(),
    description=support_embed_description,
)

support_embed.set_footer(text="Powered by Laurel")

## #accept support #############################################################################

accept_support_send = lambda invite: f"Accepted support request {invite}"
decline_support_send = "Declined support request"

accept_support_request_send = "Request submitted"


class SupportRequestDeclineInput(Modal, title="Decline Support Request"):
    declined_massage = TextInput(label="Reason")


def create_support_request_accept_embed(
    input: SupportRequestInput,
    interaction: Interaction,
    on_accept: Callable[[Interaction], None],
    on_decline: Callable[[SupportRequestDeclineInput, Interaction], None],
) -> tuple[View, Embed]:
    async def support_request_decline_modal(modal_interaction: Interaction):
        support_request_decline_input = SupportRequestDeclineInput()

        support_request_decline_input.declined_massage.default = (
            "There is already a forum post for this topic."
        )

        support_request_decline_input.on_submit = MethodType(
            on_decline, support_request_decline_input
        )

        await modal_interaction.response.send_modal(support_request_decline_input)

    accept_support_request_button = Button(label="Accept", style=ButtonStyle.green)
    decline_support_request_button = Button(label="Decline", style=ButtonStyle.danger)

    accept_support_request_button.callback = on_accept
    decline_support_request_button.callback = support_request_decline_modal

    accept_support_request_view = (
        View(timeout=None)
        .add_item(accept_support_request_button)
        .add_item(decline_support_request_button)
    )

    accept_support_request_embed = Embed(
        type="rich",
        title="Support Request",
        colour=Colour.green(),
        timestamp=datetime.now(),
    )
    accept_support_request_embed.add_field(
        name="Topic",
        value=input.topic.value,
        inline=False
    )
    accept_support_request_embed.add_field(
        name="Description",
        value=input.description.value,
        inline=False
    )
    accept_support_request_embed.set_author(
        name=interaction.user.nick, icon_url=interaction.user.avatar.url
    )

    return accept_support_request_view, accept_support_request_embed
