import telebot
bot = telebot.TeleBot('6761460410:AAFquXiLgB6DY5-HnXR0Lo2XL-F8abJ19PE')

@bot.message_handler(func=lambda message: message.text.lower() == "заново")
@bot.message_handler(commands=['start']) #бот запускается по команде /start или "заново"
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('Социальная сеть')
    button2 = telebot.types.KeyboardButton('Онлайн-игра')
    button3 = telebot.types.KeyboardButton('Форум')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, f'<b>Привет {message.from_user.first_name}</b>!\n'
                                      f'Выберите для чего вам нужен никнейм:', parse_mode='html', reply_markup=markup)#сообщение при команде /start с выбором кнопок

@bot.message_handler(func=lambda message:True)
def handle_message(message):#сообщение при выборе кнопки
    if message.text == 'Социальная сеть':
        bot.send_message(message.chat.id, '<b>Вводите все слова строчными латинскими буквами!</b>\n'
                                          'Введите ваше имя:',parse_mode='html')
        bot.register_next_step_handler(message, save_name)
    elif message.text == 'Онлайн-игра':
        bot.send_message(message.chat.id, '<b>Вводите все слова строчными латинскими буквами!</b>\n'
                                          'Введите ваше имя:',parse_mode='html')
        bot.register_next_step_handler(message, save_name2)
    elif message.text == 'Форум':
        bot.send_message(message.chat.id, '<b>Вводите все слова строчными латинскими буквами!</b>\n'
                                          'Введите ваше имя:',parse_mode='html')
        bot.register_next_step_handler(message, save_name3)
    else:
        bot.send_message(message.chat.id, 'Ой-ой. Вы ввели неправильный вариант ответа. Чтобы начать заново нажми ⇨ /start')#сообщение, если пользователь ввёл что-то не то



#СОЦИАЛЬНАЯ СЕТЬ
def save_name(message):#функция с записью имени
    global name
    name = message.text
    if name.isalpha():#проверка на то, что слово состоит только из букв
        if len(name)>2:#проверка, чтобы имя было длиннее 2 букв
            bot.send_message(message.chat.id, 'Введите вашу фамилию:')
            bot.register_next_step_handler(message, save_surname)#переход к фамилии
        else:
            bot.reply_to(message, '<b>Пожалуйста, введите имя, в котором больше 2 букв!</b>\n'
                                    'Попробуйте ввести имя еще раз:', parse_mode='html')
            bot.register_next_step_handler(message, save_name)
    else:
        bot.reply_to(message, '<b>Пожалуйста, вводите данные правильно!</b>\n'
                              '<b>Вводите имя только строчными латинскими буквами\n'
                              '(<ins>Пример: egor</ins>)</b>\n'
                              'Попробуйте ввести имя еще раз:', parse_mode='html')
        bot.register_next_step_handler(message, save_name)

def save_surname(message):#функция с записью фамилии
    global surname
    surname = message.text
    if surname.isalpha():#проверка на то, что слово состоит только из букв
        if len(surname)>2:#проверка, чтобы фамилия было длиннее 2 букв
            bot.send_message(message.chat.id, 'Введите ваш любимый цвет:')
            bot.register_next_step_handler(message, save_colour)#переход к цвету
        else:
            bot.reply_to(message, '<b>Пожалуйста, введите фамилию, в которой больше 2 букв!</b>\n'
                                    'Попробуйте ввести фамилию еще раз:', parse_mode='html')
            bot.register_next_step_handler(message, save_surname)
    else:
        bot.reply_to(message, '<b>Пожалуйста, вводите данные правильно!</b>\n'
                              '<b>Вводите фамилию только строчными латинскими буквами\n'
                              '(<ins>Пример: novikov</ins>)</b>\n'
                              'Попробуйте ввести имя еще раз:', parse_mode='html')
        bot.register_next_step_handler(message, save_surname)

def save_colour(message):#функция с записью цвета и вывода никнеймов
    global colour
    colour = message.text
    if colour.isalpha():#проверка на то, что слово состоит только из букв
        bot.send_message(message.chat.id, '<b>Список никнеймов:</b>\n\n'
                                          f'✔<i>{name.title()}_{surname.title()}</i>✔\n'
                                          f'<b>↻{surname[0:3].upper()}{name[0:3].upper()}↺</b>\n'
                                          f'👉{colour.title()}_{name.title()}👈\n'
                                          f'➳Mr.{surname.title()}_{name[0].title()}➳\n'
                                          f'<del>Sigma{name.title()}</del>😯😏\n'
                                          f'{save_nameup()}\n'
                                          f'<b>☠{colour}_chushpan☠</b>\n'
                                          f'<ins>[{name.title()}-Chinazes-{surname.title()}]</ins>\n'
                                          f'<del>「SUPERULTRAPUPERMEGA{colour.upper()}」</del>\n'
                                          f'・{name[0].title()}(°ʖ°){surname[0].title()}・\n'
                                          f'<b>{roflfont(name,surname)}</b>\n'
                                          f'⚔{roflfont2(colour,name)}⚔\n\n'
                                          '<b>Чтобы начать заново нажми ⇨︎ /start</b>', parse_mode='html')
    else:
        bot.reply_to(message, '<b>Пожалуйста, вводите данные правильно!</b>\n'
                              '<b>Вводите цвет только строчными латинскими буквами (<ins>Пример: black</ins>)</b>\n'
                              'Попробуйте ввести цвет ещё раз:', parse_mode='html')
        bot.register_next_step_handler(message, save_colour)

    if name=="nikola" and surname=="tesla" and colour=="blue":#небольшой прикол с теслой
        photo = open('tesla.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)




#ОНЛАЙН ИГРА
def save_name2(message):#функция с записью имени
    global name2
    name2 = message.text
    if name2.isalpha():#проверка на то, что слово состоит только из букв
        if len(name2)>2:#проверка, чтобы имя было длиннее 2 букв
            bot.send_message(message.chat.id, 'Введите ваш возраст:')
            bot.register_next_step_handler(message, save_age2)#переход к возрасту
        else:
            bot.reply_to(message, '<b>Пожалуйста, введите имя, в котором больше 2 букв!</b>\n'
                                    'Попробуйте ввести имя еще раз:', parse_mode='html')
            bot.register_next_step_handler(message, save_name2)
    else:
        bot.reply_to(message, '<b>Пожалуйста, вводите данные правильно!</b>\n'
                              '<b>Вводите имя только строчными латинскими буквами (<ins>Пример: vasya</ins>)</b>\n'
                              'Попробуйте ввести имя еще раз:', parse_mode='html')
        bot.register_next_step_handler(message, save_name2)


def save_age2(message):#функция с записью возраста
    global age2
    age2 = message.text
    if age2.isdigit():#проверка на то, что слово состоит только из цифр
        if int(age2)>0 and int(age2)<123:#проверка, чтобы возраст был реальным
            bot.send_message(message.chat.id, 'Введите ваше любимое животное:')
            bot.register_next_step_handler(message, save_animal2)#переход к животному
        else:
            bot.reply_to(message, '<b>Я вам не верю!</b>\n'
                                  'Попробуйте ввести возраст еще раз:', parse_mode='html')
            bot.register_next_step_handler(message, save_age2)
    else:
        bot.reply_to(message, '<b>Пожалуйста, вводите данные правильно!</b>\n'
                      '<b>Вводите возраст целым числом (<ins>Пример: 18</ins>)</b>\n'
                      'Попробуйте ввести возраст еще раз:', parse_mode='html')
        bot.register_next_step_handler(message,save_age2)

def save_animal2(message):#функция с записью животного и вывода никнеймов
    global animal2
    animal2 = message.text
    if animal2.isalpha():#проверка на то, что слово состоит только из букв
        if len(animal2)>2:#проверка, чтобы животное было длиннее 2 букв
            bot.send_message(message.chat.id,f'<b>Список никнеймов:</b>\n\n'
                                            f'{age2}_{name2[0].upper()}{name2[1]}{name2[2].upper()}{name2[0]}{name2[1].upper()}{name2[2]}_{age2}\n'
                                            f'️☠️<ins>{name2.upper()}_KILLER</ins>☠️\n'
                                            f'<b>SUPER{animal2.upper()}{age2}</b>\n'
                                            f'️☢️ToXiC_{animal2}{2023-int(age2)}☢️\n'
                                            f'ⓂⓇ{animal2}chikツ\n'
                                            f'☞{name2[0:3]}{animal2[0:3]}☜\n'
                                            f'♛︎qwerty{age2}♛︎\n️'
                                            f'<b>{save_nameup2()}</b>\n'
                                            f'✠<b>{roflfont2(animal2,name2)}</b>✠\n'
                                            f'{animal2.upper()}(╯°□°)--︻╦╤─YOU\n'
                                            f'I ℓﻉ√٥ {name2} ♥\n'
                                            f'{name2.title()}, {age2} лет, прикалывает {animal2} \n\n'
                                            f'<b>Чтобы начать заново нажми ⇨ /start</b>', parse_mode='html')
        else:
            bot.reply_to(message, '<b>Пожалуйста, введите животное, в котором больше 2 букв!</b>\n'
                                  'Попробуйте ввести животное ещё раз:', parse_mode='html')
            bot.register_next_step_handler(message, save_animal2)
    else:
        bot.reply_to(message, '<b>Пожалуйста, вводите данные правильно!</b>\n'
                              '<b>Если требуется ввести животное, то вводите его буквами\n'
                              '(<ins>Пример: bear</ins>)</b>\n'
                              'Попробуйте ввести животное ещё раз:', parse_mode='html')
        bot.register_next_step_handler(message, save_animal2)

    if name2=="steve" and animal2=="dog" and age2=="56":#небольшой прикол со Стивом Джобсом
        photo = open('jobsrofl.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)


#ФОРУМ
def save_name3(message):#функция с записью именем
    global name3
    name3 = message.text
    if name3.isalpha():#проверка на то, что слово состоит только из букв
        if len(name3)>2:#проверка, чтобы имя было длиннее 2 букв
            bot.send_message(message.chat.id, 'Введите ваше увлечение:')
            bot.register_next_step_handler(message, save_hobby3)
        else:
            bot.reply_to(message, '<b>Пожалуйста, введите имя, в котором больше 2 букв!</b>\n'
                                  'Попробуйте ввести имя еще раз:', parse_mode='html')
            bot.register_next_step_handler(message, save_name3)
    else:
        bot.reply_to(message, '<b>Пожалуйста, вводите данные правильно!</b>\n'
                              '<b>Вводите свое имя только строчными латинскими буквами (<ins>Пример: grisha</ins>)</b>\n'
                              'Попробуйте ввести имя еще раз:', parse_mode='html')
        bot.register_next_step_handler(message, save_name3)

def save_hobby3(message):#функция с записью хобби
    global hobby3
    hobby3 = message.text
    if hobby3.isalpha():#проверка на то, что слово состоит только из букв
        if len(hobby3)>2:#проверка, чтобы имя было длиннее 2 букв
            bot.send_message(message.chat.id, 'Введите ваше любимое число:')
            bot.register_next_step_handler(message, save_number3)
        else:
            bot.reply_to(message, '<b>Пожалуйста, введите увлечение, в котором больше 2 букв!</b>\n'
                                  'Попробуйте ввести увлечение еще раз:', parse_mode='html')
            bot.register_next_step_handler(message, save_hobby3)
    else:
        bot.reply_to(message, '<b>Пожалуйста, вводите данные правильно!</b>\n'
                              '<b>Вводите увлечение только строчными латинскими буквами (<ins>Пример: music</ins>)</b>\n'
                              'Попробуйте ввести увлечение еще раз:', parse_mode='html')
        bot.register_next_step_handler(message, save_hobby3)

def save_number3(message):#функция с записью числа и выводом никнеймов
    global number3
    number3 = message.text
    if number3.isdigit():#проверка на то, что число состояло только из цифр
        bot.send_message(message.chat.id, f'<b>Список никнеймов:</b>\n\n'
                                        f'🫸🏿{name3}-{hobby3}🫷🏿\n'
                                        f'{number3}_{hobby3}_{number3}\n'
                                        f'✔PRO_{hobby3.upper()}✔\n'
                                        f'{name3[0:3]}{number3}๏̯͡๏\n'
                                        f'I♥{hobby3}\n'
                                        f'{roflnumber(number3)}{roflfont2(name3,"")}{roflnumber(number3)}\n'
                                        f'◈{name3[0:3]}{hobby3[0:3]}◈\n'
                                        f'user{number3}☑\n'
                                        f'♦$♫☛<b>{name3.upper()}</b>☚♫$♦\n'
                                        f'ϟ{name3[0].upper()}{hobby3[0].upper()}{number3}ϟ\n'
                                        f'<del>{name3.title()}{hobby3.title()}{number3}</del>\n'
                                        f'<b>🔘{roflfont(name3,hobby3)}🔘</b>\n\n'
                                        f'<b>Чтобы начать заново нажми ⇨︎ /start</b>', parse_mode='html')
    else:
        bot.reply_to(message, '<b>Пожалуйста, вводите данные правильно!</b>\n'
                      '<b>Вводите число цифрами (<ins>Пример: 52</ins>)</b>\n'
                      'Попробуйте ввести любимое число еще раз:', parse_mode='html')
        bot.register_next_step_handler(message, save_number3)

    if name3=="alblak" and hobby3=="music" and number3=="52":#небольшой прикол с алблаком
        photo = open('alblak.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)

def save_nameup():#функция для вставки ✦︎︎︎ после каждой буквы в имени
    nameup = "✦︎︎︎"
    for letter in (name.upper()+surname.upper()):
        nameup += letter + "✦︎"
    return nameup

def save_nameup2():#функция для вставки ✯︎ после каждой буквы в имени
    nameup2 = "✯︎"
    for letter in name2.upper():
        nameup2 += letter + "✯︎"
    return nameup2

def roflfont(a,b):#функция для изменения шрифта всех букв
    namerofl=""
    for letter in (a+b):
        switch_case = {
            'a':'Ⓐ',
            'b':'Ⓑ',
            'c':'Ⓒ',
            'd':'Ⓓ',
            'e':'Ⓔ',
            'f':'Ⓕ',
            'g':'Ⓖ',
            'h':'Ⓗ',
            'i':'Ⓘ',
            'j':'Ⓙ',
            'k':'Ⓚ',
            'l':'Ⓛ',
            'm':'Ⓜ',
            'n':'Ⓝ',
            'o':'Ⓞ',
            'p':'Ⓟ',
            'q':'Ⓠ',
            'r':'Ⓡ',
            's':'Ⓢ',
            't':'Ⓣ',
            'u':'Ⓤ',
            'v':'Ⓥ',
            'w':'Ⓦ',
            'x':'Ⓧ',
            'y':'Ⓨ',
            'z':'Ⓩ',

        }
        namerofl += switch_case.get(letter.lower(), letter)
    return namerofl

def roflfont2(a,b):#вторая функция для изменения шрифта всех букв
    namerofl=""
    for letter in (a+b):
        switch_case = {
            'a':'𝔄',
            'b':'𝔅',
            'c':'ℭ',
            'd':'𝔇',
            'e':'𝔈',
            'f':'𝔉',
            'g':'𝔊',
            'h':'ℌ',
            'i':'ℑ',
            'j':'𝔍',
            'k':'𝔎',
            'l':'𝔏',
            'm':'𝔐',
            'n':'𝔑',
            'o':'𝔒',
            'p':'𝔓',
            'q':'𝔔',
            'r':'ℜ',
            's':'𝔖',
            't':'𝔗',
            'u':'𝔘',
            'v':'𝔙',
            'w':'𝔚',
            'x':'𝔛',
            'y':'𝔜',
            'z':'ℨ',

        }
        namerofl += switch_case.get(letter.lower(), letter)
    return namerofl

def roflnumber(a):#функция для изменения шрифта всех цифр
    namerofl=""
    for letter in (a):
        switch_case = {
            '1': '𝟙',
            '2': '𝟚',
            '3': '𝟛',
            '4': '𝟜',
            '5': '𝟝',
            '6': '𝟞',
            '7': '𝟟',
            '8': '𝟠',
            '9': '𝟡',
            '0': '𝟘',

        }
        namerofl += switch_case.get(letter.lower(), letter)
    return namerofl

bot.polling(none_stop=True)
