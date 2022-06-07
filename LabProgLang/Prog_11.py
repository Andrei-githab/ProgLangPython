"""
Лабораторная работа 11
Написать программу, окно логин, пароль, регистрация,
соответственно можно зарегистрироваться, можно войти.
Данные зарегистрированных хранится в БД пароль не
храним в открытом виде, а храним его хэш.
"""
import sqlite3
import uuid
import hashlib
from tkinter import *
from tkinter import messagebox


def clearok():
    login_entry.delete(0, END)
    password_entry.delete(0, END)


def clearwarning():
    password_entry.delete(0, END)


def getRegistration():
    rlogin = login.get()
    rpassword = password.get()
    try:
        rconnection = sqlite3.connect('bdusers.db')
        rcursor = rconnection.cursor()
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha256(salt.encode() + rpassword.encode()).hexdigest()
        sqlite_registration_query = """INSERT INTO GEEK (Login, Password, Salt) VALUES (?, ?, ?);"""
        data_registration = (rlogin, hashed_password, salt)
        rcursor.execute(sqlite_registration_query, data_registration)
        rconnection.commit()
        rconnection.close()
        messagebox.showinfo("INFO", "Вы зарегистрированы")
        clearok()

    except BaseException:
        messagebox.showerror("ERROR", "Что то пошло не так :(")


def getAuthorization():
    alogin = login.get()
    apassword = password.get()
    try:
        aconnection = sqlite3.connect('bdusers.db')
        acursor = aconnection.cursor()
        sqlite_authorization_query = """SELECT * FROM GEEK WHERE Login=?;"""
        acursor.execute(sqlite_authorization_query, (alogin,))
        output = acursor.fetchone()
        if output[1] == hashlib.sha256(output[2].encode() + apassword.encode()).hexdigest():
            messagebox.showinfo("INFO", "Вы ввели правильный пароль")
            clearok()
        else:
            messagebox.showwarning("WARNING", "Извините, вы ввели не правильный пароль")
            clearwarning()

    except BaseException:
        messagebox.showerror("ERROR", "Что то пошло не так :(")


root_window = Tk()
root_window.title("")
window_w = root_window.winfo_screenwidth()
window_h = root_window.winfo_screenheight()
w = window_w//2
h = window_h//2
w = w - 200
h = h - 200
root_window.geometry('450x300+{}+{}'.format(w, h))

login = StringVar()
password = StringVar()

title_label = Label(text="Лабораторная работа 11", font="16")
title_label.place(x=110, y=20)
login_label = Label(text="Введите логин:  ", font="16")
login_label.place(x=20, y=80)
password_label = Label(text="Введите пароль: ", font="16")
password_label.place(x=20, y=120)

login_entry = Entry(textvariable=login, font="16")
login_entry.place(x=190, y=80)
password_entry = Entry(textvariable=password, font="16", show='*')
password_entry.place(x=190, y=120)

btn_registration = Button(text="Регистрация", background="dark slate gray", foreground="ghost white", padx="20",
                          pady="8", font="16", command=getRegistration)
btn_registration.place(x=40, y=200)
btn_authorization = Button(text="Авторизация", background="dark slate gray",  foreground="ghost white", padx="20",
                           pady="8", font="16", command=getAuthorization)
btn_authorization.place(x=230, y=200)

root_window.mainloop()
