import tkinter
import tkinter.messagebox

window = tkinter.Tk()

str_var = tkinter.StringVar()


def butoon_click():
    s = str_var.get()
    if ' ' in s:
        tkinter.messagebox.showinfo("Результат", "Введено декілька слів")
    else:
        tkinter.messagebox.showinfo("Результат", "Введено одне слово")


label = tkinter.Label(window, text="Введiть текст")
label.pack()

edit = tkinter.Entry(window, textvariable=str_var)
edit.pack()

button = tkinter.Button(window, text="Пepeвiрити", command=butoon_click)
button.pack()

window.mainloop()
