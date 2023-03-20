# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.
#
# Ported by @ShicyXd
# FROM shicy-Userbot <https://github.com/ShicyXd/shicy-Userbot>
# t.me/ShicyXdSupport & t.me/shicySupport

import heroku3
import math
import shutil
import urllib3
from random import choice

from ShicyXd import HEROKU_API_KEY, HEROKU_APP_NAME, LOGS

from ._basechiy import ShicyDB
from ._hosting import HOSTED_ON
from .misc import async_searcher
from .tools import humanbytes


some_random_headers = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/72.0.3626.121 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100 101 Firefox/22.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:11.0) Gecko/20100101 Firefox/11.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/536.5 (KHTML, like Gecko) "
    "Chrome/19.0.1084.46 Safari/536.5",
    "Mozilla/5.0 (Windows; Windows NT 6.1) AppleWebKit/536.5 (KHTML, like Gecko) "
    "Chrome/19.0.1084.46 Safari/536.5",
    "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0",
]


if HOSTED_ON == "heroku":
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    heroku_api = "https://api.heroku.com"
    if HEROKU_APP_NAME is not None and HEROKU_API_KEY is not None:
        Heroku = heroku3.from_key(HEROKU_API_KEY)
        app = Heroku.app(HEROKU_APP_NAME)
        heroku_var = app.config()
    else:
        app = None


def simple_usage():
    try:
        import psutil
    except ImportError:
        return "Install 'psutil' to use this..."
    total, used, free = shutil.disk_usage(".")
    cpuUsage = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    upload = humanbytes(psutil.net_io_counters().bytes_sent)
    down = humanbytes(psutil.net_io_counters().bytes_recv)
    TOTAL = humanbytes(total)
    USED = humanbytes(used)
    FREE = humanbytes(free)
    return "**Tᴏᴛᴀʟ Rᴜᴀɴɢ Dɪsᴋ:** `{}`\n**Tᴇʀᴘᴀᴋᴀɪ:** `{}`\n**Kᴏsᴏɴɢ:** `{}`\n\n**📊 Pᴇɴɢɢᴜɴᴀᴀɴ Dᴀᴛᴀ 📊**\n**Uᴘʟᴏᴀᴅ**: `{}`\n**Dᴏᴡɴʟᴏᴀᴅ**: `{}`\n\n**CPU**: `{}%`\n**RAM**: `{}%`\n**DISK**: `{}%`".format(
        TOTAL,
        USED,
        FREE,
        upload,
        down,
        cpuUsage,
        memory,
        disk,
    )


async def heroku_usage():
    try:
        import psutil
    except ImportError:
        return (
            False,
            "'psutil' not installed!\nPlease Install it to use this.\n`pip3 install psutil`",
        )
    if not (HEROKU_API_KEY and HEROKU_APP_NAME):
        if HOSTED_ON == "heroku":
            if app is None:
                return False, "Silahkan isi `HEROKU_API_KEY` dan `HEROKU_APP_NAME`"
        return (
            False,
            f"`This command is only for Heroku Users, You are using {HOSTED_ON}`",
        )
    user_id = Heroku.account().id
    headers = {
        "User-Agent": choice(some_random_headers),
        "Authorization": f"Bearer {HEROKU_API_KEY}",
        "Accept": "application/vnd.heroku+json; version=3.account-quotas",
    }
    her_url = f"https://api.heroku.com/accounts/{user_id}/actions/get-quota"
    try:
        result = await async_searcher(her_url, headers=headers, re_json=True)
    except Exception as er:
        return False, str(er)
    quota = result["account_quota"]
    quota_used = result["quota_used"]
    remaining_quota = quota - quota_used
    percentage = math.floor(remaining_quota / quota * 100)
    minutes_remaining = remaining_quota / 60
    hours = math.floor(minutes_remaining / 60)
    minutes = math.floor(minutes_remaining % 60)
    App = result["apps"]
    try:
        App[0]["quota_used"]
    except IndexError:
        AppQuotaUsed = 0
        AppPercentage = 0
    else:
        AppQuotaUsed = App[0]["quota_used"] / 60
        AppPercentage = math.floor(App[0]["quota_used"] * 100 / quota)
    AppHours = math.floor(AppQuotaUsed / 60)
    AppMinutes = math.floor(AppQuotaUsed % 60)
    total, used, free = shutil.disk_usage(".")
    cpuUsage = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    upload = humanbytes(psutil.net_io_counters().bytes_sent)
    down = humanbytes(psutil.net_io_counters().bytes_recv)
    TOTAL = humanbytes(total)
    USED = humanbytes(used)
    FREE = humanbytes(free)
    return True, "**⚙️ Iɴғᴏʀᴍᴀsɪ Dʏɴᴏ ⚙️**:\n\n➠ **Pᴇɴɢɢᴜɴᴀᴀɴ Dʏɴᴏ** `{}`:\n  •  **{}h**  **{}m |** `[{}%]`\n➠ **Sɪsᴀ Kᴜᴏᴛᴀ Dʏɴᴏ Bᴜʟᴀɴ Iɴɪ :**\n  •  **{}h**  **{}m |** `[{}%]`\n\n**Tᴏᴛᴀʟ Rᴜᴀɴɢ Dɪsᴋ:**: `{}`\n**Tᴇʀᴘᴀᴋᴀɪ**: `{}`\n**Kᴏsᴏɴɢ**: `{}`\n\n**📊 Pᴇɴɢɢᴜɴᴀᴀɴ Dᴀᴛᴀ 📊**\n**Uᴘʟᴏᴀᴅ**: `{}`\n**Dᴏᴡɴʟᴏᴀᴅ**: `{}`\n\n**CPU**: `{}%`\n**RAM**: `{}%`\n**DISK**: `{}%`".format(
        HEROKU_APP_NAME,
        AppHours,
        AppMinutes,
        AppPercentage,
        hours,
        minutes,
        percentage,
        TOTAL,
        USED,
        FREE,
        upload,
        down,
        cpuUsage,
        memory,
        disk,
    )


def db_usage():
    adB = ShicyDB()
    if adB.name == "Redis":
        total = 30
    elif adB.name == "SQL":
        total = 20
    elif adB.name == "Mongo":
        total = 512
    total = total * (2**20)
    used = adB.usage
    a = humanbytes(used) + "/" + humanbytes(total)
    b = str(round((used / total) * 100, 2)) + "%"
    return f"**{adB.name}**\n\n**Storage Used**: `{a}`\n**Usage percentage**: **{b}**"


async def get_full_usage():
    is_hk, hk = await heroku_usage()
    her = hk if is_hk else ""
    rd = db_usage()
    return her + "\n\n" + rd
