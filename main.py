import logging
from aiogram import Bot, Dispatcher, executor, types
from parser.yandex_parser import parse_yandex_maps
from analyzer.site_checker import check_sites
from reporting.pdf_generator import generate_pdf
import os

API_TOKEN = os.getenv("BOT_TOKEN", "your_telegram_token_here")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.answer("Привет! Я бот, который находит компании без сайтов и формирует отчёт. Подождите, идёт обработка...")

    try:
        raw_data = parse_yandex_maps()
        filtered_data = check_sites(raw_data)
        pdf_path = generate_pdf(filtered_data)

        with open(pdf_path, "rb") as pdf:
            await message.answer_document(pdf, caption="Вот ваш отчёт")
    except Exception as e:
        logging.exception("Ошибка при обработке запроса")
        await message.answer("Произошла ошибка при обработке данных. Попробуйте позже.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
