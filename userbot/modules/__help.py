#    TeleBot - UserBot
#    Copyright (C) 2020 TeleBot

#    Recode by Fariz <Github.com/farizjs>
#    From Flicks-Userbot
#    <t.me/TheFlicksUserbot>


from telethon import Button

from . import BOT_USERNAME, HANDLER, CMD_HELP, bot, glx_cmd

user = bot.get_me()
DEFAULTUSER = user.first_name
CUSTOM_HELP_EMOJI = "⚡"



@glx_cmd(pattern="help ?(.*)")
async def cmd_list(event):
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await event.edit(f"**✘ Commands available in {args} ✘** \n\n" + str(CMD_HELP[args]) + "\n\n**💕 @TheFlicksUserbot**")
        else:
            await event.edit(f"**Module** `{args}` **Tidak tersedia!**")
    else:
        try:
            results = await bot.inline_query(  # pylint:disable=E0602
                BOT_USERNAME, "@FlicksSupport"
            )
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        except BaseException:
            await event.edit(
                f"** Looks like this chat or bot doesn't support inline mode.\nFor an alternative, use the command\n👉`{HANDLER}plugins`**"
            )
