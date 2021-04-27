import math
from tkinter import *
import cellpad

#Tkinter instance setup
window=Tk()
window.title("Advanced Calculator")
window.geometry('600x600')
cellpad.cellpad(window)


#Getting the inputs
lbl=Label(text="Enter the first number",  font=("Arial Bold", 30))
lbl.grid(column=0, row=0)
txt = Entry(window,width=10)
txt.grid(column=0, row=1)


lbl2=Label(text="Enter the second number", font=("Arial Bold", 30))
lbl2.grid(column=0, row=3)
txt2 = Entry(window,width=10)
txt2.grid(column=0, row=4)

#Button Functions
def add():
  try:
   a=int(txt.get())
   b=int(txt2.get())
  except: 
   print("Enter valid numbers for addition")   
  else:
    ans=a+b
    answer.configure(text=ans)

def minus():
   a=int(txt.get())
   b=int(txt2.get())
   ans=a-b
   answer.configure(text=ans)

def multiply():
   a=int(txt.get())
   b=int(txt2.get())
   ans=a*b
   answer.configure(text=ans)  

def divide():
   a=int(txt.get())
   b=int(txt2.get())
   ans=a/b
   answer.configure(text=ans)

def modulus():
   a=int(txt.get())
   b=int(txt2.get())
   ans=a%b
   answer.configure(text=ans)

def power():
   a=int(txt.get())
   b=int(txt2.get())
   ans=math.pow(a,b)
   answer.configure(text=ans)

def gcd():
   a=int(txt.get())
   b=int(txt2.get())
   ans=math.gcd(a,b)
   answer.configure(text=ans)

def log():
   a=int(txt.get())
   b=int(txt2.get())
   ans=math.log(a,b)
   answer.configure(text=ans)   

def hypotnuse():
   a=int(txt.get())
   b=int(txt2.get())
   ans=math.hypot(a,b)
   answer.configure(text=ans)   

def squrt():
  if len(txt.get())!=0:
    a=int(txt.get())
    ans=math.sqrt(a)
    answer.configure(text=ans)
  elif len(txt2.get())!=0:
    b=int(txt2.get())
    ans=math.sqrt(b)
    answer.configure(text=ans)
  elif len(txt.get())!=0 and len(txt2.get())!=0:
    a=int(txt.get())
    ans=math.sqrt(a)
    answer.configure(text=ans)
  else:
    answer.configure(text="0")

def fact():
  if len(txt.get())!=0:
    a=int(txt.get())
    ans=math.factorial(a)
    answer.configure(text=ans)
  elif len(txt2.get())!=0:
    b=int(txt2.get())
    ans=math.factorial(b)
    answer.configure(text=ans)
  elif len(txt.get())!=0 and len(txt2.get())!=0:
    a=int(txt.get())
    ans=math.factorial(a)
    answer.configure(text=ans)
  else:
    answer.configure(text="0")


#Button Setup
b1 = Button(window,text = "+",command = add,activeforeground = "red",activebackground = "pink")  
  
b2 = Button(window, text = "-",command = minus,activeforeground = "blue",activebackground = "pink")  
  
b3 = Button(window, text = "*",command = multiply,activeforeground = "green",activebackground = "pink")  
  
b4 = Button(window, text = "/",command = divide,activeforeground = "yellow",activebackground = "pink")  

b5 = Button(window, text = "%",command = modulus,activeforeground = "yellow",activebackground = "pink")

b6 = Button(window,text = "Power(^)",command = power,activeforeground = "red",activebackground = "pink")  
  
b7 = Button(window, text = "GCD",command = gcd,activeforeground = "blue",activebackground = "pink")  
  
b8 = Button(window, text = "Logarithm",command = log,activeforeground = "green",activebackground = "pink")  
  
b9 = Button(window, text = "Hypotnuse",command = hypotnuse,activeforeground = "black",activebackground = "pink")  

b10 = Button(window, text = "Squareroot",command = squrt,activeforeground = "yellow",activebackground = "pink")

b11 = Button(window, text = "Factorial",command = fact,activeforeground = "green",activebackground = "pink")
  
b1.place(x=60,y=300)
b2.place(x=150,y=300)
b3.place(x=230,y=300)  
b4.place(x=310,y=300)
b5.place(x=390,y=300)
b6.place(x=50,y=400)
b7.place(x=160,y=400)
b8.place(x=250,y=400)  
b9.place(x=360,y=400)
b10.place(x=70,y=500)
b11.place(x=190,y=500)

# Answer Label
answer=Label(text="Answer appears over here", bg="lightgreen")
answer.place(x=200,y=200)


window.mainloop()
