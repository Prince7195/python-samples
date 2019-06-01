import sqlite3

class Database:

    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTs books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        self.con.commit()

    def viewAll(self):
        self.cur.execute("SELECT * FROM books")
        rows = self.cur.fetchall()
        return rows

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.con.commit()

    def search(self, title="", author="", year="", isbn=""):
        self.cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM books WHERE id=?", (id,))
        self.con.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.con.commit()

    def __del__(self):
        self.con.close()



# insert("Lillyputs", "Vijay", 2001, 2323)
# insert("The sea", "John", 2011, 233223)
# insert("The Earth", "Deo", 2013, 2334223)
# insert("The Sun", "Smith", 2003, 755623)
# insert("The Moon", "Smith", 2003, 755623)
# update(5, "The Moon", "Smith John", 2008, 335623)
# delete(3)
# print(viewAll())
# print(search(author="Deo"))