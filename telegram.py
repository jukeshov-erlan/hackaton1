import telebot
from hackaton1 import main
from decouple import config

token = config('TOKEN')
bot = telebot.TeleBot(token)
data = []


@bot.message_handler(commands=['start'])
def starting(message):
    global data
    bot.send_message(message.chat.id, 'загрузка ...')  
    data = main()
    for num in range(1, len(data) + 1):
        bot.send_message(message.chat.id, str(num) + data[num-1][0])

    resp = bot.send_message(message.chat.id, 'выберите новость', reply_markup=inline_keyboard)
    bot.register_next_step_handler(resp, check)


def check(message):
    num = int(message.text)
    resp = bot.send_message(message.chat.id, 'Можете посмотреть описание и фото', reply_markup=income_types)
    bot.register_next_step_handler(resp, get_info, num)


def get_info(message, num):
    if message.text.title() == 'Description':
        bot.send_message(message.chat.id, data[num][2])
        bot.register_next_step_handler(message, get_info, num)
    elif message.text.title() == 'Photo':
        bot.send_message(message.chat.id, data[num][1])
        bot.register_next_step_handler(message, get_info, num)
    elif message.text.title() == 'Quit':
        bot.send_message(message.chat.id, 'До свидания!')



inline_keyboard = telebot.types.ReplyKeyboardMarkup()
btn1 = telebot.types.KeyboardButton('1')
btn2 = telebot.types.KeyboardButton('2')
btn3 = telebot.types.KeyboardButton('3')
btn4 = telebot.types.KeyboardButton('4')
btn5 = telebot.types.KeyboardButton('5')
btn6 = telebot.types.KeyboardButton('6')
btn7 = telebot.types.KeyboardButton('7')
btn8 = telebot.types.KeyboardButton('8')
btn9 = telebot.types.KeyboardButton('9')
btn10 = telebot.types.KeyboardButton('10')
btn11 = telebot.types.KeyboardButton('11')
btn12 = telebot.types.KeyboardButton('12')
btn13 = telebot.types.KeyboardButton('13')
btn14 = telebot.types.KeyboardButton('14')
btn15 = telebot.types.KeyboardButton('15')
btn16 = telebot.types.KeyboardButton('16')
btn17 = telebot.types.KeyboardButton('17')
btn18 = telebot.types.KeyboardButton('18')
btn19 = telebot.types.KeyboardButton('19')
btn20 = telebot.types.KeyboardButton('20')

inline_keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6,btn7,btn8,btn9,btn10,btn11,btn12,btn13,btn14,btn15,btn16,btn17,btn18,btn19,btn20)

income_types = telebot.types.ReplyKeyboardMarkup()
knopka1 = telebot.types.KeyboardButton('Description')
knopka2 = telebot.types.KeyboardButton('Photo')
knopka3 = telebot.types.KeyboardButton('Quit')

income_types.add(knopka1, knopka2, knopka3)




bot.polling() 