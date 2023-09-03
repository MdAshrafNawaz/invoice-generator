import tkinter
from tkinter import ttk
from docxtpl import DocxTemplate
import datetime

def clear_data():
    firstname = Firstname_entry.get()
    lastname = Lastname_entry.get()
    phone_number = phone_number_entry.get()
    quantity = float(quantity_spinbox.get())
    product = product_entry.get()
    unit = float(unit_spinbox.get())
    price = unit * quantity
    product_index = [quantity, product, unit, price]
    list_frame.insert('', 0, values=product_index)
    print(product_index)
def enter_data():
    firstname = Firstname_entry.get()
    lastname = Lastname_entry.get()
    phone_number =phone_number_entry.get()
    quantity =float(quantity_spinbox.get())
    product = product_entry.get()
    unit = float(unit_spinbox.get())
    price=unit*quantity
    product_index=[quantity,product,unit,price]
    list_frame.insert('',0,values=product_index)


def print_data():
    doc = DocxTemplate('somefile.docx')
    name = Firstname_entry.get() + Lastname_entry.get()
    number = phone_number_entry.get()
    doc_name="new invoice"+name+datetime.datetime.now().strftime("%y-%m-%d-%H-%M-%S")+".docx"
    doc.save(doc_name)
    return
def enter_new_data():
    return


window=tkinter.Tk()
window.title("Invoice")
window.geometry('500x300')

frame=tkinter.Frame(window)
frame.pack()

UserInfoFrame =tkinter.LabelFrame(frame,text="information grid")   #user info section parent box
UserInfoFrame.grid(row=0,column=0,sticky="news")

Firstname =tkinter.Label(UserInfoFrame,text="first name:")
Firstname.grid(row=0,column=0)
Firstname_entry=tkinter.Entry(UserInfoFrame)
Firstname_entry.grid(row=1,column=0)

Lastname =tkinter.Label(UserInfoFrame,text="last name:")
Lastname.grid(row=0,column=1)
Lastname_entry=tkinter.Entry(UserInfoFrame)
Lastname_entry.grid(row=1,column=1)

phone_number=tkinter.Label(UserInfoFrame,text="number:")
phone_number.grid(row=0,column=2)
phone_number_entry=tkinter.Entry(UserInfoFrame)
phone_number_entry.grid(row=1,column=2)

quantity=tkinter.Label(UserInfoFrame,text="quantity:")
quantity.grid(row=2,column=0)
quantity_spinbox=tkinter.Spinbox(UserInfoFrame,from_=1,to=200)     #limited option up down
quantity_spinbox.grid(row=3,column=0)

product =tkinter.Label(UserInfoFrame,text="product:")
product.grid(row=2,column=1)
product_entry=tkinter.Entry(UserInfoFrame)
product_entry.grid(row=3,column=1)

unit=tkinter.Label(UserInfoFrame,text="unit price:")
unit.grid(row=2,column=2)
unit_spinbox=tkinter.Spinbox(UserInfoFrame,from_=1,to=200)        #limited option up down
unit_spinbox.grid(row=3,column=2)

for widget in UserInfoFrame.winfo_children():
    widget.grid_configure(padx=30,pady=2,sticky="news")


columns=('quantity','product','Unit price','price')
list_frame=ttk.Treeview(frame,columns=columns,show='headings', height=5)
list_frame.grid(row=1, column=0,columnspan=2,  padx=10, pady=5)
scrollbar = ttk.Scrollbar(frame, orient='vertical')
scrollbar.grid(row=1, column=3, sticky="NS")
list_frame.heading('quantity',text="quantity")
list_frame.heading('product',text="product")
list_frame.heading('price',text="price")
list_frame.heading('Unit price',text="Unit price")

for widget in list_frame.winfo_children():
    widget.grid_configure(padx=10,pady=2,sticky="news")

Next_item_button=tkinter.Button(frame,text="next item",command=enter_data)
Next_item_button.grid(row=3,column=0,sticky="news",padx=10,pady=5)

save_button=tkinter.Button(frame,text="invoice",command=print_data)
save_button.grid(row=4,column=0,sticky="news",padx=10,pady=5)

new_button=tkinter.Button(frame,text="new",command=enter_new_data)
new_button.grid(row=5,column=0,sticky="news",padx=10,pady=5)

window.mainloop()