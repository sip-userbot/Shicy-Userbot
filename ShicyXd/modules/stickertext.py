import io
import textwrap


from PIL import Image, ImageDraw, ImageFont
from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd, eod, eor
from Stringchiy import get_string


@shicy_cmd(pattern="stick(.*)")
async def stext(event):
    sticktext = event.pattern_match.group(1)

    if not sticktext:
        return await eod(event, get_string("stxt_1"))
    await eor(event, get_string("com_1"))

    sticktext = textwrap.wrap(sticktext, width=10)
    sticktext = '\n'.join(sticktext)

    image = Image.new("RGBA", (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    fontsize = 200
    font = ImageFont.truetype(
        "ShicyXd/shicy/styles/ProductSans-BoldItalic.ttf",
        size=fontsize)

    while draw.multiline_textsize(sticktext, font=font) > (512, 512):
        fontsize -= 3
        font = ImageFont.truetype(
            "ShicyXd/shicy/styles/ProductSans-BoldItalic.ttf",
            size=fontsize)

    width, height = draw.multiline_textsize(sticktext, font=font)
    draw.multiline_text(
        ((512 - width) / 2,
         (512 - height) / 2),
        sticktext,
        font=font,
        fill="white")

    image_stream = io.BytesIO()
    image_stream.name = "sticker.webp"
    image.save(image_stream, "WebP")
    image_stream.seek(0)

    await event.client.send_file(event.chat_id, image_stream)


CMD_HELP.update(
    {
        "stickerteks": f"**Plugin : **`stickerteks`\
        \n\n  »  **Perintah :** `{cmd}stick` `<teks>`\
        \n  »  **Kegunaan : **Membuat Sticker Text.\
    "
    }
)
