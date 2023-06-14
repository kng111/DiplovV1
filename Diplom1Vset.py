


import telebot
from telebot import types
import Diplom2Vset
import time

bot = telebot.TeleBot('5841729632:AAGJnxJ87RHUdm5dYkVBx9ne3pnZBv6PfHY')


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.chat.id, "⚙️ Привет, {0.first_name}! Я твой бот-помошник,я пишу стихи!\nЕсли вам нужна помощь в навигации по телеграмм боту пишите /help".format(message.from_user), reply_markup=markup)

@bot.message_handler(commands=['help'])
def stop(message):
    bot.send_message(message.chat.id, "🚀 Раздел помощи и навигации.\nПеред вами навигация по телеграмм боту:\n1.⚙️ /start начало работы телеграмм бота (диалоговый стиль)\n2.🦿 /comands просмотр команд для быстрого доступа к функционалу бота\n3.🎓 /info информация о телеграмм боте, которая расскажет о работе данного бота\n4.🧳 /stop завершит работу данного телеграмм бота с вами.")

@bot.message_handler(commands=['comands'])
def stop(message):
    bot.send_message(message.chat.id, 'Раздел команд\nВвод ручной🤲🏻,напишите:\n"О любви." - для получения стиха о любви.❤️\n"О природе." - для получения стиха о природе.⛰\n"О жизни." - для получения стиха о жизни.🏫\n"О родине." - для получения стиха о родине.💪🏻\n"Хочу свой текст." - если у вас есть готовый текст который вы хотите перегенирировать с помощью бота.👁\n"Я хочу увидеть твой стих." - если вы хотите что бы бот сам придумал для вас стих.👀\nБудьте внимательны, все команды вводяться так как написанны в ковычках.👓')

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, "Этот бот создан для помощи в написании стихов. Вы можете выбрать готовый стих по жанру или создать свой собственный. Для создания своего стиха выберите нужную опцию в диалоге с ботом прописав команду /start\n или напишите: 'Я хочу создать свой стих по жанру.'\nЛибо напишите: 'Я хочу увидеть твой стих.'\nЕсли вам не нужна помощь нашего бота можете написать /stop")

@bot.message_handler(commands=['stop'])
def stop(message):
    bot.send_message(message.chat.id, "🌎 До свидания! Если вам понадобится моя помощь в будущем, просто напишите /start. 🌎")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn2 = types.KeyboardButton('Я хочу создать свой стих по жанру.')
        btn3 = types.KeyboardButton('Я хочу увидеть твой стих.')
        markup.add(btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Скажи что тебя интересует. Чего ты хочешь', reply_markup=markup) #ответ бота
    elif message.text == 'Я хочу создать свой стих по жанру.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('О любви.')
        btn2 = types.KeyboardButton('О природе.')
        btn3 = types.KeyboardButton('О жизни.')
        btn4 = types.KeyboardButton('О родине.')
        btn5 = types.KeyboardButton('Хочу свой текст.')
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, 'Будет сделано.💡', reply_markup=markup)

    elif message.text == 'Я хочу увидеть твой стих.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton('Мне понравилось')
        btn5 = types.KeyboardButton('Хочу другой стих')
        markup.add(btn4, btn5)
        bot.send_message(message.from_user.id,(Diplom2Vset.stih()), reply_markup=markup)

    elif message.text == 'Мне понравилось':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn6 = types.KeyboardButton('Да.')
        btn7 = types.KeyboardButton('Нет.')
        markup.add(btn6, btn7)
        bot.send_message(message.from_user.id, '❤️ Спасибо, я был обучен для этого, хочешь ещё?', reply_markup=markup)

    elif message.text == 'Да.':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn4 = types.KeyboardButton('Мне понравилось')
        btn5 = types.KeyboardButton('Хочу другой стих')
        markup.add(btn4, btn5)
        bot.send_message(message.from_user.id,(Diplom2Vset.stih()), reply_markup=markup)

    elif message.text == 'Нет.':
        bot.send_message(message.from_user.id,("Хорошо тогда напиши /info и посмотри что я могу сделать для тебя ещё"))
    elif message.text == 'Хочу другой стих':
        bot.send_message(message.from_user.id,(Diplom2Vset.stih()))
    elif message.text == 'О любви.':
        bot.send_message(message.from_user.id,(Diplom2Vset.stihPolz(x="love.txt")))
    elif message.text == 'О природе.':
        bot.send_message(message.from_user.id,(Diplom2Vset.stihPolz(x="priroda.txt")))
    elif message.text == 'О жизни.':
        bot.send_message(message.from_user.id,(Diplom2Vset.stihPolz(x="live.txt")))
    elif message.text == 'О родине.':
        bot.send_message(message.from_user.id,(Diplom2Vset.stihPolz(x="rodina.txt")))
    elif message.text == 'Хочу свой текст.':
        bot.send_message(message.from_user.id, "💍 Хорошо, введите свой текст:")
        bot.register_next_step_handler(message, process_custom_text)
    else:
        bot.send_message(message.from_user.id, "🐍 Неправильный ввод. Пожалуйста, выберите один из предложенных вариантов. или напиши /info или /help")
def process_custom_text(message):
    for i in range(1):
        custom_text = message.text
        if len(custom_text) > 250 and len(custom_text) < 750:
            lines = [custom_text] * 1000
            
            with open(r"inputPolz.txt", "w", encoding='utf-8') as file:
                for  line in lines:
                    file.write(line + '\n')
            time.sleep(1)
            bot.send_message(message.from_user.id, f"✉️ Вот ваш текст:")
            bot.send_message(message.from_user.id, f"{Diplom2Vset.stihPolz2()}")

            




        elif len(custom_text) < 250:
            bot.send_message(message.from_user.id, f"✉️ Ваш текст слишком мал его длина состовляет: {len(custom_text)},рекомендованная длина больше 250 символов и не более 750\n попробуйте ещё раз")
            message.text = 0
            bot.register_next_step_handler(message, process_custom_text)
            
        elif len(custom_text) > 750:
            bot.send_message(message.from_user.id, f"✉️ Ваш текст длинный его длина состовляет: {len(custom_text)},рекомендованная длина не более 750 символов и не менее 250\n попробуйте ещё раз:")
            message.text = 0
            bot.register_next_step_handler(message, process_custom_text)
bot.polling(none_stop=True, interval=0) 


