import telebot
import random

bot = telebot.TeleBot('1322664004:AAFQT7ABylJKLYJH_NL5JE3Rmz-C8-j0zbE')

name = ''
surname = ''
p = []

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.from_user.id, 'I can generate password for you. Send me /gen command to get it')

@bot.message_handler(commands=['gen'])
def handle_start(message):
    bot.send_message(message.from_user.id, 'Send me your name')
    bot.register_next_step_handler(message, get_name)

def get_name(message): #получаем фамилию
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Send me your surname')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global name
    global sur
    sur = message.text
    bot.send_message(message.from_user.id, 'Your password:')
    n = len(name)
    s = len(sur)
    g = 1

    if n >= s:
        while g <= s:
            p.append(name[g - 1])
            p.append(sur[g - 1])
            g += 1

        else:
            while g<=n:
                p.append(name[g-1])
                g += 1
    else:
        while g<= n:
            p.append(name[g-1])
            p.append(sur[g-1])
            g += 1

        else:
            while g<= s:
                p.append(sur[g-1])
                g += 1
    pp = ''.join(p)
    a = random.randint(0, 10)
    ind = random.randint(0, 10)
    z = ['!', '@', '#', '%', '&', '?', '*', '/', '\\', '$', '+']
    i = z[ind]
    elements = []
    elements.append(pp)
    elements.append(str(a))
    elements.append(i)
    a = random.randint(0, 10)
    ind = random.randint(0, 10)
    z = ['!', '@', '#', '%', '&', '?', '*', '/', '\\', '$', '+']
    i = z[ind]
    elements.append(str(a))
    elements.append(i)

    pas = ''.join(elements)

    bot.send_message(message.from_user.id, pas)

bot.polling(none_stop=True)
