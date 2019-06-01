from tkinter import *
import backend

def get_selected_item(event):
    global selected_tuple
    index=list1.curselection()[0]
    selected_tuple=list1.get(index)
    # setting value type 1
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    # setting value type 2
    year_text.set(selected_tuple[3])
    ISBN_text.set(selected_tuple[4])

def view_cmd():
    list1.delete(0, END)
    for item in backend.viewAll():
        list1.insert(END, item)

def search():
    list1.delete(0, END)
    for item in backend.search(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get()):
        list1.insert(END, item)

def add_book():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), ISBN_text.get())
    view_cmd()
    title_text.set("")
    author_text.set("")
    year_text.set("")
    ISBN_text.set("")

def delete():
    backend.delete(selected_tuple[0])
    view_cmd()

def update():
    backend.update(selected_tuple[0], selected_tuple[1], selected_tuple[2], selected_tuple[3], selected_tuple[4])
    view_cmd()


window = Tk()
window.wm_title("Book Store")

# Label creations
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# Input box creations
title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window, textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(row=1,column=1)

ISBN_text=StringVar()
e4=Entry(window, textvariable=ISBN_text)
e4.grid(row=1,column=3)

# list box creation
list1=Listbox(window, height=6,width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

# scrollbar creation
sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

# scrollbar configuring with listbox
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# adding function to the list item on select
list1.bind("<<ListboxSelect>>", get_selected_item)

# Button creations
b1=Button(window,text="View All", width=12, command=view_cmd)
b1.grid(row=2,column=3)

b2=Button(window,text="Search entry", width=12, command=search)
b2.grid(row=3,column=3)

b3=Button(window,text="Add entry", width=12, command=add_book)
b3.grid(row=4,column=3)

b4=Button(window,text="Update entry", width=12, command=update)
b4.grid(row=5,column=3)

b5=Button(window,text="Delete selected", width=12, command=delete)
b5.grid(row=6,column=3)

b6=Button(window,text="Close", width=12, command=window.destroy)
b6.grid(row=7,column=3)

window.mainloop()