import time
from datetime import datetime
from secrets import choice


from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP, StartTime
from ShicyXd import DEVS
from ShicyXd.events import register
from .ping import get_readable_time


absen = [
    "**𝙃𝙖𝙙𝙞𝙧 𝙙𝙤𝙣𝙜 𝙏𝙤𝙙** 😁",
    "**𝙃𝙖𝙙𝙞𝙧 𝙆𝙖𝙠𝙖 𝙂𝙖𝙣𝙩𝙚𝙣𝙜** 😉",
    "**𝙂𝙪𝙖 𝙃𝙖𝙙𝙞𝙧 𝘾𝙤𝙣𝙩𝙤𝙡** 😁",
    "**𝙂𝙪𝙖 𝙃𝙖𝙙𝙞𝙧 𝙂𝙖𝙣𝙩𝙚𝙣𝙜** 🥵",
    "**𝙃𝙖𝙙𝙞𝙧 𝙉𝙜𝙖𝙗** 😎",
    "**𝙂𝙪𝙖 𝙃𝙖𝙙𝙞𝙧 𝘼𝙗𝙖𝙣𝙜** 🥺",
    "**𝙎𝙞 𝘾𝙖𝙠𝙚𝙥 𝙃𝙖𝙙𝙞𝙧 𝘽𝙖𝙣𝙜** 😎",
    "**Hadir kak maap telat** 🥺",
    "**Hadir Tuan** 🙏🏻",
    "**Hadir Majikan** 🙏🏻",
    "**Hadir Sayang** 😳",
    "**Hadir Bro ꜱʜɪᴄʏ** 😁",
    "**maaf ka habis nemenin ka ꜱʜɪᴄʏ** 🥺",
    "**maaf ka habis disuruh Tuan ꜱʜɪᴄʏ** 🥺🙏🏻",
    "**Hadir Sayang** 😘"
    "**Hadir ꜱʜɪᴄʏ Akuuuuhhh** ☺️",
    "**Hadir ꜱʜɪᴄʏ brother Aku** 🥰",
]

pacar = [
    "**Kamu mau jadi pacar aku ga?** 💘",
    "**Memek mending sama aku** 😎",
    "**Hai ganteng** 🐷",
    "**Mau ga bang jadi pacar aku?** 😁",
    "**Mending pc aku bang** 🥺",
    "**Ngewe Sama Aku yuk**🥵🥵💦",
    "**card Mau Aku Crotin??**🥵",
    "**card Mau Aku Sepongin??**",
    "**card Aku Sayang Kamu ,Mwahhh😘**",
]

salam = [
    "**Wa'alaikumsalam ganteng** 🥰🥰",
    "**Wa'alaikumsalam WR WB** 👋🏻",
    "**Iyah Waalaikusalam** 🥵",
    "**Wa'alaikumsalam bang**",
    "**Wa'alaikumsalam** 🥰",
    "**Wa'alaikumsalan Warohmatullohi Wabarokatu**",
    "**Wa'alaikumsalam Ustad**",
]

repo = [
    "**buseettt repo lo keren** 🥰🥰",
    "**mantep banget bang repo lo** 👋🏻",
    "**jiah repo nya kgak ada lawan** 🥵",
    "**seh repo laen nya kalah nih mah**",
]

shicycakep = [
    "**𝙄𝙮𝙖 𝙂𝙖𝙣𝙩𝙚𝙣𝙜 𝘽𝙖𝙣𝙜𝙚𝙩** 😍",
    "**𝙂𝙖𝙣𝙩𝙚𝙣𝙜𝙣𝙮𝙖 𝙂𝙖𝙠 𝘼𝙙𝙖 𝙇𝙖𝙬𝙖𝙣** 😚",
    "**𝙠𝙖𝙢𝙪 𝙂𝙖𝙣𝙩𝙚𝙣𝙜𝙣𝙮𝙖 𝘼𝙠𝙪 𝙆𝙖𝙣** 😍",
    "**𝙞𝙮𝙖𝙖 𝙜𝙖𝙙𝙖 𝙖𝙙𝙖 𝙨𝙖𝙞𝙣𝙜** 😎",
    "**𝙠𝙖𝙢𝙪 𝙟𝙖𝙢𝙚𝙩 𝙏𝙖𝙥𝙞 𝘽𝙤𝙤𝙣𝙜** 😚",
]


@register(incoming=True, from_users=DEVS, pattern=r"^Cping$")
async def _(ping):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    user = await ping.client.get_me()
    message = "**✧ Shicy-Userbot ✧**\n\n✧ **ᴘɪɴɢᴇʀ :** `{} ms`\n✧ **ᴜᴘᴛɪᴍᴇ :** `{}`\n✧ **ᴏᴡɴᴇʀ :** `{}`\n✧ **ɪᴅ :** `{}`"
    await ping.reply(message.format(duration, uptime, user.first_name, user.id)
                     )

@register(incoming=True, from_users=DEVS, pattern=r"^Absen$")
async def shicyabsen(ganteng):
    await ganteng.reply(choice(absen))

@register(incoming=True, from_users=DEVS, pattern=r"^card$")
async def shicy(card):
    await card.reply(choice(pacar))

@register(incoming=True, from_users=DEVS, pattern=r"^Aku ganteng kan$")
async def shicy(ganteng):
    await ganteng.reply(choice(shicycakep))

@register(incoming=True, from_users=DEVS, pattern=r"^Repo$")
async def shicy(mantap):
    await mantap.reply(choice(repo))

@register(incoming=True, from_users=DEVS, pattern=r"^dancok$")
async def shicy(yeh):
    await yeh.reply(choice(salam))

# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "chiyping": f"**Plugin:** `chiyping`\
        \n\n  »  **Perintah : **`Perintah Ini Hanya Untuk Devs Shicy-Userbot Tod.`\
        \n  »  **Kegunaan :** __Silahkan Ketik `{cmd}ping` Untuk Publik.__\
    "
    }
)
