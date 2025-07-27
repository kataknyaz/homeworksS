from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from handlers.image_generation import handle_image_generation
from handlers.default import handle_default
from intents import IntentClassifier

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)
intent_classifier = IntentClassifier()

# Регистрация обработчиков
dp.register_message_handler(handle_image_generation, regexp="нарисуй|сгенерируй")
dp.register_message_handler(handle_default)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)