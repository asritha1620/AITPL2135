from tkinter import *
expression= ""
def input_number(number, equation):
    global expression
    expression = expression + str(number)
    equation.set(expression)
def clear_input_field(equation):
    global expression
    expression = ""
    equation.set("Enter the expression")
def evaluate(equation):
    global expression
# trying to evaluate the expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = ""
    except:
        expression = ""
def main():
   a=Tk()
   a.title("Basic Calculator")
   a.geometry("400x400")
   equation = StringVar()
   # input field for the expression
   input_field = Entry(a,textvariable=equation)
   input_field.place(height=200)
   input_field.grid(columnspan=4, ipadx=100, ipady=5)
   # setting the placeholder message for users
   equation.set("")
   x1=Button(a,text=0,padx=20,pady=20,command=lambda:input_number(0, equation))
   x2=Button(a,text=1,padx=20,pady=20,command=lambda:input_number(1, equation))
   x3=Button(a,text=2,padx=20,pady=20,command=lambda:input_number(2, equation))
   x4=Button(a,text=3,padx=20,pady=20,command=lambda:input_number(3, equation))
   x5=Button(a,text=4,padx=20,pady=20,command=lambda:input_number(4, equation))
   x6=Button(a,text=5,padx=20,pady=20,command=lambda:input_number(5, equation))
   x7=Button(a,text=6,padx=20,pady=20,command=lambda:input_number(6, equation))
   x8=Button(a,text=7,padx=20,pady=20,command=lambda:input_number(7, equation))
   x9=Button(a,text=8,padx=20,pady=20,command=lambda:input_number(8, equation))
   xa=Button(a,text=9,padx=20,pady=20,command=lambda:input_number(9, equation))
   xb=Button(a,text='+',padx=20,pady=20,command=lambda:input_number('+', equation))
   xc=Button(a,text='-',padx=20,pady=20,command=lambda:input_number('-', equation))
   xd=Button(a,text='*',padx=20,pady=20,command=lambda:input_number('*', equation))
   xe=Button(a,text='clear',padx=20,pady=20,command=lambda:clear_input_field(equation))
   xf=Button(a,text='=',padx=20,pady=20,command=lambda:evaluate(equation))
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
   xc.grid(row=4,column=3)
   xd.grid(row=5,column=3)
   xe.grid(row=5,column=1)
   xf.grid(row=5,column=2)
   a.mainloop()
if __name__ == '__main__':
      main()
