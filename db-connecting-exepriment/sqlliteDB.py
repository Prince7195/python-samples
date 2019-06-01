import sqlite3

def create_table():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    con.commit()
    con.close()

def insert(item, quantity, price):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quantity, price))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    con.close()
    return rows

def delete(item):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    con.commit()
    con.close()

def update(item, quantity, price):
    con = sqlite3.connect("lite.db")
    cur = con.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? where item=?", (quantity, price, item))
    con.commit()
    con.close()

# insert("Whine glass", 8, 10.5)
# insert("Water glass", 10, 8.5)
# insert("Tea glass", 20, 5.5)

# delete("Coffee cup")

# update("Water glass", 20, 18.5)

print(view())