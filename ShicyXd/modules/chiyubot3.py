from time import sleep

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd, eor
from Stringchiy import get_string

@shicy_cmd(pattern=r"chiy(?: |$)(.*)")
async def _(y):
    shicy = await eor(y, get_string("cibot_77"))
    sleep(3)
    await shicy.edit(get_string("cibot_78"))
    sleep(2)
    await shicy.edit(get_string("cibot_79"))
    sleep(3)
    await shicy.edit(get_string("cibot_80"))
# Create by myself @ShicyXd


@shicy_cmd(pattern=r"sayang(?: |$)(.*)")
async def _(i):
    xx = await eor(i, get_string("cibot_81"))
    sleep(3)
    await xx.edit(get_string("cibot_82"))
# Create by myself @ShicyXd


@shicy_cmd(pattern=r"semangat(?: |$)(.*)")
async def _(n):
    shicy = await eor(n, get_string("cibot_83"))
    sleep(3)
    await shicy.edit(get_string("cibot_84"))
    sleep(1)
    await shicy.edit(get_string("cibot_85"))
# Create by myself @ShicyXd


@shicy_cmd(pattern=r"mengeluh(?: |$)(.*)")
async def _(s):
    shicy = await eor(s, get_string("cibot_83"))
    sleep(3)
    await shicy.edit(get_string("cibot_86"))
    sleep(1)
    await shicy.edit(get_string("cibot_87"))
# Create by myself @ShicyXd


CMD_HELP.update(
    {
        "chiyubot3": f"**Plugin : **`chiyubot3`\
        \n\n  »  **Perintah :** `{cmd}chiy`\
        \n  »  **Kegunaan : **Perkenalan diri chiy\
        \n\n  »  **Perintah :** `{cmd}sayang`\
        \n  »  **Kegunaan : **Bucin\
        \n\n  »  **Perintah :** `{cmd}semangat`\
        \n  »  **Kegunaan : **Memberikan semangat!\
        \n\n  »  **Perintah :** `{cmd}mengeluh`\
        \n  »  **Kegunaan : **Ngeledek\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
