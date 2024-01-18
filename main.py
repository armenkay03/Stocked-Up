from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
from random import randint

bgColor = "#C7C7CC"
title ="Stocked Up"
size = "725x315"

def randomNumber():
    number = randint(0, 100)
    if number < 25:
        return "Out of Stock"
    else:
        return number

root = Tk()
root.title(title)
root.geometry(size)
root.configure(background=bgColor)

table = ttk.Treeview(root)
table['columns'] = ('Name', 'Price', 'Dummy')
table.column('#0', width=0, stretch=NO)
table.column('Name', anchor=CENTER, width=400)
table.column('Price', anchor=CENTER, width=150)
table.column('Dummy', anchor=CENTER, width=150)
table.heading('#0', text='', anchor=CENTER)
table.heading('Name', text='Name', anchor=CENTER)
table.heading('Price', text='Price', anchor=CENTER)
table.heading('Dummy', text='Stock', anchor=CENTER)
ttk.Style().configure("Treeview",
                    background=bgColor,
                    foreground="blue",
                    fieldbackground=bgColor)
totList = {}
index = 0
table.grid(row=2, column=0, columnspan=10, pady=5, padx=10)
varInput = Entry(root, width=30, background=bgColor, borderwidth=3)
varInput.grid(row=0, column=0, pady=10)


def delRes():
    varInput.delete(0, END)
    table.delete(*table.get_children())
    totList.clear()


def clicked():

    inputed = varInput.get()

    webpage = requests.get(
        "https://www.spinneyslebanon.com/catalogsearch/result/?q=" +
        str(inputed))
    soup = BeautifulSoup(webpage.content, "html.parser")
    title = soup.find_all("a", "product-item-link")
    price = soup.find_all("span", class_="price")

    for index, tp in enumerate(zip(title, price)):
        if index >= 20:
            break
        totList[tp[0].get_text(strip=True)] = tp[1].get_text(strip=True)

    for i in totList:
        price = totList.get(i)
        table.insert(parent='',
                index=index,
                iid=index,
                text='',
                values=(i, price, randomNumber()))
        index += 1


btn_enter = Button(root, text="Enter", command=clicked)
btn_enter.grid(row=0, column=1, ipadx=30, ipady=4)
btn_delete = Button(root, text="Delete", command=delRes)
btn_delete.grid(row=0, column=2, ipadx=30, ipady=4)
root.mainloop()
