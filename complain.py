from tkinter import *
from tkinter import messagebox

class complain:
    def __init__(self,root):
        self.root=root
        self.root.title("Complain")
        self.root.geometry("800x500+400+150")
        def popup():
            message=messagebox.showinfo("Success","Complain Submitted Successfully",parent=self.root)


        lbl_complain=Label(self.root,text ="Type your complain here:",font=("arial",24),fg="brown").place (x=100,y=20)
        text_area=Text(self.root,bg="light yellow",font=("arial",18))
        text_area.place(x=100,y=70,width=600,height=330)
        btn_submit=Button(self.root,command=popup,text="Submit",font =("arial",18,"bold"),bg="black",fg="orange")
        btn_submit.place (x=310,y=420)
        

if  __name__ == "__main__":
    root=Tk()
    obj=complain(root)
    root.mainloop()
    

