import Tkinter
import Tkinter as tk
from PIL import Image, ImageTk



#image = tk.PhotoImage(file = 'ic_7.png')
window = tk.Tk()
window.title("Calculator")






#image = Image.open("ic_"+str(i)+".png")
#photoimg[i] = ImageTk.PhotoImage(image)

ims = dict()

for x in range(0, 10):
    image = Image.open("ic_"+str(x)+".png")
    ims[x] = ImageTk.PhotoImage(image)

#can = Image.open(".png")
#ims[x] = ImageTk.PhotoImage(image)




root = window



button_frame = tk.Frame(root,width=700, height=700, background="bisque")
button_frame.pack(fill='both', side=tk.BOTTOM)


exp=""
label=""


#callback : function for changing labe;
def setexp(expn):
    global exp
    global label
    exp=exp+expn
    label.configure(text=exp)


#create label 
label=Tkinter.Label(window, text="0",font = "Arya 17 bold")
label.pack()

#Final result callback: =
def results():
    global label
    global exp
    label.config(text=str(eval(exp)))

#Final result callback: =
def clear():
    global exp
    global label
    exp=""
    label.configure(text=exp)
   


seven = tk.Button(button_frame,bg = "light grey",image=ims[7],command =lambda:  setexp('7'),height = 2, width = 2)
eight = tk.Button(button_frame, bg = "light grey",image=ims[8],command =lambda:  setexp('8'),height = 2, width = 2)
nine = tk.Button(button_frame, bg = "light grey",image=ims[9],command =lambda:  setexp('9'),height = 2, width = 2)
divide = tk.Button(button_frame, bg = "dark grey",text='/',command =lambda:  setexp('/'),height = 2, width = 2,font = "Arya 12 bold")
four = tk.Button(button_frame, bg = "light grey",image=ims[4],command =lambda:  setexp('4'),height = 2, width = 2)
five = tk.Button(button_frame,bg = "light grey",image=ims[5],command =lambda:  setexp('5'),height = 2, width = 2)
six = tk.Button(button_frame, bg = "light grey",image=ims[6],command =lambda:  setexp('6'),height = 2, width = 2)
multiply = tk.Button(button_frame, bg = "dark grey",text='*',command =lambda:  setexp('*'),height = 2, width = 2,font = "Arya 12 bold")
one = tk.Button(button_frame, bg = "light grey",image=ims[1],command =lambda:  setexp('1'),height = 2, width = 2)
two = tk.Button(button_frame, bg = "light grey",image=ims[2],command =lambda:  setexp('2'),height = 2, width = 2)
three = tk.Button(button_frame, bg = "light grey",image=ims[3],command =lambda:  setexp('3'),height = 2, width = 2)
minus = tk.Button(button_frame,bg = "dark grey",text='-',command =lambda:  setexp('-'),height = 2, width = 2,font = "Arya 12 bold")

cancel = tk.Button(button_frame, bg = "grey",text='C',command=clear,height = 2, width = 2,font = "Arya 12 bold")

zero = tk.Button(button_frame, bg = "light grey",text='0',command =lambda:  setexp('0'),height = 2, width = 2,font = "Arya 17 bold")
point = tk.Button(button_frame, bg = "dark grey",text='.',command =lambda:  setexp('.'),height = 2, width = 2,font = "Arya 12 bold")
plus = tk.Button(button_frame, bg = "dark grey",text='+',command =lambda:  setexp('+'),height = 2, width = 2,font = "Arya 12 bold")

equal = tk.Button(button_frame, bg = "dark grey",text='=',command=results,height = 2, width = 2)




button_frame.columnconfigure(0, weight=2)
button_frame.columnconfigure(1, weight=2)
button_frame.columnconfigure(2, weight=2)
button_frame.columnconfigure(3, weight=2)
                   

seven.grid(row=0, column=0, sticky="nsew")
eight.grid(row=0, column=1, sticky="nsew")
nine.grid(row=0, column=2, sticky="nsew")
divide.grid(row=0, column=3, sticky="nsew")

four.grid(row=1, column=0, sticky="nsew")
five.grid(row=1, column=1, sticky="nsew")
six.grid(row=1, column=2, sticky="nsew")
multiply.grid(row=1, column=3, sticky="nsew")

one.grid(row=2, column=0, sticky="nsew")
two.grid(row=2, column=1, sticky="nsew")
three.grid(row=2, column=2, sticky="nsew")
minus.grid(row=2, column=3, sticky="nsew")

cancel.grid(row=3, column=0, sticky="nsew")
zero.grid(row=3, column=1, sticky="nsew")
point.grid(row=3, column=2, sticky="nsew")
plus.grid(row=3, column=3, sticky="nsew")

equal.grid(row=4,columnspan=4, sticky="nsew")
label.grid(row=5,columnspan=4, sticky="nsew")

label.pack(fill='both', side='bottom',expand='true')



window.mainloop()
