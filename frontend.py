from tkinter import *
import backend

window = Tk()
window.title("Book Store Managing")
window.geometry("500x300")

# ------------------- Labels -------------------
book_name_label = Label(window, text="book name: ")
book_name_label.grid(row=0, column=0)

author_label = Label(window, text="author: ")
author_label.grid(row=0, column=2)

publication_name_label = Label(window, text="publication: ")
publication_name_label.grid(row=1, column=0)

score_name_label = Label(window, text="score: ")
score_name_label.grid(row=1, column=2)
# ------------------- Entries -------------------
book_name_string = StringVar()
author_string = StringVar()
publication_string = StringVar()
score_integer = IntVar()

book_name_entry = Entry(window, textvariable=book_name_string)
book_name_entry.grid(row=0, column=1)

author_entry = Entry(window, textvariable=author_string)
author_entry.grid(row=0, column=3)

publication_entry = Entry(window, textvariable=publication_string)
publication_entry.grid(row=1, column=1)

score_entry = Entry(window, textvariable=score_integer)
score_entry.grid(row=1, column=3)


# ------------------- ListBox -------------------
def show_book_in_entries(event):
    index = listbox.curselection()

    selected_book = listbox.get(index)

    book_name_entry.delete(0, END)
    book_name_entry.insert(END, selected_book[1])

    author_entry.delete(0, END)
    author_entry.insert(END, selected_book[2])

    publication_entry.delete(0, END)
    publication_entry.insert(END, selected_book[3])

    score_entry.delete(0, END)
    score_entry.insert(END, selected_book[4])


listbox = Listbox(window, width=45, height=15)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2, pady=4, padx=4)
listbox.bind("<<ListboxSelect>>", show_book_in_entries)

# ------------------- Buttons -------------------
viewAllButton = Button(window, text="view all", width=9, bg="cyan", command=lambda: view_command())
viewAllButton.grid(row=2, column=2)

searchButton = Button(window, text="search", width=9, bg="cyan", command=lambda: search_command())
searchButton.grid(row=3, column=2)

addButton = Button(window, text="add", width=9, bg="cyan", command=lambda: add_command())
addButton.grid(row=4, column=2)

deleteButton = Button(window, text="delete", width=9, bg="cyan", command=lambda: delete_command())
deleteButton.grid(row=5, column=2)

closeButton = Button(window, text="close", width=9, bg="red", command=window.destroy)
closeButton.grid(row=6, column=2)


# ------------------- Functions -------------------
def view_command():
    listbox.delete(0, END)
    books = backend.view_all()
    for book in books:
        listbox.insert(END, book)


def add_command():
    backend.add(book_name_string.get(), author_string.get(), publication_string.get(), score_integer.get())
    view_command()


def delete_command():
    if len(listbox.curselection()) == 0:
        return

    selected_book = listbox.get(listbox.curselection())
    backend.delete(selected_book[1])
    view_command()


def search_command():
    listbox.delete(0, END)
    found_books = backend.search(book_name_string.get(), author_string.get(), publication_string.get(),
                                 score_integer.get())

    for book in found_books:
        listbox.insert(END, book)


window.mainloop()
