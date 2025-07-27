from aiogram import types
from services.image_api import generate_image

async def handle_image_generation(message: types.Message):
    await message.answer("🖌️ Генерирую изображение...")
    
    try:
        image_url = await generate_image("живописный пейзаж")  # Можно брать текст из message.text
        await message.answer_photo(image_url)
    except Exception as e:
        await message.answer(f"❌ Ошибка: {e}")