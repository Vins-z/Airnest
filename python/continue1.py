import tkinter as tk
from tkinter import *
import tkinter.messagebox
import datetime
import sqlite3
def __init__(self, root):
    self.conn = sqlite3.connect('flight_data.db')
    self.c = self.conn.cursor()
    def cont():
        from_city = FromCity.get()
        to_city = ToCity.get()
        date = Pdate.get()

    # Retrieve the selected flight details from the database (AND departure_date=?)(, date)
        query = "SELECT * FROM flights WHERE departure_city=? AND arrival_city=?"
        self.c.execute(query, (from_city, to_city))
        flights = self.c.fetchall()

    # Create a new window to display the flight list
    flight_window = Toplevel(root)
    flight_window.title("Flight Selection")
    flight_window.geometry("600x400")

    if len(flights) == 0:
        # Display message if no flights are available
        message_label = Label(flight_window, text="No flights available for the selected date.", font=('Arial', 14))
        message_label.pack(pady=20)
    else:
        # Create a listbox to display the flight details
        flight_listbox = Listbox(flight_window, font=('Arial', 12), width=70)
        flight_listbox.pack(pady=10)

        # Display the flight details in the listbox
        for flight in flights:
            flight_info = f"Flight Number: {flight[1]}\nAirline: {flight[2]}\nDeparture Time: {flight[5]}\nArrival Time: {flight[6]}"
            flight_listbox.insert(END, flight_info)

        def select_flight():
            selected_flight = flight_listbox.get(flight_listbox.curselection())
            print("Selected Flight:")
            print(selected_flight)

        select_button = Button(flight_window, text="Select Flight", font=('Arial', 14), command=select_flight)
        select_button.pack(pady=10)

    def close_flight_window():
        flight_window.destroy()

    close_button = Button(flight_window, text="Close", font=('Arial', 14), command=close_flight_window)
    close_button.pack(pady=10)