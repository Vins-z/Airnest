# Import tkinter and sqlite3 modules
from tkinter import *
import sqlite3
# Connect to the database
conn = sqlite3.connect('flight_data.db')
cursor = conn.cursor()

# Fetch data from the user table
cursor.execute("select * from Flights")
rows = cursor.fetchall()

# Close the connection
cursor.close()
conn.close()

# Create a root window
root = Tk()
root.title("Database column records to tkinter labels")
root.geometry("300x200")

# Create a label frame to hold the labels
lf = LabelFrame(root, text="Alignment")
lf.pack(padx=20, pady=20)

# Create a listbox to display the row indices
lb = Listbox(lf)
lb.pack(side=LEFT, fill=Y)

# Loop through the rows and create labels for each column value
i = 0 # row index
for row in rows:
    j = 0 # column index
    for value in row:
        # Create a label with the value
        label = Label(lf, text=value, borderwidth=2, relief="ridge", anchor="w")
        # Place the label on the label frame using grid layout
        label.grid(row=i, column=j+1, ipadx=10, ipady=10)
        # Increment the column index
        j += 1
    # Insert the row index to the listbox
    lb.insert(END, i)
    # Increment the row index
    i += 1

# Create a button to select a row
def select_row():
    # Get the selected row index from the listbox
    index = lb.curselection()[0]
    # Print the selected row values
    print(rows[index])

btn = Button(root, text="Select", command=select_row)
btn.pack()

# Start the main loop
root.mainloop()
