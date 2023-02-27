import tkinter
import tkinter.messagebox

window = tkinter.Tk()
str_var1 = tkinter.StringVar()
str_var2 = tkinter.StringVar()


def button1_click():
    tkinter.messagebox.showinfo("Результат додавання", int(str_var1.get()) + int(str_var2.get()))


def button2_click():
    tkinter.messagebox.showinfo("Результат вiднiмання", int(str_var1.get()) - int(str_var2.get()))


label = tkinter.Label(window, text="Введiть числа")
label.pack()
edit1 = tkinter.Entry(window, textvariable=str_var1)
edit1.pack()
edit2 = tkinter.Entry(window, textvariable=str_var2)
edit2.pack()
button1 = tkinter.Button(window, text="+", command=button1_click)
button1.pack()
button2 = tkinter.Button(window, text="-", command=button2_click)
button2.pack()
window.mainloop()
