import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd, eod, eor
from Stringchiy import get_string


@shicy_cmd(pattern="logo(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    aing = await event.client.get_me()
    text = event.pattern_match.group(1)
    if not text:
        await eod(event, get_string("logo_1"))
    else:
        await eor(event, get_string("com_1"))
    chat = "@tdtapibot"
    async with event.client.conversation(chat) as conv:
        try:
            msg = await conv.send_message(f"/logo {text}")
            response = await conv.get_response()
            logo = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await event.client(UnblockRequest(chat))
            msg = await conv.send_message(f"/logo {text}")
            response = await conv.get_response()
            logo = await conv.get_response()
            await event.client.send_read_acknowledge(conv.chat_id)
        await asyncio.sleep(0.5)
        await event.client.send_file(
            event.chat_id,
            logo,
            caption=get_string("logo_2").format(aing.first_name, aing.id),
        )
        await event.client.delete_messages(conv.chat_id, [msg.id, response.id, logo.id])
        await event.delete()


CMD_HELP.update(
    {
        "logo": f"**Plugin : **`logo`\
        \n\n  »  **Perintah :** `{cmd}logo` <text>\
        \n  »  **Kegunaan : **Membuat logo dari Teks yang diberikan\
    "
    }
)
