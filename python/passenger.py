from tkinter import *
import tkinter.messagebox
import datetime
from tkcalendar import Calendar
from PIL import Image, ImageTk
from tkinter import ttk

class Passenger:
    def __init__(self, root):
        self.root = root
        self.root.title("Air Nest")
        self.root.geometry("1080x720")
        self.root.config(bg="Light Blue")

        # Load and display background image
        bg_image = Image.open("/Users/vinayak/Documents/GitHub/Dropbox/python/0.jpeg")
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(self.root, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg_photo

        bg_color="#F5F2EE"
        label_color = "black"
        button_color = "#FCAD77"

        title_font = ("Cambria", 30, "bold")
        label_font = ("Times New Roman", 14)
        button_font = ("Agency FB", 14, "bold")

        padding_x = 20
        padding_y = 10
        spacing_x = 10
        spacing_y = 10

        Pname = StringVar()
        PAddress = StringVar()
        Pmobile = StringVar()
        passengerList = StringVar()
        Pdate = StringVar()
        FromCity = StringVar()
        ToCity = StringVar()


         # Create title label
        self.lblTit = Label(self.root, font=title_font, text="Air Nest", bg=bg_color, fg=label_color)
        self.lblTit.pack(side=TOP, padx=padding_x, pady=padding_y)

        # Create frame for passenger information
        info_frame = Frame(self.root, bg=bg_color)
        info_frame.pack(side=TOP, padx=padding_x, pady=padding_y)

        

        
        def open_calendar():
            def select_date():
                selected_date = cal.selection_get()
                Pdate.set(selected_date.strftime("%Y-%m-%d"))
                top.destroy()
            top = Toplevel(root)
            cal = Calendar(top, selectmode="day", year=datetime.datetime.now().year, month=datetime.datetime.now().month, day=datetime.datetime.now().day)
            cal.pack(padx=40,pady=40)
            Button(top, text="Select Date", command=select_date).pack()
        
        def iExit():
            iExit = tkinter.messagebox.askyesno("FBS","Confirm if you want to exit")
            if iExit > 0:
                root.destroy()
                return
        
        def clearData():
            self.txtPname.delete(0, END)
            self.txtPAddress.delete(0, END)
            self.txtPMobile.delete(0, END)
            self.txtPdate.delete(0, END)
            self.comboFromCity.set('')
            self.comboToCity.set('') 
        
        def cont():
            from_city = self.comboFromCity.get()
            to_city =  self.comboToCity.get()
            print("From City:", from_city)
            print("To City:", to_city)
            import sqlite3
            import tkinter as tk

            # Create a connection object
            conn = sqlite3.connect('flight_database.db')

            # Create a cursor object
            c = conn.cursor()

            from_city = FromCity.get()
            to_city = ToCity.get()
            date = 2Pdate.get()
            date1=date.split('-')
            date2=''
            for i in date1:
                date2=date2+i
            date2=int(date2)
            

        # Retrieve the selected flight details from the database (AND departure_date=?)(, date)
            query = "SELECT * FROM flights WHERE departure_city=? AND arrival_city=? AND departure_date=?"
            c.execute(query, (from_city, to_city, date2))
            flights = c.fetchall()

            rows = flights

            root = tk.Tk()

            # Create labels for each column in the table text=['Sl No'],['Flight Number'],['Airline'],['Departure City'],['Arrival City'],['Departure Time'],['Arrival Time'] 
            for i, column_name in enumerate(c.description):
                label = tk.Label(root,text=column_name[0] ) ###Change the table head to something fancy
                label.grid(row=0, column=i,sticky='w', padx=25, pady=10)

  


            # Define a function to handle the button click
            def select_record():
                # Get the selected item from the listbox
                selection = listbox.curselection()
                # Check if there is a selection
                if selection:
                    # Get the index of the selected item
                    index = selection[0]
                    # Get the data of the selected item
                    data = rows[index]
                    # Show a message box with the data
                    tkinter.messagebox.showinfo("Selected Flight", str(data))
                    # Return the data to the main program
                    return data
                else:
                    # Show a message box with an error message
                    tkinter.messagebox.showerror("Error", "No flight selected")
            

            # Create a listbox to display the rows of data
            listbox = tk.Listbox(root)
            listbox.grid(row=1, columnspan=8, sticky=tk.NSEW)

            # Insert each row of data into the listbox
            for row in rows:
                listbox.insert(tk.END, row)

            # Create a button to select a record
            button = tk.Button(root, text="Select", command=select_record)
            button.grid(row=2, column=1)


            # Commit changes and close the connection
            conn.commit()
            conn.close()

            # Run the Tkinter event loop
        root.mainloop()
        self.lblPname = Label(info_frame, font=label_font, text="Passenger Name:", bg=bg_color, fg=label_color)
        self.lblPname.grid(row=0, column=0, sticky=W, padx=spacing_x, pady=spacing_y)
        self.lblPname.grid(row=0, column=0, sticky=W, padx=spacing_x, pady=spacing_y)
        self.lblPname.grid(row=0, column=0, sticky=W, padx=spacing_x, pady=spacing_y)
        self.txtPname = Entry(info_frame, font=label_font, textvariable=Pname)
        self.txtPname.grid(row=0, column=1, padx=spacing_x, pady=spacing_y)
        self.lblPAddress = Label(info_frame, font=label_font, text="Passenger Address:", bg=bg_color, fg=label_color)
        self.lblPAddress.grid(row=1, column=0, sticky=W, padx=spacing_x, pady=spacing_y)
        self.txtPAddress = Entry(info_frame, font=label_font, textvariable=PAddress)
        self.txtPAddress.grid(row=1, column=1, padx=spacing_x, pady=spacing_y)
        self.lblPMobile = Label(info_frame, font=label_font, text="Passenger Mobile:", bg=bg_color, fg=label_color)
        self.lblPMobile.grid(row=2, column=0, sticky=W, padx=spacing_x, pady=spacing_y)
        self.txtPMobile = Entry(info_frame, font=label_font, textvariable=Pmobile)
        self.txtPMobile.grid(row=2, column=1, padx=spacing_x, pady=spacing_y)
        # button to clear data
        self.btnClearDate = Button(self.root, text="Clear", font=button_font, bg=button_color, fg=label_color,command=clearData)
        self.btnClearDate.pack(side=LEFT, padx=padding_x, pady=padding_y)
        # button to exit
        self.btnExit = Button(self.root, text="Exit", font=button_font, bg=button_color, fg=label_color,command=iExit)
        self.btnExit.pack(side=RIGHT, padx=padding_x, pady=padding_y)
        # button to select date
        self.lblPdate = Label(info_frame, font=label_font, text="Date:", bg=bg_color, fg=label_color)
        self.lblPdate.grid(row=3, column=0, sticky=W, padx=spacing_x, pady=spacing_y)
        self.txtPdate = Entry(info_frame, font=label_font,textvariable=Pdate)
        self.txtPdate.grid(row=3, column=1, padx=spacing_x, pady=spacing_y)
        self.btnCalendar = Button(info_frame, text="Select Date", font=button_font, bg=button_color, fg=label_color, command=open_calendar)
        self.btnCalendar.grid(row=3, column=2, padx=spacing_x, pady=spacing_y)
        # button to continue
        self.btnContinue = Button(self.root, text="Continue", font=button_font, bg=button_color, fg=label_color,command=cont)
        self.btnContinue.pack(side=LEFT, padx=padding_x, pady=padding_y)      
        self.lblFromCity = Label(info_frame, font=('Times New Roman', 14),bg=bg_color, text="From:", padx=padding_x, pady=padding_y)
        self.lblFromCity.grid(row=5, column=0, sticky=W)
        self.comboFromCity = ttk.Combobox(info_frame, font=('Times new Roman', 14), textvariable=FromCity, state="readonly", width=36)
        self.comboFromCity['values'] = ('Mumbai', 'Delhi', 'Bangalore','Chennai')
        self.comboFromCity.current()
        self.comboFromCity.grid(row=5, column=1)
        self.lblToCity = Label(info_frame, font=('Times new roman', 14), text="To:", padx=padding_x, pady=padding_y, bg=bg_color)
        self.lblToCity.grid(row=6, column=0, sticky=W)
        self.comboToCity = ttk.Combobox(info_frame, font=('times new roman', 14), textvariable=ToCity, state="readonly", width=36)
        self.comboToCity['values'] = ('Mumbai', 'Delhi', 'Bangalore','Chennai')
        self.comboToCity.current()
        self.comboToCity.grid(row=6, column=1)
if __name__ == '__main__':
    root = Tk()
    application = Passenger(root)
    root.mainloop()


