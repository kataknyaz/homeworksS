from telebot import TeleBot  
import json 
import requests  # Для выполнения HTTP-запросов к API

bot = TeleBot("7587174709:AAGcwNwOxyyHBkUWMdxuV3gozSzqPYwxjQw") # экземляр бота
# @bot.message_handler(commands=['valute'])
# def valute(message):
#     api = json.loads(requests.get("https://www.cbr-xml-daily.ru/daily_json.js").text)
#     words_list = message.text.strip().split(' ')[1:]
#     if words_list[0].isupper():
#         valute = api['Valute'][words_list[0]]
#         text_list = []
#         for key, value in valute.items():
#             text_list.append(f"{key} - {value}")
#         bot.reply_to(message, '\n'.join(text_list))
#         return
#     elif words_list[0] == words_list[0].capitalize():
#         if len(words_list) == 1:
#             word = words_list[0].capitalize()
#         if len(words_list) == 2:
#             word = words_list[0].capitalize() + " " + words_list[1].lower()


bot.polling()

@bot.message_handler(commands=['valute'])
def valute(message):
    try:
        # Получаем данные от API Центробанка
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
        response.raise_for_status()  # Генерируем исключение при ошибке HTTP
        api = response.json()  # Парсим JSON-ответ
        
        
        input_text = message.text.strip().split(' ')[1:]  
        
        # аустой ли ввод(проверка)
        if not input_text:
            bot.reply_to(message, "Пожалуйста, укажите код валюты (например: USD, EUR) или название (например: Доллар, Евро)")
            return
            
        currency_input = ' '.join(input_text).upper()  # Объединяем и переводим в верхний регистр
        
        #Поиск по коду валюты
        if currency_input in api['Valute']:
            valute_data = api['Valute'][currency_input]
            response_text = (
                f"{valute_data['Name']} ({valute_data['CharCode']}):\n"
                f"Номинал: {valute_data['Nominal']}\n"
                f"Курс: {valute_data['Value']} RUB\n"
                f"Предыдущий курс: {valute_data['Previous']} RUB"
            )
            bot.reply_to(message, response_text)
            return
        
        #Если не найдено по коду, то ищем по названию
        found_currency = None
        for code, currency in api['Valute'].items():
            if currency_input.lower() in currency['Name'].lower():
                found_currency = currency
                break
                
        
        if found_currency:
            response_text = (
                f"{found_currency['Name']} ({found_currency['CharCode']}):\n"
                f"Номинал: {found_currency['Nominal']}\n"
                f"Курс: {found_currency['Value']} RUB\n"
                f"Предыдущий курс: {found_currency['Previous']} RUB"
            )
            bot.reply_to(message, response_text)
        else:
            bot.reply_to(message, f"Валюта '{' '.join(input_text)}' не найдена. Попробуйте указать код валюты (USD, EUR и т.д.)")
            
    except requests.exceptions.RequestException as e:
        
        bot.reply_to(message, f"Ошибка при получении данных: {e}")# Обработка ошибок с API
    except Exception as e:
        
        bot.reply_to(message, f"Произошла ошибка: {e}")# Обработка прочих ошибок


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    help_text = (
        "Доступные команды:\n"
        "/valute [код или название] - получить курс валюты\n"
        "Примеры:\n"
        "/valute USD - курс доллара\n"
        "/valute евро - курс евро\n"
        "/valute японская йена - курс йены\n\n"
        "Доступные валюты: USD, EUR, GBP, CNY, JPY и другие"
    )
    bot.reply_to(message, help_text)

bot.polling()     