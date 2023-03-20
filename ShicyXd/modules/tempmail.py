#
#

import asyncio

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP, bot
from ShicyXd.shicy import shicy_cmd, eor
from Stringchiy import get_string


@shicy_cmd(pattern=r"tm(?: |$)(.*)")
async def _(event):
    chat = "@TempMailBot"
    chiy = await eor(event, get_string("com_1"))
    async with bot.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(
                incoming=True,
                from_users=220112646
            )
            )
            await conv.send_message("/start")
            await asyncio.sleep(1)
            await conv.send_message("/create")
            response = await response
            shicyuserbot = ((response).reply_markup.rows[2].buttons[0].url)
            await event.client.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await chiy.edit(get_string("tempmail_2"))
            return
        await event.edit(get_string("tempmail_1").format(response.message.message, shicyuserbot))


CMD_HELP.update(
    {
        "tempmail": f"**Plugin : **`tempmail`\
        \n\n  »  **Perintah :** `{cmd}tm`\
        \n  »  **Kegunaan : Mendapatkan Email Gratis Dari Temp Mail"}
)
