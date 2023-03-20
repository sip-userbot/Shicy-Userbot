import os

import requests

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP, DEEP_AI
from ShicyXd.shicy import shicy_cmd, eod, eor
from Stringchiy import get_string


@shicy_cmd(pattern="detect$")
async def detect(event):
    if DEEP_AI is None:
        return await eod(
            event, get_string("nsfw_1"),
            time=120,
        )
    reply = await event.get_reply_message()
    if not reply:
        return await eod(event, get_string("failed9"), time=90)
    event = await eor(event, get_string("nsfw_2"))
    media = await event.client.download_media(reply)
    if not media.endswith(("png", "jpg", "webp")):
        return await eod(event, get_string("failed9"), time=90)
    chiyevent = await eor(event, get_string("nsfw_3"))
    r = requests.post(
        "https://api.deepai.org/api/nsfw-detector",
        files={
            "image": open(media, "rb"),
        },
        headers={"api-key": DEEP_AI},
    )
    os.remove(media)
    if "status" in r.json():
        return await eod(chiyevent, r.json()["status"])
    r_json = r.json()["output"]
    pic_id = r.json()["id"]
    percentage = r_json["nsfw_score"] * 100
    detections = r_json["detections"]
    link = f"https://api.deepai.org/job-view-file/{pic_id}/inputs/image.jpg"
    result = f"<b>Detected Nudity :</b>\n<a href='{link}'>>>></a> <code>{percentage:.3f}%</code>\n\n"
    if detections:
        for parts in detections:
            name = parts["name"]
            confidence = int(float(parts["confidence"]) * 100)
            result += f"<b>• {name}:</b>\n   <code>{confidence} %</code>\n"
    await eor(
        chiyevent,
        result,
        link_preview=False,
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "nsfw": f"**Plugin : **`nsfw`\
        \n\n  »  **Perintah :** `{cmd}detect` <reply media>\
        \n  »  **Kegunaan : **Untuk mendeteksi konten 18+ dengan gambar balasan.\
    "
    }
)
