from time import sleep

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd


@shicy_cmd(pattern="sadboy(?: |$)(.*)")
async def _(event):
    await event.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await event.edit("`Kedua kamu manis`")
    sleep(1)
    await event.edit("`Dan yang terakhir adalah kamu bukan jodohku`")


# Create by myself @localheart


@shicy_cmd(pattern="punten(?: |$)(.*)")
async def _(event):
    await event.edit(
        "`\n┻┳|―-∩`"
        "`\n┳┻|     ヽ`"
        "`\n┻┳|    ● |`"
        "`\n┳┻|▼) _ノ`"
        "`\n┻┳|￣  )`"
        "`\n┳ﾐ(￣ ／`"
        "`\n┻┳T￣|`"
        "\n**Punten**"
    )


@shicy_cmd(pattern="pantau(?: |$)(.*)")
async def _(event):
    await event.edit(
        "`\n┻┳|―-∩`"
        "`\n┳┻|     ヽ`"
        "`\n┻┳|    ● |`"
        "`\n┳┻|▼) _ノ`"
        "`\n┻┳|￣  )`"
        "`\n┳ﾐ(￣ ／`"
        "`\n┻┳T￣|`"
        "\n**Masih Gua Pantau**"
    )


# Create by myself @localheart


CMD_HELP.update(
    {
        "punten": f"**Plugin : **`Animasi Punten`\
        \n\n  »  **Perintah :** `{cmd}punten` ; `{cmd}pantau`\
        \n  »  **Kegunaan : **Arts Beruang kek lagi mantau.\
        \n\n  »  **Perintah :** `{cmd}sadboy`\
        \n  »  **Kegunaan : **ya sadboy coba aja.\
    "
    }
)
