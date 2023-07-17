from tkinter import *

class lbs:
    def __init__ (self, root):
        self.root=root
        self.root.title("Library Management system")
        self.root.geometry("1550x800")

        lbltitle=Label(self.root, text="Library management system",bg="powder blue", fg="green", bd=20, padx=2, relief=RIDGE, font=("times new roman",50,"bold"), pady=6)
        lbltitle.pack(side=TOP, fill=X)

        frame=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        frame.place(x=0, y=130, width=1530, height=400)


        #Dataframe left
        dataframeleft= LabelFrame(frame, text="Library member information", bg="powder blue", bd=10, relief=RIDGE, font=("times new roman",12,"bold"))
        dataframeleft.place(x=0, y=5, width=900, height=350)

        lblmember=Label(dataframeleft, text="membertype", bg="powder blue", font=("times new roman",15,"bold"), padx=2, pady=6)
        lblmember.grid(row=0, column=0, sticky=W)

                 #1) prn no
        lblprn_no=Label(dataframeleft, bg="powder blue", text="Prn no", font=("times new roman",15,"bold"),padx=2, pady=6)
        lblprn_no.grid(row=1, column=0)

        txtprn_no=Entry(dataframeleft, font=("times new roman",15,"bold"), width=29)
        txtprn_no.grid(row=1, column=1)

                #Title
        lbltitle=Label(dataframeleft, bg="powder blue", text="Title", font=("times new roman",15,"bold"),padx=2, pady=6)
        lbltitle.grid(row=2, column=0)

        txttitle=Entry(dataframeleft, font=("times new roman",15,"bold"), width=29)
        txttitle.grid(row=2, column=1)

                #First Name
        lblfirst_name=Label(dataframeleft, bg="powder blue", text="First Name", font=("times new roman",15,"bold"),padx=2, pady=6)
        lblfirst_name.grid(row=3, column=0)

        txtfirst_name=Entry(dataframeleft, font=("times new roman",15,"bold"), width=29)
        txtfirst_name.grid(row=3, column=1)

                #Last Name
        lbllast_name=Label(dataframeleft, bg="powder blue", text="Last Name", font=("times new roman",15,"bold"),padx=2, pady=6)
        lbllast_name.grid(row=4, column=0)

        txtlast_name=Entry(dataframeleft, font=("times new roman",15,"bold"), width=29)
        txtlast_name.grid(row=4, column=1)

               #Address 1
        lbladdress1=Label(dataframeleft, bg="powder blue", text="Address 1", font=("times new roman",15,"bold"),padx=2, pady=6)
        lbladdress1.grid(row= 5, column=0)

        txtaddress1=Entry(dataframeleft, font=("times new roman",15,"bold"), width=29)
        txtaddress1.grid(row=5, column=1)

               #Address 2
        lbladdress2=Label(dataframeleft, bg="powder blue", text="Address 2", font=("times new roman",15,"bold"),padx=2, pady=6)
        lbladdress2.grid(row= 6, column=0)

        txtaddress2=Entry(dataframeleft, font=("times new roman",15,"bold"), width=29)
        txtaddress2.grid(row=6, column=1)


               #Post Code
        lblpostcode=Label(dataframeleft, bg="powder blue", text="Post Code", font=("times new roman",15,"bold"),padx=2, pady=6)
        lblpostcode.grid(row= 7, column=0)

        txtpostcode=Entry(dataframeleft, font=("times new roman",15,"bold"), width=29)
        txtpostcode.grid(row=7, column=1)

               #Book ID
        lbladdress1=Label(dataframeleft, bg="powder blue", text="Book ID", font=("times new roman",15,"bold"),padx=2, pady=6)
        lbladdress1.grid(row= 1, column=2)

        txtaddress1=Entry(dataframeleft, font=("times new roman",15,"bold"), width=29)
        txtaddress1.grid(row=1, column=3)

            #Book Title
        lbladdress1=Label(dataframeleft, bg="powder blue", text="Book Title", font=("times new roman",15,"bold"),padx=2, pady=6)
        lbladdress1.grid(row=2, column=2)

        txtaddress1=Entry(dataframeleft, font=("times new roman",15,"bold"), width=29)
        txtaddress1.grid(row=2, column=3)


               #Author
        lbladdress1=Label(dataframeleft, bg="powder blue", text="Author", font=("times new roman",15,"bold"),padx=2, pady=6)
        lbladdress1.grid(row=3, column=2)

        txtaddress1=Entry(dataframeleft, font=("times new roman",15,"bold"), width=29)
        txtaddress1.grid(row=3, column=3)


               #Date Borrowed
        lbladdress1=Label(dataframeleft, bg="powder blue", text="Date Borrowed", font=("times new roman",15,"bold"),padx=2, pady=6)
        lbladdress1.grid(row=4, column=2)

        txtaddress1=Entry(dataframeleft, font=("times new roman",15,"bold"), width=29)
        txtaddress1.grid(row=4, column=3)


               #Due Date
        lbladdress1=Label(dataframeleft, bg="powder blue", text="Due Date", font=("times new roman",15,"bold"),padx=2, pady=6)
        lbladdress1.grid(row= 5, column=2)

        txtaddress1=Entry(dataframeleft, font=("times new roman",15,"bold"), width=29)
        txtaddress1.grid(row=5, column=3)


               #Days on Book
        lbladdress1=Label(dataframeleft, bg="powder blue", text="Days on Book", font=("times new roman",15,"bold"),padx=2, pady=6)
        lbladdress1.grid(row= 6, column=2)

        txtaddress1=Entry(dataframeleft, font=("times new roman",15,"bold"), width=29)
        txtaddress1.grid(row=6, column=3)


             #Late return fine
        lbladdress1=Label(dataframeleft, bg="powder blue", text="Late Return Fine", font=("times new roman",15,"bold"),padx=2, pady=6)
        lbladdress1.grid(row= 7, column=2)

        txtaddress1=Entry(dataframeleft, font=("times new roman",15,"bold"), width=29)
        txtaddress1.grid(row=7, column=3)


        #Dataframe Right
        dataframeright= LabelFrame(frame, text="Book detail", bg="powder blue", bd=10, relief=RIDGE, font=("times new roman",12,"bold"))
        dataframeright.place(x=910, y=5, width=500, height=350)

        self.txtbox=Text(dataframeright, font=("times new roman",12,"bold"), width=32, height=16, padx=2, pady=6)
        self.txtbox.grid(row=0, column=2)

        #Scroll Bar
        listscrollbar= Scrollbar(dataframeright)
        listscrollbar.grid(row=0, column=1, sticky= 'ns')


        #List of Books
        listbooks=["Python", "Everyone is a story","Attitude is Everything","Rich Dad Poor Dad", "A girl who knew too much", "Alchemist", "Hope", "Flying High", "Alice in the Wonderland","Bible","Bhagwad Gita","A ife so Beautiful","Harry Potter","Vaga Bond","Vinland saga","Sapiens","Dr. Stone"]

        #Box of list of Books
        listbox=Listbox(dataframeright, font=("times new roman",12,"bold"), width=20, height=16)
        listbox.grid(row=0, column=0, padx=4)
        listscrollbar.config(command=listbox.yview)

        for item in listbooks:
            listbox.insert(END, item)


        #Button Frame
        framebutton=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        framebutton.place(x=0, y=530, height=70, width=1530)

                #Add Data
        buttadddata=Button(framebutton, text="Add Data", font=("arials", 12, "bold"), width=21, bg="blue", pady=6)
        buttadddata.grid(row=0, column=0)

                #Show data
        buttadddata=Button(framebutton, text="Show Data", font=("arials", 12, "bold"), width=21, bg="blue", pady=6)
        buttadddata.grid(row=0, column=1)

                #Udpate Button
        buttadddata=Button(framebutton, text="Update Data", font=("arials", 12, "bold"), width=21, bg="blue", pady=6)
        buttadddata.grid(row=0, column=2)

                #Delete Button
        buttadddata=Button(framebutton, text="Delete Data", font=("arials", 12, "bold"), width=21, bg="blue", pady=6)
        buttadddata.grid(row=0, column=3)

                #reset Button
        buttadddata=Button(framebutton, text="Reset Data", font=("arials", 12, "bold"), width=21, bg="blue", pady=6)
        buttadddata.grid(row=0, column=4)

                #Exit button
        buttadddata=Button(framebutton, text="Exit", font=("arials", 12, "bold"), width=21, bg="blue", pady=6)
        buttadddata.grid(row=0, column=5)


        #Information
        framedetails=Frame(self.root, bd=12, relief=RIDGE, padx=20, bg="powder blue")
        framedetails.place(x=0, y=600, height=600, width=1530)


if __name__== "__main__":
    root=Tk()
    obj = lbs(root)
    root.mainloop()