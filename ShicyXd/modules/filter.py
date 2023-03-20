""" Userbot module for filter commands """

from asyncio import sleep
from re import IGNORECASE, escape, search

from ShicyXd import BLACKLIST_CHAT, BOTLOG_CHATID
from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP, bot
from ShicyXd.events import shicy_cmd, register
from Stringchiy import get_string


@register(incoming=True, disable_edited=True, disable_errors=True)
async def filter_incoming_handler(handler):
    """Checks if the incoming message contains handler of a filter"""
    try:
        if not (await handler.get_sender()).bot:
            try:
                from ShicyXd.modules.sql_helper.filter_sql import get_filters
            except AttributeError:
                await handler.edit(get_string("not_sql"))
                return
            name = handler.raw_text
            filters = get_filters(handler.chat_id)
            if not filters:
                return
            for trigger in filters:
                pattern = r"( |^|[^\w])" + \
                    escape(trigger.keyword) + r"( |$|[^\w])"
                pro = search(pattern, name, flags=IGNORECASE)
                if pro and trigger.f_mesg_id:
                    msg_o = await handler.client.get_messages(
                        entity=BOTLOG_CHATID, ids=int(trigger.f_mesg_id)
                    )
                    await handler.reply(msg_o.message, file=msg_o.media)
                elif pro and trigger.reply:
                    await handler.reply(trigger.reply)
    except AttributeError:
        pass


@bot.on(shicy_cmd(outgoing=True, pattern=r"filter (.*)"))
async def add_new_filter(new_handler):
    """For .filter command, allows adding new filters in a chat"""
    if new_handler.chat_id in BLACKLIST_CHAT:
        return await new_handler.edit(get_string("shicy_1")
        )
    try:
        from ShicyXd.modules.sql_helper.filter_sql import add_filter
    except AttributeError:
        await new_handler.edit(get_string("not_sql"))
        return
    value = new_handler.pattern_match.group(1).split(None, 1)
    """ - The first words after .filter(space) is the keyword - """
    keyword = value[0]
    try:
        string = value[1]
    except IndexError:
        string = None
    msg = await new_handler.get_reply_message()
    msg_id = None
    if msg and msg.media and not string:
        if BOTLOG_CHATID:
            await new_handler.client.send_message(
                BOTLOG_CHATID, get_string("flr_7").format(new_handler.chat_id, keyword)
            )
            msg_o = await new_handler.client.forward_messages(
                entity=BOTLOG_CHATID,
                messages=msg,
                from_peer=new_handler.chat_id,
                silent=True,
            )
            msg_id = msg_o.id
        else:
            return await new_handler.edit(get_string("flr_8")
            )
    elif new_handler.reply_to_msg_id and not string:
        rep_msg = await new_handler.get_reply_message()
        string = rep_msg.text
    if add_filter(str(new_handler.chat_id), keyword, string, msg_id) is True:
        await new_handler.edit(get_string("flr_4").format(keyword, "Disini"))
    else:
        await new_handler.edit(get_string("flr_4").format(keyword, "Disini"))


@bot.on(shicy_cmd(outgoing=True, pattern=r"stop (.*)"))
async def remove_a_filter(r_handler):
    """For .stop command, allows you to remove a filter from a chat."""
    try:
        from ShicyXd.modules.sql_helper.filter_sql import remove_filter
    except AttributeError:
        return await r_handler.edit(get_string("not_sql"))
    filt = r_handler.pattern_match.group(1)
    if not remove_filter(r_handler.chat_id, filt):
        await r_handler.edit(get_string("flr_9").format(filt))
    else:
        await r_handler.edit(get_string("flr_5").format(filt)
        )


@bot.on(shicy_cmd(outgoing=True, pattern=r"delfilterbot (.*)"))
async def kick_marie_filter(event):
    """ For .bersihkanbotfilter command, allows you to kick all \
        Marie(or her clones) filters from a chat. """
    bot_type = event.pattern_match.group(1).lower()
    if bot_type not in ["marie", "rose"]:
        return await event.edit(get_string("flr_10"))
    await event.edit(get_string("flr_11"))
    await sleep(3)
    resp = await event.get_reply_message()
    filters = resp.text.split("-")[1:]
    for i in filters:
        if bot_type.lower() == "marie":
            await event.reply("/stop %s" % (i.strip()))
        if bot_type.lower() == "rose":
            i = i.replace("`", "")
            await event.reply("/stop %s" % (i.strip()))
        await sleep(0.3)
    await event.respond(get_string("flr_12"))
    if BOTLOG_CHATID:
        await event.client.send_message(
            BOTLOG_CHATID, get_string("flr_13").format(str(event.chat_id))
        )


@bot.on(shicy_cmd(outgoing=True, pattern=r"filters$"))
async def filters_active(event):
    """For .filters command, lists all of the active filters in a chat."""
    try:
        from ShicyXd.modules.sql_helper.filter_sql import get_filters
    except AttributeError:
        return await event.edit(get_string("not_sql"))
    transact = get_string("flr_6")
    filters = get_filters(event.chat_id)
    for filt in filters:
        if transact == get_string("flr_6"):
            transact = get_string("flr_2")
        transact += " ⍟ `{}`\n".format(filt.keyword)
    await event.edit(transact)


CMD_HELP.update(
    {
        "filter": f"**Plugin : **`filter`\
        \n\n  »  **Perintah :** `{cmd}filters`\
        \n  »  **Kegunaan : **Melihat filter userbot yang aktif di obrolan.\
        \n\n  »  **Perintah :** `{cmd}filter` <keyword> <balasan> atau balas ke pesan ketik `{cmd}filter` <keyword>\
        \n  »  **Kegunaan : **Membuat filter di obrolan, Bot Akan Membalas Jika Ada Yang Menyebut 'keyword' yang dibuat. Bisa dipakai ke media/sticker/vn/file.\
        \n\n  »  **Perintah :** `{cmd}stop` <keyword>\
        \n  »  **Kegunaan : **Untuk Nonaktifkan Filter.\
        \n\n  »  **Perintah :** `{cmd}delfilterbot` <marie/rose>\
        \n  »  **Kegunaan : **Menghapus semua filter yang ada di bot grup (Saat ini bot yang didukung: Marie, Rose.) dalam obrolan.\
    "
    }
)
