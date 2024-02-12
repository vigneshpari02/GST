import tkinter
import tkinter as tk
from tkinter import*
from tkinter import ttk,font,messagebox
from PIL import ImageTk,Image
def ad_page(e):
    e.destroy() 
    e=Tk()
    e.geometry("1500x900")
    e.title("GST")
    frame1=Frame(e,width=1500,height=900,bg="#BEE4ED")
    f=font.Font(weight="normal",family="times new roman",size=20)
    frame1.pack()
    f1=font.Font(family="Times New Roman",size=20)
    x=Label(e,text="LIVE WIRE",fg="red",bg="#BEE4ED",font=f1).place(relx=.45,rely=.01)

    f1=font.Font(family="Times New Roman",size=20)
    x=Label(e,text=" @CopyRight by Vignesh",fg="red",bg="#BEE4ED",font=f1).place(relx=.39,rely=.87)

    tree = ttk.Treeview(e, columns=("Sheet No", "Name","Age","Phone No","O.F"), show="headings")
    tree.heading("#1", text="Staff No")
    tree.heading("#2", text="Name")
    tree.heading("#3", text="Age")
    tree.heading("#4", text="Phone No")
    tree.heading("#5", text="O.F")
    tree.column("#1", width=55)
    tree.place(relx=.10,rely=.10,height=500,width=1100)
    read_button = Button(e, text="Read File", command=lambda :ad_page(e))
    read_button.place(relx=.46,rely=.80)
    e.mainloop()


def std_register(a): 
    a.destroy() 
    a=Tk()
    a.geometry("1500x900")
    a.title("GST")
    frame1=Frame(a,width=1500,height=900,bg="#BEE4ED")
    f=font.Font(weight="normal",family="times new roman",size=20)
    frame1.pack()
    frame=Frame(a,width=500,height=590,bg="#1ABC9C").place(relx=.33,rely=.07)
    f=font.Font(a,weight="bold",family="times new roman",size=20)
    l=Label(frame,text="STUDENT REGISTER",font=f,bg="#1ABC9C").place(relx=.40,rely=.12)

    f=font.Font(a,weight="bold",family="times new roman",size=17)
    l=Label(frame,text="Name:",font=f,bg="#1ABC9C").place(relx=.38,rely=.23)
    l=Label(frame,text="Age:",font=f,bg="#1ABC9C").place(relx=.38,rely=.32)
    l=Label(frame,text="Education:",font=f,bg="#1ABC9C").place(relx=.38,rely=.43)
    l=Label(frame,text="Course:",font=f,bg="#1ABC9C").place(relx=.38,rely=.54)
    l=Label(frame,text="PhoneNo:",font=f,bg="#1ABC9C").place(relx=.38,rely=.65)
    

    l1=Entry(frame)
    l1.place(relx=.50,rely=.24)
    l2=Entry(frame)
    l2.place(relx=.50,rely=.33)
    l3=Entry(frame)
    l3.place(relx=.50,rely=.44)
    l4=Entry(frame)
    l4.place(relx=.50,rely=.55)
    l5=Entry(frame)
    l5.place(relx=.50,rely=.66)
        
    def sreg(Name,Age,Education,Course,PhoneNo):
        import pymysql as mysql
        connection = mysql.connect(host="localhost", user="root", password="livewire", database="proemp")
        cursor=connection.cursor()
        s="insert into stdreg(Name, Age, Education, Course, PhoneNo) values(%s,%s,%s,%s,%s)"
        t=(Name,Age,Education,Course,PhoneNo)
        cursor.execute(s,t)
        connection.commit()
        messagebox.showinfo( "Success", "User Insert Successfully")
        l1.delete(0,END)
        l2.delete(0,END)
        l3.delete(0,END)
        l4.delete(0,END)
        l5.delete(0,END)
    
        
    f1=font.Font(weight="bold",family="Bodoni MT",size=17)
    b1=Button(frame,text="Register",font=f1,bg="#FF6347",activebackground="#FC92C4",width=10,command=lambda: sreg(l1.get(),l2.get(),l3.get(),l4.get(),l5.get()))
    b1.place(relx=.45,rely=.77)
    f1=font.Font(family="Times New Roman",size=20)
    x=Label(a,text="LIVE WIRE",fg="red",bg="#BEE4ED",font=f1).place(relx=.45,rely=.01)

    f1=font.Font(family="Times New Roman",size=20)
    x=Label(a,text=" @CopyRight Vignesh",fg="red",bg="#BEE4ED",font=f1).place(relx=.39,rely=.87)
    a.mainloop()


def python(a):
    a.destroy()
    a=Tk()
    a.geometry("1500x720")
    a.title("GST")
    frame=Frame(a,width=1500,height=900,bg="#E6E6FA")
    f=font.Font(weight="bold",family="times new roman",size=25)
    frame.pack()
    x=Label(frame,text="PYTHON",font=f,bg="#E6E6FA")
    x.configure(fg="Blue")
    x.place(relx=.43,rely=.03)

    img = Image.open("guido-headshot.jpg")
    img = img.resize((400,300))
    img = ImageTk.PhotoImage(img)
    l=Label(a,image=img).place(relx=0.05,rely=0.17)

    f=font.Font(family="Times New Roman",size=16)
    t="""Livewire represents an electrifying blend of high-end skills, expert trainers.
    Our goal as a part of CADD Centre, a global skill development ,  
    prepare you, the students, for exciting careers in emerging technologies.."""
    l=Label(a,text=t,font=f,bg="#E6E6FA").place(relx=.37,rely=.25)

    f=font.Font(family="Times New Roman",size=16)
    t="""We provide hundreds of courses in the most advanced subjects in IT,
    , including data science, machine learning, IoT, artificial intelligence, 
    The courses prepare  for careers in industries software development, automobiles."""
    l=Label(a,text=t,font=f,bg="#E6E6FA").place(relx=.36,rely=.40)
    f=font.Font(family="Times New Roman",size=20)

    b=Button(frame,text="Go Back",font=f,fg="white",bg="blue",command=lambda:course(a)).place(relx=.57,rely=.55)
    
    x=Label(a,text=" @CopyRight Vignesh",fg="Blue",bg="#E6E6FA",font=f).place(relx=.41,rely=.87)
    a.mainloop()


def java(a):
    a.destroy()
    a=Tk()
    a.geometry("1500x720")
    a.title("GST")
    frame=Frame(a,width=1500,height=900,bg="#E6E6FA")
    f=font.Font(weight="bold",family="times new roman",size=25)
    frame.pack()
    x=Label(frame,text="JAVA",font=f,bg="#E6E6FA")
    x.configure(fg="Blue")
    x.place(relx=.43,rely=.03)

    img = Image.open("download.jpg")
    img = img.resize((300,300))
    img = ImageTk.PhotoImage(img)
    l=Label(a,image=img).place(relx=0.05,rely=0.17)

    f=font.Font(family="Times New Roman",size=16)
    t="""Livewire represents an electrifying blend of high-end skills, expert trainers.
    Our goal as a part of CADD Centre, a global skill development ,  
    prepare you, the students, for exciting careers in emerging technologies.."""
    l=Label(a,text=t,font=f,bg="#E6E6FA").place(relx=.37,rely=.25)

    f=font.Font(family="Times New Roman",size=16)
    t="""We provide hundreds of courses in the most advanced subjects in IT,
    , including data science, machine learning, IoT, artificial intelligence, 
    The courses prepare  for careers in industries software development, automobiles."""
    l=Label(a,text=t,font=f,bg="#E6E6FA").place(relx=.36,rely=.40)
    f=font.Font(family="Times New Roman",size=20)

    b=Button(frame,text="Go Back",font=f,fg="white",bg="blue",command=lambda:course(a)).place(relx=.57,rely=.55)
    
    x=Label(a,text=" @CopyRight Vignesh",fg="Blue",bg="#E6E6FA",font=f).place(relx=.41,rely=.87)
    a.mainloop()


def html(a):
    a.destroy()
    a=Tk()
    a.geometry("1500x720")
    a.title("GST")
    frame=Frame(a,width=1500,height=900,bg="#E6E6FA")
    f=font.Font(weight="bold",family="times new roman",size=25)
    frame.pack()
    x=Label(frame,text="HTML",font=f,bg="#E6E6FA")
    x.configure(fg="Blue")
    x.place(relx=.43,rely=.03)

    img = Image.open("hh.jpg")
    img = img.resize((400,300))
    img = ImageTk.PhotoImage(img)
    l=Label(a,image=img).place(relx=0.05,rely=0.17)

    f=font.Font(family="Times New Roman",size=16)
    t="""Livewire represents an electrifying blend of high-end skills, expert trainers.
    Our goal as a part of CADD Centre, a global skill development ,  
    prepare you, the students, for exciting careers in emerging technologies.."""
    l=Label(a,text=t,font=f,bg="#E6E6FA").place(relx=.37,rely=.25)

    f=font.Font(family="Times New Roman",size=16)
    t="""We provide hundreds of courses in the most advanced subjects in IT,
    , including data science, machine learning, IoT, artificial intelligence, 
    The courses prepare  for careers in industries software development, automobiles."""
    l=Label(a,text=t,font=f,bg="#E6E6FA").place(relx=.36,rely=.40)
    f=font.Font(family="Times New Roman",size=20)

    b=Button(frame,text="Go Back",font=f,fg="white",bg="blue",command=lambda:course(a)).place(relx=.57,rely=.55)
    
    x=Label(a,text=" @CopyRight Vignesh",fg="Blue",bg="#E6E6FA",font=f).place(relx=.41,rely=.87)
    a.mainloop()

""" 

def calculate_gst(a):
    try:
        amount = float(amount_entry.get())
        rate = float(rate_entry.get())

        gst_amount = (amount * rate) / 100
        total_amount = amount + gst_amount

        gst_label.config(text=f"GST Amount: {gst_amount:.2f}")
        total_label.config(text=f"Total Amount: {total_amount:.2f}")
    except ValueError:
        gst_label.config(text="Invalid Input")
        total_label.config(text="Invalid Input")

app = tk.Tk()
app.title("GST Calculator")
app.geometry("1500x720")

amount_label = tk.Label(app, text="Enter Amount:")
amount_label.place(relx=.37, rely=.20)

amount_entry = tk.Entry(app)
amount_entry.place(relx=.52, rely=.20)

rate_label = tk.Label(app, text="Enter GST Rate (%):")
rate_label.place(relx=.37, rely=.30)

rate_entry = tk.Entry(app)
rate_entry.place(relx=.52, rely=.30)

gst_button = tk.Button(app, text="Calculate GST", command=calculate_gst)
gst_button.place(relx=.45, rely=.40)

gst_label = tk.Label(app, text="")
gst_label.place(relx=.45, rely=.50)

total_label = tk.Label(app, text="")
total_label.place(relx=.45, rely=.60) 

"""

def page(a):
    a.destroy()
    a=Tk()
    a.geometry("1500x720")
    a.title("GST")
    frame=Frame(a,width=1500,height=900,bg="#E6E6FA")
    f=font.Font(weight="bold",family="times new roman",size=25)
    frame.pack()
    x=Label(frame,text="COURSES",font=f,bg="#E6E6FA")
    x.configure(fg="Blue")
    x.place(relx=.43,rely=.03)

def course(a):
    a.destroy()
    a=Tk()
    a.geometry("1500x720")
    a.title("GST")
    frame=Frame(a,width=1500,height=900,bg="#E6E6FA")
    f=font.Font(weight="bold",family="times new roman",size=25)
    frame.pack()
    x=Label(frame,text="COURSES",font=f,bg="#E6E6FA")
    x.configure(fg="Blue")
    x.place(relx=.43,rely=.03)

    f=font.Font(weight="bold",family="Times New Roman",size=16)
    t="COMPUTER EDUCTION CENTRE"
    l=Label(a,text=t,font=f,bg="#E6E6FA").place(relx=.37,rely=.12)

    frame=Frame(a,width=300,height=350,bg="#ADE6D8").place(relx=.10,rely=.3)
    f=font.Font(a,weight="bold",family="Times New Roman",size=20)
    l=Label(frame,text="Python",font=f,bg="#ADE6D8").place(relx=.18,rely=.3)
    
    e=font.Font(a,family="Times New Roman",size=15)
    l=Label(frame,text="Python is a high-level",font=e,bg="#ADE6D8") .place(relx=.14,rely=.4)
    l=Label(frame,text="general-purpose program",font=e,bg="#ADE6D8") .place(relx=.14,rely=.44)
    l=Label(frame,text="language. Python is dyn",font=e,bg="#ADE6D8") .place(relx=.14,rely=.48)
    l=Label(frame,text="amically typed and gar",font=e,bg="#ADE6D8") .place(relx=.14,rely=.52)
    b=Button(frame,text="Learn More",font=e,fg="white",bg="blue",command=lambda:python(a)).place(relx=.17,rely=.7)

    frame=Frame(a,width=300,height=350,bg="#ADE6D8").place(relx=.40,rely=.3)
    f=font.Font(a,weight="bold",family="Times New Roman",size=20)
    l=Label(frame,text="Java",font=f,bg="#ADE6D8").place(relx=.48,rely=.3)
    
    e=font.Font(a,family="Times New Roman",size=15)
    l=Label(frame,text="JAVA is a high-level",font=e,bg="#ADE6D8") .place(relx=.44,rely=.4)
    l=Label(frame,text="general-purpose program",font=e,bg="#ADE6D8") .place(relx=.44,rely=.44)
    l=Label(frame,text="language. JAVA is dyn",font=e,bg="#ADE6D8") .place(relx=.44,rely=.48)
    l=Label(frame,text="amically typed and gar",font=e,bg="#ADE6D8") .place(relx=.44,rely=.52)
    b=Button(frame,text="Learn More",font=e,fg="white",bg="blue",command=lambda:java(a)).place(relx=.47,rely=.7)

    frame=Frame(a,width=300,height=350,bg="#ADE6D8").place(relx=.70,rely=.3)
    f=font.Font(a,weight="bold",family="Times New Roman",size=20)
    l=Label(frame,text="HTML",font=f,bg="#ADE6D8").place(relx=.78,rely=.3)
    
    e=font.Font(a,family="Times New Roman",size=15)
    l=Label(frame,text="HTML is a high-level",font=e,bg="#ADE6D8") .place(relx=.74,rely=.4)
    l=Label(frame,text="general-purpose program",font=e,bg="#ADE6D8") .place(relx=.74,rely=.44)
    l=Label(frame,text="language. HTML is dyn",font=e,bg="#ADE6D8") .place(relx=.74,rely=.48)
    l=Label(frame,text="amically typed and gar",font=e,bg="#ADE6D8") .place(relx=.74,rely=.52)
    b=Button(frame,text="Learn More",font=e,fg="white",bg="blue",command=lambda:html(a)).place(relx=.77,rely=.7)

    f=font.Font(family="Times New Roman",size=20)
    x=Label(a,text=" @CopyRight Vignesh",fg="Blue",bg="#E6E6FA",font=f).place(relx=.41,rely=.87)
    a.mainloop()


def std_page(a,data):
    a.destroy() 
    a=Tk()
    a.geometry("1500x900")
    a.title("GST")
    frame1=Frame(a,width=1500,height=900,bg="#BEE4ED")
    f=font.Font(weight="normal",family="times new roman",size=20)
    f1=font.Font(weight="bold",family="Bodoni MT",size=20)
    data1=data[0]
    a="Name : "+data1[0]
    label=Label(frame1,text=a,font=f1,bg="#BEE4ED") 
    label.place(relx=.39,rely=.2)
    a="Age : "+str(data1[1])
    label=Label(frame1,text=a,font=f1,bg="#BEE4ED")
    label.place(relx=.39,rely=.3)
    a="Education : "+data1[2]
    label=Label(frame1,text=a,font=f1,bg="#BEE4ED")
    label.place(relx=.39,rely=.4)
    a="Course: "+data1[3]
    label=Label(frame1,text=a,font=f1,bg="#BEE4ED")
    label.place(relx=.39,rely=.5)
    a="Phone No : "+str(data1[4])
    label=Label(frame1,text=a,font=f1,bg="#BEE4ED")
    label.place(relx=.39,rely=.6)  
   
    frame1.pack()
  

    f1=font.Font(family="Times New Roman",size=20)
    x=Label(a,text="LIVE WIRE",fg="red",bg="#BEE4ED",font=f1).place(relx=.45,rely=.01)

    f1=font.Font(family="Times New Roman",size=20)
    x=Label(a,text=" @CopyRight Vignesh",fg="red",bg="#BEE4ED",font=f1).place(relx=.39,rely=.87)
    a.mainloop() 


def fees(a):
    a.destroy()
    a=Tk()
    a.geometry("1500x720")
    a.title("GST")
    frame=Frame(a,width=1500,height=900,bg="#E6E6FA")
    f=font.Font(weight="bold",family="times new roman",size=25)
    frame.pack()
    x=Label(frame,text="FEES",font=f,bg="#E6E6FA")
    x.configure(fg="Blue")
    x.place(relx=.43,rely=.03)

    f=font.Font(a,weight="bold",family="Times New Roman",size=18)
    l=Label(frame,text="Sheet No",font=f,bg="#E6E6FA").place(relx=.14,rely=.15)

    f=font.Font(a,weight="bold",family="Times New Roman",size=18)
    l=Label(frame,text="Name",font=f,bg="#E6E6FA").place(relx=.14,rely=.30)

    f=font.Font(a,weight="bold",family="Times New Roman",size=18)
    l=Label(frame,text="Age",font=f,bg="#E6E6FA").place(relx=.14,rely=.45)

    f=font.Font(a,weight="bold",family="Times New Roman",size=18)
    l=Label(frame,text="Phone No",font=f,bg="#E6E6FA").place(relx=.14,rely=.60)

    f=font.Font(a,weight="bold",family="Times New Roman",size=18)
    l=Label(frame,text="E-Mail",font=f,bg="#E6E6FA").place(relx=.54,rely=.15)

    f=font.Font(a,weight="bold",family="Times New Roman",size=18)
    l=Label(frame,text="Original Fees",font=f,bg="#E6E6FA").place(relx=.54,rely=.30)

    f=font.Font(a,weight="bold",family="Times New Roman",size=18)
    l=Label(frame,text="Offer Fees",font=f,bg="#E6E6FA").place(relx=.54,rely=.45)

    f=font.Font(a,weight="bold",family="Times New Roman",size=18)
    Button(frame,text="Get",font=f,bg="Red",fg="white").place(relx=.82,rely=.45)

    f=font.Font(a,weight="bold",family="Times New Roman",size=18)
    l=Label(frame,text="GST",font=f,bg="#E6E6FA").place(relx=.54,rely=.60)

    f=font.Font(a,weight="bold",family="Times New Roman",size=18)
    l=Label(frame,text="Total Amount",font=f,bg="#E6E6FA").place(relx=.36,rely=.75)

    f=font.Font(a,weight="bold",family="Times New Roman",size=18)
    Button(frame,text="Register",font=f,bg="Blue",fg="white",command=lambda:std_register(a)).place(relx=.41,rely=.82)

    l1=Entry(frame)
    l1.place(relx=.24,rely=.15)
    l2=Entry(frame)
    l2.place(relx=.24,rely=.30)
    l3=Entry(frame)
    l3.place(relx=.24,rely=.45)
    l4=Entry(frame)
    l4.place(relx=.24,rely=.60)

    l5=Entry(frame)
    l5.place(relx=.69,rely=.15)
    l6=Entry(frame)
    l6.place(relx=.69,rely=.30)
    l7=Entry(frame)
    l7.place(relx=.69,rely=.45)
    l8=Entry(frame)
    l8.place(relx=.69,rely=.60)

    l9=Entry(frame)
    l9.place(relx=.49,rely=.75)

    x=Label(a,text=" @CopyRight Vignesh",fg="Blue",bg="#E6E6FA",font=f).place(relx=.41 ,rely=.89)
    a.mainloop()


def stf_log(a1,b1,a):
    if(a1=="" and b1==""):
        ad_page(a)
    else:
      stf_log(a)


def stafflog(a):
    a.destroy()
    a=Tk()
    a.geometry("1500x720")
    a.title("GST")
    frame=Frame(a,width=1500,height=900,bg="#E6E6FA")
    f=font.Font(weight="bold",family="times new roman",size=25)
    frame.pack()
    x=Label(frame,text="COURSES",font=f,bg="#E6E6FA")
    x.configure(fg="Blue")
    x.place(relx=.43,rely=.03)

    frame=Frame(a,width=500,height=250,bg="#C6E2FF").place(relx=.35,rely=.3)
    f=font.Font(a,weight="bold",family="Times New Roman",size=20)
    l=Label(frame,text="STAFF LOGIN",font=f,bg="#C6E2FF").place(relx=.45,rely=.3)
    
    e=font.Font(a,weight="bold",family="Times New Roman",size=15)
    l=Label(frame,text="Staff ID:",font=e,bg="#C6E2FF") .place(relx=.38,rely=.4)
    l=Label(frame,text="Password:",font=e,bg="#C6E2FF").place(relx=.38,rely=.5)
    
    l1=Entry(frame)
    l1.place(relx=.48,rely=.41)
    l2=Entry(frame)
    l2.place(relx=.48,rely=.51)
    b=Button(frame,text="Login",font=e,fg="white",bg="blue",command=lambda:stf_log(l1.get(),l2.get(),a)).place(relx=.48,rely=.57)

    frame=Frame(a,width=1500,height=50)
    frame.pack()
    frame.place(relx=.0,rely=.87)
    f=font.Font(a,weight="bold",family="Times New Roman",size=15)
    x=Label(frame,text=" @CopyRight Vignesh",font=f)
    x.configure(fg="black")
    x.place(relx=.40,rely=.1)
    a.mainloop()


def Home():
    a=Tk()
    a.geometry("1500x720")
    a.title("GST")
    frame=Frame(a,width=1500,height=900,bg="#E6E6FA")
    f=font.Font(weight="bold",family="times new roman",size=25)
    frame.pack()
    x=Label(frame,text="LIVEWIRE",font=f,bg="#E6E6FA")
    x.configure(fg="Blue")
    x.place(relx=.43,rely=.03)

    f=font.Font(family="Times New Roman",size=16)
    t="""Livewire represents an electrifying blend of high-end skills, expert trainers.
    Our goal as a part of CADD Centre, a global skill development ,  
    prepare you, the students, for exciting careers in emerging technologies.."""
    l=Label(a,text=t,font=f,bg="#E6E6FA").place(relx=.25,rely=.25)

    f=font.Font(family="Times New Roman",size=16)
    t="""We provide hundreds of courses in the most advanced subjects in IT,
    , including data science, machine learning, IoT, artificial intelligence, 
    The courses prepare  for careers in industries software development, automobiles."""
    l=Label(a,text=t,font=f,bg="#E6E6FA").place(relx=.25,rely=.40)

    b=Button(a,text="Courses",font=f,bg="Red",fg="white",width=15,command=lambda:course(a)).place(relx=.18,rely=.70)
    c=Button(a,text="Fees",font=f,bg="Red",fg="white",width=15,command=lambda:fees(a)).place(relx=.38,rely=.70)
    d=Button(a,text="Staff Login",font=f,bg="Red",fg="white",width=15,command=lambda:stafflog(a)).place(relx=.58,rely=.70)
 
    f=font.Font(family="Times New Roman",size=20)
    x=Label(a,text=" @CopyRight Vignesh",fg="Blue",bg="#E6E6FA",font=f).place(relx=.41,rely=.87)

    a.mainloop()
Home() 