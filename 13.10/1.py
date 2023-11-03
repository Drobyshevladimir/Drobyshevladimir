import tkinter as Tkinter
from datetime import datetime

counter = 0
running = False


def counter_label(label):
    def count():
        if running:
            global counter
            # To manage the intial delay. 
            if counter == 0:
                display = 'Ready!'
            else:
                tt = datetime.utcfromtimestamp(counter)
                string = tt.strftime('%H:%M:%S')
                display = string

            label['text'] = display

            label.after(1000, count) # каждые 1000мс = 1с увеличиваем счетчик на 1
            counter += 1

    #включаем count
    count()


# стартуем
def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'


# тормозим
def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False


# перезагружаемся
def Reset(label):
    global counter
    counter = 0
    # Если reset нажат после stop. 
    if not running:
        reset['state'] = 'disabled'
        label['text'] = '00:00:00'
    # Если reset нажат во время работы таймера. 
    else:
        label['text'] = '00:00:00'


root = Tkinter.Tk()
root.title("Stopwatch")

# Если окно будет слишком маленьким, будет сложно нажимать на кнопки, так что зададим minsize.
root.minsize(width=250, height=70)

label = Tkinter.Label(root, text='Ready!', fg='black', font='Montserrat 30 bold')
label.pack()
#создадим Frame, на который поместим кнопки
f = Tkinter.Frame(root)

'''
Помните в предыдущем примере мы говорили, что не получится передать в command функцию с круглыми скобками?
Но как быть, если мы хотим передать функцию, которая принимает какой-то аргумент? В нашем примере это Start и Reset
В данном случае мы можем сохранить **вызов** функции с каким-либо аргументом как отдельную функцию, используя ключевое слово lambda
Таким образом, вызова функции не происходит, а saved_start и saved_reset теперь -- объекты-функции, с фиксированным принимаемым аргументом.

В общем случае лямбда-функции это более мощный инструмент, однако пока мы не будем на этом останавливаться.
'''
saved_start = lambda: Start(label)
saved_reset = lambda: Reset(label)

start = Tkinter.Button(f, text='Start', width=6, command = saved_start)
stop = Tkinter.Button(f, text='Stop', width=6, state='disabled', command = Stop)
reset = Tkinter.Button(f, text='Reset', width=6, state='disabled', command = saved_reset)

# не забываем разместить Frame и кнопки
f.pack(anchor='center', pady=5)
start.pack(side='left')
stop.pack(side='left')
reset.pack(side='left')

root.mainloop()
