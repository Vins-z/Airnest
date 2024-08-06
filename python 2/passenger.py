from tkinter import *
import tkinter.messagebox
import datetime
from tkcalendar import Calendar
from PIL import Image, ImageTk
from tkinter import ttk

class Passenger:
    def __init__(self, root):
        self.root = root
        self.root.title("")
        self.root.geometry("1366x768+0+0")
        self.root.config(bg="grey")

        # Load and display background image
        bg_image = Image.open("/Users/vinayak/Documents/GitHub/Dropbox/python/0.jpeg")
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(self.root, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg_photo
        Pname = StringVar()
        PAddress = StringVar()
        Pmobile = StringVar()
        passengerList = StringVar()
        Pdate = StringVar()
        FromCity = StringVar()
        ToCity = StringVar()
        
        
        def open_calendar():
            def select_date():
                selected_date = cal.selection_get()
                Pdate.set(selected_date.strftime("%Y-%m-%d"))
                top.destroy()
            top = Toplevel(root)
            cal = Calendar(top, selectmode="day", year=datetime.datetime.now().year, month=datetime.datetime.now().month, day=datetime.datetime.now().day)
            cal.pack(pady=20)
            Button(top, text="Select Date", command=select_date).pack()
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("FBS","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        
        def clearData():
            self.txtPno.delete(0, END)
            self.txtPname.delete(0, END)
            self.txtPAddress.delete(0, END)
            self.txtPMobile.delete(0, END) 
        
        def cont():
            from_city = FromCity.get()
            to_city = ToCity.get()
            print("From City:", from_city)
            print("To City:", to_city)
            import flight_select         
        
        MainFrame = Frame(self.root, bg='')
        MainFrame.grid()
        TitFrame = Frame(MainFrame, bd=0, bg='', relief=GROOVE)
        TitFrame.pack(side=TOP)
        root.attributes("-alpha", 0.975)
        self.lblTit = Label(TitFrame, font=('Agency FB', 30), text="Air Nest", bg='Ghost White')
        self.lblTit.grid(sticky=W)

        
        ButtonFrame = Frame(MainFrame, bd=2, width=1920, padx=20, height=70, pady=14, bg='#008080', relief=GROOVE)
        ButtonFrame.pack(side=BOTTOM)
        DataFrame = Frame(MainFrame, bd=0, width=1920, height=400, padx=23, pady=20, bg='#008080', relief=GROOVE)
        DataFrame.pack(side=BOTTOM)
        
        DataFrameLEFT = LabelFrame(DataFrame, bd=0, width=1920, height=1300, padx=20, pady=73, bg='Ghost White', relief=GROOVE, font=('Agency FB', 20), text="Enter Passenger Information\n")
        DataFrameLEFT.pack(side=TOP)
        self.lblPname = Label(DataFrameLEFT, font=('Comic Sans MS', 20), text="Passenger Name:", padx=2, pady=2, bg="Ghost White")
        self.lblPname.grid(row=1, column=0, sticky=W)
        self.txtPname = Entry(DataFrameLEFT, font=('Comic Sans MS', 20), textvariable=Pname, width=39)
        self.txtPname.grid(row=1, column=1)
        
        self.lblPAddress = Label(DataFrameLEFT, font=('Comic Sans MS', 20), text="Passenger Address:", padx=2, pady=2, bg="Ghost White")
        self.lblPAddress.grid(row=2, column=0, sticky=W)
        self.txtPAddress = Entry(DataFrameLEFT, font=('Comic Sans MS', 20), textvariable=PAddress, width=39)
        self.txtPAddress.grid(row=2, column=1)
        
        self.lblPMobile = Label(DataFrameLEFT, font=('Comic Sans MS', 20), text="Passenger Mobile:", padx=2, pady=2, bg="Ghost White")
        self.lblPMobile.grid(row=3, column=0, sticky=W)
        self.txtPMobile = Entry(DataFrameLEFT, font=('Comic Sans MS', 20), textvariable=Pmobile, width=39)
        self.txtPMobile.grid(row=3, column=1)
        
        self.lblPdate = Label(DataFrameLEFT, font=('Comic Sans MS', 20), text="Date:", padx=2, pady=2, bg="Ghost White")
        self.lblPdate.grid(row=4, column=0, sticky=W)
        self.txtPdate = Entry(DataFrameLEFT, font=('Comic Sans MS', 20), textvariable=Pdate, width=15)
        self.txtPdate.grid(row=4, column=1)
        self.btnCalendar = Button(DataFrameLEFT, text="Select Date", font=('Times New Roman', 20, 'bold'), height=1, width=8, bd=3, command=open_calendar)
        self.btnCalendar.grid(row=4, column=2)
        
        self.lblFromCity = Label(DataFrameLEFT, font=('Comic Sans MS', 20), text="From:", padx=2, pady=2, bg="Ghost White")
        self.lblFromCity.grid(row=5, column=0, sticky=W)
        self.comboFromCity = ttk.Combobox(DataFrameLEFT, font=('Comic Sans MS', 20), textvariable=FromCity, state="readonly", width=36)
        self.comboFromCity['values'] = ('Mumbai', 'Delhi', 'Bangalore')
        self.comboFromCity.current()
        self.comboFromCity.grid(row=5, column=1)
        
        self.lblToCity = Label(DataFrameLEFT, font=('Comic Sans MS', 20), text="To:", padx=2, pady=2, bg="Ghost White")
        self.lblToCity.grid(row=6, column=0, sticky=W)
        self.comboToCity = ttk.Combobox(DataFrameLEFT, font=('Comic Sans MS', 20), textvariable=ToCity, state="readonly", width=36)
        self.comboToCity['values'] = ('Mumbai', 'Delhi', 'Bangalore')
        self.comboToCity.current()
        self.comboToCity.grid(row=6, column=1)
        
        self.btnContinue = Button(ButtonFrame, text="Continue", font=('Times New Roman', 20, 'bold'), height=1, width=10, bd=3, command=cont)
        self.btnContinue.grid(row=0, column=0)
        self.btnClearDate = Button(ButtonFrame, text="Clear", font=('Times new Roman', 20, 'bold'), height=1, width=10, bd=3, command=clearData)
        self.btnClearDate.grid(row=0, column=2)
        self.btnExit = Button(ButtonFrame, text="Exit", font=('Times New Roman', 20, 'bold'), height=1, width=10, bd=3, command=iExit)
        self.btnExit.grid(row=0, column=6)


if __name__ == '__main__':
    root = Tk()
    application = Passenger(root)
    root.mainloop()
