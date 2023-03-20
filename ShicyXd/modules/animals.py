import requests

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import edit_or_reply, shicy_cmd


@shicy_cmd(pattern="shibe$")
async def shibe(event):
    xx = await edit_or_reply(event, "`Processing...`")
    response = requests.get("https://shibe.online/api/shibes").json()
    if not response:
        await event.edit("**Tidak bisa menemukan Anjing.**")
        return
    await event.client.send_message(entity=event.chat_id, file=response[0])
    await xx.delete()


@shicy_cmd(pattern="cat$")
async def cats(event):
    xx = await edit_or_reply(event, "`Processing...`")
    response = requests.get("https://shibe.online/api/cats").json()
    if not response:
        await event.edit("**Tidak bisa menemukan kucing.**")
        return
    await event.client.send_message(entity=event.chat_id, file=response[0])
    await xx.delete()


CMD_HELP.update(
    {
        "animals": f"**Plugin : **`animals`\
        \n\n  »  **Perintah :** `{cmd}cat`\
        \n  »  **Kegunaan : **Untuk Mengirim gambar kucing secara random.\
        \n\n  »  **Perintah :** `{cmd}shibe`\
        \n  »  **Kegunaan : **Untuk Mengirim gambar random dari anjing jenis Shiba.\
    "
    }
)
