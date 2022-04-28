from tkinter import*
from PIL import Image ,ImageTk
from tkinter import ttk 
from tkinter import messagebox
import mysql.connector

import urllib.request
urllib.request.urlretrieve(
  'https://iocl.com/images/indane_1.jpg',
   "indane1.png")

urllib.request.urlretrieve(
  'https://cdn5.newsnationtv.com/images/2022/01/01/lpg-gas-price-today-83.jpg',
   "cylinder.jpg")



class LPGbooking:
    def __init__(self,root):
        self.root=root
        self.root.title ("LPG Booking ")
        self.root.geometry("1295x550+30+100")


        #======variables========
        self.var_consid=StringVar()
        self.var_bookdate=StringVar()
        self.var_booking_type=StringVar()
        self.var_deldate=StringVar()
        self.var_paidtax=StringVar()
        self.var_subtotal=StringVar()
        self.var_total=StringVar()


        #*********Title*****************
        lbl_title=Label(self.root,text="LPG BOOKING ",font=("times new roman",15,"bold"),bg="black",fg="dark orange",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1290,height=70)


        #***********LOGO**************
        img1=Image.open(r"indane1.png")
        img1=img1.resize((200,70),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        labelimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        labelimg.place(x=0,y=0,width=200,height=70)

         #**************Label Frame******************
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="LPG Booking",padx=2,font=("times new roman",14,"bold"))
        labelframeleft.place(x=5,y=70,width=425,height=472)

        #********************Labels and Entries*****************
        #cust contact
        lbl_cust_contact=Label(labelframeleft,text="Consumer ID :",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_cust_contact.grid(row=0,column=0,sticky="w")

        entry_contact=ttk.Entry(labelframeleft,textvariable=self.var_consid,font=("arial",12,"bold"),width=20)
        entry_contact.grid(row=0,column=1,sticky="w")

        #fetch data button
        btnFetchData=Button(labelframeleft,command=self.Fetch_cust,text="Fetch Data",font=("arial",10,"bold"),bg="black",fg="gold",width=10)
        btnFetchData.place(x=320,y=4)
        
        #booking date
        booking_date=Label(labelframeleft,font=("arial",12,"bold"), text="Booking Date :",padx=2,pady=6)
        booking_date.grid(row=1,column=0,sticky="w")
        txt_booking_date=ttk.Entry (labelframeleft,textvariable=self.var_bookdate,font=("arial",12,"bold"))
        txt_booking_date.grid(row=1,column=1)
        
        #delivery date 
        lbl_deliverydate=Label(labelframeleft,font=("arial",12,"bold"), text="Delivery Date :",padx=2,pady=6)
        lbl_deliverydate.grid(row=2,column=0,sticky="w")
        txt_deliverydate=ttk.Entry (labelframeleft,textvariable=self.var_deldate,font=("arial",12,"bold"))
        txt_deliverydate.grid(row=2,column=1)
         

        #booking type 
        lblbookingtype=Label(labelframeleft,font=("arial",12,"bold"), text="Cylinder Type :",padx=2,pady=6)
        lblbookingtype.grid(row=3,column=0,sticky="w")
        combo_search=ttk.Combobox(labelframeleft,textvariable=self.var_booking_type,font=("arial",12,"bold"))
        combo_search["value"]=("Small","Medium","Large")
        combo_search.current(0)
        combo_search.grid(row=3,column=1,padx=8)


        #paid tax
        lbltax=Label(labelframeleft,font=("arial",12,"bold"), text="Paid Tax :",padx=2,pady=6)
        lbltax.grid(row=4,column=0,sticky="w")
        txttax=ttk.Entry (labelframeleft,textvariable=self.var_paidtax,font=("arial",12,"bold"))
        txttax.grid(row=4,column=1)
        
        #sub Total
        lblsub=Label(labelframeleft,font=("arial",12,"bold"), text="Sub Total :",padx=2,pady=6)
        lblsub.grid(row=5,column=0,sticky="w")
        txtsub=ttk.Entry (labelframeleft,textvariable=self.var_subtotal,font=("arial",12,"bold"))
        txtsub.grid(row=5,column=1)

        #Total cost
        lbltotal=Label(labelframeleft,font=("arial",12,"bold"), text="Total Amount :",padx=2,pady=6)
        lbltotal.grid(row=6,column=0,sticky="w")
        txttotal=ttk.Entry (labelframeleft,textvariable=self.var_total,font=("arial",12,"bold"))
        txttotal.grid(row=6,column=1)
        
        #========bill button======
        btnbill=Button(labelframeleft,text="BILL",command=self.total,font=("arial",12,"bold"),bg="black",fg="orange",width=9)
        btnbill.grid(row=10,column=0,padx=1,sticky="w")
        #===========btn============
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=780)

        btnadd=Button(btn_frame,text="BOOK",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="orange",width=9)
        btnadd.grid(row=0,column=0,padx=1)

        btnupdate=Button(btn_frame,text="UPDATE",command=self.update,font=("arial",12,"bold"),bg="black",fg="orange",width=9)
        btnupdate.grid(row=0,column=1,padx=1)

        btndel=Button(btn_frame,text="DELETE",command=self.deletes,font=("arial",12,"bold"),bg="black",fg="orange",width=9)
        btndel.grid(row=0,column=2,padx=1)


        btnreset=Button(btn_frame,text="RESET",command=self.reset,font=("arial",12,"bold"),bg="black",fg="orange",width=9)
        btnreset.grid(row=0,column=3,padx=1)

        #=======right side image===========
        img3=Image.open(r"cylinder.jpg")
        img3=img3.resize((430,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        labelimg=Label(self.root,image=self.photoimg3,bd=4,relief=RIDGE)
        labelimg.place(x=850,y=80,width=430,height=200)   


        #========table frame search system=============
        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="VIEW DETAILS AND SEARCH SYSTEM",font=("arial",12,"bold"),bg="white",fg="red",width=9)
        Table_Frame.place(x=435,y=280,width=850,height=260)

        lblsearch=Label(Table_Frame,font=("arial",12,"bold"),text="Search by :",bg="red",fg="yellow")
        lblsearch.grid(row=0,column=0,sticky="w",padx=8)

        self.search_var=StringVar()
        combo_search=ttk.Combobox(Table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
        combo_search["value"]=("ConsumerID")
        combo_search.current(0)
        combo_search.grid(row=0,column=1,padx=8)

        self.txt_search=StringVar()
        entry_search=ttk.Entry(Table_Frame,textvariable=self.txt_search,width=24,font=("arial",12,"bold"))
        entry_search.grid(row=0,column=2,padx=8)


        btnsearch=Button(Table_Frame,text="SEARCH",command=self.search,font=("arial",12,"bold"),bg="black",fg="orange",width=9)
        btnsearch.grid(row=0,column=3,padx=8)

        btnshowall=Button(Table_Frame,text="SHOW ALL",command=self.fetch_data,font=("arial",12,"bold"),bg="black",fg="orange",width=9)
        btnshowall.grid(row=0,column=4,padx=8)
        #=======show data table========
        
        details_tbale=Frame(Table_Frame,bd=2,relief=RIDGE)
        details_tbale.place(x=5,y=50,width=835,height=180)


        scroll_x=ttk.Scrollbar(details_tbale,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_tbale,orient=VERTICAL)

        self.book_table=ttk.Treeview(details_tbale,column=("Cons","bDate","DDate","Btype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill="x")
        scroll_y.pack(side=RIGHT,fill="y")

        scroll_x.config(command=self.book_table.xview)
        scroll_y.config(command=self.book_table.yview)

        self.book_table.heading("Cons",text="ConsumerID")
        self.book_table.heading("bDate",text="Booking Date")
        self.book_table.heading("DDate",text="Delivery Date")
        self.book_table.heading("Btype",text="Booking Type")
        

        self.book_table["show"]="headings"
        self.book_table.column("Cons",width=100)
        self.book_table.column("DDate",width=100)
        self.book_table.column("bDate",width=100)
        self.book_table.column("Btype",width=100)
        self.book_table.pack(fill=BOTH,expand=1)
        self.book_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()



    def add_data(self):
            if self.var_consid.get()=="" or self.var_bookdate=="" or self.var_deldate=="":
                messagebox.showerror("Error","Please Enter the Required Fields",parent=self.root)
            else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Aditya8318@",database="lpg_booking")
                    my_cursor=conn.cursor()
                    my_cursor.execute("INSERT INTO booking values(%s,%s,%s,%s)",(self.var_consid.get(),self.var_bookdate.get(),self.var_deldate.get(),self.var_booking_type.get()))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Booking has been Done",parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Warning",f"Something went Wrong :{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Aditya8318@",database="lpg_booking")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from booking")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.book_table.delete(*self.book_table.get_children())
            for i in rows:
                self.book_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.book_table.focus()
        content=self.book_table.item(cursor_row)
        row=content["values"]

        self.var_consid.set(row[0]),
        self.var_bookdate.set(row[1]),
        self.var_deldate.set(row[2]),
        self.var_booking_type.set(row[3])

    def update(self):
        if self.var_consid=="":
            messagebox.showerror("Error","Please Enter Consumer ID ",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Aditya8318@",database="lpg_booking")
            my_cursor=conn.cursor()
            my_cursor.execute("UPDATE booking SET BookingDate=%s,DeliveryDate=%s,BookingType=%s WHERE ConsumerID=%s",(
                                                                                                                                                                                                                   
                                                                                                                                                                                            self.var_bookdate.get(),
                                                                                                                                                                                            self.var_deldate.get(),
                                                                                                                                                                                            self.var_booking_type.get(),
                                                                                                                                                                                            self.var_consid.get()
                                                                                                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer Details Successfully Updated",parent=self.root)

    def deletes(self):
        mdel=messagebox.askyesno("LPG Booking System","Are u Sure you want to Delete the selected Booking",parent=self.root)
        if mdel>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="Aditya8318@",database="lpg_booking")
            my_cursor=conn.cursor()
            query="delete from booking where ConsumerID=%s"
            value=(self.var_consid.get(),)
            my_cursor.execute(query,value)
        else:
            if not mdel:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        # self.var_cons.set(""),
        self.var_bookdate.set(""),
        self.var_deldate.set(""),
        self.var_consid.set(""),
        self.var_paidtax.set(""),
        self.var_total.set(""),
        self.var_booking_type.set("")
        self.var_subtotal.set("")

        

    #==================All data fetch=============
    def Fetch_cust(self):
       if self.var_consid.get()=="":
           messagebox.showerror("Error","Please enter Consumer ID",parent=self.root)
       else:
           conn=mysql.connector.connect(host="localhost",username="root",password="Aditya8318@",database="lpg_booking")
           my_cursor=conn.cursor()
           query=("select Name from customer where ConsumerID=%s")
           value =(self.var_consid.get(),)
           my_cursor.execute(query,value )
           row=my_cursor.fetchone()

           if row==None:
               messagebox.showerror("Error","This Consumer ID is not Found",parent=self.root)
           else:
               conn.commit()
               conn.close()
               
               showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
               showDataframe.place(x=450,y=82,width=300,height=180)

               lblName=Label(showDataframe,text="Name :",font =("arial",12,"bold"))
               lblName.place(x=0,y=0)

               lbl=Label(showDataframe,text=row,font =("arial",12,"bold"))
               lbl.place(x=90,y=0)
              
                 
                # insert{ command=self.Fetch_contact } in fetch data button line 1 before font
            #  =============GENDER================== 
               conn=mysql.connector.connect(host="localhost",username="root",password="Aditya8318@",database="lpg_booking")
               my_cursor=conn.cursor()
               query=("select Gender from customer where ConsumerID=%s")
               value =(self.var_consid.get(),)
               my_cursor.execute(query,value )
               row=my_cursor.fetchone()
               
               lblGender=Label(showDataframe,text="Gender :",font =("arial",12,"bold"))
               lblGender.place(x=0,y=30)

               lbl2=Label(showDataframe,text=row,font =("arial",12,"bold"))
               lbl2.place(x=90,y=30)

#===================MOBILE=====================
               conn=mysql.connector.connect(host="localhost",username="root",password="Aditya8318@",database="lpg_booking")
               my_cursor=conn.cursor()
               query=("select Mobile from customer where ConsumerID=%s")
               value =(self.var_consid.get(),)
               my_cursor.execute(query , value )
               row=my_cursor.fetchone()
               
               lblmobile=Label(showDataframe,text="Mobile :",font =("arial",12,"bold"))
               lblmobile.place(x=0,y=60)

               lbl3=Label(showDataframe,text=row,font =("arial",12,"bold"))
               lbl3.place(x=90,y=60)


#===================Email=====================
               conn=mysql.connector.connect(host="localhost",username="root",password="Aditya8318@",database="lpg_booking")
               my_cursor=conn.cursor()
               query=("select Email from customer where ConsumerID=%s")
               value =(self.var_consid.get(),)
               my_cursor.execute(query , value )
               row=my_cursor.fetchone()
               
               lblEmail=Label(showDataframe,text="Email :",font =("arial",12,"bold"))
               lblEmail.place(x=0,y=90)

               lbl4=Label(showDataframe,text=row,font =("arial",12,"bold"))
               lbl4.place(x=90,y=90)


# #====================IDPROOF====================
               conn=mysql.connector.connect(host="localhost",username="root",password="Aditya8318@",database="lpg_booking")
               my_cursor=conn.cursor()
               query=("select IDProof from customer where ConsumerID=%s")
               value =(self.var_consid.get(),)
               my_cursor.execute(query , value )
               row=my_cursor.fetchone()
               
               lblidpro=Label(showDataframe,text="ID Proof :",font =("arial",12,"bold"))
               lblidpro.place(x=0,y=120)

               lbl4=Label(showDataframe,text=row,font =("arial",12,"bold"))
               lbl4.place(x=90,y=120)

# #=======================ID NUMBER========================
               conn=mysql.connector.connect(host="localhost",username="root",password="Aditya8318@",database="lpg_booking")
               my_cursor=conn.cursor()
               query=("select IDNumber from customer where ConsumerID=%s")
               value =(self.var_consid.get(),)
               my_cursor.execute(query , value )
               row=my_cursor.fetchone()
               
               lblidnum=Label(showDataframe,text="ID Number :",font =("arial",12,"bold"))
               lblidnum.place(x=0,y=150)

               lbl5=Label(showDataframe,text=row,font =("arial",12,"bold"))
               lbl5.place(x=90,y=150)


    def search(self):
         conn=mysql.connector.connect(host="localhost",username="root",password="Aditya8318@",database="lpg_booking")
         my_cursor=conn.cursor()
         s1=str(self.search_var.get())
         s2=str(self.txt_search.get())
        #  query1="SELECT * from customer WHERE "+s1+"=%s"
        #  value=(s2,)
        #  my_cursor.execute(query1,value)
         t="SELECT * from booking WHERE "+s1+" LIKE '%"+s2+"%'"
         my_cursor.execute(t)
         rows=my_cursor.fetchall()
         if len(rows)!=0:
             self.book_table.delete(*self.book_table.get_children())
             for i in rows:
                 self.book_table.insert("",END,values=i)
             conn.commit()
         conn.close()


    def total(self):
        if(self.var_booking_type.get()=="Small"):
            q1=float(546)
            tax=float(0.18*q1)
            totalbill=float(tax+q1)
            self.var_paidtax.set(tax)
            self.var_total.set(totalbill)
            self.var_subtotal.set(q1)
        elif(self.var_booking_type.get()=="Medium"):
            q1=float(870)
            tax=float(0.18*q1)
            totalbill=float(tax+q1)
            self.var_paidtax.set(tax)
            self.var_total.set(totalbill)
            self.var_subtotal.set(q1)
        elif(self.var_booking_type.get()=="Large"):
            q1=float(1136)
            tax=float(0.18*q1)
            totalbill=float(tax+q1)
            self.var_paidtax.set(tax)
            self.var_total.set(totalbill)
            self.var_subtotal.set(q1)
        
if __name__=="__main__":
    root=Tk()
    obj=LPGbooking(root)
    root.mainloop()