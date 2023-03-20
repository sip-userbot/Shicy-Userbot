import os
from pathlib import Path

from ShicyXd import CMD_HELP
from ShicyXd import CMD_HANDLER as cmd
from ShicyXd.shicy import eor
from ShicyXd.shicy import shicy_cmd, load_module, remove_plugin, reply_id
from Stringchiy import get_string


@shicy_cmd(pattern="install$")
async def _(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        try:
            xx = await eor(event, get_string("core_1"))
            downloaded_file_name = await event.client.download_media(
                await event.get_reply_message(),
                "ShicyXd/modules/",
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await xx.edit(
                    get_string("core_3").format(
                        os.path.basename(downloaded_file_name)
                    )
                )
            else:
                os.remove(downloaded_file_name)
                await xx.edit(get_string("core_2"))
        except Exception as e:
            await xx.edit(get_string("error_1").format(str(e)))
            os.remove(downloaded_file_name)


@shicy_cmd(pattern="psend ([\\s\\S]*)")
async def send(event):
    reply_to_id = await reply_id(event)
    input_str = event.pattern_match.group(1)
    the_plugin_file = f"./ShicyXd/modules/{input_str}.py"
    if os.path.exists(the_plugin_file):
        caat = await event.client.send_file(
            event.chat_id,
            the_plugin_file,
            force_document=True,
            thumb="ShicyXd/resources/logo.jpg",
            allow_cache=False,
            reply_to=reply_to_id,
            caption=get_string("core_4").format(input_str)
        )
        await event.delete()
    else:
        await eor(event, get_string("core_6"))


@shicy_cmd(pattern="uninstall (?P<shortname>\\w+)")
async def uninstall(event):
    if event.fwd_from:
        return
    shortname = event.pattern_match["shortname"]
    dir_path = f"./ShicyXd/modules/{shortname}.py"
    xx = await eor(event, get_string("com_1"))
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await xx.edit(get_string("core_5").format(shortname))
    except OSError as e:
        await xx.edit("**ERROR:** `%s` : %s" % (dir_path, e.strerror))


CMD_HELP.update(
    {
        "core": f"**Plugin : **`core`\
        \n\n  »  **Perintah :** `{cmd}install` <reply ke file module>\
        \n  »  **Kegunaan : **Untuk Menginstall module userbot secara instan.\
        \n\n  »  **Perintah :** `{cmd}uninstall` <nama module>\
        \n  »  **Kegunaan : **Untuk Menguninstall / Menghapus module userbot secara instan.\
        \n\n  »  **Perintah :** `{cmd}psend` <nama module>\
        \n  »  **Kegunaan : **Untuk Mengirim module userbot secara instan.\
    "
    }
)
