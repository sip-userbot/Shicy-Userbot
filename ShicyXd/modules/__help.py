from telethon.errors.rpcerrorlist import BotInlineDisabledError as noinline
from telethon.errors.rpcerrorlist import BotResponseTimeoutError as timout
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.contacts import UnblockRequest

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP, bot, ch, tgbot
from ShicyXd.shicy import shicy_cmd, eod, eor
from Stringchiy import get_string


@shicy_cmd(pattern="help(?: |$)(.*)")
async def helpchiy(event):
    if event.fwd_from:
        return
    args = event.pattern_match.group(1).lower()
    if args:
        if args in CMD_HELP:
            await eor(event, get_string("help_5").format(CMD_HELP[args], ch))
        else:
            await eod(event, get_string("help_10").format(args, cmd))
    else:
        shicyUBOT = await tgbot.get_me()
        BOT_USERNAME = shicyUBOT.username
        if BOT_USERNAME is not None:
            chat = "@Botfather"
            try:
                results = await event.client.inline_query(  # pylint:disable=E0602
                    BOT_USERNAME, "@ShicyyXCode"
                )
                await results[0].click(
                    event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
                )
                await event.delete()
            except timout:
                return await eor(event, f"Bot tidak menanggapi inline kueri.\nSilahkan Ketik `{cmd}restart`"
                )
            except noinline:
                xx = await eor(event, "**Inline Mode Tidak aktif.**\n__Sedang Menyalakannya, Harap Tunggu Sebentar...__",
                               )
                async with bot.conversation(chat) as conv:
                    try:
                        first = await conv.send_message("/setinline")
                        second = await conv.get_response()
                        third = await conv.send_message(BOT_USERNAME)
                        fourth = await conv.get_response()
                        fifth = await conv.send_message("Search")
                        sixth = await conv.get_response()
                        await bot.send_read_acknowledge(conv.chat_id)
                    except YouBlockedUserError:
                        await event.client(UnblockRequest(chat))
                        first = await conv.send_message("/setinline")
                        second = await conv.get_response()
                        third = await conv.send_message(BOT_USERNAME)
                        fourth = await conv.get_response()
                        fifth = await conv.send_message("Search")
                        sixth = await conv.get_response()
                        await bot.send_read_acknowledge(conv.chat_id)
                    await xx.edit(
                        f"**Berhasil Menyalakan Mode Inline**\n\n**Ketik** `{cmd}help` **lagi untuk membuka menu bantuan.**"
                    )
                await bot.delete_messages(
                    conv.chat_id,
                    [first.id, second.id, third.id, fourth.id, fifth.id, sixth.id],
                )
        else:
            await eor(
                event,
                "**Silahkan Buat BOT di @BotFather dan Tambahkan Var** `BOT_TOKEN` & `BOT_USERNAME`",
            )
