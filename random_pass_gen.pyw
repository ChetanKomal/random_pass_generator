from tkinter import *
import random
import string
import pyperclip

root = Tk()
root.title("Random Password Generator")
root.maxsize(700,400)
root.minsize(700,400)

def gen_pass():#max pass length 86 charaters
   entry_2.delete(0,END)
   leng = int(entry_1.get())
   low = string.ascii_lowercase
   upp = string.ascii_uppercase
   n = string.digits
   symb = "!@#$%^&*()_+<>?:][}{/*-+"
   all =low+upp+n+symb
   temp = random.sample(all,leng)
   password = "".join(temp)
   entry_2.insert(0,password)
   
def cpy_pass():
    pyperclip.copy(entry_2.get())

label_1= Label(text="Random Password Generator",font=(20),justify=CENTER)
label_1.place(x=208,y=0)

label_2=Label(text="Enter length:",font=(20))
label_2.place(x=180,y=100)

entry_1= Entry(width=20,font=(20))
entry_1.place(x=310,y=100)

button_1 =Button(text="Generate Password",command=gen_pass)
button_1.place(x=240,y=200)

button_2=Button(text="Copy Password",command=cpy_pass)
button_2.place(x=380,y=200)

entry_2=Entry(width=70,font=(20),bd=0,bg="#f0f0ed",justify=CENTER)
entry_2.place(x=0,y=300)


root.mainloop()