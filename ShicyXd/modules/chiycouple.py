from secrets import choice
from telethon.tl.types import InputMessagesFilterPhotos

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd, eor
from Stringchiy import get_string


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@shicy_cmd(pattern="couple(?: |$)(.*)")
async def couple(bucin):
    copl = await eor(bucin, get_string("com_1"))
    try:
        bucinan = [
            coupl
            async for coupl in bucin.client.iter_messages(
                "@ppayiinuserbot", filter=InputMessagesFilterPhotos
            )
        ]
        cang = await bucin.client.get_me()
        await bucin.client.send_file(
            bucin.chat_id,
            file=choice(bucinan),
            caption=get_string("cicpl_1"). format(cang.first_name, cang.id)
        )
        await copl.delete()
    except Exception:
        await copl.edit(get_string("cicpl_2"))


CMD_HELP.update(
    {
        "chiycouple": f"**Plugin :** `chiycouple`\
        \n\n  »  **Perintah :** `{cmd}couple`\
        \n  »  **Kegunaan :** __Untuk Mendapatkan Foto Couple Secara Random.__\
    "
    }
)
