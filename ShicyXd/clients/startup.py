import sys

from telethon.utils import get_peer_id

from ShicyXd import BOT_TOKEN
from ShicyXd import BOT_VER as version
from ShicyXd import *
from ShicyXd.modules.gcast import GCAST_BLACKLIST as GBL

EOL = "EOL\nShicy-UserBot v{}, Copyright © 2021-2022 shicy• <https://github.com/sip-userbot>"
MSG_BLACKLIST = "MAKANYA GA USAH BERTINGKAH GOBLOK, USERBOT {} GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nShicy-UserBot v{}, Copyright © 2021-2022 Shicy• <https://github.com/sip-userbot>"


async def shicy_client(client):
    client.me = await client.get_me()
    client.uid = get_peer_id(client.me)


def multishicy():
    if 1603412565 not in DEVS:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if -1001808819173 not in GBL:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    if 1603412565 not in DEFAULT:
        LOGS.warning(EOL.format(version))
        sys.exit(1)
    failed = 0
    if STRING_2:
        try:
            CHIY2.start()
            LOOP.run_until_complete(shicy_client(CHIY2))
            user = CHIY2.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
            )
            if user.id in blacklistShicy:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_3:
        try:
            CHIY3.start()
            LOOP.run_until_complete(shicy_client(CHIY3))
            user = CHIY3.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_3 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistShicy:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_4:
        try:
            CHIY4.start()
            LOOP.run_until_complete(shicy_client(CHIY4))
            user = CHIY4.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_4 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistShicy:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_5:
        try:
            CHIY4.start()
            LOOP.run_until_complete(shicy_client(CHIY4))
            user = CHIY4.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(f"STRING_5 detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——")
            if user.id in blacklistShicy:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))

    if STRING_SESSION:
        try:
            bot.start()
            LOOP.run_until_complete(shicy_client(bot))
            user = bot.get_me()
            name = user.first_name
            uid = user.id
            LOGS.info(
                f"STRING_SESSION detected!\n┌ First Name: {name}\n└ User ID: {uid}\n——"
            )
            if user.id in blacklistShicy:
                LOGS.warning(MSG_BLACKLIST.format(name, version))
                sys.exit(1)
        except Exception as e:
            LOGS.info(str(e))


    if BOT_TOKEN:
        try:
            user = tgbot.get_me()
            name = user.first_name
            uname = user.username
            LOGS.info(
                f"BOT_TOKEN detected!\n┌ First Name: {name}\n└ Username: @{uname}\n——"
            )
        except Exception as e:
            LOGS.info(str(e))

    if not STRING_SESSION:
        failed += 1
    return failed
