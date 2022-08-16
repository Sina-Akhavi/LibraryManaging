import sqlite3
import tkinter.messagebox


def connect():
    connection = sqlite3.connect("book_database2.db")
    curser = connection.cursor()

    curser.execute(
        "CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY ,bookName VARCHAR(40), author VARCHAR(40), publication VARCHAR(40), score INTEGER)")

    connection.commit()
    connection.close()


def add(bookname, author, publication, score):
    if len(bookname) == 0:
        tkinter.messagebox.showerror("ERROR", "book name cannot be empty!!!")
        return
    connection = sqlite3.connect("book_database2.db")
    curser = connection.cursor()

    curser.execute("SELECT * FROM books WHERE bookname = ?", (bookname,))
    if (len(curser.fetchall()) != 0):
        tkinter.messagebox.showerror("ERROR", "The book has already added!!")
        connection.close()
    else:
        curser.execute("INSERT INTO books VALUES (NULL, ?, ?, ?, ?)", (bookname, author, publication, score))
        connection.commit()
        connection.close()


def view_all():
    connection = sqlite3.connect("book_database2.db")
    curser = connection.cursor()

    curser.execute("SELECT * FROM books")

    all_books = curser.fetchall()
    connection.close()

    return all_books


def delete(bookname):
    connection = sqlite3.connect("book_database2.db")
    curser = connection.cursor()

    curser.execute("DELETE FROM books WHERE bookname=?", (bookname,))
    connection.commit()
    connection.close()


def search(bookName="", author="", publication="", score=0):
    connection = sqlite3.connect("book_database2.db")
    curser = connection.cursor()

    curser.execute("SELECT * FROM books WHERE bookName=? OR author=? OR publication=? OR score=?"
                   , (bookName, author, publication, score))
    found_books = curser.fetchall()
    connection.close()

    return found_books


connect()

# add("life", "Jack London", "aftab", 80)
# add("MR Key", "moori", "Aftab", 70)
# foundBooks = search(author="Aghata Christie")
