from tkinter import *
window = Tk()

window.title('multiconvert from kg')

window.resizable(0,0)

#do the math
def Mathoper():


    gramss = float(inputvar.get())*1000
    poundss = float(inputvar.get())*2.20462
    ouncess = float(inputvar.get())*35.274

#insert values the vars with double s is the math value
    grams.delete("1.0", END)
    pounds.delete("1.0", END)
    ounces.delete("1.0", END)

    grams.insert(END, gramss)
    pounds.insert(END, poundss)
    ounces.insert(END, ouncess)
#value of users input
inputvar=StringVar()


inputlabel= Label(window, text="Input kg", bg='aquamarine1', borderwidth=3, relief="raised")
inputlabel.grid(column=0,row=0)
input = Entry(window, textvariable=inputvar, width=30)
input.grid(column=1, row=0)


bt = Button(window, text='Convert', bg='black',fg='orange', command=Mathoper,width=25)
bt.grid(column=1,row=2)

gramslabel = Label(window, text="Grams", height=1,width=5,bg='deeppink1')
gramslabel.grid(column=0, row=4)
grams = Text(window, height=1, width=25)
grams.grid(column=1, row=4)


poundslabel = Label(window, text="Pounds", height=1,width=5,bg='darkorchid1')
poundslabel.grid(column=0, row=5)
pounds = Text(window, height=1, width=25)
pounds.grid(column=1, row=5)


ounceslabel = Label(window, text="Ounces", height=1,width=5,bg='darkolivegreen1')
ounceslabel.grid(column=0, row=6)
ounces = Text(window, height=1, width=25)
ounces.grid(column=1,row=6)





window.mainloop()