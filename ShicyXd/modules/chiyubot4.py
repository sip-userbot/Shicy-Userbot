from time import sleep

from ShicyXd import BLACKLIST_CHAT
from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd, eod, eor
from Stringchiy import get_string

@shicy_cmd(pattern=r"ywc(?: |$)(.*)")
async def _(a):
    await a.edit(get_string("chiy_1"))


@shicy_cmd(pattern=r"jamet(?: |$)(.*)")
async def _(y):
    shicy = await eor(y, get_string("chiy_2"))
    sleep(1.5)
    await shicy.edit(get_string("chiy_3"))
    sleep(1.5)
    await shicy.edit(get_string("chiy_4"))
    sleep(1.5)
    await shicy.edit(get_string("chiy_5"))
    sleep(1.5)
    await shicy.edit(get_string("chiy_6"))
    sleep(1.5)
    await shicy.edit(get_string("chiy_7"))
    sleep(1.5)
    await shicy.edit(get_string("chiy_8"))
    sleep(1.5)
    await shicy.edit(get_string("chiy_9"))
    sleep(1.5)
    await shicy.edit(get_string("chiy_10"))
    sleep(1.5)
    await shicy.edit(get_string("chiy_11"))
    sleep(1.5)
    await shicy.edit(get_string("chiy_12"))


@shicy_cmd(pattern=r"pp(?: |$)(.*)")
async def _(i):
    await eor(i, get_string("chiy_13"))


@shicy_cmd(pattern=r"dp(?: |$)(.*)")
async def _(i):
    await eor(i, get_string("chiy_14"))


@shicy_cmd(pattern=r"so(?: |$)(.*)")
async def _(n):
    await eor(n, get_string("chiy_15"))


@shicy_cmd(pattern=r"nb(?: |$)(.*)")
async def _(x):
    if event.chat_id in BLACKLIST_CHAT:
        return await eod(x, get_string("shicy_1"), time=50)
    await eor(x, get_string("chiy_16"))
    await x.delete()


@shicy_cmd(pattern=r"met(?: |$)(.*)")
async def _(d):
    await eor(d, get_string("chiy_17"))


@shicy_cmd(pattern=r"war(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("chiy_18"))
    await a.delete()


@shicy_cmd(pattern=r"wartai(?: |$)(.*)")
async def _(y):
    await eor(y, get_string("chiy_19"))
    await y.delete()


@shicy_cmd(pattern=r"kismin(?: |$)(.*)")
async def _(i):
    await eor(i, get_string("chiy_20"))
    await i.delete()


@shicy_cmd(pattern=r"ded(?: |$)(.*)")
async def _(i):
    await eor(i, get_string("chiy_21"))
    await i.delete()


@shicy_cmd(pattern=r"sokab(?: |$)(.*)")
async def _(n):
    await eor(n, get_string("chiy_22"))
    await n.delete()


@shicy_cmd(pattern=r"gembel(?: |$)(.*)")
async def _(x):
    await eor(x, get_string("chiy_23"))
    await x.delete()


@shicy_cmd(pattern=r"cuih(?: |$)(.*)")
async def _(d):
    await eor(d, get_string("chiy_24"))
    await d.delete()


@shicy_cmd(pattern=r"dih(?: |$)(.*)")
async def _(y):
    await eor(y, get_string("chiy_25"))
    await y.delete()


@shicy_cmd(pattern=r"gcs(?: |$)(.*)")
async def _(i):
    if i.chat_id in BLACKLIST_CHAT:
        return await eod(i, get_string("shicy_1"))
    await eor(i, get_string("chiy_26"))
    await i.delete()


@shicy_cmd(pattern=r"skb(?: |$)(.*)")
async def _(n):
    await eor(n, get_string("chiy_27"))
    await n.delete()


@shicy_cmd(pattern=r"virtual(?: |$)(.*)")
async def _(s):
    shicy = await eor(s, get_string("chiy_28"))
    sleep(1.5)
    await shicy.edit(get_string("chiy_29"))
    sleep(1.5)
    await shicy.edit(get_string("chiy_30"))
    sleep(1.5)
    await shicy.edit(get_string("chiy_31"))
    sleep(1.5)
    await shicy.edit(get_string("chiy_32"))
    sleep(1.5)
    await shicy.edit(get_string("chiy_33"))
    sleep(1.5)
    await shicy.edit(get_string("chiy_34"))
    sleep(1.5)
    await shicy.edit(get_string("chiy_35"))


CMD_HELP.update(
    {
        "chiyubot4": f"**Plugin : **`war`\
        \n\n  »  **Perintah :** `{cmd}jamet`\
        \n  »  **Kegunaan : **Menghina Jamet telegram\
        \n\n  »  **Perintah :** `{cmd}pp`\
        \n  »  **Kegunaan : **Menghina Jamet telegram yang ga pake foto profil\
        \n\n  »  **Perintah :** `{cmd}dp`\
        \n  »  **Kegunaan : **Menghina Jamet muka hina!\
        \n\n  »  **Perintah :** `{cmd}so`\
        \n  »  **Kegunaan : **Ngeledek orang sokab\
        \n\n  »  **Perintah :** `{cmd}nb`\
        \n  »  **Kegunaan : **Ngeledek orang norak baru pake bot\
        \n\n  »  **Perintah :** `{cmd}skb`\
        \n  »  **Kegunaan : **Ngeledek orang sokab versi 2\
        \n\n  »  **Perintah :** `{cmd}met`\
        \n  »  **Kegunaan : **Ngeledek si jamet caper\
        \n\n  »  **Perintah :** `{cmd}war`\
        \n  »  **Kegunaan : **Ngeledek orang so keras ngajak war\
        \n\n  »  **Perintah :** `{cmd}wartai`\
        \n  »  **Kegunaan : **Ngeledek orang so ketrigger ngajak cod minta sharelok\
        \n\n  »  **Perintah :** `{cmd}kismin`\
        \n  »  **Kegunaan : **Ngeledek orang kismin so jagoan di tele\
        \n\n  »  **Perintah :** `{cmd}ded`\
        \n  »  **Kegunaan : **Nyuruh orang mati aja goblok wkwk\
        \n\n  »  **Perintah :** `{cmd}sokab`\
        \n  »  **Kegunaan : **Ngeledek orang so kenal so dekat padahal kga kenal goblok\
        \n\n  »  **Perintah :** `{cmd}gembel`\
        \n  »  **Kegunaan : **Ngeledek bapaknya si jamet\
        \n\n  »  **Perintah :** `{cmd}cuih`\
        \n  »  **Kegunaan : **Ngeludahin keluarganya satu satu wkwk\
        \n\n  »  **Perintah :** `{cmd}dih`\
        \n  »  **Kegunaan : **Ngeledek anak haram\
        \n\n  »  **Perintah :** `{cmd}gcs`\
        \n  »  **Kegunaan : **Ngeledek gc sampah\
        \n\n  »  **Perintah :** `{cmd}virtual`\
        \n  »  **Kegunaan : **Ngeledek orang pacaran virtual\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
