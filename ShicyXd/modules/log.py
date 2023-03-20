# Credits: mrconfused
# Recode by @mrismanaziz
# t.me/SharingUserbot

import asyncio

from telethon import events

from ShicyXd import BOTLOG_CHATID
from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP, LOGS, bot
from ShicyXd.modules.sql_helper import no_log_pms_sql
from ShicyXd.modules.sql_helper.globals import addgvar, gvarstatus
from ShicyXd.modules.carbon import vcmention
from ShicyXd.shicy import _format, shicy_cmd, edit_delete, edit_or_reply
from ShicyXd.shicy.tools import media_type


class LOG_CHATS:
    def __init__(self):
        self.RECENT_USER = None
        self.NEWPM = None
        self.COUNT = 0


LOG_CHATS_ = LOG_CHATS()


@bot.on(events.ChatAction)
async def logaddjoin(chiy):
    user = await chiy.get_user()
    chat = await chiy.get_chat()
    if not (user and user.is_self):
        return
    if hasattr(chat, "username") and chat.username:
        chat = f"[{chat.title}](https://t.me/{chat.username}/{chiy.action_message.id})"
    else:
        chat = f"[{chat.title}](https://t.me/c/{chat.id}/{chiy.action_message.id})"
    if chiy.user_added:
        tmp = chiy.added_by
        text = f"📩 **#TAMBAH_LOG\n •** {vcmention(tmp)} **Menambahkan** {vcmention(user)}\n **• Ke Group** {chat}"
    elif chiy.user_joined:
        text = f"📨 **#LOG_GABUNG\n •** [{user.first_name}](tg://user?id={user.id}) **Bergabung\n • Ke Group** {chat}"
    else:
        return
    await chiy.client.send_message(BOTLOG_CHATID, text)


@bot.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
@bot.on(events.MessageEdited(incoming=True, func=lambda e: e.is_private))
async def monito_p_m_s(chiy):
    if BOTLOG_CHATID == -100:
        return
    if gvarstatus("PMLOG") and gvarstatus("PMLOG") == "false":
        return
    sender = await chiy.get_sender()
    await asyncio.sleep(0.5)
    if not sender.bot:
        chat = await chiy.get_chat()
        if not no_log_pms_sql.is_approved(chat.id) and chat.id != 777000:
            if LOG_CHATS_.RECENT_USER != chat.id:
                LOG_CHATS_.RECENT_USER = chat.id
                if LOG_CHATS_.NEWPM:
                    await LOG_CHATS_.NEWPM.edit(
                        LOG_CHATS_.NEWPM.text.replace(
                            "**💌 #PESAN_BARU**",
                            f" • `{LOG_CHATS_.COUNT}` **Pesan**",
                        )
                    )
                    LOG_CHATS_.COUNT = 0
                LOG_CHATS_.NEWPM = await chiy.client.send_message(
                    BOTLOG_CHATID,
                    f"**💌 #MENERUSKAN #PESAN_BARU**\n** • Dari : **{_format.mentionuser(sender.first_name , sender.id)}\n** • User ID:** `{chat.id}`",
                )
            try:
                if chiy.message:
                    await chiy.client.forward_messages(
                        BOTLOG_CHATID, chiy.message, silent=True
                    )
                LOG_CHATS_.COUNT += 1
            except Exception as e:
                LOGS.warn(str(e))


@bot.on(events.NewMessage(incoming=True, func=lambda e: e.mentioned))
@bot.on(events.MessageEdited(incoming=True, func=lambda e: e.mentioned))
async def log_tagged_messages(event):
    if BOTLOG_CHATID == -100:
        return
    xnxx = await event.get_chat()

    if gvarstatus("GRUPLOG") and gvarstatus("GRUPLOG") == "false":
        return
    if (
        (no_log_pms_sql.is_approved(xnxx.id))
        or (BOTLOG_CHATID == -100)
        or (await event.get_sender() and (await event.get_sender()).bot)
    ):
        return
    full = None
    try:
        full = await event.client.get_entity(event.message.from_id)
        namechiy = full.first_name
        idchiy = full.id
    except Exception as e:
        LOGS.info(str(e))
    messaget = media_type(event)
    resalt = f"<b>📨 #TAGS #MESSAGE</b>\n<b> • Dari : </b>{_format.htmlmentionuser(namechiy, idchiy)}"
    if full is not None:
        resalt += f"\n<b> • Grup : </b><code>{xnxx.title}</code>"
    if messaget is not None:
        resalt += f"\n<b> • Jenis Pesan : </b><code>{messaget}</code>"
    else:
        resalt += f"\n<b> • 👀 </b><a href = 'https://t.me/c/{xnxx.id}/{event.message.id}'>Lihat Pesan</a>"
    resalt += f"\n<b> • Message : </b>{event.message.message}"
    await asyncio.sleep(0.5)
    if not event.is_private:
        await event.client.send_message(
            BOTLOG_CHATID,
            resalt,
            parse_mode="html",
            link_preview=False,
        )


@shicy_cmd(pattern="save(?: |$)(.*)")
async def log(log_text):
    if BOTLOG_CHATID:
        if log_text.reply_to_msg_id:
            reply_msg = await log_text.get_reply_message()
            await reply_msg.forward_to(BOTLOG_CHATID)
        elif log_text.pattern_match.group(1):
            user = f"**#LOG / Chat ID:** {log_text.chat_id}\n\n"
            textx = user + log_text.pattern_match.group(1)
            await log_text.client.send_message(BOTLOG_CHATID, textx)
        else:
            await edit_delete(log_text, "**Apa yang harus saya simpan?**")
            return
        await edit_delete(log_text, "**Berhasil disimpan di Grup Log**")
    else:
        await edit_delete(
            log_text,
            "**Untuk Menggunakan Module ini, Anda Harus Mengatur** `BOTLOG_CHATID` **di Config Vars**",
            30,
        )


@shicy_cmd(pattern="log$")
async def set_no_log_p_m(event):
    if BOTLOG_CHATID != -100:
        chat = await event.get_chat()
        if no_log_pms_sql.is_approved(chat.id):
            no_log_pms_sql.disapprove(chat.id)
            await edit_delete(
                event, "**LOG Chat dari Grup ini Berhasil Diaktifkan**", 15
            )


@shicy_cmd(pattern="nolog$")
async def set_no_log_p_m(event):
    if BOTLOG_CHATID != -100:
        chat = await event.get_chat()
        if not no_log_pms_sql.is_approved(chat.id):
            no_log_pms_sql.approve(chat.id)
            await edit_delete(
                event, "**LOG Chat dari Grup ini Berhasil Dimatikan**", 15
            )


@shicy_cmd(pattern="pmlog (on|off)$")
async def set_pmlog(event):
    if BOTLOG_CHATID == -100:
        return await edit_delete(
            event,
            "**Untuk Menggunakan Module ini, Anda Harus Mengatur** `BOTLOG_CHATID` **di Config Vars**",
            30,
        )
    input_str = event.pattern_match.group(1)
    if input_str == "off":
        h_type = False
    elif input_str == "on":
        h_type = True
    if gvarstatus("PMLOG") and gvarstatus("PMLOG") == "false":
        PMLOG = False
    else:
        PMLOG = True
    if PMLOG:
        if h_type:
            await edit_or_reply(event, "**PM LOG Sudah Diaktifkan**")
        else:
            addgvar("PMLOG", h_type)
            await edit_or_reply(event, "**PM LOG Berhasil Dimatikan**")
    elif h_type:
        addgvar("PMLOG", h_type)
        await edit_or_reply(event, "**PM LOG Berhasil Diaktifkan**")
    else:
        await edit_or_reply(event, "**PM LOG Sudah Dimatikan**")


@shicy_cmd(pattern="gruplog (on|off)$")
async def set_gruplog(event):
    if BOTLOG_CHATID == -100:
        return await edit_delete(
            event,
            "**Untuk Menggunakan Module ini, Anda Harus Mengatur** `BOTLOG_CHATID` **di Config Vars**",
            30,
        )
    input_str = event.pattern_match.group(1)
    if input_str == "off":
        h_type = False
    elif input_str == "on":
        h_type = True
    if gvarstatus("GRUPLOG") and gvarstatus("GRUPLOG") == "false":
        GRUPLOG = False
    else:
        GRUPLOG = True
    if GRUPLOG:
        if h_type:
            await edit_or_reply(event, "**Group Log Sudah Diaktifkan**")
        else:
            addgvar("GRUPLOG", h_type)
            await edit_or_reply(event, "**Group Log Berhasil Dimatikan**")
    elif h_type:
        addgvar("GRUPLOG", h_type)
        await edit_or_reply(event, "**Group Log Berhasil Diaktifkan**")
    else:
        await edit_or_reply(event, "**Group Log Sudah Dimatikan**")


CMD_HELP.update(
    {
        "log": f"**Plugin : **`log`\
        \n\n  »  **Perintah :** `{cmd}save`\
        \n  »  **Kegunaan : **__Untuk Menyimpan pesan yang ditandai ke grup pribadi.__\
        \n\n  »  **Perintah :** `{cmd}log`\
        \n  »  **Kegunaan : **__Untuk mengaktifkan Log Chat dari obrolan/grup itu.__\
        \n\n  »  **Perintah :** `{cmd}nolog`\
        \n  »  **Kegunaan : **__Untuk menonaktifkan Log Chat dari obrolan/grup itu.__\
        \n\n  »  **Perintah :** `{cmd}pmlog on/off`\
        \n  »  **Kegunaan : **__Untuk mengaktifkan atau menonaktifkan pencatatan pesan pribadi__\
        \n\n  »  **Perintah :** `{cmd}gruplog on/off`\
        \n  »  **Kegunaan : **__Untuk mengaktifkan atau menonaktifkan tag grup, yang akan masuk ke grup pmlogger.__"
    }
)
