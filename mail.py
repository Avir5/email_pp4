import smtplib
from copyreg import pickle
from  email.message import EmailMessage
from tkinter import *

def send_message():
    save()
    sender = sender_entry.get()
    recepient = rec_entry.get()
    password = pas_entry.get()
    subject = subj_entry.get()
    body = message_entry.get(1.0,END)

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recepient

    server=None

    try:
        server = smtplib.SMTP('smtp.mail.ru', 465)
        print(server)
        server.login(sender, password)
        server.send_message(msg)
        print('Письмо успешно отправлено!')
    except Exception as e:
        print(e)
    finally:
        if server:
            server.quit()


def save():
    with open('save.txt', 'w') as file:
        file.write(sender_entry.get()+'\n')
        file.write(rec_entry.get() + '\n')
        file.write(pas_entry.get() + '\n')


def load():
    try:
        with open('save.txt', 'r') as file:
            text=file.readlines()
            print(text)
    except FileNotFoundError:
        pass


window=Tk()
window.title('Отправка письма')

Label(text='Отправитель(email)').grid(row=0,column=0)
sender_entry=Entry()
sender_entry.grid(row=0,column=1)

Label(text='Получатель(email)').grid(row=1,column=0)
rec_entry=Entry()
rec_entry.grid(row=1,column=1)

Label(text='Пароль приложения)').grid(row=2,column=0)
pas_entry=Entry()
pas_entry.grid(row=2,column=1)

Label(text='Тема)').grid(row=3,column=0)
subj_entry=Entry()
subj_entry.grid(row=3,column=1)

Label(text='Сообщение').grid(row=4,column=0)
message_entry=Entry(width=15, hiegth=10)
message_entry.grid(row=4,column=1)

Button(text='Отправить', command=send_message).grid(row=5,column=0,columnspan=2)

load()

window.mainloop()

'''
import smtplib
from email.message import EmailMessage

sender="kenia2k3@yandex.ru"
recepient="kalachickova.e@yandex.ru"
password="bikotpulhykdbcng"
subject="Проверка связи 2"
body="Какой-то текст письма"

msg=EmailMessage()
msg.set_content(body)
msg["Subject"]=subject
msg["From"]=sender
msg["To"]=recepient

server=smtplib.SMTP("smtp.yandex.ru", 465)
server.login(sender,password)
server.send_message(msg)
print("Письмо успешно отправлено")
'''

'''

try:
    server=smtplib.SMTP_SSL("smtp.yandex.ru", 465)
    server.login(sender,password)
    server.send_message(msg)
    print("Письмо успешно отправлено")
except Exception as e:
    print(e)
finally:
    if server:
        server.quit()'''