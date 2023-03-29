import telebot
import pytube
from  telebot import  types

bot = telebot.TeleBot('6229906007:AAGdg4sKOnsqtnHAgGhPao8KnpPHCfENKFI');
keyboard = types.InlineKeyboardMarkup();
name = '';
surname = '';
age = '';

@bot.message_handler(commands=['button'])
def button_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(True)
    markup.row("/start")
    markup.row("Регистрация")
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)



@bot.message_handler(commands=['start'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, я бот компании!")
        bot.send_message(message.from_user.id, "Напишите или нажмите /reg для регистрации")
    else:
        bot.send_message(message.from_user.id, "Напишите или нажмите /start")

@bot.message_handler(commands=['reg'])
def start(message):
    if message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?");
        bot.register_next_step_handler(message, get_name); #следующий шаг – функция get_name
    else:
        bot.send_message(message.from_user.id, "Напишите имя")


def get_name(message): #получаем фамилию
    global name;
    name = message.text;
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global surname;
    surname = message.text;
    bot.send_message(message.from_user.id, 'Сколько тебе лет?');
    bot.register_next_step_handler(message, get_age);

def get_age(message):
    global age;
    age = message.text;

    keyboard = types.InlineKeyboardMarkup();
    key_yes = types.InlineKeyboardButton(text = 'Да',  callback_data='yes');
    keyboard.add(key_yes);
    key_no = types.InlineKeyboardButton(text = 'Нет', callback_data='no');
    keyboard.add(key_no);
    question = 'Тебе ' + age + ' лет, тебя зовут ' + name + ' ' + surname + '?';
    bot.send_message(message.from_user.id, text = question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        bot.send_message(call.message.chat.id, 'Запомню');
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, 'Ладно')

bot.infinity_polling()