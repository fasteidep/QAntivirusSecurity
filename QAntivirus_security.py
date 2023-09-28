import tkinter as tk
from tkinter import Tk
from tkinter import *
import webbrowser
from tkinter import messagebox
from PIL import ImageTk
from tkinter import ttk
from tkinter.ttk import Progressbar
from time import sleep
import os

#Функции


def zvonok_v_podderjku():
    webbrowser.open('https://www.youtube.com/shorts/WNsWjc7-lwE', new=2)

def save_settings():
    messagebox.showinfo("Настройки", "Обойдёшься")
def podderjka():
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', new=2)

def dop():
    webbrowser.open("https://www.youtube.com/@nedohackerslite?sub_confirmation=1", new=2)

def o_programme():
    messagebox.showinfo("О программе", "Это моя первая программа. Я её создал полностью на языке python за 5 дней")
def avtor():
    webbrowser.open("https://www.youtube.com/channel/UCxbGYXWuowtcM1_jbTOaEJg", new=2)

def donat():
    webbrowser.open("qiwi.com/p/79642733974", new=2)

def exit():
    messagebox.showinfo("Error", 'Отказано в доступе')

def language():
    messagebox.showinfo("Язык", "Ты больше не армянин")

def Podderjka_2():
    messagebox.showinfo("Поддержка", "Вам никто не поможет, смиритесь")







def settings():
    settings_window = tk.Toplevel(root)
    settings_window.title('Настройки программы')
    settings_window.geometry('600x450')
    settings_window.attributes('-alpha', 0.954)
    settings_window['bg'] = '#6c4ced'
    settings_window.iconphoto(False, icon_main)
    settings_window.resizable(False, False)

    Label_settings = Label(settings_window, text='Настройки', bg='#6c4ced', font=('Arial', 15), fg='white')
    Label_settings.place(x=230, y=3)

    Label_soed = Label(settings_window, text='Скорость проверки', bg='#6c4ced', font=('Arial', 10), fg='white')
    Label_soed.place(x=5, y=47)



    chois_soed_cort = ("Ах*енная", 'Высокая', "Выше среднего","Средняя", "Низкая")

    choise_soed = ttk.Combobox(settings_window, values=chois_soed_cort)
    choise_soed.current(1)
    choise_soed.place(x=5, y=70)

    Button_language = Button(settings_window, text='Сменить язык', bd=0, bg='white', font=('Arial', 10), command=language)
    Button_language.place(x=5, y=100)

    mnog_yad_obr = tk.Checkbutton(settings_window, text='Многоядерная обработка (Может плохо сказаться на производительности компьютера)', bg='#6c4ced', activebackground='#6c4ced', fg='red', font=('Arial', 10))
    mnog_yad_obr.place(x=5, y=130)

    neh_files = tk.Radiobutton(settings_window, text='Докачать дополнительные нехорошие файлы', bg='#6c4ced', font=('Arial', 10), fg='red', activebackground='#6c4ced')
    neh_files.place(x=5, y=160)


    Button_Save = Button(settings_window, text='Сохранить', bd=0, bg='white', font=('Arial', 12), command=save_settings, activebackground='#00ffea')
    Button_Save.place(x=505, y=420)

    Button_podderjka_2 = Button(settings_window, text='Что-то непонятно? Пиши поддержке!', bd=0, bg='white', font=('Arial', 12), command=Podderjka_2, activebackground='#00ffea')
    Button_podderjka_2.place(x=5, y=420)

    Label_proverka_2 = Label(settings_window, text='Проверка', bg='#6c4ced', font=('Arial', 10), fg='white')
    Label_proverka_2.place(x=5, y=190)

    Proverka_cort_2 = ("Полная", "Быстрая")
    choise_proverka = ttk.Combobox(settings_window, values=Proverka_cort_2)
    choise_proverka.current(0)
    choise_proverka.place(x=5, y=220)

    Button_podderjka_2 = Button(settings_window, text='Звонок в поддержку', bd=0, bg='white',
                                font=('Arial', 12), command=zvonok_v_podderjku, activebackground='#00ffea')
    Button_podderjka_2.place(x=300, y=420)

    Label_s_vir = Label(settings_window, text='Вирусы:', bg='#6c4ced', font=('Arial', 10), fg='white')
    Label_s_vir.place(x=5, y=250)

    s_virusami = ("Удалять", "Докачивать к ним друзей", "Игнорировать", "Поддерживать ")
    choise_s_virusami = ttk.Combobox(settings_window, values=s_virusami)
    choise_s_virusami.current(0)
    choise_s_virusami.place(x=5, y=280)

def Proverka_progressbar():
    Label_provereno_files = Label(text=f'Проверено файлов:', bg='#6c4ced', font=('Arial', 15), fg='white', bd=0)
    Label_provereno_files.place(x=410, y=136)

    progressbar_scan = Progressbar(root, orient=HORIZONTAL, mode='determinate', length=200)
    progressbar_scan.configure(value=0)
    progressbar_scan.place(x=400, y=170)
    for i in range(101):
        progressbar_scan.configure(value=i)
        progressbar_scan.update()
        sleep(0.05)
    update_scan()

        
def script():
    os.system('"C:/Program Files (x86)/QAntivirus_security/Files/Scripts/Mat.bat"')


def update_scan():
    global Label_obnarejeno
    Label_obnarejeno = Label(text=('            Обнаружено 2 вируса'), bg='#6c4ced', font=('Arial', 15), fg='red', bd=0)
    Label_obnarejeno.place(x=325, y=239)
    Label_obnarejeno.update()

    Button_delete = Button(root, text='Удалить', width=26, height=2, bd=0, activebackground='#0af28d', command=script)
    Button_delete.place(x=405, y=330)

def Proverka_start():
    global proverka
    proverka += 1
    if proverka == 1:
        Proverka_progressbar()
    else:
        messagebox.showinfo("Проверка", "Куда ещё раз?")


#Главное окно
root = Tk()
root.attributes('-alpha', 0.9515)
root.geometry('850x600')
root['bg'] = '#6c4ced'
icon_main = tk.PhotoImage(file="Files/Images/antivirus_icon.png")
root.iconphoto(False, icon_main)
root.resizable(False, False)
root.title("QAntivirus Security")




#Canvas
canvas = Canvas(root, height=600, width=850, highlightthickness=0)
canvas['bg'] = '#6c4ced'
canvas.pack()

#Фигуры
canvas.create_line(200, 0, 200, 600, width=3, fill='#5832f0')
canvas.create_rectangle(200, 0, 850, 125, fill='#5832f0', outline='#5832f0')

antivirus_icon = PhotoImage(file='Files/Images/Antivirus_icon_2.png')
antivirus_icon = antivirus_icon.subsample(4)
antivirus_icon_output = canvas.create_image(100, 73, image=antivirus_icon)

canvas.create_line(200, 450, 850, 450, width=3, fill='#5832f0')



#Переменные
proverka = 0
files = 0



# Виджеты
button_settings = Button(root, text='Настройки', width=26, height=2, bd=0, activebackground='#0af28d', command=settings)
button_settings.place(x=7, y=150)

button_Podderjka = Button(root, text='Поддержка', width=26, height=2, bd=0, command=podderjka, activebackground='#0aacf2')
button_Podderjka.place(x=7, y=190)

button_dop = Button(root, text='Дополнительно', width=26, height=2, bd=0, command=dop, activebackground='#0aacf2')
button_dop.place(x=7, y=230)

button_o_prog = Button(root, text='О программе', width=26, height=2, bd=0, command=o_programme, activebackground='#0aacf2')
button_o_prog.place(x=7, y=270)

button_dop = Button(root, text='Автор', width=26, height=2, bd=0, command=avtor, activebackground='#00ffea')
button_dop.place(x=7, y=310)

button_donate = Button(root, text='Поддержать автора', width=26, height=2, bd=0, command=donat, activebackground='#00ffea')
button_donate.place(x=7, y=350)

button_exit = Button(root, text='Выход', width=26, height=2, bd=0, command=exit, activebackground='red')
button_exit.place(x=7, y=390)

scan_image = ImageTk.PhotoImage(file='Files/Images/Проверка.png')
button_scan = Button(root, image=scan_image, bd=0, bg='#5832f0', activebackground='#5832f0', command=Proverka_start)
button_scan.place(x=745, y=4)

Label_1 = Label(text='Регулярное проверяйте вашу систему на вирусы', bg='#5832f0', font=('Arial', 15), fg='white')
Label_1.place(x=250, y=10)

Label_2 = Label(text='Ваш компьютер ещё не проверялся', bg='#5832f0', font=('Arial', 13), fg='white')
Label_2.place(x=250, y=40)




system_icon = PhotoImage(file='Files/Images/system.png')
system_icon_output = canvas.create_image(270, 232, image=system_icon)

Label_system = Label(text='Система', bg='#6c4ced', font=('Arial', 12), fg='white', bd=0)
Label_system.place(x=222, y=299)

Label_obnarejeno = Label(text=('Обнаружено 0 вирусов'), bg='#6c4ced', font=('Arial', 15), fg='white', bd=0)
Label_obnarejeno.place(x=325, y=239)

Label_QAntivirus = Label(text=f'Почему именно QAntivirus Security? На вооружении программы стоит сканер, от ',
                          bg='#6c4ced', font=('Arial', 12), fg='white', bd=0
                         )
Label_QAntivirus.place(x=205, y=459)

Label_QAntivirus_2 = Label(text='которого не может спрятаться ни одна угроза. Быстро и слаженно работает, чтобы', bg='#6c4ced', font=('Arial', 12), fg='white', bd=0)
Label_QAntivirus_2.place(x=205, y=482)

Label_QAntivirus_3 = Label(text='обеспечить вас лучшей защитой.', bg='#6c4ced', font=('Arial', 12), fg='white', bd=0)
Label_QAntivirus_3.place(x=205, y=504)

root.mainloop()