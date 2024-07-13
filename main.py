import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

TOKEN = "7380017732:AAE_7YC9-b6VeUnGC_7HwrYz6iCPb5RjLhU"

bot = Bot(TOKEN)

dp = Dispatcher()

btn = [
    [KeyboardButton(text="video"),
     KeyboardButton(text="image")]
]

keyboard = ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True)


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Assalomu Alaykum", reply_markup=keyboard)


@dp.message(F.text == "video")
async def send_video(message: Message):
    await message.answer_video(video="https://videos.pexels.com/video-files/3512545/3512545-hd_1920_1080_25fps.mp4",
                               caption="Video")


@dp.message(F.text == "image")
async def send_image(message: Message):
    await message.answer_photo(
        photo="https://images.app.goo.gl/qqcA5EsrnDa6vwFQ8",
        caption="Image")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
