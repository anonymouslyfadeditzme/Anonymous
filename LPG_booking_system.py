from tkinter import *
import urllib.request
from PIL import Image,ImageTk
from customer import Cust_win
from booking import LPGbooking
from complain import complain
urllib.request.urlretrieve(
  'https://iocl.com/images/indane_1.jpg',
   "indane1.png")
urllib.request.urlretrieve(
  'https://m.media-amazon.com/images/I/41epU94kA7L.jpg',
   "modiji.png")  
urllib.request.urlretrieve(
  'https://www.financialexpress.com/wp-content/uploads/2021/08/Ujjwala-Yojana-620x400.jpg',
   "modijigas.jpg")
urllib.request.urlretrieve(
  'https://5.imimg.com/data5/BB/MP/GLADMIN-61446788/auto-lpg-500x500.png',
   "img4.png")


urllib.request.urlretrieve(
  'https://english.newstrack.com/wp-content/uploads/2019/07/lpg-tanker-operators-commence-indefinite-strike-in-southern_2019.jpg',
   "cgas.jpg")
class LPG_Booking:
    def __init__(self,root):
        self.root=root
        self.root.title("LPG BOOKING SYSTEM")
        self.root.geometry("1550x800+0+0")

        #*************LOGO****************
        img1=Image.open(r"indane1.png")
        img1=img1.resize((200,140),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        labelimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        labelimg.place(x=0,y=0,width=200,height=140)


        #**************Right corner Modiji***********
        img2=Image.open(r"modiji.png")
        img2=img2.resize((200,140),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        labelimg1=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        labelimg1.place(x=1350,y=0,width=200,height=140)


        lbl_title=Label(self.root,text="LPG BOOKING SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="dark orange",bd=4,relief=RIDGE)
        lbl_title.place(x=202,y=0,width=1148,height=140)


        # *******************MAIN FRAME****************
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=170,width=1550,height=620)

        #*******************MENU***************
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="dark orange",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="ADD CUSTOMER",command=self.cust_details,width=22,font=("times new roman",14,"bold"),bg="black",fg="dark orange",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        book_btn=Button(btn_frame,text="BOOK LPG",command=self.booking,width=22,font=("times new roman",14,"bold"),bg="black",fg="dark orange",bd=0,cursor="hand1")
        book_btn.grid(row=1,column=0,pady=1)

        details_btn=Button(btn_frame,text="SUPPLIERS",width=22,font=("times new roman",14,"bold"),bg="black",fg="dark orange",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        Complain_btn=Button(btn_frame,text="COMPLAIN",command=self.complain,width=22,font=("times new roman",14,"bold"),bg="black",fg="dark orange",bd=0,cursor="hand1")
        Complain_btn.grid(row=3,column=0,pady=1)

        Exit_btn=Button(btn_frame,text="EXIT",command=quit,width=22,font=("times new roman",14,"bold"),bg="black",fg="dark orange",bd=0,cursor="hand1")
        Exit_btn.grid(row=4,column=0,pady=1)



        #************Right Side image*****************

        img3=Image.open(r"modijigas.jpg")
        img3=img3.resize((1325,490),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        labelimg3=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        labelimg3.place(x=225,y=0,width=1325,height=490)


        img4=Image.open(r"img4.png")
        img4=img4.resize((220,130),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        labelimg4=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        labelimg4.place(x=0,y=230,width=220,height=130)

        img5=Image.open(r"cgas.jpg")
        img5=img5.resize((220,130),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        labelimg5=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        labelimg5.place(x=0,y=365,width=220,height=130)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)

    def booking(self):
        self.new_window1=Toplevel(self.root)
        self.app1=LPGbooking(self.new_window1)
    
    def complain(self):
        self.new_window2=Toplevel(self.root)
        self.app2=complain(self.new_window2)

    
  

if  __name__ == "__main__":
    root=Tk()
    obj=LPG_Booking(root)
    root.mainloop()



