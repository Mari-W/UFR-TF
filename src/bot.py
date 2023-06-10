from datetime import datetime
import re
from discord import ButtonStyle, Client, Colour, Embed, Forbidden, Intents, Interaction, Member, NotFound, PermissionOverwrite, Role, VoiceState, utils
from discord.ui import View, Button, Modal, TextInput

from .env import env
from .shared import state, mapping

class Bot(Client):

  def __init__(self, **options) -> None:
    intents = Intents.all()
    super().__init__(intents=intents, **options)
    
  async def on_ready(self):
    await self.about()
    await self.authentication()
    await self.account()

  async def about(self):
    # get about channel
    chan = utils.get(self.guilds[0].text_channels, name="about")
   
    # add message if not exists
    try:
      msg = await chan.fetch_message(chan.last_message_id)
    except NotFound:
      msg = await chan.send(content="...")

    embed = Embed(type="rich", title="About this Discord Server", colour=Colour.blue(), timestamp=datetime.now(), description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam.")
   
    embed.add_field(name="1. Orga", value="Donec sapien turpis, aliquet sit amet magna quis, ornare ullamcorper est. Morbi pharetra suscipit ex, vel feugiat tortor facilisis quis. Pellentesque nec leo in lacus malesuada varius ut eu erat. Nam dignissim aliquam orci, non lobortis quam imperdiet sollicitudin. Sed dapibus vulputate purus quis tincidunt. Sed non ipsum eget nibh hendrerit gravida a ac nibh. Cras ut tempor elit.", inline=False)
    embed.add_field(name="2. Rules", value="Vestibulum et consequat dolor, tincidunt molestie odio. Maecenas orci elit, pulvinar vel lorem vitae, tristique feugiat libero. Sed sit amet purus vitae lectus porttitor dignissim. Fusce lacinia augue turpis, vel ullamcorper ante ultricies eget. Curabitur vulputate ornare quam, eu gravida orci aliquet a. Pellentesque eget mi mi. Donec sollicitudin cursus velit, vel aliquam risus vehicula quis. Nulla lacinia enim a nibh malesuada, a imperdiet nulla imperdiet. Aliquam rutrum pulvinar purus, in porttitor turpis interdum vel.", inline=False)

    await msg.edit(content="", embed=embed)

  async def authentication(self):
    # get login channel
    chan = utils.get(self.guilds[0].text_channels, name="authenticate")
   
    # add message if not exists
    try:
      msg = await chan.fetch_message(chan.last_message_id)
    except NotFound:
      msg = await chan.send(content="...")
    
    # modal that receives the token via input field
    class TokenInput(Modal, title="Enter Authentication Token"):
      token = TextInput(label="Token", placeholder="Paste Authentication Token Here")

      async def on_submit(self, interaction: Interaction): 
          await login(str(self.token), interaction)
    
    # starts the authentication process
    async def start_authentication(interaction: Interaction):
      await interaction.response.send_modal(TokenInput())
      

    authenticate_button = Button(label="Authenticate", style=ButtonStyle.primary)
    authenticate_button.callback = start_authentication 

    view = View(timeout=None).add_item(authenticate_button)

    embed = Embed(type="rich", title="Login using University Account", url=env.url + "auth/token", colour=Colour.blue(), timestamp=datetime.now(), description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam.")
   
    embed.add_field(name="1. Login using Web", value="Donec sapien turpis, aliquet sit amet magna quis, ornare ullamcorper est. Morbi pharetra suscipit ex, vel feugiat tortor facilisis quis. Pellentesque nec leo in lacus malesuada varius ut eu erat. Nam dignissim aliquam orci, non lobortis quam imperdiet sollicitudin. Sed dapibus vulputate purus quis tincidunt. Sed non ipsum eget nibh hendrerit gravida a ac nibh. Cras ut tempor elit.", inline=False)
    embed.add_field(name="2. Enter Token", value="Vestibulum et consequat dolor, tincidunt molestie odio. Maecenas orci elit, pulvinar vel lorem vitae, tristique feugiat libero. Sed sit amet purus vitae lectus porttitor dignissim. Fusce lacinia augue turpis, vel ullamcorper ante ultricies eget. Curabitur vulputate ornare quam, eu gravida orci aliquet a. Pellentesque eget mi mi. Donec sollicitudin cursus velit, vel aliquam risus vehicula quis. Nulla lacinia enim a nibh malesuada, a imperdiet nulla imperdiet. Aliquam rutrum pulvinar purus, in porttitor turpis interdum vel.", inline=False)
    embed.set_footer(text="Powered by Laurel")
    
    await msg.edit(content="", embed=embed, view=view)
  
  async def account(self):
    chan = utils.get(self.guilds[0].text_channels, name="account")

    try:
      msg = await chan.fetch_message(chan.last_message_id)
    except NotFound:
      msg = await chan.send(content="...")    

    logout_button = Button(label="Logout", style=ButtonStyle.danger)
    logout_button.callback = logout 

    # modal that receives the token via input field
    class TokenInput(Modal, title="Enter Authorization Token"):
      token = TextInput(label="Token", placeholder="Paste Token Here")

      async def on_submit(self, interaction: Interaction): 
          await logout()
          await login(str(self.token), interaction)
    
    # starts the authentication process
    async def start_update(interaction: Interaction):
      await interaction.response.send_modal(TokenInput())
      

    update_button = Button(label="Sync Account", style=ButtonStyle.primary)
    update_button.callback = start_update 

    async def update_name(interaction: Interaction):
      try:
        matches =  matches = re.findall(r"^\[[a-z0-9]+\]", interaction.user.display_name)
        print(matches)
        if len(matches) != 1:
          await interaction.response.send_message("<name does not follow guidlines `[xy123] name`>", ephemeral=True)
          return
        await interaction.user.edit(nick=f"{matches[0]} {interaction.user.name}")  
      except Forbidden:
        # user is server owner
        pass
      await interaction.response.send_message("<name update successful>", ephemeral=True)
      

    update_name_button = Button(label="Sync Name", style=ButtonStyle.secondary)
    update_name_button.callback = update_name 


    view = View(timeout=None).add_item(logout_button).add_item(update_button).add_item(update_name_button)

    embed = Embed(type="rich", title="Manage Your Connected Account", colour=Colour.blue(), timestamp=datetime.now(), description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam.")
   
    embed.add_field(name="1. Disconnect University Account", value="Donec sapien turpis, aliquet sit amet magna quis, ornare ullamcorper est. Morbi pharetra suscipit ex, vel feugiat tortor facilisis quis. Pellentesque nec leo in lacus malesuada varius ut eu erat. Nam dignissim aliquam orci, non lobortis quam imperdiet sollicitudin. Sed dapibus vulputate purus quis tincidunt. Sed non ipsum eget nibh hendrerit gravida a ac nibh. Cras ut tempor elit.", inline=False)
    embed.add_field(name="2. Sync University Account", value="Vestibulum et consequat dolor, tincidunt molestie odio. Maecenas orci elit, pulvinar vel lorem vitae, tristique feugiat libero. Sed sit amet purus vitae lectus porttitor dignissim. Fusce lacinia augue turpis, vel ullamcorper ante ultricies eget. Curabitur vulputate ornare quam, eu gravida orci aliquet a. Pellentesque eget mi mi. Donec sollicitudin cursus velit, vel aliquam risus vehicula quis. Nulla lacinia enim a nibh malesuada, a imperdiet nulla imperdiet. Aliquam rutrum pulvinar purus, in porttitor turpis interdum vel.", inline=False)
    embed.add_field(name="3. Sync Discord Name", value="Vestibulum et consequat dolor, tincidunt molestie odio. Maecenas orci elit, pulvinar vel lorem vitae, tristique feugiat libero. Sed sit amet purus vitae lectus porttitor dignissim. Fusce lacinia augue turpis, vel ullamcorper ante ultricies eget. Curabitur vulputate ornare quam, eu gravida orci aliquet a. Pellentesque eget mi mi. Donec sollicitudin cursus velit, vel aliquam risus vehicula quis. Nulla lacinia enim a nibh malesuada, a imperdiet nulla imperdiet. Aliquam rutrum pulvinar purus, in porttitor turpis interdum vel.", inline=False)
    embed.set_footer(text="Powered by Laurel")

    await msg.edit(content="", embed=embed, view=view)

  async def voice(self, member: Member, before: VoiceState, after: VoiceState):
    create = utils.get(member.guild.voice_channels, name="create")
    category = utils.get(member.guild.categories, name="voice")
    if before.channel != after.channel and after.channel == create:
      channel = await member.guild.create_voice_channel(name=f"{member.display_name}",
                                                overwrites={member : PermissionOverwrite(manage_channels=True)},
                                                category=category,
                                                position=1)
      await member.move_to(channel)
    if before.channel != after.channel and before.channel.category == category and not before.channel.members and before.channel.name != "create":
      await before.channel.delete()
 
async def logout(interaction: Interaction):
  roles = list(filter(lambda role: role.name != "Admin" and role.name != "@everyone" , interaction.user.roles))
  await interaction.user.remove_roles(*roles)
  try:
    await interaction.user.edit(nick=None)
  except Forbidden:
    # user is server owner
    pass
  await interaction.response.send_message("<logged out>", ephemeral=True)

async def login(token: str, interaction: Interaction):
  # token is valid
  if token in state:

    # get user information
    user = state[token]

    # creates a role if it does not exist
    async def role(name: str) -> Role:
      role = utils.get(interaction.guild.roles, name=name)
      if role is None:
        role = await interaction.guild.create_role(name=name, colour = Colour.from_rgb(255, 255, 255))
      return role
            
    # assign according roles
    studies = mapping.get(user["studies"], user["studies"]) if user["studies"] is not None else "Employee"
    await interaction.user.add_roles(await role("Authenticated"), await role(studies))
    
    # set name
    # TODO is .name correct? might use .{global, display}_name
    try:
      await interaction.user.edit(nick=f"[{user['sub']}] {interaction.user.name}")  
    except Forbidden:
      # user is server owner
      pass
    
    # send success message
    await interaction.response.send_message(f"<logged in as {user['sub']}>", ephemeral=True)
  # token is invalid
  else:
    # send failure message
    await interaction.response.send_message("<token not found>", ephemeral=True)
