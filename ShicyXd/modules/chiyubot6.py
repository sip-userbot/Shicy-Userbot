from time import sleep
from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd, eor
from Stringchiy import get_string


@shicy_cmd(pattern="cacad(?: |$)(.*)")
async def _(x):
    chiy = await eor(x, get_string("chiy_47"))
    sleep(2)
    await chiy.edit(get_string("chiy_48"))
    sleep(1)
    await chiy.edit(get_string("chiy_49"))
    sleep(2)
    await chiy.edit(get_string("chiy_50"))


@shicy_cmd(pattern="hayo(?: |$)(.*)")
async def _(d):
    shicy = await eor(d, get_string("chiy_51"))
    sleep(1)
    await shicy.edit(get_string("chiy_52"))
    sleep(1)
    await shicy.edit(get_string("chiy_53"))
    sleep(1)
    await shicy.edit(get_string("chiy_54"))
    sleep(3)
    await shicy.edit(get_string("chiy_55"))
    sleep(2)
    await shicy.edit(get_string("chiy_56"))
    sleep(2)
    await shicy.edit(get_string("chiy_57"))
    sleep(2)
    await shicy.edit(get_string("chiy_58"))

CMD_HELP.update(
    {
        "chiyubot6": f"**Plugin : **`chiyubot6`\
        \n\n  »  **Perintah :** `{cmd}cacad`\
        \n  »  **Kegunaan :** Coba Sendiri Tod.\
        \n\n  »  **Perintah :** `{cmd}hayolo`\
        \n  »  **Kegunaan :** Coba Senditi Tod.\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
