from tkinter import *
import time

pencere = Tk()
pencere.title("Dijital Saatim")

zaman = ''
tiktak = Label(pencere, font=('times',100,'bold'),bg='white')

tiktak.grid()

def saat():
    global zaman
    zaman1 = time.strftime("%H:%M:%S")

    if zaman != zaman1:
        zaman = zaman1
        tiktak.config(text=(zaman1))

    tiktak.after(50,saat)
saat()
pencere.mainloop()