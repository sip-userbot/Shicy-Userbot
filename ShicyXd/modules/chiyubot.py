from time import sleep

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd, eor
from Stringchiy import get_string


@shicy_cmd(pattern=r"sadboy(?: |$)(.*)")
async def _(a):
    shicy = eor(a, get_string("cibot_1"))
    sleep(2)
    await shicy.edit(get_string("cibot_2"))
    sleep(1)
    await shicy.edit(get_string("cibot_3"))

# Create by myself @localheart


@shicy_cmd(pattern=r"lah(?: |$)(.*)")
async def _(y):
    shicy = await eor(y, get_string("cibot_4"))
    sleep(1)
    await shicy.edit(get_string("cibot_5"))
    sleep(1)
    await shicy.edit(get_string("cibot_6"))
    sleep(1)
    await shicy.edit(get_string("cibot_7"))


@shicy_cmd(pattern=r"sok(?: |$)(.*)")
async def _(i):
    shicy = await eor(i, get_string("cibot_8"))
    sleep(2)
    await shicy.edit(get_string("cibot_9"))
    sleep(2)
    await shicy.edit(get_string("cibot_10"))
    sleep(2)
    await shicy.edit(get_string("cibot_11"))
    sleep(2)
    await shicy.edit(get_string("cibot_12"))


@shicy_cmd(pattern=r"wah(?: |$)(.*)")
async def _(i):
    shicy = await eor(i, get_string("cibot_13"))
    sleep(2)
    await shicy.edit(get_string("cibot_14"))
    sleep(2)
    await shicy.edit(get_string("cibot_15"))
    sleep(2)
    await shicy.edit(get_string("cibot_16"))
    sleep(2)
    await shicy.edit(get_string("cibot_17"))
    sleep(2)
    await shicy.edit(get_string("cibot_18"))
    sleep(3)
    await shicy.edit(get_string("cibot_19"))


@shicy_cmd(pattern=r"alay(?: |$)(.*)")
async def _(n):
    shicy = await eor(n, get_string("cibot_20"))
    sleep(2)
    await shicy.edit(get_string("cibot_21"))
    sleep(2)
    await shicy.edit(get_string("cibot_22"))
    sleep(2)
    await shicy.edit(get_string("cibot_23"))
    sleep(2)
    await shicy.edit(get_string("cibot_24"))


@shicy_cmd(pattern=r"erpe(?: |$)(.*)")
async def _(x):
    shicy = await eor(x, get_string("cibot_25"))
    sleep(1)
    await shicy.edit(get_string("cibot_26"))
    sleep(1)
    await shicy.edit(get_string("cibot_27"))
    sleep(1)
    await shicy.edit(get_string("cibot_28"))
    sleep(1)
    await shicy.edit(get_string("cibot_29"))
    sleep(1)
    await shicy.edit(get_string("cibot_30"))
    sleep(1)
    await shicy.edit(get_string("cibot_31"))
    sleep(1)
    await shicy.edit(get_string("cibot_32"))
    sleep(1)
    await shicy.edit(get_string("cibot_33"))


@shicy_cmd(pattern=r"tittle(?: |$)(.*)")
async def _(d):
    shicy = await eor(d, get_string("cibot_34"))
    sleep(2)
    await shicy.edit(get_string("cibot_35"))
    sleep(2)
    await shicy.edit(get_string("cibot_36"))
    sleep(2)
    await shicy.edit(get_string("cibot_37"))
    sleep(2)
    await shicy.edit(get_string("cibot_38"))
    sleep(2)
    await shicy.edit(get_string("cibot_39"))
    sleep(2)
    await shicy.edit(get_string("cibot_40"))
    sleep(2)
    await shicy.edit(get_string("cibot_41"))
    sleep(2)
    await shicy.edit(get_string("cibot_42"))
    sleep(2)
    await shicy.edit(get_string("cibot_43"))
    sleep(2)
    await shicy.edit(get_string("cibot_44"))
    sleep(2)
    await shicy.edit(get_string("cibot_45"))
    sleep(2)
    await shicy.edit(get_string("cibot_46"))
    sleep(4)
    await shicy.edit(get_string("cibot_47"))
    sleep(2)
    await shicy.edit(get_string("cibot_48"))
    sleep(3)
    await shicy.edit(get_string("cibot_49"))
    sleep(3)
    await shicy.edit(get_string("cibot_50"))


CMD_HELP.update(
    {
        "chiyubot": f"**Plugin : **`chiyubot`\
        \n\n  »  **Perintah :** `{cmd}sadboy`\
        \n  »  **Kegunaan : **Gombalan sad\
        \n\n  »  **Perintah :** `{cmd}wah`\
        \n  »  **Kegunaan : **Ngeledek orang sok war\
        \n\n  »  **Perintah :** `{cmd}sok`\
        \n  »  **Kegunaan : **Ngeledek orang sok keras\
        \n\n  »  **Perintah :** `{cmd}lah`\
        \n  »  **Kegunaan : **Engga ketrigger tod\
        \n\n  »  **Perintah :** `{cmd}alay`\
        \n  »  **Kegunaan : **Ngatain orang spam bot\
        \n\n  »  **Perintah :** `{cmd}erpe`\
        \n  »  **Kegunaan : **Ngatain anak erpe\
        \n\n  »  **Perintah :** `{cmd}tittle`\
        \n  »  **Kegunaan : **Ngatain jamet haus tittle\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
