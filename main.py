from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb
from tkcalendar import DateEntry
import datetime
from db import Database


db = Database("Student.db")
# Creating the universal font variables
hfont = ("Noto Sans CJK TC", 15, 'bold')
lfont = ('Garamond', 14)
efont = ('Garamond', 12)
# Creating the background and foreground color variables
h_bg = '#456268'  # bg color for the header
sh_bg = '#3aa6b9'  # bg color for the Sub_header
lf_bg = '#99bdff'  # bg color for the left_frame
cf_bg = '#12e6f6'  # bg color for the center_frame
# Initializing the GUI window
main = Tk()
main.title('Student Records Management')
main.geometry('1330x690+10+1')
main.resizable(0, 0)
main.state("zoomed")
main.config(bg="black")
# Creating the StringVar or IntVar variables
name = StringVar()
rno = StringVar()
std = StringVar()
contact = StringVar()
email = StringVar()
gender = StringVar()
dob = StringVar()
address = StringVar()
dist = StringVar()
pin = StringVar()
fname = StringVar()
mname = StringVar()
focc = StringVar()
mocc = StringVar()
fcno = StringVar()
mcno = StringVar()
pemail = StringVar()
#frames
frame_1 = Frame(main, bg=lf_bg, bd=4, relief=GROOVE)
frame_1.place(x=1.5, y=31, relheight=0.956, relwidth=0.27)

frame_2 = Frame(main, bg=sh_bg, bd=4, relief=GROOVE)
frame_2.place(x=362, y=31, relheight=0.956, relwidth=0.325)

frame_3 = Frame(main, bd=3, relief=GROOVE)
frame_3.place(relx=0.591, y=30, relheight=0.556, relwidth=0.409)

frame_4 = Frame(main, bg=cf_bg, bd=4, relief=GROOVE)
frame_4.place(relx=0.591, y=445, relheight=0.4, relwidth=0.408)
# Placing the components in the main window
Label(main, text=" STUDENTS RECORDS MANAGEMENT SYSTEM ", font=hfont,bg=h_bg, fg='#bffa38').pack(side=TOP, fill=X)
Label(frame_1, text="Student Details", font=hfont,bg=h_bg, fg='#b1d13e').pack(side=TOP, fill=X)
Label(frame_2, text="Parents Details", font=hfont,bg=h_bg, fg='#b1d13e').pack(side=TOP, fill=X)
Label(frame_3, text='Students Records', font=hfont,bg=sh_bg, fg='#f31159').pack(side=TOP, fill=X)
#msg
Label(frame_2, text="*If you have no value to input,You can use 'Nill'",
      font=('times', 15, 'italic'), bg=sh_bg, fg="red").place(relx=0.04, rely=0.77)
# Placing components in the first frame names
Label(frame_1, text="Name :", font=lfont, bg=lf_bg).place(relx=0.06, rely=0.06)
Label(frame_1, text="Roll No :", font=lfont,bg=lf_bg).place(relx=0.06, rely=0.14)
Label(frame_1, text="Standard :", font=lfont,bg=lf_bg).place(relx=0.06, rely=0.22)
Label(frame_1, text="Contact No :", font=lfont,bg=lf_bg).place(relx=0.06, rely=0.30)
Label(frame_1, text="Email :", font=lfont,bg=lf_bg).place(relx=0.06, rely=0.38)
Label(frame_1, text="Gender :", font=lfont,bg=lf_bg).place(relx=0.06, rely=0.46)
Label(frame_1, text="Date of Birth :", font=lfont,bg=lf_bg).place(relx=0.05, rely=0.54)
Label(frame_1, text="Address :", font=lfont,bg=lf_bg).place(relx=0.06, rely=0.62)
Label(frame_1, text="District :", font=lfont,bg=lf_bg).place(relx=0.06, rely=0.77)
Label(frame_1, text="Pin Code :", font=lfont,bg=lf_bg).place(relx=0.06, rely=0.84)
# Placing components in the first frame lables values
Entry(frame_1, width=23, textvariable=name, font=efont).place(x=135, rely=0.06)
Entry(frame_1, width=23, textvariable=rno, font=efont).place(x=135, rely=0.14)
Entry(frame_1, width=23, textvariable=std, font=efont).place(x=135, rely=0.22)
Entry(frame_1, width=23, textvariable=contact,font=efont).place(x=135, rely=0.30)
Entry(frame_1, width=23, textvariable=email,font=efont).place(x=135, rely=0.38)
#Entry(first_frame, width=23, textvariable=address_strvar, font=entryfont).place(x=135, rely=0.62,relheight=0.13)
Entry(frame_1, width=23, textvariable=pin, font=efont).place(x=135, rely=0.845)
OptionMenu(frame_1, gender, "Male", "Female").place(x=135, rely=0.46, relwidth=0.57)
OptionMenu(frame_1, dist, "Ariyalur", "Chengalpet", "Chennai", "Coimbatore", "Cuddalore", "Dharmapuri", "Dindigul",
           "Erode", "Kallakurichi", "Kancheepuram", "Karur", "Krishnagiri", "Madurai", "Mayiladuthurai", "Nagapattinam",
           "Kanyakumari", "Namakkal", "Perambalur", "Pudukottai", "Ramanathapuram", "Ranipet", "Salem", "Sivagangai", "Tenkasi",
           "Thanjavur", "Theni", "Thiruvallur", "Thiruvarur", "Tuticorin", "Tiruchirappalli", "Thirunelveli", "Tirupathur", "Tiruppur",
           "Tiruvannamalai", "Nilgiris", "Vellore", "Viluppuram", "Virudhunagar").place(x=135, rely=0.77, relwidth=0.57)
dob = DateEntry(frame_1, font=("Arial", 12), width=19)
dob.place(x=140, rely=0.54)
address = Text(frame_1, width=23, font=efont)
address.place(x=135, rely=0.62, relheight=0.13)
# Placing components in the second frame names
Label(frame_2, text="Father Name :", font=lfont,bg=sh_bg).place(relx=0.06, rely=0.07)
Label(frame_2, text="Mother Name :", font=lfont,bg=sh_bg).place(relx=0.06, rely=0.17)
Label(frame_2, text="Father Occupation :", font=lfont,bg=sh_bg).place(relx=0.06, rely=0.27)
Label(frame_2, text="Mother Occupation :", font=lfont,bg=sh_bg).place(relx=0.06, rely=0.37)
Label(frame_2, text="Father Contact No :", font=lfont,bg=sh_bg).place(relx=0.06, rely=0.47)
Label(frame_2, text="Mother Contact No :", font=lfont,bg=sh_bg).place(relx=0.06, rely=0.57)
Label(frame_2, text="Parent Email :", font=lfont,bg=sh_bg).place(relx=0.06, rely=0.67)
# Placing components in the second frame lables values
Entry(frame_2, width=23, textvariable=fname,font=efont).place(x=205, rely=0.07)
Entry(frame_2, width=23, textvariable=mname,font=efont).place(x=205, rely=0.17)
Entry(frame_2, width=23, textvariable=focc, font=efont).place(x=205, rely=0.27)
Entry(frame_2, width=23, textvariable=mocc, font=efont).place(x=205, rely=0.37)
Entry(frame_2, width=23, textvariable=fcno, font=efont).place(x=205, rely=0.47)
Entry(frame_2, width=23, textvariable=mcno, font=efont).place(x=205, rely=0.57)
Entry(frame_2, width=23, textvariable=pemail,font=efont).place(x=205, rely=0.67)
#functions
def getData(event):
    selected_row = tree.focus()
    data = tree.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    rno.set(row[2])
    std.set(row[3])
    contact.set(row[4])
    email.set(row[5])
    gender.set(row[6])
    #dob.set(row[7])
    address.delete(1.0, END)
    address.insert(END, row[8])
    dist.set(row[9])
    pin.set(row[10])
    fname.set(row[11])
    mname.set(row[12])
    focc.set(row[13])
    mocc.set(row[14])
    fcno.set(row[15])
    mcno.set(row[16])
    pemail.set(row[17])

def displayAll():
    tree.delete(*tree.get_children())
    for row in db.fetch():
        tree.insert("", END, values=row)

def add_student():
    if name.get() == "" or rno.get() == "" or std.get() == "" or contact.get() == "" or email.get() == "" or gender.get() == "" or dob.get() == "" or address.get(
            1.0, END) == "" or dist.get() == "" or pin.get() == "" or fname.get() == "" or mname.get() == "" or focc.get() == "" or mocc.get() == "" or fcno.get() == "" or mcno.get() == "" or pemail.get() == "":
        mb.showerror("Input Erorr", "Please Fill All the Details")
        return
    db.insert(name.get(), rno.get(), std.get(), contact.get(), email.get(), gender.get(), dob.get(), address.get(
        1.0, END), dist.get(), pin.get(), fname.get(), mname.get(), focc.get(), mocc.get(), fcno.get(), mcno.get(), pemail.get())

    mb.showinfo("Success", f"Record of {name.get()} was successfully added")
    clearAll()
    displayAll()

def update_student():
    if name.get() == "" or rno.get() == "" or std.get() == "" or contact.get() == "" or email.get() == "" or gender.get() == "" or dob.get() == "" or address.get(
            1.0, END) == "" or dist.get() == "" or pin.get() == "" or fname.get() == "" or mname.get() == "" or focc.get() == "" or mocc.get() == "" or fcno.get() == "" or mcno.get() == "" or pemail.get() == "":
        mb.showerror("Input Erorr", "Please Fill All the Details")
        return
    db.update(row[0], name.get(), rno.get(), std.get(), contact.get(), email.get(), gender.get(), dob.get(), address.get(
        1.0, END), dist.get(), pin.get(), fname.get(), mname.get(), focc.get(), mocc.get(), fcno.get(), mcno.get(), pemail.get())

    mb.showinfo("Success", "Record Updated")
    clearAll()
    displayAll()

def delete_student():
    db.remove(row[0])
    clearAll()
    displayAll()

def clearAll():
    name.set("")
    rno.set("")
    std.set("")
    contact.set("")
    email.set("")
    gender.set("")
    dob.set_date(datetime.datetime.now().date())
    address.delete(1.0, END)
    dist.set("")
    pin.set("")
    fname.set("")
    mname.set("")
    focc.set("")
    mocc.set("")
    fcno.set("")
    mcno.set("")
    pemail.set("")

def reset_form():
    global tree
    tree.delete(*tree.get_children())
    clearAll()

#Placing Submit Button in between frame_1&2
Button(main, text='Submit and Add Record', font=lfont, command=add_student,width=25, bd=3,bg='#ffd6a5', fg='#f31559').place(relx=0.165, rely=0.92)
# Placing Buttons in the  frame_4
Button(frame_4, text='Update Record', font=lfont, command=update_student,width=18, height=2,bd=4, bg='#cbffa9', fg='#263a29').place(relx=0.06, rely=0.15)
Button(frame_4, text='Delete Record', font=lfont, command=delete_student,width=18, height=2,bd=4, bg='#ed7d31', fg='#0802a3').place(relx=0.56, rely=0.15)
Button(frame_4, text='Reset Fields', font=lfont, command=clearAll,width=18, height=2,bd=4, bg='#068da9', fg='#fff').place(relx=0.06, rely=0.59)
Button(frame_4, text='Reset database', font=lfont, command=reset_form,width=18, height=2,bd=4, bg='#fc5050', fg='yellow').place(relx=0.56, rely=0.59)
# Placing components in the Tree View
tree = ttk.Treeview(frame_3, height=1, columns=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19),style="mystyle.Treeview")
tree.place(y=30, relwidth=1.0,relheight=0.935, relx=0)
style = ttk.Style()
style.configure("mystyle.Treeview.Heading", font=('times', 13,'bold'))  # Modify the font of the headings
style.configure("mystyle.Treeview", font=('Calibri', 12),bg='#ffd6a5', fg='#f31559')  # Modify the font of the body

X_scroller = Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
Y_scroller = Scrollbar(tree, orient=VERTICAL, command=tree.yview)

tree.heading('1', text='ID', anchor=CENTER)
tree.heading('2', text='Name', anchor=CENTER)
tree.heading('3', text='Roll No', anchor=CENTER)
tree.heading('4', text='Standard', anchor=CENTER)
tree.heading('5', text='Contact No', anchor=CENTER)
tree.heading('6', text='Email ID', anchor=CENTER)
tree.heading('7', text='Gender', anchor=CENTER)
tree.heading('8', text='DOB', anchor=CENTER)
tree.heading('9', text='Address', anchor=CENTER)
tree.heading('10', text='District', anchor=CENTER)
tree.heading('11', text='pincode', anchor=CENTER)
tree.heading('12', text='Father Name', anchor=CENTER)
tree.heading('13', text='Mother Name', anchor=CENTER)
tree.heading('14', text='Father Occupation', anchor=CENTER)
tree.heading('15', text='Mother Occupation', anchor=CENTER)
tree.heading('16', text='Father Contact No', anchor=CENTER)
tree.heading('17', text='Mother Contact No', anchor=CENTER)
tree.heading('18', text='Parent Email', anchor=CENTER)

X_scroller.pack(side=BOTTOM, fill=X)
Y_scroller.pack(side=RIGHT, fill=Y)
tree.config(yscrollcommand=Y_scroller.set, xscrollcommand=X_scroller.set)

tree.column('#0', width=0, stretch=NO)
tree.column('#1', width=40, stretch=NO)
tree.column('#2', width=130, stretch=YES)
tree.column('#3', width=100, stretch=NO)
tree.column('#4', width=80, stretch=NO)
tree.column('#5', width=90, stretch=NO)
tree.column('#6', width=150, stretch=YES)
tree.column('#7', width=70, stretch=NO)
tree.column('#8', width=70, stretch=NO)
tree.column('#9', width=150, stretch=YES)
tree.column('#10', width=100, stretch=NO)
tree.column('#11', width=90, stretch=NO)
tree.column('#12', width=160, stretch=NO)
tree.column('#13', width=160, stretch=NO)
tree.column('#14', width=160, stretch=NO)
tree.column('#15', width=160, stretch=NO)
tree.column('#16', width=160, stretch=NO)
tree.column('#17', width=160, stretch=NO)
tree.column('#18', width=160, stretch=NO)
tree.bind("<ButtonRelease-1>", getData)


displayAll()
main.mainloop()
