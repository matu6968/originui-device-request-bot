# OriginUi Device Request Bot

> what's this??? - **Literally** ***everyone***

This a device submission bot used in the [ester ROM's server](https://discord.gg/vYcFc6mYa5) where you can submit a device using slash commands and any updates about the request is sent via a DM.
Curently no code since it's unfinished lol.

## Features of the bot:
 - Submitting device requests over slash commands 
 - Device requests are sent over another channel and will let you pick if you want the device accepted, denied<sup>with a reason</sup>, and for further review.
	 - If you ever notice a person with a weird obsession of sending weird device requests, feel free to blacklist them with a click of a button!
	 - **Did a person send wrong device info?** No worries! Let them know with also a click of a button!
  - Whitelisting and blacklisting unsupported devices so that people can't just sneakily request a unsupported device

## Planned features for the bot:
 - Viewing and deleting user submitted supported devices in DB
 - Viewing the blacklist list and removing blacklisted users
 - Replying to further review requests (this will be added once viewing user submitted supported devices is added)

> [!NOTE]
> Requirements of the bot:
> - Python 3.8 or later as it uses [discord.py](https://discordpy.readthedocs.io/en/stable/#) for handling the requests of the bot.
> - A writable user directory so that it can save a database of supported devices (the ability to view currently supported devices in DB is coming soon)
> - A Discord account so that you can... make a bot
> - Some experience with editing files
> - 
## Instructions on setting up the bot
1. If you haven't made a bot, create one in the [Discord Developer Portal](https://discord.com/developers/applications)
2. Then grab the token in Bot > Token > Reset Token
3. Copy the token to something (like a notepad, this will come handy later)
4. Open main.py and edit the string at the top labled TOKEN and it's value INSERT_BOT_TOKEN_HERE with the actual bot token.
5. Invite the bot to your server and test it by running main.py in a terminal, you should see a message called like "OriginUI Device Request Bot#5153 is ready and online!" if thats the case congrats! You got the bot to work!
