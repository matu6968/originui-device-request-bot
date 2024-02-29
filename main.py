import discord
import json
import os
import re
from whitelist_and_blacklist import *
DATA_FILE = "database.json"
TOKEN = "INSERT_BOT_TOKEN_HERE"


intents = discord.Intents.default()
intents.message_content = True
token = TOKEN
bot = discord.Bot(command_prefix="o!", intents=intents)

def load_data():
  try:
      with open(DATA_FILE, 'r') as f:
          return json.load(f)
  except FileNotFoundError:
      return {}

db = load_data()

def save_data(db=db):
  with open(DATA_FILE, 'w') as f:
      json.dump(db, f, indent=4)
    
# beta testing on ester ROM's server
request_channel = 1212473969043578921
request_guilds = [1154485858142003220]
#ester devs id's:
#request_channel = 1195446572700405893
#request_guilds = [1144953241919033424]

pattern = r"\*\*Request for (?P<manufacturer2>[^\s]+) (?P<model2>[^<]+) by <@(?P<user_id>\d+)>\*\*\s+" \
r"Manufacturer: (?P<manufacturer>[^\s]+)\s+" \
r"Model: (?P<model>[^\n]+)\n" \
r"Device codename\(s\): `(?P<codenames>[^`]+)`\s+" \
r"URL to XDA Forums: (?P<url>https?://[^\s]+)"

# CLEAR THE DATABASE
# PLEASE DELETE AFTER THE TESTING PHASE
#for i in db.keys():
#   del db[i]
#   print("deleted all the shit! :)")

# only for the testing phase
# print(db.keys())


def is_in_blacklist(user_id):
  try:
    blacklist = db["blacklist"]
  except KeyError:
    return False
  return user_id in blacklist


def add_to_blacklist(user_id):
  try:
    blacklist = db["blacklist"]
  except KeyError:
    blacklist = [user_id]
  else:
    blacklist.append(user_id)
  db["blacklist"] = blacklist


def get_details(message):
  matches = re.search(pattern, message)
  return matches.groupdict()

class RequestView(discord.ui.View):
  def __init__(self):
    super().__init__(timeout=None)

  @discord.ui.button(label="Yes", style=discord.ButtonStyle.success, emoji="✅")
  async def yes(self, button, interaction):
    details = get_details(interaction.message.content)
    user_id = int(details["user_id"])
    manufacturer = details["manufacturer"]
    model = details["model"]
    codenames = details["codenames"]
    got_from_db = db[
        f"{manufacturer.lower()} {model.lower()} {codenames.lower()}"]
    if got_from_db["accepted"]:
      await interaction.response.send_message(
          "Device has already been accepted!")
      return
    got_from_db["accepted"] = True
    db[f"{manufacturer.lower()} {model.lower()} {codenames.lower()}"] = got_from_db
    save_data(db)
    user = await bot.fetch_user(user_id)
    await user.send(
        f"<@{user_id}>, the device {manufacturer} {model} (`{codenames}`) has been accepted!"
    )
    await interaction.response.send_message("Device accepted!")
    self.disable_all_items()

  @discord.ui.button(label="No", style=discord.ButtonStyle.danger, emoji="❌")
  async def no(self, button, interaction):
    details = get_details(interaction.message.content)
    user_id = int(details["user_id"])
    manufacturer = details["manufacturer"]
    model = details["model"]
    codenames = details["codenames"]
    got_from_db = db[
        f"{manufacturer.lower()} {model.lower()} {codenames.lower()}"]
    await interaction.response.send_message(
        "Enter reason for rejecting the device:")

    def check(message: discord.Message):
      return message.channel == interaction.message.channel and message.author != bot.user

    reject_reason = await bot.wait_for('message', check=check)
    got_from_db["rejected"] = reject_reason.content
    db[f"{manufacturer.lower()} {model.lower()} {codenames.lower()}"] = got_from_db
    save_data(db)
    user = await bot.fetch_user(user_id)
    await user.send(
        f"<@{user_id}>, the device {manufacturer} {model} (`{codenames}`) has been rejected!\nReason: `{reject_reason.content}`"
    )
    await reject_reason.channel.send(
        f"Device {manufacturer} {model} (`{codenames}`) rejected for reason: `{reject_reason.content}`"
    )
    self.disable_all_items()

  @discord.ui.button(label="""Consider request for further review""",
                     style=discord.ButtonStyle.secondary,
                     emoji="❔")
  async def later(self, button, interaction):
    details = get_details(interaction.message.content)
    user_id = int(details["user_id"])
    manufacturer = details["manufacturer"]
    model = details["model"]
    codenames = details["codenames"]
    user = await bot.fetch_user(user_id)
    await user.send(f"Your device {manufacturer} {model} `{codenames}` is being considered, hold on tight and we will reply if your device will get accepted!")
    await interaction.response.send_message(f"Device {manufacturer} {model} `{codenames}` considered for further review!")

  @discord.ui.button(label="Wrong Device Info",
                     style=discord.ButtonStyle.primary)
  async def wrong(self, button, interaction):
    details = get_details(interaction.message.content)
    user_id = int(details["user_id"])
    manufacturer = details["manufacturer"]
    model = details["model"]
    codenames = details["codenames"]
    del db[f"{manufacturer.lower()} {model.lower()} {codenames.lower()}"]
    save_data(db)
    await interaction.response.send_message(
        f"Device {manufacturer} {model} `{codenames}` has been deleted from the database!"
    )
    user = await bot.fetch_user(user_id)
    await user.send(
        f"<@{user_id}>, you entered the wrong device info for {manufacturer} {model} `{codenames}`. Please request again, but this time with the correct device info!"
    )

  @discord.ui.button(label="Blacklist (Ban) User",
                     style=discord.ButtonStyle.danger,
                     emoji="🔨")
  async def blacklist(self, button, interaction):
    details = get_details(interaction.message.content)
    user_id = int(details["user_id"])
    manufacturer = details["manufacturer"]
    model = details["model"]
    codenames = details["codenames"]
    del db[f"{manufacturer.lower()} {model.lower()} {codenames.lower()}"]
    add_to_blacklist(user_id)
    save_data(db)

    await interaction.response.send_message(
        f"Blacklisted <@{user_id}> successfully! The user did not get any notification (unless they have access to this channel)"
    )
    self.disable_all_items()


@bot.event
async def on_ready():
  print(f"{bot.user} is ready and online!")


def is_xda_url_valid(url):
  if url.startswith("http://"):
    url = url.removeprefix("http://")
  elif url.startswith("https://"):
    url = url.removeprefix("https://")

  if url.startswith("xdaforums.com/f/") or url.startswith(
      "www.xdaforums.com/f/"):
    url = f"https://{url}"
  else:
    url = None
  return url


@bot.command(description="Submit a device request for OriginUi.",
             guild_ids=request_guilds)
async def requestdevice(ctx, phone_manufacturer: discord.Option(
    discord.SlashCommandOptionType.string,
    description="Manufacturer of the device (example: Samsung)",
    required=True
), phone_model: discord.Option(
    discord.SlashCommandOptionType.string,
    description=
    "Model of the device (example: Galaxy S21 Ultra 5G) (don't include the manufacturer!)",
    required=True
), device_codenames: discord.Option(
    discord.SlashCommandOptionType.string,
    description="Device codename(s) (example: Unbound) (NOT DEVICE MODEL)",
    required=True
), url_to_xdaforums: discord.Option(
    discord.
    SlashCommandOptionType.string,
    description=
    "URL to the XDA thread of device (ex: https://xdaforums.com/f/samsung-galaxy-s21-roms-kernel.11941)",
    required=True)):
  if not is_in_blacklist(ctx.author.id):
    url_to_xdaforums = is_xda_url_valid(url_to_xdaforums)
    if phone_manufacturer is None:
      await ctx.respond("Please specify a phone manufacturer!")
    elif phone_model is None:
      await ctx.respond("Please specify a phone model!")
    elif device_codenames is None:
      await ctx.respond("Please specify your devices codename(s)!")
    elif url_to_xdaforums is None:
      await ctx.respond(
          "You provided an invalid URL to the XDA thread of your device! (the link has to have /f/ in it)"
      )
    else:
      request_dict = {
          "phone_manufacturer": phone_manufacturer.lower(),
          "phone_model": phone_model.lower(),
          "device_codenames": device_codenames.lower(),
          "xda_thread_url": url_to_xdaforums,
          "requested_by": ctx.author.id,
          "accepted": False,
          "rejected": False,
      }
      db[f"{phone_manufacturer.lower()} {phone_model.lower()} {device_codenames.lower()}"] = request_dict
      request_message = f"""
**Request for {phone_manufacturer} {phone_model} by <@{ctx.author.id}>**
Manufacturer: {phone_manufacturer}
Model: {phone_model}
Device codename(s): `{device_codenames}`
URL to XDA Forums: {url_to_xdaforums}
**Would you like to accept this request?**
"""
      await ctx.respond("Request sent!")
      await bot.get_channel(request_channel).send(request_message,
                                                  view=RequestView())
      await ctx.author.send(f"""
Your request for {phone_manufacturer} {phone_model} (`{device_codenames}`) has been sent!"""
                            )
  else:
    await ctx.respond(
        "The bot is having some issues right now, please try again later!")

bot.run(token)
