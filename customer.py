from tkinter import *
from PIL import Image,ImageTk
import urllib.request
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
urllib.request.urlretrieve(
  'https://iocl.com/images/indane_1.jpg',
   "indane1.png")




class Cust_win:
    def __init__(self,root):
        self.root=root
        self.root.title("LPG Booking System")
        self.root.geometry("1250x560+110+138")


        #***********Variables*******
        self.var_cons=StringVar()
        x=random.randint(1000,9999)
        self.var_cons.set(str(x))

        self.var_name=StringVar()
        self.var_mname=StringVar()
        self.var_gender=StringVar()
        self.var_mobile=StringVar()
        self.var_altmo=StringVar()
        self.var_email=StringVar()
        self.var_nation=StringVar()
        self.var_address=StringVar()
        self.var_idpr=StringVar()
        self.var_id_num=StringVar()


        #*********Title*****************
        lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",15,"bold"),bg="black",fg="dark orange",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1244,height=50)


        #***********LOGO**************
        img1=Image.open(r"indane1.png")
        img1=img1.resize((200,50),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        labelimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        labelimg.place(x=0,y=0,width=200,height=50)


        #**************Label Frame******************
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DETAILS",padx=2,font=("times new roman",14,"bold"))
        labelframeleft.place(x=5,y=50,width=425,height=490)

        #********************Labels and Entries*****************
        #cust ref
        lbl_cust_ref=Label(labelframeleft,text="Consumer ID :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0,column=0,sticky="w")
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_cons,width=22,state="readonly",font=("times new roman",12,"bold"))
        entry_ref.grid(row=0,column=1)

        #cust name
        lbl_cust_name=Label(labelframeleft,text="Customer Name :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_name.grid(row=1,column=0,sticky="w")
        entry_name=ttk.Entry(labelframeleft,textvariable=self.var_name,width=22,font=("times new roman",12,"bold"))
        entry_name.grid(row=1,column=1)

        #Mother's name
        lblmname=Label(labelframeleft,text="Mother's Name :",font=("arial",12,"bold"),padx=2,pady=6)
        lblmname.grid(row=2,column=0,sticky="w")
        entry_mname=ttk.Entry(labelframeleft,textvariable=self.var_mname,width=22,font=("times new roman",12,"bold"))
        entry_mname.grid(row=2,column=1)

        #Gender
        lblgender=Label(labelframeleft,text="Gender :",font=("arial",12,"bold"),padx=2,pady=6)
        lblgender.grid(row=3,column=0,sticky="w")
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=20,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        #Mobile
        lblmobile=Label(labelframeleft,text="Mobile No. :",font=("arial",12,"bold"),padx=2,pady=6)
        lblmobile.grid(row=4,column=0,sticky="w")
        entry_mobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,width=22,font=("times new roman",12,"bold"))
        entry_mobile.grid(row=4,column=1)

        #alt mobile
        lblmobile1=Label(labelframeleft,text="Alt. Mobile No. :",font=("arial",12,"bold"),padx=2,pady=6)
        lblmobile1.grid(row=5,column=0,sticky="w")
        entry_mobile1=ttk.Entry(labelframeleft,textvariable=self.var_altmo,width=22,font=("times new roman",12,"bold"))
        entry_mobile1.grid(row=5,column=1)

        #email
        lblemail=Label(labelframeleft,text="Email :",font=("arial",12,"bold"),padx=2,pady=6)
        lblemail.grid(row=6,column=0,sticky="w")
        entry_email=ttk.Entry(labelframeleft,textvariable=self.var_email,width=22,font=("times new roman",12,"bold"))
        entry_email.grid(row=6,column=1)

        #nationality
        lblnation=Label(labelframeleft,text="Nationality :",font=("arial",12,"bold"),padx=2,pady=6)
        lblnation.grid(row=7,column=0,sticky="w")
        combo_nation=ttk.Combobox(labelframeleft,textvariable=self.var_nation,font=("arial",12,"bold"),width=20,state="readonly")
        combo_nation["value"]=("Indian","Non-Resedential Indian","Other")
        combo_nation.current(0)
        combo_nation.grid(row=7,column=1)

        #id prrof type
        lblidproof=Label(labelframeleft,text="Id Proof Type :",font=("arial",12,"bold"),padx=2,pady=6)
        lblidproof.grid(row=8,column=0,sticky="w")
        combo_idproof=ttk.Combobox(labelframeleft,textvariable=self.var_idpr,font=("arial",12,"bold"),width=20,state="readonly")
        combo_idproof["value"]=("Aadhar Card","Pan Card","Driving License","Passport")
        combo_idproof.current(0)
        combo_idproof.grid(row=8,column=1)

        #id number
        lblidnumber=Label(labelframeleft,text="Id Number :",font=("arial",12,"bold"),padx=2,pady=6)
        lblidnumber.grid(row=9,column=0,sticky="w")
        entry_idnumber=ttk.Entry(labelframeleft,textvariable=self.var_id_num,width=22,font=("times new roman",12,"bold"))
        entry_idnumber.grid(row=9,column=1)

        #address
        lbladdress=Label(labelframeleft,text="Address :",font=("arial",12,"bold"),padx=2,pady=6)
        lbladdress.grid(row=10,column=0,sticky="w")
        entry_address=ttk.Entry(labelframeleft,textvariable=self.var_address,width=22,font=("times new roman",12,"bold"))
        entry_address.grid(row=10,column=1)


        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnadd=Button(btn_frame,text="ADD",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="orange",width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",12,"bold"),bg="black",fg="orange",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndel=Button(btn_frame,text="DELETE",command=self.deletes,font=("arial",12,"bold"),bg="black",fg="orange",width=9)
        btndel.grid(row=0,column=2,padx=1)


        btnreset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",12,"bold"),bg="black",fg="orange",width=9)
        btnreset.grid(row=0,column=3,padx=1)



        #**********************Tabel Frame**********************

        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW DETAILS AND SEARCH SYSTEM",padx=2,font=("times new roman",14,"bold"))
        tableframe.place(x=435,y=50,width=790,height=490)

        lblsearchby=Label(tableframe,text="Search By :",font=("arial",12,"bold"),bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky="w",padx=2)


        self.search_var=StringVar()


        combo_search=ttk.Combobox(tableframe,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("Mobile","ConsumerID","MothersName ","IDNumber")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=2)

        self.txt_search=StringVar()


        entry_search=ttk.Entry(tableframe,textvariable=self.txt_search,width=24,font=("arial",12,"bold"))
        entry_search.grid(row=0,column=2,padx=2)


        btnsearch=Button(tableframe,command=self.search,text="SEARCH",font=("arial",12,"bold"),bg="black",fg="orange",width=9)
        btnsearch.grid(row=0,column=3,padx=1)

        btnshowall=Button(tableframe,command=self.fetch_data,text="SHOW ALL",font=("arial",12,"bold"),bg="black",fg="orange",width=9)
        btnshowall.grid(row=0,column=4,padx=1)


        #*************Shwo data table**********************
        details_tbale=Frame(tableframe,bd=2,relief=RIDGE)
        details_tbale.place(x=0,y=50,width=777,height=350)


        scroll_x=ttk.Scrollbar(details_tbale,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_tbale,orient=VERTICAL)

        self.Cust_Details_table=ttk.Treeview(details_tbale,column=("Cons","name","id","idpro","mname","gender","mobile","altmo","email","address","nationality"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill="x")
        scroll_y.pack(side=RIGHT,fill="y")

        scroll_x.config(command=self.Cust_Details_table.xview)
        scroll_y.config(command=self.Cust_Details_table.yview)

        self.Cust_Details_table.heading("Cons",text="Consumer ID")
        self.Cust_Details_table.heading("name",text="Name")
        self.Cust_Details_table.heading("mname",text="Mother's Name")
        self.Cust_Details_table.heading("gender",text="Gender")
        self.Cust_Details_table.heading("mobile",text="Mobile")
        self.Cust_Details_table.heading("altmo",text="Alt. Mobile")
        self.Cust_Details_table.heading("email",text="Email")
        self.Cust_Details_table.heading("id",text="ID Number")
        self.Cust_Details_table.heading("idpro",text="ID proof")
        self.Cust_Details_table.heading("address",text="Address")
        self.Cust_Details_table.heading("nationality",text="Nationality")

        self.Cust_Details_table["show"]="headings"
        self.Cust_Details_table.column("Cons",width=100)
        self.Cust_Details_table.column("name",width=100)
        self.Cust_Details_table.column("mname",width=100)
        self.Cust_Details_table.column("gender",width=100)
        self.Cust_Details_table.column("mobile",width=100)
        self.Cust_Details_table.column("altmo",width=100)
        self.Cust_Details_table.column("email",width=150)
        self.Cust_Details_table.column("id",width=100)
        self.Cust_Details_table.column("idpro",width=100)
        self.Cust_Details_table.column("address",width=100)
        self.Cust_Details_table.column("nationality",width=100)



        self.Cust_Details_table.pack(fill=BOTH,expand=1)
        self.Cust_Details_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_id_num=="" or self.var_address=="":
            messagebox.showerror("Error","Please Enter the Required Fields",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Aditya8318@",database="lpg_booking")
                my_cursor=conn.cursor()
                my_cursor.execute("INSERT INTO customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_cons.get(),self.var_name.get(),self.var_id_num.get(),self.var_idpr.get(),self.var_mname.get(),self.var_gender.get(),self.var_mobile.get(),self.var_altmo.get(),self.var_email.get(),self.var_address.get(),self.var_nation.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went Wrong :{str(es)}",parent=self.root)


    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Aditya8318@",database="lpg_booking")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_table.delete(*self.Cust_Details_table.get_children())
            for i in rows:
                self.Cust_Details_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_table.focus()
        content=self.Cust_Details_table.item(cursor_row)
        row=content["values"]



        self.var_cons.set(row[0]),
        self.var_name.set(row[1]),
        self.var_id_num.set(row[2]),
        self.var_idpr.set(row[3]),
        self.var_mname.set(row[4]),
        self.var_gender.set(row[5]),
        self.var_mobile.set(row[6]),
        self.var_altmo.set(row[7]),
        self.var_email.set(row[8]),
        self.var_address.set(row[9]),
        self.var_nation.set(row[10])

    def update(self):
        if self.var_id_num=="":
            messagebox.showerror("Error","Please Enter ID NUMBER",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Aditya8318@",database="lpg_booking")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE customer SET Name=%s,IDNumber=%s,IDProof=%s,MothersName=%s,Gender=%s,Mobile=%s,AltMobile=%s,Email=%s,Address=%s,Nationality=%s WHERE ConsumerID=%s",(
                                                                                                                                                                                                                   
                                                                                                                                                                                            self.var_name.get(),
                                                                                                                                                                                            self.var_id_num.get(),
                                                                                                                                                                                            self.var_idpr.get(),
                                                                                                                                                                                            self.var_mname.get(),
                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                            self.var_mobile.get(),
                                                                                                                                                                                            self.var_altmo.get(),
                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                                            self.var_nation.get(),
                                                                                                                                                                                            self.var_cons.get()
                                                                                                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details Successfully Updated",parent=self.root)


    def deletes(self):
        mdel=messagebox.askyesno("LPG Booking System","Are u Sure you want to Delete the selected record",parent=self.root)
        if mdel>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Aditya8318@",database="lpg_booking")
            my_cursor=conn.cursor()
            query="delete from customer where ConsumerID=%s"
            value=(self.var_cons.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdel:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset(self):
        # self.var_cons.set(""),
        self.var_name.set(""),
        self.var_id_num.set(""),
        # self.var_idpr.set(""),
        self.var_mname.set(""),
        # self.var_gender.set(""),
        self.var_mobile.set(""),
        self.var_altmo.set(""),
        self.var_email.set(""),
        self.var_address.set(""),
        # self.var_nation.set("")
        x=random.randint(1000,9999)
        self.var_cons.set(str(x))

    def search(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="Aditya8318@",database="lpg_booking")
         my_cursor=conn.cursor()
         s1=str(self.search_var.get())
         s2=str(self.txt_search.get())
        #  query1="SELECT * from customer WHERE "+s1+"=%s"
        #  value=(s2,)
        #  my_cursor.execute(query1,value)
         t="SELECT * from customer WHERE "+s1+" LIKE '%"+s2+"%'"
         my_cursor.execute(t)
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.Cust_Details_table.delete(*self.Cust_Details_table.get_children())
             for i in rows:
                 self.Cust_Details_table.insert("",END,values=i)
             conn.commit()
         conn.close()




if  __name__ == "__main__":
    root=Tk()
    obj=Cust_win(root)
    root.mainloop()