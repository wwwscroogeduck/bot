#подключение библиотек
import telebot
from telebot import types
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


#обращение к библиотеке и классу TeleBot + токен бота
bot = telebot.TeleBot('6928668290:AAGGEyPBLn3eO3pjOTB8jBsfxQJnWxCZ-to')

#декоратор для функции отслеживания команды
@bot.message_handler(commands = ['start'])
#функция принимающая один параметр (принимает команду старт, а бот каждый раз отправляет "Привет и имя")
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton ('О боте', message.chat.id, f'Этот бот предназначен для получения мотивирующих картинок под настроение')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton ('Перейти на сайт с играми', url='https://igroutka.ru/onlayn-igry.html')
    btn3 = types.InlineKeyboardButton ('Удалить', callback_data = 'delete')
    markup.row(btn2, btn3)
    #метод, содержащий id чата, с которым взаимодействуем
    bot.send_message(message.chat.id, f'Привет! {message.from_user.first_name} {message.from_user.last_name}', reply_markup=markup)

#для того чтобы бот работал постоянно
bot.polling(non_stop=True)