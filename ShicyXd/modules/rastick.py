from secrets import choice

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd, deEmojify, eod, eor
from Stringchiy import get_string


@shicy_cmd(pattern="rst(?: |$)(.*)")
async def rastick(animu):
    text = animu.pattern_match.group(1)
    xx = await eor(animu, get_string("com_1"))
    if not text:
        if animu.is_reply:
            text = (await animu.get_reply_message()).message
        else:
            return await xx.answer(get_string("rstick_1"))
    animus = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        29,
        30,
        31,
        32,
        33,
        34,
        35,
        36,
        37,
        38,
        39,
        40,
        41,
        42,
        43,
        44,
        45,
        46,
        47,
        48,
        49,
        50,
        51,
        52,
        53,
        54,
        55,
        56,
        57,
        58,
        59,
        60,
        61,
        62,
        63,
    ]
    sticcers = await animu.client.inline_query(
        "stickerizerbot", f"#{choice(animus)}{(deEmojify(text))}"
    )
    try:
        await sticcers[0].click(
            animu.chat_id,
            reply_to=animu.reply_to_msg_id,
            silent=bool(animu.is_reply),
            hide_via=True,
        )

    except Exception:
        return await eod(
            xx, get_string("rstick_2")
        )
    await sleep(5)
    await animu.delete()


CMD_HELP.update(
    {
        "rastick": f"**Plugin : **`rastick`\
        \n\n  »  **Perintah :** `{cmd}rst`\
        \n  »  **Kegunaan : **Untuk membuat stiker teks Anda dengan templat stiker acak daro @StickerizerBot\
    "
    }
)
