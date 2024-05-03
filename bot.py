from aiogram import Bot, Dispatcher, types, F
import asyncio
import os
import time
from moviepy.editor import *

folder = "input_image"
if not os.path.exists(folder):
    os.makedirs(folder)
folder_out = "out_image"
if not os.path.exists(folder_out):
    os.makedirs(folder_out)
token = "6871114067:AAHrDHSIkgPSXBi8vlfPoRLx_MBpUBDPrXQ"

bot = Bot(token=token)
dp = Dispatcher()
@dp.message(F.video)
async def test(message: types.Message):
    video = message.video
    file_id = video.file_id
    width = video.width
    height = video.height
    size = (video.file_size) / (1024*1024)
    file_name = video.file_name
    file_type = video.mime_type
    duration = video.duration
    print(width, height, file_name, file_type)

    if size > 20:
        await message.answer("tashlagan videoing hajmni kichikroq tashla eeey odam bulaysan 10 mb dam kam bulsin")
    else:
        file = await bot.get_file(file_id=file_id)
        name = f"{folder}/{message.video.file_name}_{time.time()}.mp4"
        await bot.download(file=file,   destination=name)  # buni boshqa usuli ham bor unda vaqt bilan nomlanadi yani await bot.download(file=file, destination=f"{time.time()}"
        # await message.answer_video(video=file_id)# user yoborgan videoni uziga qaytarib yuborish uchun ishlatildi
        # await message.answer(f"{file_name}\n{file_type}\n{width}\n{height}")

        clip = VideoFileClip(filename=name)
        audio = clip.audio
        name_out = f"{folder_out}/{message.video.file_name}_{time.time()}.mp3"
        audio.write_audiofile(name_out)

        send = types.input_file.FSInputFile(path=name_out)
        await bot.send_chat_action(action='upload_audio', chat_id=message.chat.id)
        await message.answer_audio(audio=send)

        # agar vediolarni uchirin tashlamoqchi bulsangiz
        try:
            if os.path.isfile(name_out):
                os.remove(name_out)
            if os.path.isfile(name):
                os.remove(name)
        except:
            pass

    if duration>60:
         await message.answer("1 minutdan kam vidoe tashla")
    else:
        if size>10:
            await message.answer("tashlagan videoing hajmni kichikroq tashla eeey odam bulaysan 10 mb dam kam bulsin")
        else:
            file = await bot.get_file(file_id=file_id)
            name=f"{folder}/{message.video.file_name}_{time.time()}.mp4"
            await bot.download(file=file, destination=name)#buni boshqa usuli ham bor unda vaqt bilan nomlanadi yani await bot.download(file=file, destination=f"{time.time()}"
            #await message.answer_video(video=file_id)# user yoborgan videoni uziga qaytarib yuborish uchun ishlatildi
            #await message.answer(f"{file_name}\n{file_type}\n{width}\n{height}")
            clip = VideoFileClip(filename=name)
            target_width = 1000
            target_height = 1000
            resize = clip.resize((target_width, target_height))
            name_out=f"{folder_out}/{message.video.file_name}_{time.time()}.mp4"
            resize.write_videofile(name_out, codec="libx264")
            send = types.input_file.FSInputFile(path=name_out)
            await bot.send_chat_action(action="upload_video_note", chat_id=message.chat.id)
            await message.answer_video_note(video_note=send)

            # agar vediolarni uchirin tashlamoqchi bulsangiz
            try:
                if os.path.isfile(name_out):
                    os.remove(name_out)
                if os.path.isfile(name):
                    os.remove(name)
            except:
                pass

@dp.message(F.video_note)
async def test(message: types.Message):
    video = message.video_note.thumbnail
    file_id = message.video_note.file_id

    width = video.width
    height = video.height
    size = (video.file_size) / (1024*1024)
    duration = message.video_note.duration
    print(width, height)

    if size > 20:
        await message.answer("tashlagan videoing hajmni kichikroq tashla eeey odam bulaysan 10 mb dam kam bulsin")
    else:
        file = await bot.get_file(file_id=file_id)
        name = f"{folder}/{time.time()}.mp4"
        await bot.download(file=file,   destination=name)  # buni boshqa usuli ham bor unda vaqt bilan nomlanadi yani await bot.download(file=file, destination=f"{time.time()}"
        # await message.answer_video(video=file_id)# user yoborgan videoni uziga qaytarib yuborish uchun ishlatildi
        # await message.answer(f"{file_name}\n{file_type}\n{width}\n{height}")

        clip = VideoFileClip(filename=name)
        audio = clip.audio
        name_out = f"{folder_out}/{time.time()}.mp3"
        audio.write_audiofile(name_out)

        send = types.input_file.FSInputFile(path=name_out)
        await bot.send_chat_action(action='upload_audio', chat_id=message.chat.id)
        await message.answer_audio(audio=send)

        # agar vediolarni uchirin tashlamoqchi bulsangiz
        try:
            if os.path.isfile(name_out):
                os.remove(name_out)
            if os.path.isfile(name):
                os.remove(name)
        except:
            pass

    if duration>60:
         await message.answer("1 minutdan kam vidoe tashla")
    else:
        if size>10:
            await message.answer("tashlagan videoing hajmni kichikroq tashla eee 10 mb dam kam bulsin")
        else:
            file = await bot.get_file(file_id=file_id)
            name=f"{folder}/{time.time()}.mp4"
            await bot.download(file=file, destination=name)#buni boshqa usuli ham bor unda vaqt bilan nomlanadi yani await bot.download(file=file, destination=f"{time.time()}"
            #await message.answer_video(video=file_id)# user yoborgan videoni uziga qaytarib yuborish uchun ishlatildi
            #await message.answer(f"{file_name}\n{file_type}\n{width}\n{height}")
            clip = VideoFileClip(filename=name)
            target_width = 1000
            target_height = 1000
            resize = clip.resize((target_width, target_height))
            name_out=f"{folder_out}/{time.time()}.mp4"
            resize.write_videofile(name_out, codec="libx264")
            send = types.input_file.FSInputFile(path=name_out)
            await bot.send_chat_action(action="upload_video_note", chat_id=message.chat.id)
            await message.answer_video_note(video_note=send)

            # agar vediolarni uchirin tashlamoqchi bulsangiz
            try:
                if os.path.isfile(name_out):
                    os.remove(name_out)
                if os.path.isfile(name):
                    os.remove(name)
            except:
                pass

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())


















