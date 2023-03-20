from time import sleep

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd, eor
from Stringchiy import get_string

@shicy_cmd(pattern=r"ganteng(?: |$)(.*)")
async def _(y):
    shicy = await eor(y, get_string("chiy_36"))
    sleep(3)
    await shicy.edit(get_string("chiy_37"))
    sleep(3)
    await shicy.edit(get_string("chiy_38"))

@shicy_cmd(pattern=r"wibu(?: |$)(.*)")
async def _(i):
    shicy = await eor(i, get_string("chiy_39"))
    sleep(2)
    await shicy.edit(get_string("chiy_40"))
    sleep(3)
    await shicy.edit(get_string("chiy_41"))
    sleep(3)
    await shicy.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻`")
    await shicy.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨`")
    await shicy.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤ`")
    await shicy.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤ`")
    await shicy.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤ`")
    await shicy.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤ`")
    await shicy.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤ`")
    await shicy.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤ`")
    await shicy.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤ`")
    await shicy.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await shicy.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await shicy.edit("`ㅤㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await shicy.edit("`ㅤㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await shicy.edit("`ㅤㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await shicy.edit("`ㅤㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await shicy.edit("`ㅤㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await shicy.edit("`ㅤㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await shicy.edit("`ㅤㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await shicy.edit("`ㅤ🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await shicy.edit("`🏃🏻💨ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ`")
    await shicy.edit(get_string("chiy_42"))

# create by shicy


@shicy_cmd(pattern=r"senggol(?: |$)(.*)")
async def _(n):
    shicy = await eor(n, get_string("chiy_43"))
    sleep(2)
    await shicy.edit(get_string("chiy_44"))


@shicy_cmd(pattern=r"^P(?: |$)(.*)")
async def _(s):
    shicy = await eor(s, get_string("chiy_45"))
    sleep(1)
    await shicy.edit(get_string("chiy_46"))


CMD_HELP.update(
    {
        "chiyubot5": f"**Plugin : **`chiyubot5`\
        \n\n  »  **Perintah :** `{cmd}ganteng`\
        \n  »  **Kegunaan : **Fakta Kalo Gua Ganteng\
        \n\n  »  **Perintah :** `{cmd}wibu`\
        \n  »  **Kegunaan : **Lari tod ada wibu\
        \n\n  »  **Perintah :** `{cmd}senggol`\
        \n  »  **Kegunaan : **Senggol dong tod\
        \n\n  »  **Perintah :** `P`\
        \n  »  **Kegunaan : **Bucin sopan\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
