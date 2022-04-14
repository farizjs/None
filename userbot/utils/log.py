import os

from telethon.errors import (
    ChannelsTooMuchError,
)
from telethon.tl.functions.channels import (
    CreateChannelRequest,
    EditPhotoRequest,
)
from telethon.tl.types import (
    ChatPhotoEmpty,
)

import heroku3

from userbot import BOTLOG_CHATID, HEROKU_API_KEY, HEROKU_APP_NAME, LOGS, bot

heroku_api = "https://api.heroku.com"
if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
    Heroku = heroku3.from_key(HEROKU_API_KEY)
    app = Heroku.app(HEROKU_APP_NAME)
    heroku_var = app.config()
else:
    app = None

# by : kenkan


async def autopilot():
    if BOTLOG_CHATID and str(BOTLOG_CHATID).startswith("-100"):
        return
    k = []  # To Refresh private ids
    async for x in bot.iter_dialogs():
        k.append(x.id)
    if BOTLOG_CHATID:
        try:
            await bot.get_entity(int("BOTLOG_CHATID"))
            return
        except BaseException:
            del heroku_var["BOTLOG_CHATID"]
    try:
        r = await bot(
            CreateChannelRequest(
                title="GALAXY USERBOT LOGS",
                about="Group log Galaxy-Userbot.\n\nJoin @FlicksSupport & @TheFicksUserbot",
                megagroup=True,
            ),
        )

    except ChannelsTooMuchError:
        LOGS.info(
            "too many channels and groups, delete one and restart again"
        )
        exit(1)
    except BaseException:
        LOGS.info(
            "an error occurs, create a group then fill in the id in the config var BOTLOG_CHATID."
        )
        exit(1)
    chat = r.chats[0]
    chat_id = r.chats[0].id
    if not str(chat_id).startswith("-100"):
        heroku_var["BOTLOG_CHATID"] = "-100" + str(chat_id)
    else:
        heroku_var["BOTLOG_CHATID"] = str(chat_id)

    if isinstance(chat.photo, ChatPhotoEmpty):

        ppk = "userbot/files/20211115_142004.jpg"
        try:
            await bot(
                EditPhotoRequest(int(chat_id), await bot.upload_file(ppk)))
        except BaseException as er:
            LOGS.exception(er)
        os.remove(ppk)
