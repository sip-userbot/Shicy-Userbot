from secrets import choice

from telethon.tl.types import InputMessagesFilterVideo

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP, BLACKLIST_CHAT
from ShicyXd.shicy import shicy_cmd, eod, eor
from Stringchiy import get_string


@shicy_cmd(pattern="bokp$")
async def _(shicy):
    if shicy.chat_id in BLACKLIST_CHAT:
        return await eod(shicy, get_string("shicy_1"), time=45)
    chiy = await eor(shicy, get_string("com_1"))
    try:
        asuchiy = [
            asupan
            async for asupan in shicy.client.iter_messages(
                "@ShicyBokep", filter=InputMessagesFilterVideo
            )
        ]
        awake = await shicy.client.get_me()
        await shicy.client.send_file(
            shicy.chat_id,
            file=choice(asuchiy),
            caption=get_string("cibkp_1").format(awake.first_name, awake.id)
        )
        await chiy.delete()
    except Exception:
        await chiy.edit(get_string("cibkp_2"))


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "chiybokep": f"**Plugin :** `chiybokep`\
        \n\n  »  **Perintah :** {cmd}bokp\
        \n  »  **Kegunaan : **Untuk Mengirim bokp secara random.\
    "
    }
)
