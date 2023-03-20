from time import sleep
from secrets import choice

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy.truthdare import Dare as d
from ShicyXd.shicy.truthdare import Truth as t
from ShicyXd.shicy import shicy_cmd, eor
from Stringchiy import get_string


Tod = ["Truth", "Dare"]


@shicy_cmd(pattern=r"tod( truth| dare|$)")
async def truth_or_dare(tord):
    trod = tord.pattern_match.group(1).strip()
    troll = choice(Tod)
    if trod == "":
        await tord.edit(get_string("tod_1").format(troll))

    if trod == "truth":
        shicy = await eor(tord, get_string("tod_2"))
        sleep(1)
        trth = choice(t)
        await shicy.edit(get_string("tod_3").format(trth))
        return

    if trod == "dare":
        Xd = await eor(tord, get_string("tod_4"))
        sleep(1)
        dr = choice(d)
        await Xd.edit(get_string("tod_5").format(dr))

        return


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "chiytod": f"**Plugin:** `chiytod`\
        \n\n  »  **Perintah :** `{cmd}tod`\
        \n  »  **Kegunaan :** __Mendapatkan Pilihan Secara Acak.__\
        \n\n  »  **Perintah :** `{cmd}tod <truth/dare>`\
        \n  »  **Kegunaan :** __Untuk Mendapatkan Truth or Dare Secara Acak.__\
    "
    }
)
