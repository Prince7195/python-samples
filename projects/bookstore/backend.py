import sqlite3

def connect():
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    con.commit()
    con.close()

def viewAll():
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    con.close()
    return rows

def insert(title, author, year, isbn):
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    con.commit()
    con.close()

def search(title="", author="", year="", isbn=""):
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    con.close()
    return rows

def delete(id):
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (id,))
    con.commit()
    con.close()

def update(id, title, author, year, isbn):
    con = sqlite3.connect("store.db")
    cur = con.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    con.commit()
    con.close()


connect()
# insert("Lillyputs", "Vijay", 2001, 2323)
# insert("The sea", "John", 2011, 233223)
# insert("The Earth", "Deo", 2013, 2334223)
# insert("The Sun", "Smith", 2003, 755623)
# insert("The Moon", "Smith", 2003, 755623)
# update(5, "The Moon", "Smith John", 2008, 335623)
# delete(3)
# print(viewAll())
# print(search(author="Deo"))