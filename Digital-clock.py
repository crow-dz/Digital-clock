from tkinter import *
import time

window = Tk()
window.title('Digital Clock')
window.geometry('400x200')
window.resizable(width=False,height=False)
window.iconbitmap('digital_clock.ico')
background_img=PhotoImage(file='new-background.png')
img_label=Label(window,image=background_img).place(relwidth=1,relheight=1)


def Time():
    time_string=time.strftime('%H:%M:%S')
    label.config(text=time_string)
    label.after(100,Time)

label=Label(window,font=('digital-7',50,'bold'),bg="#0d0604",fg='red')
label.pack(pady=60)
Time()


window.mainloop()
# Done here !
