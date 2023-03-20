# Port By @VckyouuBitch From GeezProject
# Perkontolan Dengan Hapus Credits
# Recode By : @ShicyXd

from asyncio import sleep

from telethon.tl.types import ChatBannedRights
from telethon.tl.functions.channels import EditBannedRequest
from telethon.tl.types import ChannelParticipantsKicked

from ShicyXd import CMD_HELP
from ShicyXd import CMD_HANDLER as cmd
from ShicyXd.shicy import shicy_cmd, eod, eor
from Stringchiy import get_string


@shicy_cmd(pattern="banall(?: |$)(.*)")
async def testing(shicyxd):
    shicy = await shicyxd.get_chat()
    chiy = await shicyxd.client.get_me()
    admin = shicy.admin_rights
    creator = shicy.creator
    if not admin and not creator:
        await eod(shicyxd, get_string("stvc_1").format(chiy.first_name))
        return
    xnxx = await eor(shicyxd, get_string("ciban_1"))
# Thank for Dark_Cobra
    shicykontol = await shicyxd.client.get_participants(shicyXd.chat_id)
    for user in shicykontol:
        if user.id == chiy.id:
            pass
        try:
            xx = await shicyxd.client(EditBannedRequest(ShicyXd.chat_id, int(user.id), ChatBannedRights(until_date=None, view_messages=True)))
        except Exception as e:
            await eod(xnxx, get_string("error_1").format(str(e)))
        await sleep(.5)
    await xnxx.edit(get_string("ciban_2"))


@shicy_cmd(pattern="unbanall(?: |$)(.*)")
async def _(shicy):
    chiy = await eor(shicy, get_string("ciban_3"))
    p = 0
    (await shicy.get_chat()).title
    async for i in shicy.client.iter_participants(
        shicy.chat_id,
        filter=ChannelParticipantsKicked,
        aggressive=True,
    ):
        try:
            await shicy.client.edit_permissions(shicy.chat_id, i, view_messages=True)
            p += 1
        except BaseException:
            pass
    await chiy.edit(get_string("ciban_4").format(p))


CMD_HELP.update(
    {
        "chiyban": f"**Plugin : **`chiyban`\
        \n\n  »  **Perintah :** `{cmd}banall`\
        \n  »  **Kegunaan :** Banned Semua Member Dalam Satu Ketikan.\
        \n\n  »  **Perintah :** `{cmd}unbanall`\
        \n  »  **Kegunaan :** Membatalkan Banned Anggota Group.\
    "
    }
)
