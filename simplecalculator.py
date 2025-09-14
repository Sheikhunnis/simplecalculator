#simple calulator 
import tkinter
from tkinter import *
root=Tk()
root.minsize(500,600)
root.maxsize(900,900)
root.title('calculator')
db=Entry(root,width=14,font=('Arial', 28),justify=RIGHT)
db.grid(row=0, column=0, padx=10, pady=10)
def clear():
    db.delete(0,END)


def btn_click(num):
    cur_num=db.get()
    clear()
    f_num=cur_num+num
    db.insert(0,f_num)
math=''
def calc(math_type):
    global first_num,math
    math=math_type
    first_num=db.get()
    clear()

def equal():
    global first_num
    global second_num,math
    second_num=db.get()
    clear()
    if(math=='add'):
        result=int(first_num)+int(second_num)
        db.insert(0,result)
    elif(math=='div'):
        result=int(first_num)/int(second_num)
        db.insert(0,result)

    elif(math == 'sub'):
        result = int(first_num)-int(second_num)
        db.insert(0,result)
    else:
        result=int(first_num)*int(second_num)
        db.insert(0,result)






#buttons

btn_0=Button(root,text='0',padx=36,pady=10,font=('Arial',14),command=lambda: btn_click('0',))
btn_1=Button(root,text='1',padx=36,pady=10,font=('Arial',14),command=lambda: btn_click('1'))
btn_2=Button(root,text='2',padx=36,pady=10,font=('Arial',14),command=lambda: btn_click('2'))
btn_3=Button(root,text='3',padx=36,pady=10,font=('Arial',14),command=lambda: btn_click('3'))
btn_4=Button(root,text='4',padx=36,pady=10,font=('Arial',14),command=lambda: btn_click('4'))
btn_5=Button(root,text='5',padx=36,pady=10,font=('Arial',14),command=lambda: btn_click('5'))
btn_6=Button(root,text='6',padx=36,pady=10,font=('Arial',14),command=lambda: btn_click('6'))
btn_7=Button(root,text='7',padx=36,pady=10,font=('Arial',14),command=lambda: btn_click('7'))
btn_8=Button(root,text='8',padx=36,pady=10,font=('Arial',14),command=lambda: btn_click('8'))
btn_9=Button(root,text='9',padx=36,pady=10,font=('Arial',14),command=lambda: btn_click('9'))
btn_clear=Button(root,text='clear',padx=75,pady=14,font=('Arial',14),command=lambda: clear())
btn_clear.grid(row=4,column=1,columnspan=2)

btn_div=Button(root,text='/',padx=38,pady=10,font=('Arial',14),command=lambda:calc('div'))
btn_mil=Button(root,text='*',padx=39,pady=10,font=('Arial',14),command=lambda:calc('mil'))

btn_add=Button(root,text='+',padx=35,pady=10,font=('Arial',14),command=lambda:calc('add'))
btn_add.grid(row=6,column=0)

btn_sub=Button(root,text='-',padx=39,pady=10,font=('Arial',14),command=lambda:calc('sub'))
btn_sub.grid(row=6,column=1)
btn_result=Button(root,text='=',padx=39,pady=40,font=('Arial',14),command=equal)
btn_result.grid(row=5,column=2,rowspan=2,padx=2,pady=2)

btn_div.grid(row=5,column=0,padx=2,pady=2)
btn_mil.grid(row=5,column=1,padx=2,pady=2)



btn_0.grid(row=4,column=0,padx=2,pady=2)
btn_1.grid(row=3,column=0,padx=2,pady=2)
btn_2.grid(row=3,column=1,padx=2,pady=2)
btn_3.grid(row=3,column=2,padx=2,pady=2)
btn_4.grid(row=2,column=0,padx=2,pady=2)
btn_5.grid(row=2,column=1,padx=2,pady=2)
btn_6.grid(row=2,column=2,padx=2,pady=2)
btn_7.grid(row=1,column=0,padx=2,pady=2)
btn_8.grid(row=1,column=1,padx=2,pady=2)
btn_9.grid(row=1,column=2,padx=2,pady=2)

db.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


root.mainloop()




