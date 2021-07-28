import telebot
import qrcode

from peremen import token, privetstvie, planeta, bigviz, UPS, mxP, mxU, mxV, chisla
bD=0
bV=0
bU=0
mP=4
mV=33
mU=21
mesP = int(mxP) - (int(bD) + int(mP))
mesV = int(mxV) - (int(bV) + int(mV))
mesU = int(mxU) - (int(bU) + int(mU))
p=0
v=0
u=0
bot = telebot.TeleBot(token)
qrBS, qrBV, qrUPS="","",""
user_id=''

@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.from_user.id
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Просмотреть мероприятия')
    keyboard.row('Забронировать билет')
    keyboard.row('Забронированные мероприятия')
    bot.send_message(message.chat.id, privetstvie , reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'просмотреть мероприятия':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Белка и Стрелка. Правда.', callback_data=1))
        markup.add(telebot.types.InlineKeyboardButton(text='Большие вызовы', callback_data=2))
        markup.add(telebot.types.InlineKeyboardButton(text='Уральская Проектная Смена', callback_data=3))
        bot.send_message(message.chat.id, text="Выберите интересующее Вас мероприятие, чтобы узнать информацию о нем", reply_markup=markup)
    elif message.text.lower() == 'забронировать билет':
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Белка и Стрелка. Правда.', callback_data=4))
        markup.add(telebot.types.InlineKeyboardButton(text='Защита проектов в конкурсе "Большие вызовы"', callback_data=5))
        markup.add(telebot.types.InlineKeyboardButton(text='Защита проектов "Уральская Проектная Смена"', callback_data=6))
        bot.send_message(message.chat.id, text="Выберите интересующее Вас мероприятие", reply_markup=markup)
    elif message.text.lower() == 'забронированные мероприятия':
        if p<=0 and v<=0 and u<=0:
            bot.send_message(message.chat.id, "Нет забронированных мероприятий")
        else:
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row('Просмотреть билет на "Белка и Стрелка. Правда."')
            keyboard.row('Просмотреть билет на "Большие вызовы"')
            keyboard.row('Просмотреть билет на "Уральская Проектная Смена"')
            bot.send_message(message.chat.id, "У вас " + str(p + v + u) + " забронированных(ый) билет(а)", reply_markup=keyboard)
    elif message.text == 'Просмотреть билет на "Белка и Стрелка. Правда."' and p==1:
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Просмотреть мероприятия')
        keyboard.row('Забронировать билет')
        keyboard.row('Забронированные мероприятия')
        bot.send_message(message.chat.id, text='Ваш билет', reply_markup=keyboard)
        qrBS = open('qr'+str(user_id)+'BS.png', 'rb')
        bot.send_photo(message.chat.id, qrBS)
        bot.send_message(message.chat.id, 'Мероприятие: Белка и Стрелка. Правда.\n'
                                          'Количество мест: ' + str(bD) + '\n'
                                          'Дата: 03.09.2021\n'
                                          'Время: 16:00')
    elif message.text == 'Просмотреть билет на "Белка и Стрелка. Правда."' and p==0:
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Просмотреть мероприятия')
        keyboard.row('Забронировать билет')
        keyboard.row('Забронированные мероприятия')
        bot.send_message(message.chat.id, 'Вы не забронировали места на это мероприятие ')
    elif message.text == 'Просмотреть билет на "Большие вызовы"' and v==1:
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Просмотреть мероприятия')
        keyboard.row('Забронировать билет')
        keyboard.row('Забронированные мероприятия')
        bot.send_message(message.chat.id, text='Ваш билет', reply_markup=keyboard)
        qrBS = open('qr' + str(user_id) + 'BV.png', 'rb')
        bot.send_photo(message.chat.id, qrBS)
        bot.send_message(message.chat.id, 'Мероприятие: Большие вызовы, защита проектов.\n'
                                          'Количество мест: ' + str(bV) + '\n'
                                          'Дата: 27.07.2021\n'
                                          'Время: 10:00')
    elif message.text == 'Просмотреть билет на "Большие вызовы"' and v==0:
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Просмотреть мероприятия')
        keyboard.row('Забронировать билет')
        keyboard.row('Забронированные мероприятия')
        bot.send_message(message.chat.id, 'Вы не забронировали места на это мероприятие ')
    elif message.text == 'Просмотреть билет на "Уральская Проектная Смена"' and u==1:
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Просмотреть мероприятия')
        keyboard.row('Забронировать билет')
        keyboard.row('Забронированные мероприятия')
        bot.send_message(message.chat.id, text='Ваш билет', reply_markup=keyboard)
        qrUPS = open('qr' + str(user_id) + 'UPS.png', 'rb')
        bot.send_photo(message.chat.id, qrUPS)
        bot.send_message(message.chat.id, 'Мероприятие: Уральская Проектная Смена, защита проектов.\n'
                                          'Количество мест: ' + str(bU) + '\n'
                                          'Дата: 24.01.2022\n'
                                          'Время: 12:00')
    elif message.text == 'Просмотреть билет на "Уральская Проектная Смена"' and u==0:
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('Просмотреть мероприятия')
        keyboard.row('Забронировать билет')
        keyboard.row('Забронированные мероприятия')
        bot.send_message(message.chat.id, 'Вы не забронировали места на это мероприятие ')

def get_biletP(message):
    bronP = message.text
    if bronP in chisla:
        if user_id=='':
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row('/start')
            bot.send_message(message.chat.id, 'ОШИБКА! Начните пожалуйста сначала', reply_markup=keyboard)
        else:

            if int(bronP) <= int(mesP):
                global bD
                bD = bD + int(bronP)
                img = qrcode.make('Мероприятие: Белка и Стрелка. Правда.\n'
                                  'Количество мест: ' + str(bD) + '\n'
                                  'Дата: 03.09.2021\n'
                                   'Время: 16:00')
                img.save('qr'+str(user_id)+'BS.png')
                global qrBS
                qrBS = open('qr'+str(user_id)+'BS.png', 'rb')
                bot.send_photo(message.chat.id, qrBS)
                bot.send_message(message.chat.id, 'Мероприятие: Белка и Стрелка. Правда.\n'
                                                  'Количество мест: ' + str(bD) + '\n'
                                                  'Дата: 03.09.2021\n'
                                                  'Время: 16:00')
                bot.send_message(message.chat.id, 'Вы забронировали ' + str(bronP) + ' мест. Предъявите этот QR код на входе.')
                global p
                p = 1
            else:
                keyboard = telebot.types.ReplyKeyboardMarkup(True)
                keyboard.row('/start')
                bot.send_message(message.chat.id, 'ОШИБКА! Вы хотели забронировать слишком большое количество мест ', reply_markup=keyboard)
    else:
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/start')
        bot.send_message(message.chat.id, 'ОШИБКА! Начните пожалуйста сначала', reply_markup=keyboard)

def get_biletV(message):
    bronV = message.text
    if bronV in chisla:
        if user_id=='':
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row('/start')
            bot.send_message(message.chat.id, 'ОШИБКА! Начните пожалуйста сначала', reply_markup=keyboard)
        elif int(bronV) <= int(mesV):
            global bV
            bV = bV + int(bronV)
            img = qrcode.make('Мероприятие: Большие вызовы, защита проектов.\n'
                              'Количество мест: ' + str(bV) +'\n'
                              'Дата: 27.07.2021\n'
                              'Время: 10:00')
            img.save('qr' + str(user_id) + 'BV.png')
            global qrBV
            qrBV = open('qr' + str(user_id) + 'BV.png', 'rb')
            bot.send_photo(message.chat.id, qrBV)
            bot.send_message(message.chat.id, 'Мероприятие: Большие вызовы, защита проектов.\n'
                                              'Количество мест: ' + str(bV) +'\n'
                                              'Дата: 27.07.2021\n'
                                              'Время: 10:00')
            bot.send_message(message.chat.id, 'Предъявите этот QR код на входе.')
            global v
            v=1
        else:
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row('/start')
            bot.send_message(message.chat.id, 'ОШИБКА! Вы хотели забронировать слишком большое количество мест ', reply_markup=keyboard)
    else:
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/start')
        bot.send_message(message.chat.id, 'ОШИБКА! Начните пожалуйста сначала', reply_markup=keyboard)

def get_biletU(message):
    bronU = message.text
    if bronU in chisla:
        if user_id == '':
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row('/start')
            bot.send_message(message.chat.id, 'ОШИБКА! Начните пожалуйста сначала', reply_markup=keyboard)
        if int(bronU) <= int(mesU):
            global bU
            bU = bU + int(bronU)
            img = qrcode.make('Мероприятие: Уральская Проектная Смена, защита проектов.\n'
                              'Количество мест: ' + str(bU) + '\n'
                              'Дата: 24.01.2022\n'
                              'Время: 12:00')
            img.save('qr' + str(user_id) + 'UPS.png')
            global qrUPS
            qrUPS = open('qr' + str(user_id) + 'UPS.png', 'rb')
            bot.send_photo(message.chat.id, qrUPS)
            bot.send_message(message.chat.id, 'Мероприятие: Уральская Проектная Смена, защита проектов.\n'
                                              'Количество мест: ' + str(bU) + '\n'
                                              'Дата: 24.01.2022\n'
                                              'Время: 12:00')
            bot.send_message(message.chat.id, 'Предъявите этот QR код на входе.')
            global u
            u=1
        else:
            keyboard = telebot.types.ReplyKeyboardMarkup(True)
            keyboard.row('/start')
            bot.send_message(message.chat.id, 'ОШИБКА! Вы хотели забронировать слишком большое количество мест ', reply_markup=keyboard)
    else:
        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        keyboard.row('/start')
        bot.send_message(message.chat.id, 'ОШИБКА! Начните пожалуйста сначала', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == '1':
        answer = planeta
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Забронировать', callback_data=4))
        bot.send_message(call.message.chat.id, answer, reply_markup=markup)

    elif call.data == '2':
        answer = bigviz
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Забронировать', callback_data=5))
        bot.send_message(call.message.chat.id, answer, reply_markup=markup)

    elif call.data == '3':
        answer = UPS
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Забронировать', callback_data=6))
        bot.send_message(call.message.chat.id, answer, reply_markup=markup)

    elif call.data == '4':
        if mP+bD >= mxP:
            answer = 'Все места забронированы'
            bot.send_message(call.message.chat.id, answer)
        elif mP<mxP:
            bot.send_message(call.message.chat.id, 'Свободно мест: '+str(int(mxP)-(bD+int(mP))))
            sent =bot.send_message(call.message.chat.id, 'Сколько мест вы хотите забронировать? Введите количество.')
            bot.register_next_step_handler(sent, get_biletP)

    elif call.data == '5':
        if mV+bV >= mxV:
            answer = 'Все места забронированы'
            bot.send_message(call.message.chat.id, answer)
        elif mV < mxV:
            bot.send_message(call.message.chat.id, 'Свободно мест: '+str(int(mxV)-(bV+int(mV))))
            sent = bot.send_message(call.message.chat.id, 'Сколько мест вы хотите забронировать? Введите количество.')
            bot.register_next_step_handler(sent, get_biletV)

    elif call.data == '6':
        if mU+bU >= mxU:
            answer = 'Все места забронированы'
            bot.send_message(call.message.chat.id, answer)
        elif mU < mxU:
            bot.send_message(call.message.chat.id, 'Свободно мест: ' +str(int(mxU)-(bU+int(mU))))
            sent = bot.send_message(call.message.chat.id, 'Сколько мест вы хотите забронировать? Введите количество.')
            bot.register_next_step_handler(sent, get_biletU)

bot.polling()
