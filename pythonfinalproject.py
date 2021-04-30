import tkinter as tk
from cProfile import label
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime



class Demo1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title("Hospital  Management System")
        self.master.geometry("1400x780+0+0")
        self.master.configure(background="pink")
        self.frame.configure(background="pink")
        self.frame.grid()

        self.username = StringVar()
        self.password = StringVar()

        # frames
        self.newframe = Frame(self.frame, height=300, width=1010, bd=20, relief='ridge')
        self.newframe.grid(row=1, column=0)

        self.newframe1 = Frame(self.frame, height=100, width=1010, bd=20, relief='ridge')
        self.newframe1.grid(row=2, column=0)

        self.newframe2 = Frame(self.frame, height=100, width=1010, bd=10, relief='ridge')
        self.newframe2.grid(row=3, column=0)

        # label
        self.lbltitle = Label(self.frame, font=("arial", 50, "bold"), text="           Hospital management system",
                              bd=10, bg="pink", anchor='n')
        self.lbltitle.grid(row=0, column=0, pady=20)

        self.lblusrmne = Label(self.newframe, font=('arial', 10, 'bold'), text="Username", bd=30)
        self.lblusrmne.grid(row=0, column=0)
        self.txtusrmne = Entry(self.newframe, font=("ariel", 20, "bold"), textvariable=self.username, bd=30)
        self.txtusrmne.grid(row=0, column=1, columnspan=4)

        self.lblpswd = Label(self.newframe, font=('arial', 10, 'bold'), text="Password", bd=30)
        self.lblpswd.grid(row=1, column=0)
        self.txtpswd = Entry(self.newframe, font=("ariel", 20, "bold"),show="*" ,textvariable=self.password, bd=30)
        self.txtpswd.grid(row=1, column=1, columnspan=4)

        # buttons
        self.button1 = tk.Button(self.newframe2, text='Patient registration  System', width=30, state=DISABLED,
                                 command=self.new_window, font=("arial", 10, "bold"))
        self.button1.grid(row=1, column=0)
        self.button2 = tk.Button(self.newframe2, text='Medicine registration System', width=30, state=DISABLED,
                                 command=self.new_window1, font=("arial", 10, "bold"))
        self.button2.grid(row=1, column=1)

        self.btnlogin = tk.Button(self.newframe1, font=("arial", 10, "bold"), text='Login', width=19,
                                  command=self.login_system)
        self.btnlogin.grid(row=1, column=1)
        self.btnreset = tk.Button(self.newframe1, font=("arial", 10, "bold"), text='Reset', width=19,
                                  command=self.for_reset)
        self.btnreset.grid(row=1, column=2)
        self.btnexit = tk.Button(self.newframe1, font=("arial", 10, "bold"), text='exit', width=19,
                                 command=self.close_windows)
        self.btnexit.grid(row=1, column=3)

    def login_system(self):
        user = self.username.get()
        pas = self.password.get()
        if user == str('kartik') and pas == str('123'):
            self.button1.config(state=NORMAL)
            self.button2.config(state=NORMAL)
        else:
            tkinter.messagebox.askretrycancel("Pharmacy Management Sysytem", "Invalid Inputs")
            self.button1.config(state=DISABLED)
            self.button2.config(state=DISABLED)
            self.username.set("")
            self.password.set("")
            self.txtusrmne.focus()

    def for_reset(self):
        self.username.set("")
        self.password.set("")
        self.button1.config(state=DISABLED)
        self.button2.config(state=DISABLED)

    def new_window(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo2(self.newWindow)

    def new_window1(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Demo3(self.newWindow)

    def close_windows(self):
        self.master.destroy()


class Demo2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title("Patient registration  System")
        self.master.geometry("1600x750+0+0")
        # self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        # self.quitButton.pack()
        self.frame.pack()

        self.rand = StringVar()
        self.name = StringVar()
        self.age = StringVar()
        self.occupation = StringVar()
        self.address = StringVar()
        self.gender = StringVar()
        self.pincode = StringVar()
        self.mar = StringVar()
        self.blood = StringVar()
        self.days = StringVar()
        self.total = StringVar()
        self.method = StringVar()
        self.contact = StringVar()
        self.dat = time.asctime(time.localtime(time.time()))

        # frames

        self.Tops = Frame(self.frame, width=1350, padx=26, relief=RIDGE)
        self.Tops.pack(side=TOP)
        self.f1 = Frame(self.frame, width=1350, height=500, bd=20, relief=RIDGE)
        self.f1.pack(side=LEFT)
        self.f2 = Frame(self.frame, width=900, height=700, bd=20, relief=RIDGE)
        self.f2.pack(side=RIGHT)

        # labels
        self.lblinfo = Label(self.Tops, font=('ariel', 50, 'bold'), text="Patient Registration System", fg="black",
                             bd=10, anchor='w')
        self.lblinfo.grid(row=0, column=0)

        self.lblreference = Label(self.f1, font=("ariel", 10, "bold"), text="Reference", bd=16, anchor="w")
        self.lblreference.grid(row=0, column=0)
        self.al = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.rand, bd=10, insertwidth=4,
                        justify="right")
        self.al.grid(row=0, column=1)

        self.lblname = Label(self.f1, font=("ariel", 10, "bold"), text="Name", bd=16, anchor="w")
        self.lblname.grid(row=1, column=0)
        self.txtname = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.name, bd=10, insertwidth=4,
                             justify="right")
        self.txtname.grid(row=1, column=1)

        self.lblage = Label(self.f1, font=("ariel", 10, "bold"), text="Age", bd=16, anchor="w")
        self.lblage.grid(row=2, column=0)
        self.textage = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.age, bd=10, insertwidth=4,
                             justify="right")
        self.textage.grid(row=2, column=1)

        self.lblocc = Label(self.f1, font=("ariel", 10, "bold"), text="Occupation", bd=16, anchor="w")
        self.lblocc.grid(row=4, column=0)
        self.textocc = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.occupation, bd=10, insertwidth=4,
                             justify="right")
        self.textocc.grid(row=4, column=1)

        self.lblgen = Label(self.f1, font=("ariel", 10, "bold"), text="Gender", bd=16, anchor="w")
        self.lblgen.grid(row=3, column=0)

        self.textgen = ttk.Combobox(self.f1, font=("ariel", 10, "bold"), textvariable=self.gender, state='readonly',
                                    width=19)
        self.textgen["value"] = ("", "Male", "Female", "Others")
        self.textgen.current(0)
        self.textgen.grid(row=3, column=1)

        # self.textgen=Entry(self.f1,font=("ariel",10,"bold"),textvariable=self.gender,bd=10,insertwidth=4,justify="right")
        # self.textgen.grid(row=3,column=1)

        self.lblmar = Label(self.f1, font=("ariel", 10, "bold"), text="Marital Status", bd=16, anchor="w")
        self.lblmar.grid(row=5, column=0)

        self.textmar = ttk.Combobox(self.f1, font=("ariel", 10, "bold"), textvariable=self.mar, state='readonly',
                                    width=19)
        self.textmar["value"] = ("", "Married", "Single", "Divorced")
        self.textmar.current(0)
        self.textmar.grid(row=5, column=1)

        # self.textmar=Entry(self.f1,font=("ariel",10,"bold"),textvariable=self.mar,bd=10,insertwidth=4,justify="right")
        # self.textmar.grid(row=5,column=1)

        self.lblcontact = Label(self.f1, font=("ariel", 10, "bold"), text="Contact", bd=16, anchor="w")
        self.lblcontact.grid(row=6, column=0)
        self.textcontact = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.contact, bd=10, insertwidth=4,
                                 justify="right")
        self.textcontact.grid(row=6, column=1)

        self.lblblood = Label(self.f1, font=("ariel", 10, "bold"), text="Blood Group", bd=16, anchor="w")
        self.lblblood.grid(row=0, column=2)

        self.textblood = ttk.Combobox(self.f1, font=("ariel", 10, "bold"), textvariable=self.blood, state='readonly',
                                      width=19)
        self.textblood["value"] = ("", "A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-")
        self.textblood.current(0)
        self.textblood.grid(row=0, column=3)

        # self.textblood=Entry(self.f1,font=("ariel",10,"bold"),textvariable=self.blood,bd=10,insertwidth=4,justify="right")
        # self.textblood.grid(row=0,column=3)

        self.lbladd = Label(self.f1, font=("ariel", 10, "bold"), text="Address", bd=16, anchor="w")
        self.lbladd.grid(row=1, column=2)
        self.textadd = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.address, bd=10, insertwidth=4,
                             justify="right")
        self.textadd.grid(row=1, column=3)

        self.lblpin = Label(self.f1, font=("ariel", 10, "bold"), text="Pin Code", bd=16, anchor="w")
        self.lblpin.grid(row=2, column=2)
        self.textpin = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.pincode, bd=10, insertwidth=4,
                             justify="right")
        self.textpin.grid(row=2, column=3)

        self.lblday = Label(self.f1, font=("ariel", 10, "bold"), text="No of days", bd=16, anchor="w")
        self.lblday.grid(row=3, column=2)
        self.textday = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.days, bd=10, insertwidth=4,
                             justify="right")
        self.textday.grid(row=3, column=3)

        self.lbldis = Label(self.f1, font=("ariel", 10, "bold"), text="Disease", bd=16, anchor="w")
        self.lbldis.grid(row=4, column=2)
        self.textdis = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.total, bd=10, insertwidth=4,
                             justify="right")
        self.textdis.grid(row=4, column=3)

        self.lblmethod = Label(self.f1, font=("ariel", 10, "bold"), text="Payement method", bd=16, anchor="w")
        self.lblmethod.grid(row=5, column=2)

        self.textmethod = ttk.Combobox(self.f1, font=("ariel", 10, "bold"), textvariable=self.method, state='readonly',
                                       width=19)
        self.textmethod["value"] = ("", "credit card", "Debit card", "paytm", "Gpay", "cash")
        self.textmethod.current(0)
        self.textmethod.grid(row=5, column=3)

        # self.textmethod=Entry(self.f1,font=("ariel",10,"bold"),textvariable=self.method,bd=10,insertwidth=4,justify="right")
        # self.textmethod.grid(row=5,column=3)

        # part2

        self.lblinfo = Label(self.f2, font=('ariel', 10, 'bold'),
                             text="Refernce/Name/Age/gender/occupation/Marital sattus/contact/Blood group/address/Pincode/nofdays/Disease",
                             fg="black", bd=7, pady=10)
        self.lblinfo.grid(row=0, column=0, columnspan=4)

        self.lblreceipt = Text(self.f2, font=('ariel', 10, 'bold'), fg="black", width=99, height=22)
        self.lblreceipt.grid(row=1, column=0, columnspan=4)

        # buttons

        self.btnreset = Button(self.f1, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, 'bold'), width=8,
                               text="RESET", command=self.reset, bg="orange").grid(row=8, column=0)

        self.btnexit = Button(self.f1, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, 'bold'), width=8,
                              text="EXIT", command=self.close_windows, bg="red").grid(row=8, column=1)

        self.btnreceipt = Button(self.f1, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, 'bold'), width=10,
                                 text="RECEIPT", command=self.receipt1, bg="blue").grid(row=8, column=2)

    def ref(self):
        self.x = random.randint(1290, 456754)
        self.r = str(self.x)
        self.rand.set(self.r)
        # new
    def reset(self):
        self.rand.set("")
        self.name.set("")
        self.age.set("")
        self.occupation.set("")
        self.address.set("")
        self.gender.set("")
        self.pincode.set("")
        self.mar.set("")
        self.blood.set("")
        self.days.set("")
        self.total.set("")
        self.method.set("")
        self.contact.set("")

    def receipt1(self):
        self.ref()
        self.lblreceipt.insert(END,
                               self.rand.get() + "/" + self.name.get() + "/" + self.age.get() + "/" + self.gender.get() + "/" + self.occupation.get() + "/" + self.mar.get() + "/" + self.contact.get() + "/" + self.blood.get() + "/" + self.address.get() + "/" + self.pincode.get() + "/" + self.days.get() + "/" + self.total.get() + '/' + self.method.get() + "\n")

    def close_windows(self):
        self.master.destroy()


class Demo3:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.master.title("Pharmacy registration System")
        self.master.geometry("1600x700+0+0")
        # self.quitButton = tk.Button(self.frame, text = 'Quit', width = 25, command = self.close_windows)
        # self.quitButton.pack()
        self.frame.pack()
        self.rand = StringVar()
        self.name = StringVar()
        self.age = StringVar()
        self.occupation = StringVar()
        self.address = StringVar()
        self.gender = StringVar()
        self.pincode = StringVar()
        self.mar = StringVar()
        self.blood = StringVar()
        self.days = StringVar()
        self.total = StringVar()
        self.method = StringVar()
        self.contact = StringVar()
        self.dat = time.asctime(time.localtime(time.time()))

        # frames

        self.Tops = Frame(self.frame, width=1350, padx=26, relief=RIDGE)
        self.Tops.pack(side=TOP)
        self.f1 = Frame(self.frame, width=500, height=500, bd=20, relief=RIDGE)
        self.f1.pack(side=LEFT)
        self.f2 = Frame(self.frame, width=1100, height=700, bd=20, relief=RIDGE)
        self.f2.pack(side=RIGHT)

        # labels
        self.lblinfo = Label(self.Tops, font=('ariel', 50, 'bold'), text="Medicine Registration System", fg="black",
                             bd=10, anchor='w')
        self.lblinfo.grid(row=0, column=0)

        self.lblreference = Label(self.f1, font=("ariel", 10, "bold"), text="Reference", bd=16, anchor="w")
        self.lblreference.grid(row=0, column=0)
        self.al = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.rand, bd=10, insertwidth=4,
                        justify="right")
        self.al.grid(row=0, column=1)

        self.lblname = Label(self.f1, font=("ariel", 10, "bold"), text="Name of the tablet", bd=10, anchor="w")
        self.lblname.grid(row=1, column=0)
        self.txtname = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.name, bd=10, insertwidth=4,
                             justify="right")
        self.txtname.grid(row=1, column=1)

        self.lblage = Label(self.f1, font=("ariel", 10, "bold"), text="Dose", bd=10, anchor="w")
        self.lblage.grid(row=2, column=0)
        self.textage = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.age, bd=10, insertwidth=4,
                             justify="right")
        self.textage.grid(row=2, column=1)

        self.lblocc = Label(self.f1, font=("ariel", 10, "bold"), text="No of tablet", bd=10, anchor="w")
        self.lblocc.grid(row=4, column=0)
        self.textocc = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.occupation, bd=10, insertwidth=4,
                             justify="right")
        self.textocc.grid(row=4, column=1)

        self.lblgen = Label(self.f1, font=("ariel", 10, "bold"), text="Issue Date", bd=10, anchor="w")
        self.lblgen.grid(row=3, column=0)
        self.textgen = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.gender, bd=10, insertwidth=4,
                             justify="right")
        self.textgen.grid(row=3, column=1)

        self.lblmar = Label(self.f1, font=("ariel", 10, "bold"), text="Expiry Date", bd=10, anchor="w")
        self.lblmar.grid(row=5, column=0)
        self.textmar = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.mar, bd=10, insertwidth=4,
                             justify="right")
        self.textmar.grid(row=5, column=1)

        self.lblcontact = Label(self.f1, font=("ariel", 10, "bold"), text=" Patient Contact", bd=10, anchor="w")
        self.lblcontact.grid(row=0, column=2)
        self.textcontact = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.contact, bd=10, insertwidth=4,
                                 justify="right")
        self.textcontact.grid(row=0, column=3)

        self.lblblood = Label(self.f1, font=("ariel", 10, "bold"), text="Side effect", bd=10, anchor="w")
        self.lblblood.grid(row=6, column=0)
        self.textblood = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.blood, bd=10, insertwidth=4,
                               justify="right")
        self.textblood.grid(row=6, column=1)

        self.lbladd = Label(self.f1, font=("ariel", 10, "bold"), text="Address", bd=16, anchor="w")
        self.lbladd.grid(row=1, column=2)
        self.textadd = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.address, bd=10, insertwidth=4,
                             justify="right")
        self.textadd.grid(row=1, column=3)

        self.lblpin = Label(self.f1, font=("ariel", 10, "bold"), text="Patient Name", bd=10, anchor="w")
        self.lblpin.grid(row=2, column=2)
        self.textpin = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.pincode, bd=10, insertwidth=4,
                             justify="right")
        self.textpin.grid(row=2, column=3)

        self.lblday = Label(self.f1, font=("ariel", 10, "bold"), text="Dr name", bd=10, anchor="w")
        self.lblday.grid(row=3, column=2)
        self.textday = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.days, bd=10, insertwidth=4,
                             justify="right")
        self.textday.grid(row=3, column=3)

        self.lbldis = Label(self.f1, font=("ariel", 10, "bold"), text="Disease", bd=16, anchor="w")
        self.lbldis.grid(row=4, column=2)
        self.textdis = Entry(self.f1, font=("ariel", 10, "bold"), textvariable=self.total, bd=10, insertwidth=4,
                             justify="right")
        self.textdis.grid(row=4, column=3)

        self.lblmethod = Label(self.f1, font=("ariel", 10, "bold"), text="Payement method used", bd=16, anchor="w")
        self.lblmethod.grid(row=5, column=2)

        self.textmethod = ttk.Combobox(self.f1, font=("ariel", 10, "bold"), textvariable=self.method, state='readonly',
                                       width=19)
        self.textmethod["value"] = ("", "credit card", "Debit card", "paytm", "Gpay", "cash")
        self.textmethod.current(0)
        self.textmethod.grid(row=5, column=3)

        # self.textmethod=Entry(self.f1,font=("ariel",10,"bold"),textvariable=self.method,bd=10,insertwidth=4,justify="right")
        # self.textmethod.grid(row=5,column=3)

        # part2

        self.lblinfo = Label(self.f2, font=('ariel', 8, 'bold'),
                             text="Refernce//Name//Dose//IssueDate//NO of tablet//ExpiryDate//Side effect//contact//address//PatientName//DrName//Disease//payementmethod used",
                             fg="black", bd=7, pady=10)
        self.lblinfo.grid(row=0, column=0, columnspan=4)

        self.lblreceipt = Text(self.f2, font=('ariel', 10, 'bold'), fg="black", width=99, height=22)
        self.lblreceipt.grid(row=1, column=0, columnspan=4)

        # buttons

        self.btnreset = Button(self.f1, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, 'bold'), width=8,
                               text="RESET", command=self.reset, bg="orange").grid(row=8, column=0)

        self.btnexit = Button(self.f1, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, 'bold'), width=8,
                              text="EXIT", command=self.close_windows, bg="red").grid(row=8, column=1)

        self.btnreceipt = Button(self.f1, padx=16, pady=8, bd=16, fg="black", font=("arial", 16, 'bold'), width=10,
                                 text="RECEIPT", command=self.receipt1, bg="blue").grid(row=8, column=2)

    def ref(self):
        self.x = random.randint(1290, 456754)
        self.r = str(self.x)
        self.rand.set(self.r)

    def reset(self):
        self.rand.set("")
        self.name.set("")
        self.age.set("")
        self.occupation.set("")
        self.address.set("")
        self.gender.set("")
        self.pincode.set("")
        self.mar.set("")
        self.blood.set("")
        self.days.set("")
        self.total.set("")
        self.method.set("")
        self.contact.set("")

    def receipt1(self):
        self.ref()
        self.lblreceipt.insert(END,
                               self.rand.get() + "//" + self.name.get() + "//" + self.age.get() + "//" + self.gender.get() + "//" + self.occupation.get() + "//" + self.mar.get() + "//" + self.contact.get() + "//" + self.blood.get() + "//" + self.address.get() + "//" + self.pincode.get() + "//" + self.days.get() + "//" + self.total.get() + '//' + self.method.get() + "\n")

    def close_windows(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    app = Demo1(root)
    root.mainloop()


if __name__ == '__main__':
    main()