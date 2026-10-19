import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# Tokenni Render muhitidan (Environment Variables) olamiz
API_TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    welcome_text = (
        f"Assalomu alaykum, {message.from_user.first_name}!\n\n"
        f"<b>BullDrop.uz</b> rasmiy botiga xush kelibsiz! 🎲\n\n"
        f"Saytimizdan foydalanish uchun quyidagi tugmani bosing:"
    )
    
    # Tugma orqali to'g'ridan-to'g'ri saytni ochish (Web App ko'rinishida)
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [types.InlineKeyboardButton(text="🎮 BullDrop.uz ochish", web_app=types.WebAppInfo(url="https://bulldrop.uz"))]
        ]
    )
    
    await message.answer(welcome_text, parse_mode="HTML", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
