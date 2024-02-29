# OriginUi Device Request Bot

> what's this??? - **Literally** ***everyone***

This a device submission bot used in the [ester ROM's server](https://discord.gg/vYcFc6mYa5) where you can submit a device using slash commands and any updates about the request is sent via a DM.

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

## Instructions on setting up the bot
1. Install the needed stuff on your target by typing the following:
```bash
pip3 install discord dsc-py
```
2. Download the repo by either typing the following:
```bash
git clone https://github.com/matu6968/origin-device-request-bot
```
or by downloading the repo using the Code button and then the ZIP option and extracting that onto your target.

3. If you haven't made a bot, create one in the [Discord Developer Portal](https://discord.com/developers/applications)
4. Then grab the token in Bot > Token > Reset Token
5. Copy the token to something (like a notepad, this will come handy later)
6. Open main.py and edit the string at the top labled TOKEN and it's value INSERT_BOT_TOKEN_HERE with the actual bot token, otherwaise you will see this when running it:
```bash
Traceback (most recent call last):
  File "/home/esterdev/bot/main.py", line 259, in <module>
    bot.run(token)
  File "/home/esterdev/.local/lib/python3.10/site-packages/discord/client.py", line 717, in run
    return future.result()
  File "/home/esterdev/.local/lib/python3.10/site-packages/discord/client.py", line 696, in runner
    await self.start(*args, **kwargs)
  File "/home/esterdev/.local/lib/python3.10/site-packages/discord/client.py", line 659, in start
    await self.login(token)
  File "/home/esterdev/.local/lib/python3.10/site-packages/discord/client.py", line 515, in login
    data = await self.http.static_login(token.strip())
  File "/home/esterdev/.local/lib/python3.10/site-packages/discord/http.py", line 422, in static_login
    raise LoginFailure("Improper token has been passed.") from exc
discord.errors.LoginFailure: Improper token has been passed.
```
8. Invite the bot to your server and test it by running main.py in a terminal, you should see a message called like "OriginUI Device Request Bot#5153 is ready and online!" if thats the case congrats, you got the bot to work!
