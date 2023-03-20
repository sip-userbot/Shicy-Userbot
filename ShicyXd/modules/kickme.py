from telethon.tl.functions.channels import LeaveChannelRequest

from ShicyXd import BLACKLIST_CHAT
from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd, eor
from Stringchiy import get_string


@shicy_cmd(pattern="kickme$", allow_sudo=False)
async def kickme(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await eor(
            event, get_string("shicy_1"))
    user = await event.client.get_me()
    await eor(event, get_string("kikme_1").format(user.first_name))
    await event.client.kick_participant(event.chat_id, "me")


@shicy_cmd(pattern="kikme$", allow_sudo=False)
async def kikme(event):
    if event.chat_id in BLACKLIST_CHAT:
        return await eor(
            event, get_string("shicy_1")
        )
    await eor(event, get_string("kikme_2"))
    await event.client.kick_participant(event.chat_id, "me")


@shicy_cmd(pattern="leaveall$", allow_sudo=False)
async def kickmeall(event):
    chiy = await eor(event, get_string("kikme_3"))
    er = 0
    done = 0
    async for x in event.client.iter_dialogs():
        if x.is_group:
            chat = x.id
            try:
                done += 1
                await event.client(LeaveChannelRequest(chat))
            except BaseException:
                er += 1
    await chiy.edit(get_string("kikme_4").format(done, er)
    )


CMD_HELP.update(
    {
        "kickme": f"**Plugin : **`kickme`\
        \n\n  »  **Perintah :** `{cmd}kickme`\
        \n  »  **Kegunaan : **Keluar grup dengan menampilkan pesan Master has left this group, bye!!\
        \n\n  »  **Perintah :** `{cmd}kikme`\
        \n  »  **Kegunaan : **Keluar grup dengan menampilkan pesan GC NYA JELEK GOBLOK KELUAR DULU AH CROTT 🥴\
        \n\n  »  **Perintah :** `{cmd}leaveall`\
        \n  »  **Kegunaan : **Keluar dari semua grup telegram yang anda gabung.\
    "
    }
)
