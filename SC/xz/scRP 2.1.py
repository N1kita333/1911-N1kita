import tkinter
window = tkinter.Tk()
window.title('Планування')
label1 = tkinter. Label (window, text="1. Нагадування про день народження", height=1, bg='Light gray', fg='black', font="windows")
label1.pack()
label2 = tkinter. Label (window, text="2. Важлива подiя", height=1, fg='black', font='windows 24')
label2.pack()
label3 = tkinter. Label (window, text="3. завдання (виконати домашне завдання)", height=1, fg='black', font='windows 24')
label3.pack()
label4 = tkinter. Label (text='Планування дiяльностi родини', height=1, font='windows 16')
label4.pack()
window.mainloop()