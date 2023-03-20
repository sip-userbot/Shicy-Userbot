from asyncio import sleep
from io import BytesIO

from telethon import types
from telethon.errors import PhotoInvalidDimensionsError
from telethon.tl.functions.messages import SendMediaRequest

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import edit_or_reply, shicy_cmd


@shicy_cmd(pattern="pic(?: |$)(.*)")
async def on_file_to_photo(pics):
    xx = await edit_or_reply(pics, "`Processing...`")
    await sleep(1.5)
    await pics.delete()
    target = await pics.get_reply_message()
    try:
        image = target.media.document
    except AttributeError:
        return
    if not image.mime_type.startswith("image/"):
        return
    if image.mime_type == "image/webp":
        return
    if image.size > 10 * 2560 * 1440:
        return
    file = await pics.client.download_media(target, file=BytesIO())
    file.seek(0)
    img = await pics.client.upload_file(file)
    img.name = "image.png"
    await xx.delete()
    try:
        await pics.client(
            SendMediaRequest(
                peer=await pics.get_input_chat(),
                media=types.InputMediaUploadedPhoto(img),
                message=target.message,
                entities=target.entities,
                reply_to_msg_id=target.id,
            )
        )
    except PhotoInvalidDimensionsError:
        return


CMD_HELP.update(
    {
        "pic": f"**Plugin : **`pic`\
        \n\n  »  **Perintah :** `{cmd}pic` <reply ke file document foto>\
        \n  »  **Kegunaan : **Untuk Mengubah Gambar Dokumen apa pun menjadi Gambar Ukuran Penuh.\
    "
    }
)
