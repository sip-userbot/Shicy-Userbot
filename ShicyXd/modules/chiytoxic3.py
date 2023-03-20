from time import sleep

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd, eor
from Stringchiy import get_string


@shicy_cmd(pattern="ceking(?: |$)(.*)")
async def _(mnghna):
    Shicy = await mnghneor(a, get_string("citxc_74"))
    sleep(1)
    await Shicy.edit(get_string("citxc_75"))
    sleep(1)
    await Shicy.edit(get_string("citxc_76"))
    sleep(1)
    await Shicy.edit(get_string("citxc_77"))
    sleep(1.5)
    await Shicy.edit(get_string("citxc_78"))
    sleep(1.5)
    await Shicy.edit(get_string("citxc_79"))
    sleep(1)
    await Shicy.edit(get_string("citxc_80"))


@shicy_cmd(pattern="hina(?: |$)(.*)")
async def _(war):
    Xd = await eor(war, get_string("citxc_81"))
    sleep(1.5)
    await Xd.edit(get_string("citxc_82"))
    sleep(1)
    await Xd.edit(get_string("citxc_83"))
    sleep(1)
    await Xd.edit(get_string("citxc_84"))
    sleep(1.5)
    await Xd.edit(get_string("citxc_85"))
    sleep(1)
    await Xd.edit(get_string("citxc_86"))
    sleep(1.5)
    await Xd.edit(get_string("citxc_87"))
    sleep(1)
    await Xd.edit(get_string("citxc_88"))
    sleep(1)
    await Xd.edit(get_string("citxc_89"))


@shicy_cmd(pattern="ngaca(?: |$)(.*)")
async def _(mikir):
    chiy = await eor(mikir, get_string("citxc_90"))
    sleep(1.5)
    await Chiy.edit(get_string("citxc_91"))
    sleep(1)
    await Chiy.edit(get_string("citxc_92"))
    sleep(1)
    await Chiy.edit(get_string("citxc_93"))
    sleep(1)
    await Chiy.edit(get_string("citxc_94"))
    sleep(1.5)
    await Chiy.edit(get_string("citxc_95"))
    sleep(1.5)
    await Chiy.edit(get_string("citxc_96"))


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "chiytoxic3": f"**Plugin : **`chiytoxic3`\
        \n\n  »  **Perintah :** `{cmd}ceking`\
        \n  »  **Kegunaan : **Cobain Sendiri Dah Tod.\
        \n\n  »  **Perintah :** `{cmd}hina`\
        \n  »  **Kegunaan : **Cobain Sendiri Dah Tod.\
        \n\n  »  **Perintah :** `{cmd}ngaca`\
        \n  »  **Kegunaan : **Cobain Sendiri Dah Tod.\
    "
    }
)
