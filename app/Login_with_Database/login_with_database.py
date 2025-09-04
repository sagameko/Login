import sqlite3

# Create connection

conn = sqlite3.connect("user.db")
c = conn.cursor()

#Create table
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          username TEXT UNIQUE,
          password TEXT
    )          
''')


#Add a demo account
c.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?,?)", ("admin","1234"))

conn.commit()
conn.close()

