
from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd, eor
from Stringchiy import get_string


@shicy_cmd(pattern="d(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("citxc_1"))


@shicy_cmd(pattern="e(?: |$)(.*)")
async def _(y):
    await eor(y, get_string("citxc_2"))


@shicy_cmd(pattern="f(?: |$)(.*)")
async def _(i):
    await eor(i, get_string("citxc_3"))


@shicy_cmd(pattern="i(?: |$)(.*)")
async def _(n):
    await eor(n, get_string("citxc_4"))


@shicy_cmd(pattern="r(?: |$)(.*)")
async def _(x):
    await eor(x, get_string("citxc_5"))


@shicy_cmd(pattern="t(?: |$)(.*)")
async def _(d):
    await eor(d, get_string("citxc_6"))


@shicy_cmd(pattern="u(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("citxc_7"))


@shicy_cmd(pattern="w(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("citxc_8"))


@shicy_cmd(pattern="bct(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("citxc_9"))


@shicy_cmd(pattern="n(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("citxc_10"))


@shicy_cmd(pattern="b(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("citxc_11"))


@shicy_cmd(pattern="m(?: |$)(.*)")
async def _(y):
    await eor(y, get_string("citxc_12"))


@shicy_cmd(pattern="c(?: |$)(.*)")
async def _(y):
    await eor(y, get_string("citxc_13"))


@shicy_cmd(pattern="x(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("citxc_14"))


@shicy_cmd(pattern="v(?: |$)(.*)")
async def _(y):
    await eor(y, get_string("citxc_15"))


@shicy_cmd(pattern="j(?: |$)(.*)")
async def _(i):
    await eor(i, get_string("citxc_16"))


@shicy_cmd(pattern="z(?: |$)(.*)")
async def _(i):
    await eor(i, get_string("citxc_17"))


@shicy_cmd(pattern="g(?: |$)(.*)")
async def _(n):
    await eor(n, get_string("citxc_18"))


@shicy_cmd(pattern="yy(?: |$)(.*)")
async def _(x):
    await eor(x, get_string("citxc_19"))

@shicy_cmd(pattern="h(?: |$)(.*)")
async def _(d):
    await eor(d, get_string("citxc_20"))


@shicy_cmd(pattern="o(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("citxc_21"))


@shicy_cmd(pattern="a(?: |$)(.*)")
async def _(a):
    await eor(a, get_string("citxc_22"))


CMD_HELP.update(
    {
        "chiytoxic": f"**Plugin : **`chiytoxic`\
        \n\n  »  **Perintah :** `{cmd}d`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}e`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}f`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}i`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}r`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}t`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}u`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}w`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}z`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}n`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}b`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}m`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}c`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}x`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}v`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}a`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}j`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}g`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}yy`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}h`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}o`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n  »  **Perintah :** `{cmd}bct`\
        \n  »  **Kegunaan : **Cobain sendiri tod\
        \n\n**Klo mau Req, kosa kata dari lu Bisa pake Module costum. Ketik** `{cmd}help costum`\
    "
    }
)
