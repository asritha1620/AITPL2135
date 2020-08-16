from tkinter import *
a=Tk()
a.title("Untitled-Notepad")
a.geometry("500x500+100+100")
m1=Menu()
l1=Menu()
l1.add_command(label="New")
l1.add_command(label="Open...")
l1.add_command(label="Save")
l1.add_command(label="Save As...")
l1.add_command(label="Page Setup")
l1.add_command(label="Print...")
l1.add_command(label="Exit")
l2=Menu()
l2.add_command(label="Undo")
l2.add_command(label="Cut")
l2.add_command(label="Copy")
l2.add_command(label="Paste")
l2.add_command(label="Delete")
l2.add_command(label="Find...")
l2.add_command(label="Find Next")
l2.add_command(label="Replace...")
l2.add_command(label="Go To...")
l2.add_command(label="Select All")
l2.add_command(label="Time/Date")
l3=Menu()
l3.add_command(label="Wordwrap")
l3.add_command(label="Font...")
l4=Menu()
l4.add_command(label="Status Bar")
l5=Menu()
l5.add_command(label="View Help")
l5.add_command(label="About Notepad")
l5.add_command(label="Viewhelp")
l5.add_command(label="Feedback")
m1.add_cascade(label="File",menu=l1)
m1.add_cascade(label="Edit",menu=l2)
m1.add_cascade(label="Format",menu=l3)
m1.add_cascade(label="View",menu=l4)
m1.add_cascade(label="Help",menu=l5)
a.config(menu=m1)
a.mainloop()














from tkinter import *
a=Tk()
a.title(" Basic Calculator")
b=Entry(a,width=15,borderwidth=5)
b.grid(row=0,column=0,columnspan=5,padx=10,pady=10)
def click(number):
    c=b.get()
    b.delete(0,number)
    b.insert(0,str(c)+str(number))
def add():
    fnum=b.get()
    global f_num
    f_num=int(fnum)
    b.delete(0,END)
def equal():
    s_num=b.get()
    b.delete(0,END)
    b.insert(0,f_num + int(s_num))
expression=" "
def input_number(number, equation):
    global expression
   # concatenation of string
    expression = expression + str(number)
    equation.set(expression)
def clear_input_field(equation):
    global expression
    expression = ""


def clear():
    b.delete(0,END)
x1=Button(a,text=0,padx=20,pady=20,command=lambda:input_number(0, equation))
x2=Button(a,text=1,padx=20,pady=20,command=lambda:(1))
x3=Button(a,text=2,padx=20,pady=20,command=lambda:click(2))
x4=Button(a,text=3,padx=20,pady=20,command=lambda:click(3))
x5=Button(a,text=4,padx=20,pady=20,command=lambda:click(4))
x6=Button(a,text=5,padx=20,pady=20,command=lambda:click(5))
x7=Button(a,text=6,padx=20,pady=20,command=lambda:click(6))
x8=Button(a,text=7,padx=20,pady=20,command=lambda:click(7))
x9=Button(a,text=8,padx=20,pady=20,command=lambda:click(8))
xa=Button(a,text=9,padx=20,pady=20,command=lambda:click(9))
xb=Button(a,text='+',padx=20,pady=20,command=add)
#xc=Button(a,text='-',padx=20,pady=20,command=add)
#xd=Button(a,text='*',padx=20,pady=20,command=add)
xe=Button(a,text='clear',padx=20,pady=20,command=clear)
xf=Button(a,text='=',padx=20,pady=20,command=equal)
x1.grid(row=4,column=1)
x2.grid(row=3,column=1)
x3.grid(row=3,column=2)
x4.grid(row=3,column=3)
x5.grid(row=2,column=1)
x6.grid(row=2,column=2)
x7.grid(row=2,column=3)
x8.grid(row=1,column=1)
x9.grid(row=1,column=2)
xa.grid(row=1,column=3)
xb.grid(row=4,column=2)
#xc.grid(row=4,column=3)
#xd.grid(row=5,column=3)
xe.grid(row=5,column=1,columnspan=2)
xf.grid(row=5,column=2,columnspan=2)
a.mainloop()
