import sqlite3

# Establish a connection to the SQLite database file
conn = sqlite3.connect('flight_database.db')
cursor = conn.cursor()

# Create Airports table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Airports (
  airport_id INTEGER PRIMARY KEY,
  airport_name TEXT,
  city TEXT
)
''')

# Create Flights table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Flights (
  flight_id INTEGER PRIMARY KEY,
  airline_name TEXT,
  source_airport_id INTEGER,
  destination_airport_id INTEGER,
  departure_time TEXT,
  arrival_time TEXT,
  duration INTEGER,
  price REAL,
  FOREIGN KEY (source_airport_id) REFERENCES Airports(airport_id),
  FOREIGN KEY (destination_airport_id) REFERENCES Airports(airport_id)
)
''')

# Insert the flight data
cursor.executemany('''
INSERT INTO Flights (flight_id, airline_name, source_airport_id, destination_airport_id, departure_time, arrival_time, duration, price)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
''', [
  (1, 'Air India', 1, 2, '2023-05-31 08:00:00', '2023-05-31 10:30:00', 150, 200.00),
  (2, 'Indigo', 1, 2, '2023-05-31 10:30:00', '2023-05-31 12:00:00', 90, 150.00),
  (3, 'SpiceJet', 1, 3, '2023-05-31 14:00:00', '2023-05-31 16:30:00', 150, 250.00),
  (4, 'Vistara', 2, 1, '2023-05-31 09:30:00', '2023-05-31 11:00:00', 90, 180.00),
  (5, 'Air India', 2, 3, '2023-05-31 12:30:00', '2023-05-31 15:00:00', 150, 200.00),
  (6, 'Indigo', 2, 4, '2023-05-31 16:00:00', '2023-05-31 18:30:00', 150, 220.00),
  (7, 'SpiceJet', 3, 1, '2023-05-31 13:30:00', '2023-05-31 16:00:00', 150, 260.00),
  (8, 'Vistara', 3, 2, '2023-05-31 17:00:00', '2023-05-31 19:30:00', 150, 190.00),
  (9, 'Air India', 3, 4, '2023-05-31 20:00:00', '2023-05-31 22:30:00', 150, 230.00),
  (10, 'Indigo', 4, 1, '2023-05-31 10:00:00', '2023-05-31 12:30:00', 150, 180.00),
  (11, 'SpiceJet', 4, 2, '2023-05-31 13:00:00', '2023-05-31 15:30:00', 150, 250.00);

  # Insert additional flights here
])

# Commit the changes and close the connection
conn.commit()
conn.close()
