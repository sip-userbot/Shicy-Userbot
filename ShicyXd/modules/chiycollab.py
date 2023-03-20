import asyncio
from secrets import choice
from time import sleep

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import BLACKLIST_CHAT, CMD_HELP
from ShicyXd.shicy import asupan_sagapung, exolink
from ShicyXd.shicy import shicy_cmd, edit_or_reply


exorcist = "https://telegra.ph/file/fccecf320b30088410dcd.jpg"
asupung = "https://telegra.ph/file/82598bc741e3010339d4c.jpg"
exorcist2 = "https://telegra.ph/file/1002a84a022bd13663742.jpg"


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@shicy_cmd(pattern="exo(?: |$)(.*)")
async def _(chiy):
    if chiy.chat_id in BLACKLIST_CHAT:
        return await chiy.edit("**[ᴋᴏɴᴛᴏʟ]** - Perintah Itu Dilarang Di Gc Ini Goblok...")
    await edit_or_reply(chiy, "`Exorcist Nih Boss...`")
    sleep(2)
    text = str(chiy.pattern_match.group(1).split(" ", 1)[0])
    link = str(chiy.pattern_match.group(1).split(" ", 2)[0])
    shicy = text.replace(".", " ")
    user = await chiy.client.get_me()
    link_2 = choice(exolink)
    thumb = exorcist
    output = (
        f"**ʀᴇǫᴜᴇsᴛ ʙʏ :** @{user.username}\n\n"
        f"**{shicy}**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**               𝙴𝚇𝙾𝚁𝙲𝙸𝚂𝚃**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n\n"
        f"**⌲ 𝙻𝙸𝙽𝙺**\n"
        f"**⌲ {link_2} {link}**\n\n"
        f"**       𝙆𝙊𝙉𝙏𝙀𝙉 𝙋𝙍𝙀𝙈𝙄𝙐𝙈**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**          @premiumexor**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n"
        f"**    𝙅𝘼𝙉𝙂𝘼𝙉 𝙇𝙐𝙋𝘼 𝙎𝙃𝘼𝙍𝙀 💦**\n\n"
        f"**❖ᴠᴠɪᴩ ᴠɪᴅɪᴏ ʙᴏᴋᴇᴩ ᴛᴀɴᴩᴀ ʟɪɴᴋ❖**\n\n"
        f"**ɪɴғᴏ : @CarddSamss**\n"
        f"**ᴛᴇsᴛɪ : @vvipexor**\n"
    )
    if thumb:
        try:
            logo = thumb
            await chiy.delete()
            msg = await chiy.client.send_file(chiy.chat_id, logo, caption=output)
            await asyncio.sleep(300)
            await msg.delete()
        except BaseException:
            await chiy.edit(
                output + "\n\n **Logo yang diberikan tidak valid.**"
                "\n**Pastikan link diarahkan ke gambar logo**"
            )
            await asyncio.sleep(100)
            await chiy.delete()
    else:
        await edit_or_reply(chiy, output)


@shicy_cmd(pattern="as(?: |$)(.*)")
async def _(asupng):
    if asupng.chat_id in BLACKLIST_CHAT:
        return await asupng.edit("**[ᴋᴏɴᴛᴏʟ]** - Perintah Itu Dilarang Di Gc Ini Goblok...")
    await edit_or_reply(asupng, "`Asupan Sagapung...`")
    sleep(1)
    text = str(asupng.pattern_match.group(1).split(" ", 1)[0])
    link = str(asupng.pattern_match.group(1).split(" ", 2)[0])
    shicy = text.replace(".", " ")
    user = await asupng.client.get_me()
    link_2 = choice(asupan_sagapung)
    image = asupung
    output = (
        f"**ʀᴇǫᴜᴇsᴛ ʙʏ:** @{user.username}\n\n"
        f"**{shicy}**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**       Asᴜᴘᴀɴ Sᴀɢᴀᴘᴜɴɢ**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n\n"
        f"**⌲ 𝙻𝙸𝙽𝙺**\n"
        f"**⌲ {link_2} {link}**\n\n"
        f"**       𝙆𝙊𝙉𝙏𝙀𝙉 𝙋𝙍𝙀𝙈𝙄𝙐𝙈**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**          @PussyTubeCh**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n"
        f"**    𝙅𝘼𝙉𝙂𝘼𝙉 𝙇𝙐𝙋𝘼 𝙎𝙃𝘼𝙍𝙀 💦**\n\n"
        f"**❖𝚂𝚄𝙿𝙿𝙾𝚁𝚃❖**\n"
        f"**♕︎ @MovieSagapung**\n"
        f"**♕︎ @PussyTubeCh**"
    )
    if image:
        try:
            logo = image
            await asupng.delete()
            msg = await asupng.client.send_file(asupng.chat_id, logo, caption=output)
            await asyncio.sleep(300)
            await msg.delete()
        except BaseException:
            await asupng.edit(
                output + "\n\n **Logo yang diberikan tidak valid."
                "\nPastikan link diarahkan ke gambar logo**"
            )
            await asyncio.sleep(100)
            await asupng.delete()
    else:
        await edit_or_reply(asupng, output)

# ========================×========================
#               For Admin Collaborator
# ========================×========================


@shicy_cmd(pattern="^Exo(?: |$)(.*)")
async def chiycollab(exor):
    if exor.chat_id in BLACKLIST_CHAT:
        return await exor.edit("**[ᴋᴏɴᴛᴏʟ]** - Perintah Itu Dilarang Di Gc Ini Goblok...")
    await edit_or_reply(exor, "`Exorcist Nih Boss...`")
    sleep(1)
    if exor.pattern_match.group(1):
        text, link = exor.pattern_match.group(1).split()
    shicy = text.replace(".", " ")
    thumbnail = exorcist2
    output = (
        f"**{shicy}**\n\n"
        f"**⌲ 𝙻𝙸𝙽𝙺**\n"
        f"**⌲ {link}**\n\n"
        f"**❖ᴠᴠɪᴩ ᴠɪᴅɪᴏ ʙᴏᴋᴇᴩ ᴛᴀɴᴩᴀ ʟɪɴᴋ❖**\n\n"
        f"**ɪɴғᴏ : @zereefff**\n"
        f"**ᴛᴇsᴛɪ : @vvipexor**\n"
    )
    if thumbnail:
        try:
            logo = thumbnail
            await exor.delete()
            msg = await exor.client.send_file(exor.chat_id, logo, caption=output)
            await asyncio.sleep(300)
            await msg.delete()
        except BaseException:
            await exor.edit(
                output + "\n\n **Logo yang diberikan tidak valid.**"
                "\n**Pastikan link diarahkan ke gambar logo**"
            )
            await asyncio.sleep(100)
            await exor.delete()
    else:
        await edit_or_reply(exor, output)


@shicy_cmd(pattern="^As(?: |$)(.*)")
async def _(asupng):
    if asupng.chat_id in BLACKLIST_CHAT:
        return await asupng.edit("**[ᴋᴏɴᴛᴏʟ]** - Perintah Itu Dilarang Di Gc Ini Goblok...")
    await edit_or_reply(asupng, "`Asupan Sagapung...`")
    sleep(1)
    link = asupng.pattern_match.group(1)
    image = asupung
    output = (
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**       Asᴜᴘᴀɴ Sᴀɢᴀᴘᴜɴɢ**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n\n"
        f"**⌲ 𝙻𝙸𝙽𝙺**\n"
        f"**⌲ {link}**\n\n"
        f"**       𝙆𝙊𝙉𝙏𝙀𝙉 𝙋𝙍𝙀𝙈𝙄𝙐𝙈**\n"
        f"**╭✠━━━━━━❖━━━━━━✠╮**\n"
        f"**          @PussyTubeCh**\n"
        f"**╰✠━━━━━━❖━━━━━━✠╯**\n"
        f"**    𝙅𝘼𝙉𝙂𝘼𝙉 𝙇𝙐𝙋𝘼 𝙎𝙃𝘼𝙍𝙀 💦**\n\n"
        f"**❖𝚂𝚄𝙿𝙿𝙾𝚁𝚃❖**\n"
        f"**♕︎ @MovieSagapung**\n"
        f"**♕︎ @PussyTubeCh**"
    )
    if image:
        try:
            logo = image
            await asupng.delete()
            msg = await asupng.client.send_file(asupng.chat_id, logo, caption=output)
            await asyncio.sleep(800)
            await msg.delete()
        except BaseException:
            await asupng.edit(
                output + "\n\n **Logo yang diberikan tidak valid.**"
                "\n**Pastikan link diarahkan ke gambar logo**"
            )
            await asyncio.sleep(100)
            await asupng.delete()
    else:
        await edit_or_reply(asupng, output)


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "chiycollab": f"**Plugin:** `chiycollab`\
        \n\n  »  **Perintah :** `{cmd}exo`\
        \n  »  **Kegunaan :** Untuk Mendapatkan Link Bokp Dari Ch Exorcist.\
        \n\n  »  **Perintah :** `{cmd}as`\
        \n  »  **Kegunaan :** Untuk Mendapatkan Link Bokp Dari Ch Asupan Sagapung.\
    "
    }
)


CMD_HELP.update(
    {
        "chiyexo": f"**Plugin : **`chiyexo`\
        \n\n  »  **Perintah:** `Ini Khusus Admin Exorcist Tod Bukan Publik.`\
        \n  »  **Silahkan Ketik** `{cmd}help chiycollab` **Untuk Mendapatkan Konten.**\
    "
    }
)
