from datetime import datetime
from discord import ButtonStyle, Colour, Embed
from discord.ui import View, Button, Modal, TextInput

from .env import env

## #about ###############################################################################

about_embed_description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."
about_embed_auth = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."
about_embed_rules = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."

about_embed = Embed(
    type="rich",
    title="About this Discord Server",
    colour=Colour.blue(),
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

auth_token_button = Button(label="Authenticate", style=ButtonStyle.primary)
auth_link_button = Button(label="Get Token", url=env.url + "auth/token")
auth_view = (
    lambda: View(timeout=None).add_item(auth_link_button).add_item(auth_token_button)
)

auth_embed = Embed(
    type="rich",
    title="Login using University Account",
    url=env.url + "auth/token",
    colour=Colour.blue(),
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
account_embed_description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."
account_embed_disconnect = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."
account_embed_sync = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."
account_embed_name = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."

account_logout_button = Button(label="Logout", style=ButtonStyle.danger)


class AccountTokenInput(Modal, title="Enter Authorization Token"):
    token = TextInput(label="Token", placeholder="Paste Authorization Token Here")


account_update_button = Button(label="Sync Account", style=ButtonStyle.primary)
account_token_button = Button(label="Get Token", url=env.url + "auth/token")

class AccountNameInput(Modal, title="Change Nickname"):
    name = TextInput(label="New Nickname")

account_name_button = Button(label="Set Name", style=ButtonStyle.secondary)

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
    colour=Colour.blue(),
    timestamp=datetime.now(),
    description=account_embed_description
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

channels_embed_description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam."

class ChannelRequestInput(Modal, title="Request a Text Channel"):
    name_of_lecture = TextInput(label="Name", placeholder="Enter Name of Lecture Here")
    kind_of_lecture = TextInput(label="Kind", placeholder="Lecture / Seminar / ...")
    description_of_lecture = TextInput(label="Description", placeholder="Enter Description Here")


channel_request_input = ChannelRequestInput()

channels_request_button = Button(label="Request", style=ButtonStyle.danger)

channel_view = lambda: (
    View(timeout=None)
    .add_item(channels_request_button)
)

channel_embed = Embed(
    type="richt",
    title="Request a text channel",
    colour=Colour.blue(),
    timestamp=datetime.now(),
    description=channels_embed_description
)

channel_embed.set_footer(text="Powered by Laurel")
