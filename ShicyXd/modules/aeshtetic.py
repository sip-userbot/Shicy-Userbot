from telethon import events

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import edit_or_reply, shicy_cmd

PRINTABLE_ASCII = range(0x21, 0x7F)


def aesthetify(string):
    for c in string:
        c = ord(c)
        if c in PRINTABLE_ASCII:
            c += 0xFF00 - 0x20
        elif c == ord(" "):
            c = 0x3000
        yield chr(c)


@shicy_cmd(pattern="ae(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    text = event.pattern_match.group(1)
    text = "".join(aesthetify(text))
    await edit_or_reply(event, text=text, parse_mode=None, link_preview=False)
    raise events.StopPropagation


CMD_HELP.update(
    {
        "aeshtetic": f"**Plugin : **`aeshtetic`\
        \n\n  »  **Perintah :** `{cmd}ae <teks>`\
        \n  »  **Kegunaan : **Mengubah font teks Menjadi aeshtetic.\
    "
    }
)
