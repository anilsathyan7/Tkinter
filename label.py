#GUI: Sample Program 

import Tkinter
window = Tkinter.Tk()
window.title("Button_Label")

num = 0

#callback : function for changing labe;
def increment():

    global num
    num += 1
    lbl.configure(text=num)#update label object

#create label 
lbl=Tkinter.Label(window, text=num)
lbl.pack()

#create button
btn=Tkinter.Button(window,text="Click Me",command=increment).pack()

window.mainloop()
