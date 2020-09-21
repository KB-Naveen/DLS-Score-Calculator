from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import webbrowser

class DLS:
    def __init__(self,master):

        master.title('DLS Score Calculator')
        master.configure(bg='white')
        master.resizable(False, False)

        self.photo1 = PhotoImage(file='cricket1.png')
        self.photo2 = PhotoImage(file='icc2.gif')
        lable1 = Label(master, image=self.photo1).pack()

        url = 'https://www.icc-cricket.com'
        def OpenUrl():
            webbrowser.open_new(url)

        button3 = Button(master, image=self.photo2,command=OpenUrl, bg='white').place(x=10,y=455)

        def close():
            master.destroy()

        def both():
            close()
            Calculator()

        button1 = Button(master, text='Start', width=10, bg='white', command=both).place(x=315, y=300)

def run():
    root = Tk()
    dls = DLS(root)
    root.geometry('700x500')
    root.mainloop()

def Calculator():
    root1 = Tk()
    root1.title("Calculator")
    root1.configure(bg='#ffffcc')
    root1.resizable(False, False)

    def radio():
        e1=DoubleVar()
        e2=DoubleVar()
        e3=DoubleVar()
        e7=DoubleVar()
        e8=DoubleVar()
        e9=DoubleVar()
        e4 = IntVar()
        e5 = IntVar()
        e6 = IntVar()
        e10 = IntVar()
        e11 = IntVar()
        e12 = IntVar()
        o1 = DoubleVar()
        o2 = DoubleVar()
        o3 = DoubleVar()
        o4 = DoubleVar()
        o5 = DoubleVar()
        o6 = DoubleVar()
        ascore = IntVar()
        def enter1():
            entry1 = Entry(root1, width=7, textvariable=e1).place(x=130, y=330)
            entry4 = Entry(root1, width=7, textvariable=e4).place(x=130, y=380)
            over1 = Entry(root1, width=7, textvariable=o1).place(x=130, y=430)
        def enter2():
            entry2 = Entry(root1, width=7, textvariable=e2).place(x=225, y=330)
            entry5 = Entry(root1, width=7, textvariable=e5).place(x=225, y=380)
            over2 = Entry(root1, width=7, textvariable=o2).place(x=225, y=430)
        def enter3():
            entry3 = Entry(root1, width=7, textvariable=e3).place(x=320, y=330)
            entry6 = Entry(root1, width=7, textvariable=e6).place(x=320, y=380)
            over3 = Entry(root1, width=7, textvariable=o3).place(x=320, y=430)
        def enter4():
            entry7 = Entry(root1, width=7, textvariable=e7).place(x=425, y=330)
            entry10 = Entry(root1, width=7, textvariable=e10).place(x=425, y=380)
            over4 = Entry(root1, width=7, textvariable=o4).place(x=425, y=430)
        def enter5():
            entry8 = Entry(root1, width=7, textvariable=e8).place(x=520, y=330)
            entry11 = Entry(root1, width=7, textvariable=e11).place(x=520, y=380)
            over5 = Entry(root1, width=7, textvariable=o5).place(x=520, y=430)
        def enter6():
            entry9 = Entry(root1, width=7, textvariable=e9).place(x=615, y=330)
            entry12 = Entry(root1, width=7, textvariable=e12).place(x=615, y=380)
            over6 = Entry(root1, width=7, textvariable=o6).place(x=615, y=430)
        def enter12():
            enter1()
            enter2()
        def enter123():
            enter1()
            enter2()
            enter3()
        def enter45():
            enter4()
            enter5()
        def enter456():
            enter4()
            enter5()
            enter6()

        var3 = var1.get()
        var4 = var2.get()

        if (var3 == 0):
            state1 = DISABLED
        else:
            state1 = ACTIVE

        if (var4 == 0):
            state2 = DISABLED
        else:
            state2 = ACTIVE

        lable = Label(text='Overs alloted to 1st innings at start of the match:\n(Team A-Batting and Team B-Bowling)',
                      font=('Sombir'), bg='#ffffcc').place(x=0, y=60)
        sp1 = IntVar()
        spin1 = Entry(root1, width=10,textvariable=sp1,bg='#ffffcc').place(x=465, y=60)

        lable2 = Label(text='How many times 1st innings interrupted:', font=('Sombir'),bg='#ffffcc').place(x=0, y=110)

        radio1 = Radiobutton(root1, text='1', value=1, variable=1, state=state1, command=enter1,bg='#ffffcc').place(x=400, y=110)
        radio2 = Radiobutton(root1, text='2', value=2, variable=1, state=state1, command=enter12,bg='#ffffcc').place(x=480, y=110)
        radio3 = Radiobutton(root1, text='3', value=3, variable=1, state=state1, command=enter123,bg='#ffffcc').place(x=560, y=110)

        lable3 = Label(text='How many times 2nd innings interrupted:', font=('Sombir'),bg='#ffffcc').place(x=0, y=150)

        radio4 = Radiobutton(root1, text='1', value=1, variable=2, state=state2, command=enter4,bg='#ffffcc').place(x=400, y=150)
        radio5 = Radiobutton(root1, text='2', value=2, variable=2, state=state2, command=enter45,bg='#ffffcc').place(x=480, y=150)
        radio6 = Radiobutton(root1, text='3', value=3, variable=2, state=state2, command=enter456,bg='#ffffcc').place(x=560, y=150)

        lable11 = Label(text='Overs alloted to 2nd innings at start of the 2nd innings:\n(Team B-Batting and Team A-Bowling)',
                      font=('Sombir'), bg='#ffffcc').place(x=0, y=200)
        sp2 = IntVar()
        spin2 = Entry(root1, width=10,textvariable=sp2, bg='#ffffcc').place(x=465, y=200)

        lable4 = Label(text='1st innigs itteruption details:-', font=('Sombir',13,'bold'),bg='#ffffcc').place(x=130, y=260)
        lable5 = Label(text='Overs Left:', font=('Sombir',13,'bold'),bg='#ffffcc').place(x=0, y=330)
        lable6 = Label(text='Wickets Lost:', font=('Sombir',13,'bold'),bg='#ffffcc').place(x=0, y=380)
        lable14 = Label(text='Overs alloted:', font=('Sombir', 13, 'bold'), bg='#ffffcc').place(x=0, y=430)
        lable7 = Label(text='2nd innigs itteruption details:-', font=('Sombir',13,'bold'),bg='#ffffcc').place(x=425, y=260)
        lable11 = Label(text='Interuptions:', font=('Sombir',13,'bold'),bg='#ffffcc').place(x=0, y=290)
        lable8 = Label(text='1', font=('Sombir'),bg='#ffffcc').place(x=130, y=290)
        lable9 = Label(text='2', font=('Sombir'),bg='#ffffcc').place(x=225, y=290)
        lable10 = Label(text='3', font=('Sombir'),bg='#ffffcc').place(x=320, y=290)
        lable8 = Label(text='1', font=('Sombir'),bg='#ffffcc').place(x=425, y=290)
        lable9 = Label(text='2', font=('Sombir'),bg='#ffffcc').place(x=520, y=290)
        lable10 = Label(text='3', font=('Sombir'),bg='#ffffcc').place(x=615, y=290)

        lable12 = Label(text='Team A total:',font=('Sombir'),bg='#ffffcc').place(x=0,y=480)
        enters = Entry(root1, width=7, textvariable=ascore).place(x=150,y=480)



        def values():

            p1 = (e1.get() - (sp1.get() - o1.get()))
            p2 = (e2.get() - (o1.get() - o2.get()))
            p3 = (e3.get() - (o2.get() - o3.get()))
            p4 = (e7.get() - (sp2.get() - o4.get()))
            p5 = (e8.get() - (o4.get() - o5.get()))
            p6 = (e9.get() - (o5.get() - o6.get()))

            if (p1 < 0):
                p1 = 0
            if (p2 < 0):
                p2 = 0
            if (p3 < 0):
                p3 = 0
            if (p4 < 0):
                p4 = 0
            if (p5 < 0):
                p5 = 0
            if (p6 < 0):
                p6 = 0

            m = open("resourceTable.txt", "r")
            line = m.readlines()

            def find(z, y):
                for x in range(301):
                    k = line[x].split()
                    if (float(k[0]) == z):
                        return float(k[y + 1])

            leftA = [sp1.get(),e1.get(),p1,e2.get(),p2,e3.get(),p3]
            leftB = [sp2.get(),e7.get(),p4,e8.get(),p5,e9.get(),p6]
            lostA = [0,e4.get(),e4.get(),e5.get(),e5.get(),e6.get(),e6.get()]
            lostB = [0,e10.get(),e10.get(),e11.get(),e11.get(),e12.get(),e12.get()]

            sourceA = []
            sourceB = []

            for i in range(7):
                s = find(leftA[i], lostA[i])
                sourceA.append(s)

            for i in range(7):
                s = find(leftB[i], lostB[i])
                sourceB.append(s)

            RoA = (sourceA[0]-(sourceA[1]-sourceA[2])-(sourceA[3]-sourceA[4])-(sourceA[5]-sourceA[6]))
            RoB = (sourceB[0]-(sourceB[1]-sourceB[2])-(sourceB[3]-sourceB[4])-(sourceB[5]-sourceB[6]))

            if(RoB>RoA):
                target = ascore.get()+((RoB-RoA)*2.45)+1
            else:
                target = (ascore.get()*(RoB/RoA))+1

            vartar = IntVar()

            targetlable1 = Label(root1,text='Target for Team B:', font=("Helvetica", 14, "bold italic"),bg='#ffffcc').place(x=455,y=470)
            targetlable2 = Label(root1, textvariable=vartar, font=("Helvetica", 19, "bold italic"),bg='#ffffcc').place(x=520, y=505)
            vartar.set(round(target))
        button2 = Button(root1,text='Calculte',width=10,bg='white',command=values).place(x=305,y=480)
        button3 = Button(root1,text='Exit',width=10,bg='white',command=root1.destroy).place(x=305,y=513)

    lable1 = Label(text='In which Innings game interrupted:\n(Check both boxes if match interrupted in both innings)',
                   font=('Sombir'),bg='#ffffcc').place(x=0,y=5)
    var1 = IntVar()
    check1 = Checkbutton(root1, text='1st Innings',state=ACTIVE,variable=var1,command=radio,bg='#ffffcc').place(x=420,y=5)
    var2 = IntVar()
    check2 = Checkbutton(root1, text='2nd Innings',state=ACTIVE,variable=var2,command=radio,bg='#ffffcc').place(x=520,y=5)

    root1.geometry('700x560')
    root1.mainloop()

if __name__ == "__main__": run()