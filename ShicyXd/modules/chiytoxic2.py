from time import sleep

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd, eor
from Stringchiy import get_string


@shicy_cmd(pattern=r"ngentot(?: |$)(.*)")
async def _(shicy):
    chiy = await eor(shicy, get_string("citxc_23"))
    sleep(1)
    await chiy.edit(get_string("citxc_24"))
    sleep(1)
    await chiy.edit(get_string("citxc_25"))
    sleep(1)
    await chiy.edit(get_string("citxc_26"))
    sleep(1)
    await chiy.edit(get_string("citxc_27"))
    sleep(1)
    await chiy.edit(get_string("citxc_28"))
    sleep(1)
    await chiy.edit(get_string("citxc_29"))
    sleep(1)
    await chiy.edit(get_string("citxc_30"))
    sleep(1)
    await chiy.edit(get_string("citxc_31"))
    sleep(1)
    await chiy.edit(get_string("citxc_32"))
# Create by myself @localheart


@shicy_cmd(pattern=r"goblok(?: |$)(.*)")
async def _(gblk):
    shicy = await eor(gblk, get_string("citxc_33"))
    sleep(1)
    await shicy.edit(get_string("citxc_34"))
    sleep(1)
    await shicy.edit(get_string("citxc_35"))
    sleep(1)
    await shicy.edit(get_string("citxc_36"))
    sleep(1)
    await shicy.edit(get_string("citxc_37"))
    sleep(1)
    await shicy.edit(get_string("citxc_38"))
    sleep(1)
    await shicy.edit(get_string("citxc_39"))
    sleep(1)
    await shicy.edit(get_string("citxc_40"))
    sleep(1)
    await shicy.edit(get_string("citxc_41"))
    sleep(1)
    await shicy.edit(get_string("citxc_42"))
# Create by myself @localheart


@shicy_cmd(pattern=r"ngatain(?: |$)(.*)")
async def _(kntl):
    xd = await eor(kntl, get_string("citxc_43"))
    sleep(1)
    await xd.edit(get_string("citxc_44"))
    sleep(1)
    await xd.edit(get_string("citxc_45"))
    sleep(1)
    await xd.edit(get_string("citxc_46"))
    sleep(1)
    await xd.edit(get_string("citxc_47"))
    sleep(1)
    await xd.edit(get_string("citxc_48"))
    sleep(1)
    await xd.edit(get_string("citxc_49"))
    sleep(1)
    await xd.edit(get_string("citxc_50"))
    sleep(1)
    await xd.edit(get_string("citxc_51"))
    sleep(1)
    await xd.edit(get_string("citxc_52"))
# Create by myself @localheart


@shicy_cmd(pattern=r"yatim(?: |$)(.*)")
async def _(ytim):
    ShicyXd = await eor(ytim, get_string("citxc_53"))
    sleep(1)
    await ShicyXd.edit(get_string("citxc_54"))
    sleep(1)
    await ShicyXd.edit(get_string("citxc_55"))
    sleep(1)
    await ShicyXd.edit(get_string("citxc_56"))
    sleep(1)
    await ShicyXd.edit(get_string("citxc_57"))
    sleep(1)
    await ShicyXd.edit(get_string("citxc_58"))
    sleep(1)
    await ShicyXd.edit(get_string("citxc_59"))
    sleep(1)
    await ShicyXd.edit(get_string("citxc_60"))
    sleep(1)
    await ShicyXd.edit(get_string("citxc_61"))
    sleep(1)
    await ShicyXd.edit(get_string("citxc_62"))
# Create by myself @localheart


@shicy_cmd(pattern=r"kont(?: |$)(.*)")
async def _(kontol):
    chiy = await eor(kontol, get_string("citxc_23"))
    sleep(1.5)
    await chiy.edit(get_string("citxc_63"))
    sleep(1.5)
    await chiy.edit(get_string("citxc_64"))
    sleep(1.5)
    await chiy.edit(get_string("citxc_65"))
    sleep(1.5)
    await chiy.edit(get_string("citxc_66"))
    sleep(1.5)
    await chiy.edit(get_string("citxc_67"))
    sleep(1.5)
    await chiy.edit(get_string("citxc_68"))
    sleep(1.5)
    await chiy.edit(get_string("citxc_69"))
    sleep(1.5)
    await chiy.edit(get_string("citxc_70"))
    sleep(1.5)
    await chiy.edit(get_string("citxc_71"))
    sleep(1.5)
    await chiy.edit(get_string("citxc_72"))
    sleep(1.5)
    await chiy.edit(get_string("citxc_73"))

CMD_HELP.update(
    {
        "chiytoxic2": f"**Plugin : **`chiytoxic2`\
        \n\n  »  **Perintah :** `{cmd}ngentot`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}goblok`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}ngatain`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}kont`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}yatim`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
