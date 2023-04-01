# Credits: @mrconfused
# Recode by @mrismanaziz
# FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio
import inspect
import re
from pathlib import Path

from telethon import events
from telethon.errors import (
    AlreadyInConversationError,
    BotInlineDisabledError,
    BotResponseTimeoutError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
    ChatSendStickersForbiddenError,
    FloodWaitError,
    MessageIdInvalidError,
    MessageNotModifiedError,
)

from ShicyXd import *

from .toolschiy import eod, eor


def shicy_cmd(
    pattern: str = None,
    allow_sudo: bool = True,
    group_only: bool = False,
    admins_only: bool = False,
    private_only: bool = False,
    disable_edited: bool = False,
    forword=False,
    command: str = None,
    **args,
):
    args["func"] = lambda e: e.via_bot_id is None
    stack = inspect.stack()
    previous_stack_frame = stack[1]
    file_test = Path(previous_stack_frame.filename)
    file_test = file_test.stem.replace(".py", "")

    if "disable_edited" in args:
        del args["disable_edited"]

    args["blacklist_chats"] = True
    black_list_chats = list(BL_CHAT)
    if len(black_list_chats) > 0:
        args["chats"] = black_list_chats

    if pattern is not None:
        global shicy_reg
        global sudo_reg
        if (
            pattern.startswith(r"\#")
            or not pattern.startswith(r"\#")
            and pattern.startswith(r"^")
        ):
            shicy_reg = sudo_reg = re.compile(pattern)
        else:
            shicy_ = "\\" + CMD_HANDLER
            sudo_ = "\\" + SUDO_HANDLER
            shicy_reg = re.compile(shicy_ + pattern)
            sudo_reg = re.compile(sudo_ + pattern)
            if command is not None:
                cmd1 = shicy_ + command
                cmd2 = sudo_ + command
            else:
                cmd1 = (
                    (shicy_ +
                     pattern).replace(
                        "$",
                        "").replace(
                        "\\",
                        "").replace(
                        "^",
                        ""))
                cmd2 = (
                    (sudo_ + pattern)
                    .replace("$", "")
                    .replace("\\", "")
                    .replace("^", "")
                )
            try:
                CMD_LIST[file_test].append(cmd1)
            except BaseException:
                CMD_LIST.update({file_test: [cmd1]})

    def decorator(func):
        async def wrapper(event):
            chat = event.chat
            if admins_only:
                if event.is_private:
                    return await eor(
                        event, "**Perintah ini hanya bisa digunakan di grup.**", time=10
                    )
                if not (chat.admin_rights or chat.creator):
                    return await eor(
                        event, f"**Maaf anda bukan admin di {chat.title}**", time=10
                    )
            if group_only and not event.is_group:
                return await eor(
                    event, "**Perintah ini hanya bisa digunakan di grup.**", time=10
                )
            if private_only and not event.is_private:
                return await eor(
                    event, "**Perintah ini hanya bisa digunakan di private chat.**", time=10
                )
            try:
                await func(event)
            # Credits: @mrismanaziz
            # FROM Man-Userbot <https://github.com/mrismanaziz/Man-Userbot>
            # t.me/SharingUserbot & t.me/Lunatic0de
            except MessageNotModifiedError as er:
                LOGS.error(er)
            except MessageIdInvalidError as er:
                LOGS.error(er)
            except BotInlineDisabledError:
                await eor(
                    event, "**Silahkan aktifkan mode Inline untuk bot**", time=10
                )
            except ChatSendStickersForbiddenError:
                await eor(
                    event, "**Tidak dapat mengirim stiker di obrolan ini**", time=10
                )
            except BotResponseTimeoutError:
                await eod(
                    event, "**The bot didnt answer to your query in time**"
                )
            except ChatSendMediaForbiddenError:
                await eor(
                    event, "**Tidak dapat mengirim media dalam obrolan ini**", time=10
                )
            except AlreadyInConversationError:
                await eod(
                    event,
                    "**Percakapan sudah terjadi dengan obrolan yang diberikan. coba lagi setelah beberapa waktu.**",
                )
            except ChatSendInlineForbiddenError:
                await eor(
                    event,
                    "**Tidak dapat mengirim pesan inline dalam obrolan ini.**",
                    time=10,
                )
            except FloodWaitError as e:
                LOGS.error(
                    f"Telah Terjadi flood wait error tunggu {e.seconds} detik dan coba lagi"
                )
                await event.delete()
                await asyncio.sleep(e.seconds + 5)
            except events.StopPropagation:
                raise events.StopPropagation
            except KeyboardInterrupt:
                pass
            except BaseException as e:
                LOGS.exception(e)

        if bot:
            if not disable_edited:
                bot.add_event_handler(
                    wrapper, events.MessageEdited(
                        **args, outgoing=True, pattern=shicy_reg))
            bot.add_event_handler(wrapper, events.NewMessage(
                **args, outgoing=True, pattern=shicy_reg))
        if bot:
            if allow_sudo:
                if not disable_edited:
                    bot.add_event_handler(
                        wrapper,
                        events.MessageEdited(
                            **args,
                            from_users=list(SUDO_USERS),
                            pattern=sudo_reg),
                    )
                bot.add_event_handler(
                    wrapper,
                    events.NewMessage(
                        **args, from_users=list(SUDO_USERS), pattern=sudo_reg
                    ),
                )
        if CHIY2:
            if not disable_edited:
                CHIY2.add_event_handler(
                    wrapper,
                    events.MessageEdited(**args, outgoing=True, pattern=shicy_reg),
                )
            CHIY2.add_event_handler(
                wrapper, events.NewMessage(**args, outgoing=True, pattern=shicy_reg)
            )
        if CHIY3:
            if not disable_edited:
                CHIY3.add_event_handler(
                    wrapper,
                    events.MessageEdited(**args, outgoing=True, pattern=shicy_reg),
                )
            CHIY3.add_event_handler(
                    wrapper, events.NewMessage(**args, outgoing=True, pattern=shicy_reg)
            )
        if CHIY4:
            if not disable_edited:
                CHIY4.add_event_handler(
                    wrapper,
                    events.MessageEdited(**args, outgoing=True, pattern=shicy_reg),
                )
            CHIY4.add_event_handler(
                 wrapper, events.NewMessage(**args, outgoing=True, pattern=shicy_reg)
             )
        if CHIY5:
            if not disable_edited:
                CHIY5.add_event_handler(
                    wrapper,
                    events.MessageEdited(**args, outgoing=True, pattern=shicy_reg),
                )
            CHIY5.add_event_handler(
                wrapper, events.NewMessage(**args, outgoing=True, pattern=shicy_reg)
            )
        try:
            LOAD_PLUG[file_test].append(wrapper)
        except Exception:
            LOAD_PLUG.update({file_test: [wrapper]})
        return wrapper

    return decorator


def shicy_handler(
    **args,
):
    def decorator(func):
        if bot:
            bot.add_event_handler(func, events.NewMessage(**args))
        if CHIY2:
            bot2.add_event_handler(func, events.NewMessage(**args))
        if CHIY3:
            bot3.add_event_handler(func, events.NewMessage(**args))
        if CHIY4:
            CHIY4.add_event_handler(func, events.NewMessage(**args))
        if CHIY5:
            CHIY5.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator


def asst_cmd(**args):
    pattern = args.get("pattern", None)
    r_pattern = r"^[/!]"
    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern
    args["pattern"] = pattern.replace("^/", r_pattern, 1)

    def decorator(func):
        if tgbot:
            tgbot.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator


def chataction(**args):
    def decorator(func):
        if bot:
            bot.add_event_handler(func, events.ChatAction(**args))
        if CHIY2:
            CHIY2.add_event_handler(func, events.ChatAction(**args))
        if CHIY3:
            CHIY3.add_event_handler(func, events.ChatAction(**args))
        if CHIY4:
            CHIY4.add_event_handler(func, events.ChatAction(**args))
        if CHIY5:
            CHIY5.add_event_handler(func, events.ChatAction(**args))
        return func

    return decorator


def callback(**args):
    def decorator(func):
        if tgbot:
            tgbot.add_event_handler(func, events.CallbackQuery(**args))
        return func

    return decorator
