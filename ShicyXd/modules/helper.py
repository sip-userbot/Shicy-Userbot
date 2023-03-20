""" Userbot module for other small commands. """
from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd, eor
from Stringchiy import get_string


@shicy_cmd(pattern="ihelp$")
async def usit(event):
    me = await event.client.get_me()
    await eor(event, get_string("hlpr_1").format(me.first_name)
    )


@shicy_cmd(pattern="listvar$")
async def var(event):
    await eor(event, get_string("hlpr_2")
    )


CMD_HELP.update(
    {
        "helper": f"**Plugin : **`helper`\
        \n\n  »  **Perintah :** `{cmd}ihelp`\
        \n  »  **Kegunaan : **Bantuan Untuk Shicy-Userbot.\
        \n\n  »  **Perintah :** `{cmd}listvar`\
        \n  »  **Kegunaan : **Melihat Daftar Vars.\
        \n\n  »  **Perintah :** `{cmd}repo`\
        \n  »  **Kegunaan : **Melihat Repository Shicy-Userbot.\
        \n\n  »  **Perintah :** `{cmd}string`\
        \n  »  **Kegunaan : **Link untuk mengambil String Shicy-Userbot.\
    "
    }
)
