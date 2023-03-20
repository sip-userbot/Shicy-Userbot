from time import sleep

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd, eor
from Stringchiy import get_string

@shicy_cmd(pattern=r"lipkol(?: |$)(.*)")
async def _(a):
    shicy = await eor(a, get_string("cibot_51"))
    sleep(2)
    await shicy.edit(get_string("cibot_52"))
    sleep(1)
    await shicy.edit(get_string("cibot_53"))


# Create by myself @localheart


@shicy_cmd(pattern=r"nakal(?: |$)(.*)")
async def _(y):
    shicy = await eor(y, get_string("cibot_54"))
    sleep(1)
    await shicy.edit(get_string("cibot_55"))
    sleep(1)
    await shicy.edit(get_string("cibot_56"))
    sleep(1)
    await shicy.edit(get_string("cibot_57"))


@shicy_cmd(pattern=r"favboy(?: |$)(.*)")
async def _(i):
    shicy = await eor(i, get_string("cibot_58"))
    sleep(1.5)
    await shicy.edit(get_string("cibot_59"))
    sleep(1.5)
    await shicy.edit(get_string("cibot_60"))
    sleep(1.5)
    await shicy.edit(get_string("cibot_61"))
    sleep(1.5)
    await shicy.edit(get_string("cibot_62"))


@shicy_cmd(pattern=r"favgirl(?: |$)(.*)")
async def _(i):
    shicy = await eor(i, get_string("cibot_63"))
    sleep(2)
    await shicy.edit(get_string("cibot_64"))
    sleep(2)
    await shicy.edit(get_string("cibot_65"))
    sleep(2)
    await shicy.edit(get_string("cibot_66"))
    sleep(2)
    await shicy.edit(get_string("cibot_67"))


@shicy_cmd(pattern=r"canlay(?: |$)(.*)")
async def _(n):
    shicy = await eor(n, get_string("cibot_68"))
    sleep(2)
    await shicy.edit(get_string("cibot_69"))
    sleep(2)
    await shicy.edit(get_string("cibot_70"))
    sleep(2)
    await shicy.edit(get_string("cibot_71"))
    sleep(2)
    await shicy.edit(get_string("cibot_72"))


@shicy_cmd(pattern=r"ganlay(?: |$)(.*)")
async def _(x):
    shicy = await eor(x, get_string("cibot_73"))
    sleep(2)
    await shicy.edit(get_string("cibot_69"))
    sleep(2)
    await shicy.edit(get_string("cibot_70"))
    sleep(2)
    await shicy.edit(get_string("cibot_71"))
    sleep(2)
    await shicy.edit(get_string("cibot_72"))


@shicy_cmd(pattern=r"ange(?: |$)(.*)")
async def _(d):
    shicy = await eor(d, get_string("cibot_74"))
    sleep(1)
    await shicy.edit(get_string("cibot_75"))
    sleep(1)
    await shicy.edit(get_string("cibot_76"))


CMD_HELP.update(
    {
        "chiyubot2": f"**Plugin : **`chiyubot2`\
        \n\n  »  **Perintah :** `{cmd}lipkol`\
        \n  »  **Kegunaan : **Ngajakin ayang slipkol\
        \n\n  »  **Perintah :** `{cmd}nakal`\
        \n  »  **Kegunaan : **Ga like ayang nakal\
        \n\n  »  **Perintah :** `{cmd}favboy`\
        \n  »  **Kegunaan : **Cowo idaman\
        \n\n  »  **Perintah :** `{cmd}favgirl`\
        \n  »  **Kegunaan : **Cewe idaman\
        \n\n  »  **Perintah :** `{cmd}canlay`\
        \n  »  **Kegunaan : **Ngatain si cantik alay\
        \n\n  »  **Perintah :** `{cmd}ganlay`\
        \n  »  **Kegunaan : **Ngatain si ganteng alay\
        \n\n  »  **Perintah :** `{cmd}ange`\
        \n  »  **Kegunaan : **Minta jatah ke ayang\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
