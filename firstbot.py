import os
from dotenv import load_dotenv
from telebot import TeleBot, types


load_dotenv()

token = os.getenv('token')
bot = TeleBot(token)

print('token:', token)
# Функция создания клавиатуры с категориями
def create_category_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True)
    button1 = types.KeyboardButton('Button1')
    button2 = types.KeyboardButton('Button2')
    keyboard.add(button1, button2)
    return keyboard

# Функция создания клавиатуры с разделами
def create_section_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = types.KeyboardButton('CondletName')
    button2 = types.KeyboardButton('CondletName1')
    keyboard.add(button1, button2)
    return keyboard

# Функция создания клавиатуры с коллбэками
def create_callback_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    callback1 = types.KeyboardButton('CallBack1')
    callback2 = types.KeyboardButton('CallBack2')
    keyboard.add(callback1, callback2)
    return keyboard

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Выберите раздел для операций! ", reply_markup=create_category_keyboard())

# Обработчик выбора категории
@bot.message_handler(func=lambda message: message.text in ['Button1', 'Button2'])
def catalog_operation(message):
    if message.text == 'Button1':
        bot.reply_to(message, 'Выберите имя кондлета  ', reply_markup=create_section_keyboard())
    elif message.text == 'Button2':
        bot.reply_to(message, 'Выберите другой раздел  ', reply_markup=create_callback_keyboard())

# Обработчик выбора коллбэка
@bot.message_handler(func=lambda message: message.text in ['CallBack1', 'CallBack2'])
def handle_callback(message):
    if message.text == 'CallBack1':
        bot.send_message(message.chat.id, 'Ожидаем настройки для CallBack1...')
    elif message.text == 'CallBack2':
        bot.send_message(message.chat.id, 'Ожидаем настройки для CallBack2...')

# Обработчик выбора раздела
@bot.message_handler(func=lambda message: message.text in ['CondletName', 'CondletName1'])
def handle_condlet(message):
    if message.text == 'CondletName':
        bot.send_message(message.chat.id, 'Ожидаем настройки...')
    elif message.text == 'CondletName1':
        bot.send_message(message.chat.id, 'Ожидаем настройки для Condlet1...')

bot.polling()
