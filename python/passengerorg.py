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
        self.root.geometry("800x600")
        self.root.config(bg="light gray")

        # Load and display background image
        bg_image = Image.open("background.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        bg_label = Label(self.root, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg_photo

        # Define colors
        bg_color = "light gray"
        label_color = "white"
        button_color = "steel blue"

        # Define fonts
        title_font = ("Arial", 30, "bold")
        label_font = ("Arial", 14)
        button_font = ("Arial", 14, "bold")

        # Define padding and spacing
        padding_x = 20
        padding_y = 10
        spacing_x = 10
        spacing_y = 10

        # Create title label
        self.lblTit = Label(self.root, font=title_font, text="Air Nest", bg=bg_color, fg=label_color)
        self.lblTit.pack(side=TOP, padx=padding_x, pady=padding_y)

        # Create frame for passenger information
        info_frame = Frame(self.root, bg=bg_color)
        info_frame.pack(side=TOP, padx=padding_x, pady=padding_y)

        # Create labels and entry fields for passenger information
        self.lblPname = Label(info_frame, font=label_font, text="Passenger Name:", bg=bg_color, fg=label_color)
        self.lblPname.grid(row=0, column=0, sticky=W, padx=spacing_x, pady=spacing_y)
        self.txtPname = Entry(info_frame, font=label_font)
        self.txtPname.grid(row=0, column=1, padx=spacing_x, pady=spacing_y)

        self.lblPAddress = Label(info_frame, font=label_font, text="Passenger Address:", bg=bg_color, fg=label_color)
        self.lblPAddress.grid(row=1, column=0, sticky=W, padx=spacing_x, pady=spacing_y)
        self.txtPAddress = Entry(info_frame, font=label_font)
        self.txtPAddress.grid(row=1, column=1, padx=spacing_x, pady=spacing_y)

        self.lblPMobile = Label(info_frame, font=label_font, text="Passenger Mobile:", bg=bg_color, fg=label_color)
        self.lblPMobile.grid(row=2, column=0, sticky=W, padx=spacing_x, pady=spacing_y)
        self.txtPMobile = Entry(info_frame, font=label_font)
        self.txtPMobile.grid(row=2, column=1, padx=spacing_x, pady=spacing_y)

        # Create button to select date
        self.lblPdate = Label(info_frame, font=label_font, text="Date:", bg=bg_color, fg=label_color)
        self.lblPdate.grid(row=3, column=0, sticky=W, padx=spacing_x, pady=spacing_y)
        self.txtPdate = Entry(info_frame, font=label_font)
        self.txtPdate.grid(row=3, column=1, padx=spacing_x, pady=spacing_y)
        self.btnCalendar = Button(info_frame, text="Select Date", font=button_font, bg=button_color, fg=label_color)
        self.btnCalendar.grid(row=3, column=2, padx=spacing_x, pady=spacing_y)

        # Create button to continue
        self.btnContinue = Button(self.root, text="Continue", font=button_font, bg=button_color, fg=label_color)
        self.btnContinue.pack(side=LEFT, padx=padding_x, pady=padding_y)

        # Create button to clear data
        self.btnClearDate = Button(self.root, text="Clear", font=button_font, bg=button_color, fg=label_color)
        self.btnClearDate.pack(side=LEFT, padx=padding_x, pady=padding_y)

        # Create button to exit
        self.btnExit = Button(self.root, text="Exit", font=button_font, bg=button_color, fg=label_color)
        self.btnExit.pack(side=RIGHT, padx=padding_x, pady=padding_y)


if __name__ == '__main__':
    root = Tk()
    application = Passenger(root)
    root.mainloop()
