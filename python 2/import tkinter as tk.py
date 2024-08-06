import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar

def get_selected_date():
    date = cal.get_date()
    selected_date.set(date)
    root.destroy()

root = tk.Tk()
root.title("Date Selection")

selected_date = tk.StringVar()

cal = Calendar(root, selectmode="day")
cal.pack()

ok_button = ttk.Button(root, text="OK", command=get_selected_date)
ok_button.pack()

root.mainloop()

date_variable = selected_date.get()
print("Selected date:", date_variable)
