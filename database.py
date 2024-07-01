import sqlite3

def setup_database():
    """
    Sets up the SQLite database and creates a 'weather' table if it doesn't exist.
    """
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            weather_data TEXT
        )
    ''')
    conn.commit()
    conn.close()

def store_weather_data(city_name, weather_data):
    """
    Stores weather data for a specific city in the 'weather' table.

    Args:
        city_name (str): Name of the city.
        weather_data (dict): Weather data to store in JSON format.
    """
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('INSERT INTO weather (city, weather_data) VALUES (?, ?)', (city_name, str(weather_data)))
    conn.commit()
    conn.close()

def fetch_weather_data_from_db(city_name):
    """
    Fetches weather data for a specific city from the 'weather' table.

    Args:
        city_name (str): Name of the city.

    Returns:
        dict: Weather data fetched from the database.
    """
    conn = sqlite3.connect('weather_data.db')
    c = conn.cursor()
    c.execute('SELECT weather_data FROM weather WHERE city=?', (city_name,))
    row = c.fetchone()
    conn.close()

    if row:
        return eval(row[0])  # Convert string representation of dictionary back to dictionary
    else:
        return None
