import tkinter
import tkinter.messagebox


def button1_click():
    tkinter.messagebox.showinfo("Biдповiдь", "Cупep")


def button2_click():
    tkinter.messagebox.showerror("Bigповiдь", "шкода")


window = tkinter.Tk()
window.title('Bпpaва 3')
window.geometry('400x300')
label1 = tkinter.Label(text="чи подобаеться Вам вивчати Python?")
label1.pack()
button1 = tkinter.Button(window, text="Tak", command=button1_click)
button1.pack()
button2 = tkinter.Button(window, text="Hi", command=button2_click)
button2.pack()
window.mainloop()
