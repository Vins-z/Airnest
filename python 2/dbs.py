import sqlite3

# Connect to the database or create a new one if it doesn't exist
conn = sqlite3.connect('flight_database.db')
c = conn.cursor()

# Create a flights table
c.execute('''CREATE TABLE IF NOT EXISTS flights (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flight_number TEXT,
    airline TEXT,
    departure_city TEXT,
    arrival_city TEXT,
    departure_time TEXT,
    arrival_time TEXT
)''')

# Insert flight data into the table
flights = [
    ('AI101', 'Air India', 'Delhi', 'Mumbai', '08:00', '10:00'),
    ('6E202', 'IndiGo', 'Delhi', 'Mumbai', '10:30', '12:30'),
    ('SG702', 'SpiceJet', 'Delhi', 'Bangalore', '09:00', '11:00'),
    ('AI502', 'Air India', 'Mumbai', 'Delhi', '08:30', '10:30'),
    ('6E303', 'IndiGo', 'Mumbai', 'Delhi', '11:00', '13:00'),
    ('SG803', 'SpiceJet', 'Mumbai', 'Bangalore', '12:00', '14:00'),
    ('AI903', 'Air India', 'Bangalore', 'Delhi', '09:30', '11:30'),
    ('6E404', 'IndiGo', 'Bangalore', 'Delhi', '11:30', '13:30'),
    ('SG905', 'SpiceJet', 'Bangalore', 'Mumbai', '10:00', '12:00')
]

c.executemany("INSERT INTO flights (flight_number, airline, departure_city, arrival_city, departure_time, arrival_time) VALUES (?, ?, ?, ?, ?, ?)", flights)

# Commit the changes and close the connection
conn.commit()
conn.close()
