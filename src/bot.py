from datetime import datetime
import functools
import traceback
from discord import ButtonStyle, Client, Colour, Embed, Forbidden, Game, Intents, Interaction, NotFound, Role, SelectOption, utils
from discord.ui import View, Button, Modal, TextInput, Select

from .env import env
from .state import state

def try_catch(f):
    @functools.wraps(f)
    def decorated_function(*args, **kws):
        try:
          x = f(*args, **kws)
        except Exception as e:
          print(e)
          print(traceback.print_exc())
        return x

    return decorated_function

class Bot(Client):

  def __init__(self, **options) -> None:
    intents = Intents.all()
    super().__init__(intents=intents, **options)
    
  async def on_ready(self):
    await self.change_presence(activity=Game(name=f"{datetime.now()}"))
    await self.authentication()
    

  @try_catch
  async def authentication(self):
    # get login channel
    chan = self.get_channel(int(env.discord_auth_channel))
    
    # add message if not exists
    try:
      msg = await chan.fetch_message(chan.last_message_id)
    except NotFound:
      msg = await chan.send(content="...")

    # modal that receives the token via input field
    class TokenInput(Modal, title="Enter Authentication Token"):
      token = TextInput(label="Token", placeholder="Paste Token Here")

      @try_catch
      async def on_submit(self, interaction: Interaction): 
          token = str(self.token)

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
            studies = user["studies"] if user["studies"] is not None else "employee"

            roles = [await role(studies)]

            if studies != "employee":
              roles.append(await role("student"))

            await interaction.user.add_roles(*roles)

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
    
    # starts the authentication process
    @try_catch
    async def start_authentication(interaction: Interaction):
      role = utils.find(lambda role: role.colour == Colour.from_rgb(255, 255, 255), interaction.user.roles)

      # check if user is already authenticated
      if role is not None:
        await interaction.response.send_message(f"<already logged in as {role.name}>", ephemeral=True)
        return
          
      
      await interaction.response.send_modal(TokenInput())
      

    authenticate_button = Button(label="Enter Authentication Token", style=ButtonStyle.primary)
    authenticate_button.callback = start_authentication 

    view = View(timeout=None).add_item(authenticate_button)

    embed = Embed(type="rich", title="Login using University Account", url=env.url + "auth/token", colour=Colour.blue(), timestamp=datetime.now(), description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer vehicula pulvinar urna quis hendrerit. In hendrerit odio ac molestie sagittis. In fermentum nulla ac fringilla finibus. Fusce non mi porta, cursus urna id, tempor nibh. Morbi vitae turpis iaculis, imperdiet ex vitae, rhoncus ex. Phasellus congue odio eget pellentesque sagittis. Donec metus enim, molestie sit amet rutrum quis, vehicula eget diam.")
   
    embed.add_field(name="1. Login using Web", value="Donec sapien turpis, aliquet sit amet magna quis, ornare ullamcorper est. Morbi pharetra suscipit ex, vel feugiat tortor facilisis quis. Pellentesque nec leo in lacus malesuada varius ut eu erat. Nam dignissim aliquam orci, non lobortis quam imperdiet sollicitudin. Sed dapibus vulputate purus quis tincidunt. Sed non ipsum eget nibh hendrerit gravida a ac nibh. Cras ut tempor elit.", inline=False)
    embed.add_field(name="2. Enter Token", value="Vestibulum et consequat dolor, tincidunt molestie odio. Maecenas orci elit, pulvinar vel lorem vitae, tristique feugiat libero. Sed sit amet purus vitae lectus porttitor dignissim. Fusce lacinia augue turpis, vel ullamcorper ante ultricies eget. Curabitur vulputate ornare quam, eu gravida orci aliquet a. Pellentesque eget mi mi. Donec sollicitudin cursus velit, vel aliquam risus vehicula quis. Nulla lacinia enim a nibh malesuada, a imperdiet nulla imperdiet. Aliquam rutrum pulvinar purus, in porttitor turpis interdum vel.", inline=False)
    embed.set_footer(text="Login powered by Laurel")
    embed.set_image(url="https://cd.uni-freiburg.de/app/uploads/2023/02/UFR-vorlage-designsystem-typo-farben-V1.96.png")

    await msg.edit(content="", embed=embed, view=view)
   