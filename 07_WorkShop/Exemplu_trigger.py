import sqlite3
# conexiune baza de date
connection = sqlite3.connect("mydb4.db")
cursor = connection.cursor()


## Create the cities table
#cursor.execute("""
#CREATE TABLE cities (
#    city_id INTEGER PRIMARY KEY,
#    city_name TEXT NOT NULL,
#    country_code VARCHAR(10) NOT NULL,
#    population BIGINT
#)
#""")
#
# Insert sample data into cities
cursor.executemany("""
INSERT INTO cities (city_name, country_code, population) VALUES (?, ?, ?)
""", [
    ('New York', 'US', 8175133),
    ('Los Angeles', 'US', 3792621),
    ('London', 'UK', 8787892),
    ('Tokyo', 'JP', 13751500)
])

# Create the history_cities table
#cursor.execute("""
#CREATE TABLE history_cities (
#    history_id INTEGER PRIMARY KEY,
#    city_id INTEGER,
#    city_name TEXT,
#    country_code VARCHAR(10),
#    population BIGINT,
#    deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#)
#""")
#
# Create the trigger for the cities table
cursor.execute("""
CREATE TRIGGER trigger_log_city_deletion 
AFTER DELETE ON cities 
BEGIN 
    INSERT INTO history_cities (city_id, city_name, country_code, population) 
    VALUES (OLD.city_id, OLD.city_name, OLD.country_code, OLD.population); 
END;
""")

# Commit the transactions
connection.commit()


city_to_delete = 'New York'
cursor.execute("DELETE FROM cities WHERE city_name = ?", (city_to_delete,))


cursor.execute("SELECT * FROM history_cities")
rows = cursor.fetchall()

print("\nHistory Cities Table Content:")
print("-------------------------------")
for row in rows:
    print(row)
