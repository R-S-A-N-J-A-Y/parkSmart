from flask import Flask, render_template, jsonify, request  # Import request
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Function to get database connection
def get_db_connection():
    conn = sqlite3.connect('parking_system.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create the parking data table (run once)
def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS parking_data')  # Drop the table if it exists
    cursor.execute('''CREATE TABLE parking_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        parking_space TEXT NOT NULL,
        slots_filled INTEGER NOT NULL,
        total_slots INTEGER NOT NULL,
        date TEXT NOT NULL,
        location TEXT NOT NULL  -- New location column
    )''')
    conn.commit()
    conn.close()

# Insert data for parking spaces with locations (run once)
def insert_parking_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM parking_data WHERE date = DATE('now')''')  # Clear existing data for today
    cursor.execute('''INSERT INTO parking_data (parking_space, slots_filled, total_slots, date, location)
        VALUES
            ('A', 10, 20, DATE('now'), 'singanallur'),  -- Parking A in Singanallur
            ('B', 20, 20, DATE('now'), 'singanallur'),  -- Parking B in Singanallur
            ('C', 5, 20, DATE('now'), 'sulur'),         -- Parking C in Sulur
            ('D', 10, 15, DATE('now'), 'sulur'),         -- Parking D in Sulur
            ('E', 3, 15, DATE('now'), 'singanallur')         -- Parking E in singanallur
    ''')
    conn.commit()
    conn.close()

# Route to display parking availability
@app.route('/')
def index():
    location = request.args.get('location')  # Get location from query parameter
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if location:
        cursor.execute('SELECT parking_space, slots_filled, total_slots FROM parking_data WHERE date = DATE("now") AND location = ?', (location,))
    else:
        cursor.execute('SELECT parking_space, slots_filled, total_slots FROM parking_data WHERE date = DATE("now")')
    
    parking_data = cursor.fetchall()
    conn.close()
    
    # Get today's date
    from datetime import datetime
    today_date = datetime.now().strftime('%Y-%m-%d')
    
    return render_template('index.html', parking_data=parking_data, date=today_date)

# API to fetch data (for front-end JavaScript if needed)
@app.route('/api/parking')
def get_parking_data():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT DISTINCT parking_space, slots_filled, total_slots FROM parking_data WHERE date = DATE("now")')
    parking_data = cursor.fetchall()
    conn.close()

    # Return the data as a JSON response
    return jsonify([dict(row) for row in parking_data])

if __name__ == '__main__':
    create_table()  # Create the table on the first run
    insert_parking_data()  # Insert data for A, B, C, and D parking (run once)
    app.run(debug=True)
