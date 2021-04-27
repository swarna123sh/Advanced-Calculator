from tkinter import *
def cellpad(p):
    button1 = Button(p, text=' 1 ', fg='black', bg='turquoise', command=lambda: press(p,1), height=1, width=3) 
    button1.place(x=10,y=250)
  
    button2 = Button(p, text=' 2 ', fg='black', bg='turquoise', command=lambda: press(p,2), height=1, width=3) 
    button2.place(x=60,y=250)
  
    button3 = Button(p, text=' 3 ', fg='black', bg='turquoise', command=lambda: press(p,3), height=1, width=3) 
    button3.place(x=110,y=250)
  
    button4 = Button(p, text=' 4 ', fg='black', bg='turquoise', command=lambda: press(p,4), height=1, width=3) 
    button4.place(x=160,y=250) 
  
    button5 = Button(p, text=' 5 ', fg='black', bg='turquoise', command=lambda: press(p,5), height=1, width=3) 
    button5.place(x=210,y=250) 
  
    button6 = Button(p, text=' 6 ', fg='black', bg='turquoise', command=lambda: press(p,6), height=1, width=3) 
    button6.place(x=260,y=250) 
  
    button7 = Button(p, text=' 7 ', fg='black', bg='turquoise', command=lambda: press(p,7), height=1, width=3) 
    button7.place(x=310,y=250) 
  
    button8 = Button(p, text=' 8 ', fg='black', bg='turquoise', command=lambda: press(p,8), height=1, width=3) 
    button8.place(x=360,y=250) 
  
    button9 = Button(p, text=' 9 ', fg='black', bg='turquoise', command=lambda: press(p,9), height=1, width=3) 
    button9.place(x=410,y=250)
  
    button0 = Button(p, text=' 0 ', fg='black', bg='turquoise', command=lambda: press(p,0), height=1, width=3) 
    button0.place(x=460,y=250) 

def press(p,num):
  y=p.focus_get()
  y.insert(END,num)
  
    