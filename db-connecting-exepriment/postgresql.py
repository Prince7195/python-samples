import psycopg2

dbConnection = "dbname='postgresdb' user='postgres' password='postgres' host='localhost' port='5432'"

def create_table():
    con = psycopg2.connect(dbConnection)
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    con.commit()
    con.close()

def insert(item, quantity, price):
    con = psycopg2.connect(dbConnection)
    cur = con.cursor()
    cur.execute("INSERT INTO store VALUES(%s, %s, %s)", (item, quantity, price))
    con.commit()
    con.close()

def view():
    con = psycopg2.connect(dbConnection)
    cur = con.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    con.close()
    return rows

def delete(item):
    con = psycopg2.connect(dbConnection)
    cur = con.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    con.commit()
    con.close()

def update(item, quantity, price):
    con = psycopg2.connect(dbConnection)
    cur = con.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s where item=%s", (quantity, price, item))
    con.commit()
    con.close()

# create_table()

# insert("Whine glass", 8, 10.5)
# insert("Water glass", 10, 8.5)
# insert("Tea glass", 20, 5.5)
# insert("Coffee cup", 30, 6.5)

# delete("Coffee cup")

# update("Water glass", 20, 18.5)

print(view())