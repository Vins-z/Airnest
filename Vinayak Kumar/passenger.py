from tkinter import *
import tkinter.messagebox
import pasDatabase
import datetime
class Passenger:
    def __init__(self, root):
        self.root = root
        self.root.title("")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg="white")
        Pno = StringVar()
        Pname = StringVar()
        PAddress = StringVar()
        Pmobile = StringVar()
        def cal():
            from tkcalendar import Calendar
            tkobj = Tk()
            tkobj.geometry("400x400")
            tkobj.title("Calendar picker")
            tkc = Calendar(tkobj,selectmode = "day",year=2022,month=1,date=1)
            tkc.pack(pady=40)
            def fetch_date():
                date.config(text = "Selected Date is: " + tkc.get_date())
                but = Button(tkobj,text="Select Date",command=fetch_date, bg="black", fg='white')
                but.pack()
                date = Label(tkobj,text="",bg='black',fg='white')
                date.pack(pady=20)
                tkobj.mainloop()
                d=tkc.get_date()
                return d
        Pdate= cal()
        def iExit():
            iExit = tkinter.messagebox.askyesno("Transport Management System","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        def clearData():
            self.txtPno.delete(0,END)
            self.txtPname.delete(0,END)
            self.txtPAddress.delete(0,END)
            self.txtPMobile.delete(0,END) 
        def addData():
            if(len(Pno.get())!=0):
                pasDatabase.addPas(Pno.get(),Pname.get(),PAddress.get(),Pmobile.get(),Bno.get(),Rname.get())
                passengerList.delete(0,END)
                passengerList.insert(END,(Pno.get(),Pname.get(),PAddress.get(),Pmobile.get(),Bno.get(),Rname.get()))
        def displayData():
            passengerList.delete(0,END)
            for row in pasDatabase.viewDat():
                passengerList.insert(END,row,str(""))
        def pasRec(event):
            global sd
            searchpas = passengerList.curselection()[0]
            sd = passengerList.get(searchpas)
            self.txtPno.delete(0,END)
            self.txtPno.insert(END,sd[1])
            self.txtPname.delete(0,END)
            self.txtPname.insert(END,sd[2])
            self.txtPAddress.delete(0,END)
            self.txtPAddress.insert(END,sd[3])
            self.txtPMobile.delete(0,END)
            self.txtPMobile.insert(END,sd[4])           
        def deleteData():
            if(len(Pno.get())!=0):
                pasDatabase.deleteDat(sd[0])
                clearData()
                displayData()
        def searchData():
            passengerList.delete(0,END)
            for row in pasDatabase.searchDat(Pno.get(),Pname.get(),PAddress.get(),Pmobile.get()):
                passengerList.insert(END,row,str(""))
        def update():
            if(len(Pno.get())!=0):
                pasDatabase.deleteDat(sd[0])
            if(len(Pno.get())!=0):
                pasDatabase.addPas(Pno.get(),Pname.get(),PAddress.get(),Pmobile.get())
                passengerList.delete(0,END)
                passengerList.insert(END,(Pno.get(),Pname.get(),PAddress.get(),Pmobile.get()))
        MainFrame = Frame(self.root, bg='gray99')
        MainFrame.grid()
        TitFrame = Frame(MainFrame, bd=2,  bg='Ghost White', relief= RIDGE)
        TitFrame.pack(side = TOP)
        self.lblTit = Label(TitFrame, font=('Times New Roman', 30, 'bold'),text="Transport Management System",bg="Ghost White")
        self.lblTit.grid(sticky=W)
        ButtonFrame = Frame(MainFrame, bd=2, width=1920,padx=20, height=70,pady=14, bg='grey', relief= RIDGE)
        ButtonFrame.pack(side = BOTTOM)
        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=23, pady=20, bg='Grey', relief= RIDGE)
        DataFrame.pack(side = BOTTOM)
        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width =600, height=1000, padx=20,pady=73, bg='Ghost White', relief= RIDGE, 
                                    font=('Helvetica', 20, 'bold'), text="Passenger Information\n")
        DataFrameLEFT.pack(side = LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, pady=31, bg='Ghost White', relief= RIDGE,
                                    font=('arial', 20, 'bold'),text = "Passenger Details\n")
        DataFrameRIGHT.pack(side = RIGHT)
        self.lblPno = Label(DataFrameLEFT, font=('arial', 20, 'bold'),text="Passenger Number : ",padx=2,pady=2,bg="Ghost White")
        self.lblPno.grid(row=0,column=0,sticky=W)
        self.txtPno = Entry(DataFrameLEFT, font=('arial', 20, 'bold'),textvariable=Pno, width=39)
        self.txtPno.grid(row=0,column=1)
        self.lblPname = Label(DataFrameLEFT, font=('arial', 20, 'bold'),text="Passenger Name : ",padx=2,pady=2,bg="Ghost White")
        self.lblPname.grid(row=1,column=0,sticky=W)
        self.txtPname = Entry(DataFrameLEFT, font=('arial', 20, 'bold'),textvariable=Pname, width=39)
        self.txtPname.grid(row=1,column=1)
        self.lblPAddress = Label(DataFrameLEFT, font=('arial', 20, 'bold'),text="Passenger Address : ",padx=2,pady=2,bg="Ghost White")
        self.lblPAddress.grid(row=2,column=0,sticky=W)
        self.txtPAddress = Entry(DataFrameLEFT, font=('arial', 20, 'bold'),textvariable=PAddress, width=39)
        self.txtPAddress.grid(row=2,column=1)
        self.lblPMobile = Label(DataFrameLEFT, font=('arial', 20, 'bold'),text="Passenger Mobile : ",padx=2,pady=2,bg="Ghost White")
        self.lblPMobile.grid(row=3,column=0,sticky=W)
        self.txtPMobile = Entry(DataFrameLEFT, font=('arial', 20, 'bold'),textvariable=Pmobile, width=39)
        self.txtPMobile.grid(row=3,column=1)
        self.lblPdate = Label(DataFrameLEFT,font=('arial',20, 'bold'),text="Date : ",padx=2,pady=2,bg="Ghost White")
        self.lblPdate.grid(row=4,column=1)
        self.txtPdate = Entry(DataFrameLEFT, font=('arial', 20, 'bold'),textvariable=Pdate, width=39)
        
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')
        
        passengerdtailsList = Listbox(DataFrameRIGHT, width=41,height=16,font=('arial',12,'bold'),yscrollcommand=scrollbar.set)
        passengerList.bind('<<ListboxSelect>>',pasRec)
        passengerList.grid(row=0,column=0,padx=8)
        scrollbar.config(command  = passengerList.yview)
        self.btnAddDate = Button(ButtonFrame,text="Add New",font=('arial', 20, 'bold'),height=1,width=10,bd=4,command=addData)
        self.btnAddDate.grid(row=0,column=0)
        
        self.btnDisplayDate = Button(ButtonFrame,text="Display",font=('arial', 20, 'bold'),height=1,width=10,bd=4,command=displayData)
        self.btnDisplayDate.grid(row=0,column=1)
        
        self.btnClearDate = Button(ButtonFrame,text="Clear",font=('arial', 20, 'bold'),height=1,width=10,bd=4,command=clearData)
        self.btnClearDate.grid(row=0,column=2)
        self.btnDeleteDate = Button(ButtonFrame,text="Delete",font=('arial', 20, 'bold'),height=1,width=10,bd=4,command=deleteData)
        self.btnDeleteDate.grid(row=0,column=3)
        self.btnSearchDate = Button(ButtonFrame,text="Search",font=('Times New Roman', 20, 'bold'),height=1,width=10,bd=4,command=searchData)
        self.btnSearchDate.grid(row=0,column=4)
        self.btnExit = Button(ButtonFrame,text="Exit",font=('arial', 20, 'bold'),height=1,width=10,bd=4,command=iExit)
        self.btnExit.grid(row=0,column=6)
if __name__=='__main__':
    root = Tk()
    application = Passenger(root)
    root.mainloop()
