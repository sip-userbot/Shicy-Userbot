import asyncio

from telethon.tl.functions.channels import EditAdminRequest, InviteToChannelRequest
from telethon.tl.types import ChatAdminRights

from ShicyXd import BOT_VER as version
from ShicyXd import BOTLOG_CHATID
from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import bot, branch, tgbot
from ShicyXd.shicy import shicy_version as py_ver
from ShicyXd.shicy import HOSTED_ON, checking

MSG_ON = """
❏ Shicy - ᴜsᴇʀʙᴏᴛ ʙᴇʀʜᴀsɪʟ ᴅɪᴀᴋᴛɪғᴋᴀɴ
╭╼┅━━━━━╍━━━━━┅╾
├▹ Shicy Vᴇʀsɪᴏɴ - {} •[{}]•
├▹ Usᴇʀʙᴏᴛ Vᴇʀsɪᴏɴ - {}
├▹ @{}
├▹ Kᴇᴛɪᴋ {}alive Uɴᴛᴜᴋ Mᴇɴɢᴇᴄᴇᴋ Bᴏᴛ
╰╼┅━━━━━╍━━━━━┅╾
"""


async def shicy_userbot_on():
    new_rights = ChatAdminRights(
        add_admins=True,
        invite_users=True,
        change_info=True,
        ban_users=True,
        delete_messages=True,
        pin_messages=True,
        manage_call=True,
    )
    try:
        if bot and tgbot:
            ShicyUBOT = await tgbot.get_me()
            BOT_USERNAME = ShicyUBOT.username
            await bot(InviteToChannelRequest(int(BOTLOG_CHATID), [BOT_USERNAME]))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot and tgbot:
            ShicyUBOT = await tgbot.get_me()
            BOT_USERNAME = ShicyUBOT.username
            await bot(EditAdminRequest(BOTLOG_CHATID, BOT_USERNAME, new_rights, "Assɪsᴛᴀɴᴛ Shicy"))
            await asyncio.sleep(3)
    except BaseException:
        pass
    try:
        if bot:
            await checking(bot)
            await asyncio.sleep(3)
            if BOTLOG_CHATID != 0:
                await bot.send_message(
                    BOTLOG_CHATID,
                    MSG_ON.format(py_ver, HOSTED_ON, version, branch, cmd),
                )
    except BaseException:
        pass
