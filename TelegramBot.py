import telebot
import requests
import json


bot = telebot.TeleBot("5558127085:AAHuEByTiMzX6N4SqReYS-Bad9DNRZSJRNA")

keys = {
    'доллар': 'USD',
    'евро': 'EUR',
    'рубль': 'RUB'
}

@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    bot.reply_to(message, f"Приветствую тебя {message.chat.username}")

@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите команду боту в следующем формате: \n<имя валюты> \
<в какую валюту перевести> \
<количество переводимой валюты>\nУвидеть все доступные валюты: /valutes'
    bot.reply_to(message, text)

@bot.message_handler(commands=['valutes'])
def valutes(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(commands=['converter'])
def converter(message: telebot.types.Message):
    base, sym, amount = message.text.split(' ')
    r = requests.get(f"https://v6.exchangerate-api.com/v6/f040ed82315fbb26bdc898ed/latest/")
    resp = json.loads(r.content)
    new_price = resp ['rates'][sym] * float(amount)
    bot.reply_to(message, f"Цена {amount} {base} в {sym} : {new_price}")

bot.polling(none_stop=True)