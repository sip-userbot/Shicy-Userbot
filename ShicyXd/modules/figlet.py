import pyfiglet

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd, deEmojify, eod
from Stringchiy import get_string


@shicy_cmd(pattern="figlet (\\w+) (.*)")
async def figlet(event):
    if event.fwd_from:
        return
    style_list = {
        "slant": "slant",
        "3d": "3-d",
        "5line": "5lineoblique",
        "alpha": "alphabet",
        "banner": "banner3-D",
        "doh": "doh",
        "iso": "isometric1",
        "letter": "letters",
        "allig": "alligator",
        "dotm": "dotmatrix",
        "bubble": "bubble",
        "bulb": "bulbhead",
        "digi": "digital",
    }
    style = event.pattern_match.group(1)
    text = event.pattern_match.group(2)
    try:
        font = style_list[style]
    except KeyError:
        return await eod(event, get_string("fglet").format(cmd)
                         )
    result = pyfiglet.figlet_format(deEmojify(text), font=font)
    await event.respond(f"‌‌‎`{result}`")
    await event.delete()


CMD_HELP.update(
    {
        "figlet": f"**Plugin : **`figlet`\
        \n\n  »  **Perintah :** `{cmd}figlet` <style> <text>\
        \n  »  **Kegunaan : **Menyesuaikan gaya teks Anda dengan figlet.\
        \n\n  •  **List style :** `slant`, `3d`, `5line`, `alpha`, `banner`, `doh`, `iso`, `letter`, `allig`, `dotm`, `bubble`, `bulb`, `digi`\
    "
    }
)
