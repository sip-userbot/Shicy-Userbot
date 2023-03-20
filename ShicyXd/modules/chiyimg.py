import asyncio
import os

import cv2
import numpy as np

from ShicyXd import CMD_HANDLER as cmd
from ShicyXd import CMD_HELP
from ShicyXd.shicy import shicy_cmd, eod, eor
from Stringchiy import get_string


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


@shicy_cmd(pattern=r"sketch(?: |$)(.*)")
async def sketch(e):
    ureply = await e.get_reply_message()
    xx = await eor(e, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(xx, get_string("failed9"))

    chiy = await ureply.download_media()
    if chiy.endswith(".tgs"):
        await xx.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", chiy, "shicy.png"]
        file = "shicy.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xx.edit(get_string("yimg_1"))
        img = cv2.VideoCapture(chiy)
        heh, lol = img.read()
        cv2.imwrite("shicy.png", lol)
        file = "shicy.png"
    img = cv2.imread(file)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inverted_gray_image = 255 - gray_image
    blurred_img = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
    inverted_blurred_img = 255 - blurred_img
    pencil_sketch_IMG = cv2.divide(
        gray_image, inverted_blurred_img, scale=256.0)
    cv2.imwrite("shicyxd.png", pencil_sketch_IMG)
    await xx.respond(get_string("yimg_3"), file="shicyxd.png")
    await xx.delete()
    os.remove(file)
    os.remove("shicyxd.png")


@shicy_cmd(pattern=r"grey(?: |$)(.*)")
async def xnxx(event):
    ureply = await event.get_reply_message()
    chiy = await eor(event, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(chiy, get_string("failed9"))

    shicy = await ureply.download_media()
    if shicy.endswith(".tgs"):
        await chiy.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", shicy, "chi.png"]
        file = "chi.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await chiy.edit(get_string("cimg_1"))
        img = cv2.VideoCapture(shicy)
        heh, lol = img.read()
        cv2.imwrite("chi.png", lol)
        file = "chi.png"
    chi = cv2.imread(file)
    shicyxd = cv2.cvtColor(chi, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("chi.jpg", shicyxd)
    await event.client.send_file(
        event.chat_id,
        "chi.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await chiy.delete()
    os.remove("chi.png")
    os.remove("chi.jpg")
    os.remove(shicy)


@shicy_cmd(pattern=r"blur(?: |$)(.*)")
async def shicy(event):
    ureply = await event.get_reply_message()
    xd = await eor(event, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(xd, get_string("failed9"))

    chiy = await ureply.download_media()
    if chiy.endswith(".tgs"):
        await xd.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", chiy, "chi.png"]
        file = "chi.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xd.edit(get_string("cimg_1"))
        img = cv2.VideoCapture(chiy)
        heh, lol = img.read()
        cv2.imwrite("chi.png", lol)
        file = "chi.png"
    chi = cv2.imread(file)
    shicyxd = cv2.GaussianBlur(chi, (35, 35), 0)
    cv2.imwrite("chi.jpg", shicyxd)
    await event.client.send_file(
        event.chat_id,
        "chi.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xd.delete()
    for i in ["chi.png", "chi.jpg", chiy]:
        if os.path.exists(i):
            os.remove(i)


@shicy_cmd(pattern=r"negative(?: |$)(.*)")
async def chiyxd(event):
    ureply = await event.get_reply_message()
    shicy = await eor(event, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(shicy, get_string("failed9"))

    shicycd = await ureply.download_media()
    if shicyxd.endswith(".tgs"):
        await shicy.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", shicyxd, "chi.png"]
        file = "chi.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await shicy.edit(get_string("cimg_1"))
        img = cv2.VideoCapture(shicyxd)
        heh, lol = img.read()
        cv2.imwrite("chi.png", lol)
        file = "chi.png"
    chiyex = cv2.imread(file)
    kntlxd = cv2.bitwise_not(chiyex)
    cv2.imwrite("chi.jpg", kntlxd)
    await event.client.send_file(
        event.chat_id,
        "chi.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await shicy.delete()
    os.remove("chi.png")
    os.remove("chi.jpg")
    os.remove(kntlxd)


@shicy_cmd(pattern=r"miror(?: |$)(.*)")
async def kntl(event):
    ureply = await event.get_reply_message()
    kentu = await eor(event, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(kentu, get_string("failed9"))

    xnxx = await ureply.download_media()
    if xnxx.endswith(".tgs"):
        await kentu.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", xnxx, "chi.png"]
        file = "chi.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await kentu.edit(get_string("yimg_1"))
        img = cv2.VideoCapture(xnxx)
        kont, tol = img.read()
        cv2.imwrite("chi.png", tol)
        file = "chi.png"
    chi = cv2.imread(file)
    mmk = cv2.flip(chi, 1)
    shicyxd = cv2.hconcat([chi, mmk])
    cv2.imwrite("chi.jpg", shicyxd)
    await event.client.send_file(
        event.chat_id,
        "chi.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await kentu.delete()
    os.remove("chi.png")
    os.remove("chi.jpg")
    os.remove(xnxx)


@shicy_cmd(pattern=r"flp(?: |$)(.*)")
async def shicy(kontol):
    ureply = await kontol.get_reply_message()
    mmk = await eor(kontol, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(mmk, get_string("failed9"))

    shicyxd = await ureply.download_media()
    if shicyxd.endswith(".tgs"):
        await mmk.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", shicyxd, "chiy.png"]
        file = "chiy.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await mmk.edit(get_string("yimg_1"))
        img = cv2.VideoCapture(shicyxd)
        kon, tol = img.read()
        cv2.imwrite("chiy.png", tol)
        file = "chiy.png"
    achi = cv2.imread(file)
    trn = cv2.flip(achi, 1)
    asu = cv2.rotate(trn, cv2.ROTATE_180)
    chiz = cv2.vconcat([achi, asu])
    cv2.imwrite("chiy.jpg", chiz)
    await kontol.client.send_file(
        kontol.chat_id,
        "chiy.jpg",
        force_document=False,
        reply_to=kontol.reply_to_msg_id,
    )
    await mmk.delete()
    os.remove("chiy.png")
    os.remove("chiy.jpg")
    os.remove(shicyxd)


@shicy_cmd(pattern=r"quad(?: |$)(.*)")
async def shicy(memek):
    ureply = await memek.get_reply_message()
    kntl = await eor(memek, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(kntl, get_string("failed9"))

    chiyex = await ureply.download_media()
    if chiyex.endswith(".tgs"):
        await kntl.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", chiyex, "chiy.png"]
        file = "chiy.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await kntl.edit(get_string("yimg_1"))
        img = cv2.VideoCapture(chiyex)
        kon, tol = img.read()
        cv2.imwrite("chiy.png", tol)
        file = "chiy.png"
    achi = cv2.imread(file)
    xnxx = cv2.flip(achi, 1)
    mici = cv2.hconcat([achi, xnxx])
    fr = cv2.flip(mici, 1)
    trn = cv2.rotate(fr, cv2.ROTATE_180)
    shicyxd = cv2.vconcat([mici, trn])
    cv2.imwrite("chiy.jpg", shicyxd)
    await memek.client.send_file(
        memek.chat_id,
        "chiy.jpg",
        force_document=False,
        reply_to=memek.reply_to_msg_id,
    )
    await kntl.delete()
    os.remove("chiy.png")
    os.remove("chiy.jpg")
    os.remove(chiyex)


@shicy_cmd(pattern=r"toon(?: |$)(.*)")
async def chiy(event):
    ureply = await event.get_reply_message()
    xd = await eor(event, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(xd, get_string("failed9"))

    chiyex = await ureply.download_media()
    if chiyex.endswith(".tgs"):
        await xd.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", chiyex, "chiy.png"]
        file = "chiy.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await xd.edit(get_string("yimg_1"))
        img = cv2.VideoCapture(chiyex)
        kon, tol = img.read()
        cv2.imwrite("chiy.png", tol)
        file = "chiy.png"
    chiy = cv2.imread(file)
    height, width, channels = chiy.shape
    samples = np.zeros([height * width, 3], dtype=np.float32)
    count = 0
    for x in range(height):
        for y in range(width):
            samples[count] = chiy[x][y]
            count += 1
    compactness, labels, centers = cv2.kmeans(
        samples,
        12,
        None,
        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001),
        5,
        cv2.KMEANS_PP_CENTERS,
    )
    centers = np.uint8(centers)
    asu = centers[labels.flatten()]
    shicyxd = asu.reshape(chiy.shape)
    cv2.imwrite("chiy.jpg", shicyxd)
    await event.client.send_file(
        event.chat_id,
        "chiy.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await xd.delete()
    os.remove("chiy.png")
    os.remove("chiy.jpg")
    os.remove(chiyex)


@shicy_cmd(pattern=r"danger(?: |$)(.*)")
async def shicy(event):
    ureply = await event.get_reply_message()
    shicy = await eor(shicy, get_string("com_1"))
    if not (ureply and (ureply.media)):
        return await eod(shicy, get_string("failed9"))

    shicyxd = await ureply.download_media()
    if shicyxd.endswith(".tgs"):
        await shicy.edit(get_string("com_1"))
        cmd = ["lottie_convert.py", shicyxd, "chiy.png"]
        file = "chiy.png"
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        stderr.decode().strip()
        stdout.decode().strip()
    else:
        await shicy.edit(get_string("yimg_1"))
        img = cv2.VideoCapture(shicyxd)
        kon, tol = img.read()
        cv2.imwrite("chiy.png", tol)
        file = "chiy.png"
    chiy = cv2.imread(file)
    dan = cv2.cvtColor(chiy, cv2.COLOR_BGR2RGB)
    kontol = cv2.cvtColor(dan, cv2.COLOR_HSV2BGR)
    cv2.imwrite("chiy.jpg", kontol)
    await event.client.send_file(
        event.chat_id,
        "chiy.jpg",
        force_document=False,
        reply_to=event.reply_to_msg_id,
    )
    await shicy.delete()
    os.remove("chiy.png")
    os.remove("chiy.jpg")
    os.remove(shicyxd)


@shicy_cmd(pattern=r"border(?: |$)(.*)")
async def shicyxd(event):
    mmk = await event.get_reply_message()
    if not (mmk and (mmk.photo or mmk.sticker)):
        return await eod(event, get_string("failed9"))
    kntl = event.pattern_match.group(1).strip()
    wh = 20
    if not kntl:
        kntl = [255, 255, 255]
    else:
        try:
            if ";" in kntl:
                col_ = kntl.split(";", maxsplit=1)
                wh = int(col_[1])
                kntl = col_[0]
            kntl = [int(kntl) for kntl in kntl.split(",")[:2]]
        except ValueError:
            return await eod(event, get_string("yimg_2"))
    yups = await mmk.download_media()
    img1 = cv2.imread(yups)
    constant = cv2.copyMakeBorder(
        img1, wh, wh, wh, wh, cv2.BORDER_CONSTANT, value=kntl)
    cv2.imwrite("output.png", constant)
    await event.client.send_file(event.chat.id, "output.png")
    os.remove("output.png")
    os.remove(yups)
    await event.delete()


@shicy_cmd(pattern=r"pixelator(?: |$)(.*)")
async def pixelator(event):
    reply_message = await event.get_reply_message()
    if not (reply_message and reply_message.photo):
        return await eod(event, get_string("failed9"))
    hw = 50
    try:
        hw = int(event.pattern_match.group(1).strip())
    except (ValueError, TypeError):
        pass
    chiy = await eor(event, get_string("com_1"))
    imshicy = await reply_message.download_media()
    input_ = cv2.imread(imshicy)
    height, width = input_.shape[:2]
    w, h = (hw, hw)
    temp = cv2.resize(input_, (w, h), interpolation=cv2.INTER_LINEAR)
    output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)
    cv2.imwrite("output.jpg", output)
    await chiy.respond(get_string("yimg_4"), file="output.jpg")
    await chiy.delete()
    os.remove("output.jpg")
    os.remove(imshicy)


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


CMD_HELP.update(
    {
        "chiyimg": f"**Plugin : **`chiyimg`\
        \n\n  »  **Perintah :** `{cmd}sketch` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}grey` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}blur` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}negative` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}miror` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}flp` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}quad` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}toon` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}danger` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}border` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
        \n\n  »  **Perintah :** `{cmd}pixelator` <reply ke Foto/Sticker>\
        \n  »  **Kegunaan :** Coba Dulu Tod.\
    "
    }
)
