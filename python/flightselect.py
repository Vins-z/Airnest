import sqlite3
import tkinter as tk
import tkinter.messagebox as mb

# Create a connection object
conn = sqlite3.connect('flight_database.db')

# Create a cursor object
c = conn.cursor()

# Execute a SELECT statement
c.execute("SELECT * FROM Flights")

# Fetch all rows of the executed statement
rows = c.fetchall()

# Create a Tkinter window
root = tk.Tk()

# Create labels for each column in the table
for i, column_name in enumerate(c.description):
    label = tk.Label(root, text=column_name[0])
    label.grid(row=0, column=i,sticky='w', padx=10, pady=5)

# Create labels for each row of data in the table
for i, row in enumerate(rows):
    for j, value in enumerate(row):
        label = tk.Label(root, text=value)
        label.grid(row=i+1, column=j,sticky='w', padx=10, pady=5)


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
        mb.showinfo("Selected Record", str(data))
        # Return the data to the main program
        return data
    else:
        # Show a message box with an error message
        mb.showerror("Error", "No record selected")

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