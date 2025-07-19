import asyncio
from telebot.async_telebot import AsyncTeleBot
import requests
import json
import aiohttp

TELEGRAM_TOKEN = '7587174709:AAGcwNwOxyyHBkUWMdxuV3gozSzqPYwxjQw'
OPENROUTER_KEY = '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'

bot = AsyncTeleBot(TELEGRAM_TOKEN)

# Память бота
user_memory = {}

print('Приложение запущено')


async def sendAi(message, user_id):
    try:
        # Добавляем контекст из памяти пользователя
        context = user_memory.get(user_id, [])
        context.append({"role": "user", "content": message})

        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_KEY}",
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "model": "google/gemma-3n-e2b-it:free",
                "messages": context,
            })
        )
        
        # Обновляем память с ответом AI
        ai_response = response.json()
        context.append({"role": "assistant", "content": ai_response['choices'][0]['message']['content']})
        user_memory[user_id] = context  # Сохраняем обновленный контекст

        return ai_response
    except Exception as e:
        print(e)


async def free_generate(prompt):
    async with aiohttp.ClientSession() as session:
        payload = {
            "token": 'YOUR_GENERATE_TOKEN',
            "prompt": prompt,
            "stream": True
        }

        async with session.post(
            "https://neuroimg.art/api/v1/free-generate",
            json=payload
        ) as response:
            async for line in response.content:
                if line:
                    data = json.loads(line)
                    if data["status"] == "SUCCESS":
                        return data["image_url"]
                    print(f"Статус: {data['status']}")
    return response.json()


@bot.message_handler(commands=['draw'])
async def generate(message):
    str = message.text.split(' ')
    str.remove(str[0])
    await bot.send_message(message.chat.id, " ".join(str))

    await bot.send_message(message.chat.id, 'Генерирую изображение')
    await bot.send_chat_action(message.chat.id, 'upload_photo')
    image_url = await free_generate(message.text)
    await bot.send_photo(message.chat.id, image_url)


@bot.message_handler(content_types=['text'])
async def echo(message):
    await bot.send_chat_action(message.chat.id, 'typing')
    response = await sendAi(message.text, message.from_user.id)
    await bot.send_message(message.chat.id, response['choices'][0]['message']['content'])

asyncio.run(bot.polling())
