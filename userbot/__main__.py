# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
"""Userbot start point"""

from importlib import import_module
from sys import argv
from platform import python_version

from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from telethon import version
from telethon.errors.rpcerrorlist import PhoneNumberInvalidError
from userbot import ALIVE_NAME, LOGS, BOTLOG_CHATID, bot
# from userbot.utils import autobot, autopilot
from userbot.modules import ALL_MODULES


INVALID_PH = '\nERROR: The Phone No. entered is INVALID' \
             '\n Tip: Use Country Code along with number.' \
             '\n or check your phone number and try again !'

try:
    bot.start()
except PhoneNumberInvalidError:
    print(INVALID_PH)
    exit(1)

for module_name in ALL_MODULES:
    imported_module = import_module("userbot.modules." + module_name)


# if not BOTLOG_CHATID:
#    LOGS.info(
#        "BOTLOG_CHATID Unallocated vars, Starting Automatic Grouping..."
#    )
#    bot.loop.run_until_complete(autopilot())

# if not BOT_TOKEN:
#    LOGS.info(
#        "BOT_TOKEN Vars not filled, Started Automating BOT in @Botfather..."
#    )
#    bot.loop.run_until_complete(autobot())


LOGS.info(
    "Congratulations, your userbot is now running !!"
    f"\nTelethon: {version.__version__}"
    f"\nPython: {python_version()}")


async def send_alive_status():
    try:
        if BOTLOG_CHATID != 0:
            message = (
                "**Bot is up and running!**\n\n"
                f"**Telethon:** {version.__version__}\n"
                f"**Python:** {python_version()}\n"
                f"**User:** {ALIVE_NAME} !!'")
            await bot.send_message(BOTLOG_CHATID, message)
    except Exception as e:
        LOGS.info(str(e))
    try:
        await bot(JoinChannelRequest("@TheFlicksUserbot"))
    except BaseException:
        pass
    try:
        await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
    except BaseException:
        pass


if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
