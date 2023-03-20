""" Userbot start point """


import sys
from importlib import import_module
from platform import python_version

from pytgcalls import __version__ as pytgcalls
from telethon import version
from telethon.tl.alltlobjects import LAYER

from ShicyXd import BOT_TOKEN
from ShicyXd import BOT_VER as ubotversion
from ShicyXd import BOTLOG_CHATID, LOGS, LOOP, bot
from ShicyXd.clients import shicy_userbot_on, multishicy
from ShicyXd.core.git import git
from ShicyXd.modules import ALL_MODULES
from ShicyXd.shicy import ShicyDB, HOSTED_ON, autobot, autopilot, shicy_version

try:
    for module_name in ALL_MODULES:
        imported_module = import_module(f"ShicyXd.modules.{module_name}")
    adB = ShicyDB()
    client = multishicy()
    total = 10 - client
    git()
    LOGS.info(f"Total Clients = {total} User")
    LOGS.info(f"Python Version - {python_version()}")
    LOGS.info(f"Telethon Version - {version.__version__} [Layer: {LAYER}]")
    LOGS.info(f"PyTgCalls Version - {pytgcalls}")
    LOGS.info(f"Userbot Version - {ubotversion} •[{adB.name}]•")
    LOGS.info(f"shicy Version - {shicy_version} •[{HOSTED_ON}]•")
    LOGS.info("[✨ BERHASIL DIAKTIFKAN! ✨]")
except (ConnectionError, KeyboardInterrupt, NotImplementedError, SystemExit):
    pass
except BaseException as e:
    LOGS.info(str(e), exc_info=True)
    sys.exit(1)


LOOP.run_until_complete(shicy_userbot_on())
if not BOTLOG_CHATID:
    LOOP.run_until_complete(autopilot())
if not BOT_TOKEN:
    LOOP.run_until_complete(autobot())

if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    try:
        bot.run_until_disconnected()
    except ConnectionError:
        pass
