from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox  
import mysql.connector
import numpy as np
from tabulate import tabulate

con=mysql.connector.connect(
    host="Localhost",
    user="root",
    passwd="161017",
    database="museum_management")
cur=con.cursor()
adminpasswd='1234'
checkfun=0
def rootmain():
    global root,checkfun
    root=Tk()
    checkfun=1
    root.title("GLOBAL MUSEUM")
    root.geometry("600x600+0+0")
    root.config(bg="sky blue")
    root.resizable(width=False,height=False)
    a=Label(root,text='\t         GLOBAL MUSEUMS            ',font=("Courier",15,"bold","underline"),bg="sky blue").place(x=0,y=30)
    b=Label(root,text='GLOBAL MUSEUMS.Ltd is focused on a singular task—finding the',font=("Courier",11,"italic"),bg="white").place(x=20,y=70)
    c=Label(root,text=' very best museums around the globe according to your Hobby.',font=("Courier",11,'italic'),bg="white").place(x=20,y=90)
    p1=PhotoImage(file="download1.png")
    l1=Label(image=p1)
    l1.place(x=0,y=0)
    button1=Button(root,text="LOGIN",command=login,font=("Courier",12,"bold"),background="red").place(x=150,y=450)
    button2=Button(root,text="SIGN UP",command=signup,font=("Courier",12,"bold"),background="red").place(x=250,y=450)
    button3=Button(root,text="ADMIN",command=adm_login,font=("courier",12,"bold"),background="red").place(x=350,y=450)
    p=PhotoImage(file="globall.png")
    l=Label(image=p)
    l.place(x=0,y=120)
    root.mainloop()
def authenticate(user,passwd):
    global usr
    query='select username from user where username =\'{}\''.format(user)
    cur.execute(query)
    rec=cur.fetchall()
    if rec!=[]:
        query='select password from user where username = \'{}\''.format(user)
        cur.execute(query)
        rec=cur.fetchall()
        if passwd==rec[0][0]:
            usr=user
            return 1
        else:
            return 0
    else:
        return 0
def fun1(x,y):
    global win1,b1,b2,usr,paswd,intr
    if authenticate(x,y)==1:
        usr=x
        paswd=y
        messagebox.showinfo('','Done')
        intr={1:"SCIENCE AND TECH",2:"SPORTS",3:"ART",4:"TOY"}
        ad_pas='1234'
        print("_"*120)
        print("                                            ╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗  ╔╦╗╔═╗")
        print("                                            ║║║║╣ ║  ║  ║ ║║║║║╣    ║ ║ ║")
        print("                                            ╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝   ╩ ╚═╝")
        print('    ██████╗ ██╗      ██████╗ ██████╗  █████╗ ██╗         ███╗   ███╗██╗   ██╗███████╗███████╗██╗   ██╗███╗   ███╗')
        print('   ██╔════╝ ██║     ██╔═══██╗██╔══██╗██╔══██╗██║         ████╗ ████║██║   ██║██╔════╝██╔════╝██║   ██║████╗ ████║')      
        print('   ██║  ███╗██║     ██║   ██║██████╔╝███████║██║         ██╔████╔██║██║   ██║███████╗█████╗  ██║   ██║██╔████╔██║')
        print('   ██║   ██║██║     ██║   ██║██╔══██╗██╔══██║██║         ██║╚██╔╝██║██║   ██║╚════██║██╔══╝  ██║   ██║██║╚██╔╝██║')
        print('   ╚██████╔╝███████╗╚██████╔╝██████╔╝██║  ██║███████╗    ██║ ╚═╝ ██║╚██████╔╝███████║███████╗╚██████╔╝██║ ╚═╝ ██║')
        print('    ╚═════╝ ╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝')
        print("_"*120)
        main()
    else:
         messagebox.showinfo('Key error','Wrong password')
         e2.delete(0,END)

def booking(cost,museum):
    n=int(input("\t\tENTER NO. OF VISITERS : "))
    price=n*cost
    gst=price*0.18
    transaction(name,museum,n,gst,price)
def option(table):
    qry="select mcode,museum_name from "+str(table)
    cur.execute(qry)
    rec=cur.fetchall()
    print("\t MUSEUMS AVAILABLE")
    l=[]
    no_museum=[]
    museum=[]
    print(tabulate([("MCODE","MUSEUM NAME")]+rec,tablefmt='grid',header='firstrow'))
    for i in range(len(rec)):
        l.append(rec[i][2])
        no_museum.append(i+1)
        museum.append(rec[i][0])

    ques=int(input('ENTER MUSEUM NUMBER : '))
    for i in no_museum:
        if ques==i:
            booking(l[ques-1],museum[i-1])
    
def billtk(p,t,typ,ch):
    win7=Tk()
    win7.title("||BILL||")
    win7.geometry("600x600+0+0")
    ime12=PhotoImage(file="bill.png")
    l12=Label(image=ime12)
    l12.place(x=0,y=0)
    a=Label(win7,text="VISITER NAME",font=('Courier New',9),fg='blue')
    b=Label(win7,text="MUSEUM  NAME",font=('Courier New',9),fg='blue')
    c=Label(win7,text="NUMBER OF PERSON",font=('Courier New',9),fg='blue')
    d=Label(win7,text="TOTAL",font=('Courier New',9),fg='blue')
    e=Label(win7,text="GST AMOUNT",font=('Courier New',9),fg='blue')
    f=Label(win7,text="NET PAYABLE AMT",font=('Courier New',9),fg='blue')
    a.place(x=190,y=250)
    b.place(x=190,y=270)
    c.place(x=190,y=290)
    d.place(x=190,y=310)
    e.place(x=190,y=330)
    f.place(x=190,y=350)
    b1=Label(win7,text=str(p),font=('Courier New',9),fg='blue')
    b2=Label(win7,text=str(t),font=('Courier New',9),fg='blue')
    b3=Label(win7,text=str(typ),font=('Courier New',9),fg='blue')
    b4=Label(win7,text=str(ch),font=('Courier New',9),fg='blue')
    b1.place(x=350,y=250)
    b2.place(x=350,y=270)
    b3.place(x=350,y=290)
    b4.place(x=350,y=310)
    win7.mainloop()
    
    
def transaction(name,museum,n,gst,price):
    print("\tName\t",name)
    print("\tMUSEUM NAME\t",museum)
    print("\tNUMBER OF PERSON",n)
    print("\tTOTAL",price)
    print("\tGST AMT",gst)
    print("\tNET PAYABLE AMOUNT",price+gst)
def bill(p,t,typ,ch):
    global user,n
    print("\t","_"*50)
    print("\t\t  BILL")
    print("\t","_"*50)
    qry="select * from user where username = '"+usr+"'"
    cur.execute(qry)
    rec=cur.fetchone()
    gst=t*0.18
    print("\t\t VISITER NAME        :  ", rec[2]+" "+rec[3])
    print("\t\t NUMBER OF VISITOR   :  ",n)
    print("\t\t CHARGE PER VISITOR  :  ",p)
    print("\t\t TOTAL CHARGE        :  ",t)
    print("\t\t GST(18%)            :  ",gst)
    print("\t\t GRAND TOTAL         :  ",gst+t)
    print()
    print("\t","_"*50)

def book(ch,typ):
    global n
    print('\t\t',"_"*80)
    n=int(input('\t\t\t\tENTER NUMBER OF VISITOR\t:'))
    qry='select charges from MUSEUM where MCODE = '+str(ch)
    cur.execute(qry)
    rec=cur.fetchone()
    price=rec[0]
    tot=n*price
    billtk(price,tot,typ,ch)
def fun2(typ):
    global lis
    print('\t\t',"_"*80)
    while True:
        ch=int(input("\t\t\t\tENTER YOUR CHOICE : "))
        if ch in lis:
            book(ch,typ)
            print('done')
            break
        elif ch not in lis:
            print('Invalid entry')
            ch=input("try again(y/n)")
            if ch in 'Yy':
                continue
            else:
                break
def fun(typ):
    global lis
    qry="select MCODE,MUSEUM_NAME,MUSEUM_ADDRESS,COUNTRY from MUSEUM where type = '{}'".format(typ)
    cur.execute(qry)
    rec=cur.fetchall()
    print('\t\t',"_"*80)
    print("\t\t\t\t\tMUSEUMS AS PER YOUR INTEREST")
    print('\t\t',"_"*80)
    lis=[]
    print(tabulate([("MCODE",'MUSEUM','ADDRESS','COUNTRY')]+rec,tablefmt='grid',headers='firstrow'))
    for i in rec:
        lis.append(i[0])
    #ch=int(input("\t\t\t\tENTER YOUR CHOICE : "))
    fun2(typ)

def main():
    global intr,win1
    win1.destroy()
    print()
    print('\t\t',"_"*80)
    for i in intr:
        print("\t\t\t\t\t  ",'(',i,')',intr[i])
    print('\t\t',"_"*80)
    ch=int(input("\t\t\t\t\tYOUR BASICS INTEREST : "))
    print('\t\t',"_"*80)
    if ch==1:
        fun(intr[1])
    elif ch==2:
        fun(intr[2])
    elif ch==3:
        fun(intr[3])
    elif ch==4:
        fun(intr[4])


def userr():
    global win1
    win1=Tk()
    win1.title('LOGIN')
    win1.config(bg='lightcoral')
    e1=Entry(win1,font=('segoe print',13))
    e2=Entry(win1,font=('segoe print',13),show='*')
    e1.grid(row=3,column=1)
    e2.grid(row=5,column=1)
    h1=Label(win1,text='Please login',font=('segoe print',28),bg='lightcoral')
    h1.grid(row=0,column=0,sticky=W)
    l1=Label(win1,text='Username\t:',font=('segoe print',17),bg='lightcoral')
    l2=Label(win1,text='Password\t:',font=('segoe print',17),bg='lightcoral')
    l1.grid(row=3,column=0,sticky=W)
    l2.grid(row=5,column=0,sticky=W)
    b1=Button(win1,text='Login',font=('segoe print',15),command=lambda:fun1(e1.get(),e2.get()))
    b1.grid(row=7,column=1)
    win1.mainloop()
def clear11(event):
    e2.delete(0,END)
    e2.config(show="*")
def clear12(event):
    e1.delete(0,END)
    e1.config(show="")    
def login():
    global win1,e2,e1,chk,root,checkfun
    global b1
    if checkfun==1:
        root.destroy()
    win1=Tk()
    win1.title("||USER LOGIN||")
    chk=IntVar()
    win1.geometry("600x600+0+0")
    p2=PhotoImage(file="login.png")
    l2=Label(image=p2)
    l2.place(x=0,y=0)
    e1=Entry(win1,font=('Calibri (Body)',13),bg='#D2D2D2',fg='#6C6D65',borderwidth=0)
    e2=Entry(win1,font=('Calibri (Body)',13),bg='#D2D2D2',fg='#6C6D65',borderwidth=0)  
    e1.place(x=205,y=222,width=235,height=40)
    e2.place(x=205,y=279,width=235,height=40)
    e1.insert(0,"USERNAME")
    e1.bind("<Button-1>",clear12)
    e2.insert(0,"ENTER PASSWORD")
    e2.bind("<Button-1>",clear11)
    check=Checkbutton(win1,text="SHOW PASSWORD",variable=chk,onvalue=1,offvalue=0,height=0,width=0,fg='white',bg='#14285B',command= lambda:show_psd(e2))
    check.place(x=158,y=420)
    b1=Button(win1,text='LOGIN',font=('Calibri (Body)',13),fg='white',bg='#FE5387',command=lambda:fun1(e1.get(),e2.get()))
    b1.place(x=157,y=343,width=290,height=41)
    but=Button(win1,text='BACK',font=('Calibri (Body)',10),fg='white',bg='#FE5387',command=lambda:leave1(win1))
    but.place(x=165,y=445)
    win1.mainloop()
def leave1(win1):
    win1.destroy()
    rootmain()
def show_psd(*a):
    if(chk.get()):
        for i in a:
            i.config(show="")
    else:
        for i in a:
            i.config(show="*")
    
def sub(usr,pas,fn,ln,phn,em,y,m,d,g):
    print(usr,pas,fn,ln,phn,em,y,m,d,g)
    global win3
    query='xc'
    if fn=='':
        messagebox.showinfo('','Enter Your First name !')
    elif ln=='':
        messagebox.showinfo('','Enter Your Lastname !')
    elif phn=='':
        messagebox.showinfo('','Enter Your Phone Number!')
    elif em=='':
        messagebox.showinfo('','Enter Your Email !')
    elif g not in ('Male','Female'):
        messagebox.showinfo('','Select Your Gender!')
    else:
        try:
            dob="{}-{}-{}".format(y,M[m],d)
        except KeyError:
            messagebox.showwarning('','Please Select DOB Correctly!!')
            return 0
        query="insert into users values('{}','{}','{}','{}',{},'{}','{}','{}')".format(usr,pas,fn,ln,phn,em,dob,g)
        try :
            cur.execute(query)
            messagebox.showinfo('','Registered successfully!!')
            win3.destroy()
        except mysql.connector.errors.ProgrammingError:
            messagebox.showerror('','Please fill all the details!!')
        except mysql.connector.errors.DataError:
            messagebox.showerror('','Follow DOB format - (YYYY-MM-DD)!!')
        except mysql.connector.errors.IntegrityError:
            messagebox.showwarning('','username already taken!!')
        con.commit()
    rootmain()

        
def dropdn(event):
    if int(event.type) is 4:
        a=event.widget
        a.event_generate('<Down>',when='head')

def signup():
    global win3,p3,firstname,lastname,pho_no,email,gender,username,passwd,root,M
    root.destroy()
    win3=Tk()
    win3.title("||SIGNUP||")
    win3.geometry("600x600+0+0")
    p3=PhotoImage(file="register.png")
    l3=Label(image=p3)
    l3.place(x=0,y=0)
    firstname=Entry(win3,font=('Calibri (Body)',16),borderwidth=0)
    lastname=Entry(win3,font=('Calibri (Body)',16),borderwidth=0)
    pho_no=Entry(win3,font=('Calibri (Body)',16),borderwidth=0)
    email=Entry(win3,font=('Calibri (Body)',16),borderwidth=0)
    gender=Combobox(win3,font=('Calibri (Body)',16),values=('Male','Female'))
    username=Entry(win3,font=('Calibri (Body)',16),borderwidth=0)
    passwd=Entry(win3,font=('Calibri (Body)',16),borderwidth=0)
    gender.set('Select Gender')
    YY=list(np.arange(1990,2019))
    M={'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
    MM=list(M.keys())
    DD=list(np.arange(1,32))
    yy=Combobox(win3,text='year',values=YY,font=('Calibri (Body)',16))
    mm=Combobox(win3,values=MM,font=('Calibri (Body)',16))
    dd=Combobox(win3,values=DD,font=('Calibri (Body)',16))
    yy.state(['readonly'])
    mm.state(['readonly'])
    dd.state(['readonly'])
    yy.bind('<Button-1>',dropdn)
    mm.bind('<Button-1>',dropdn)
    dd.bind('<Button-1>',dropdn)
    yy.set('Year')
    mm.set('Month')
    dd.set('Day')
    firstname.place(x=189,y=164,width=225,height=25)
    lastname.place(x=189,y=204,width=225,height=25)
    pho_no.place(x=189,y=244,width=225,height=25)
    email.place(x=189,y=284,width=225,height=25)
    yy.place(x=189,y=324,height=25,width=70)
    mm.place(x=262,y=324,height=25,width=80)
    dd.place(x=345,y=324,height=25,width=69)
    gender.place(x=189,y=364,width=225,height=25)
    username.place(x=189,y=404,width=225,height=25)
    passwd.place(x=189,y=444,width=225,height=25)
    firstname.insert(0,"First Name")
    firstname.bind("<Button-1>",clear2)
    lastname.insert(0,"Last Name")
    lastname.bind("<Button-1>",clear3)
    pho_no.insert(0,"Phone Number")
    pho_no.bind("<Button-1>",clear4)
    email.insert(0,"Email Address")
    email.bind("<Button-1>",clear5)
    username.insert(0,"Username")
    username.bind("<Button-1>",clear6)
    passwd.insert(0,"Password")
    passwd.bind("<Button-1>",clear7)
    b=Button(win3,text='SIGN UP',font=('Calibri (Body)',12,"bold"),fg='white',bg='#2881B8',command=lambda:sub(username.get(),passwd.get(),firstname.get(),lastname.get(),pho_no.get(),email.get(),yy.get(),mm.get(),dd.get(),gender.get())) 
    b.place(x=189,y=484,width=100,height=32)
    c=Button(win3,text="RETURN",font=('Calibri (Body)',12,"bold"),fg='white',bg='#2881B8',command=lambda:do11())
    c.place(x=314,y=484,width=100,height=32)
def clear7(event):
    passwd.delete(0,END)
    passwd.config(show='')
def clear6(event):
    username.delete(0,END)
    username.config(show='')
def clear5(event):
    email.delete(0,END)
    email.config(show="")
def clear4(event):
    pho_no.delete(0,END)
    pho_no.config(show='')
def clear3(event):
    lastname.delete(0,END)
    lastname.config(show="")
def clear2(event):
    firstname.delete(0,END)
    firstname.config(show='')    
def clear1(event):
    E.delete(0,END)
    E.config(show="*")
def a_login(E):
    global adminpasswd
    if E.get()==adminpasswd:
        messagebox.showinfo('','CORRECT PASSWORD')
        do()
    elif E.get()=='ENTER PASSWORD' or E.get()=='':
        messagebox.showerror('','PLEASE ENTER PASSWORD')
    else:
        messagebox.showwarning('',"INCORRECT PASSWORD")
        E.delete(0,END)
def adm_login():
    global win5,p5,E,check_var,a_b1,a_b2,a_b3,a_2,b8,bbb8,chp,l5,l,submit,check_show_psw,root
    root.destroy()
    win5=Tk()
    check_var=IntVar()
    win5.title("||ADMIN LOGIN||")
    win5.geometry("600x600+0+0")
    win5.resizable(width=False,height=False)
    p5=PhotoImage(file="adminlogin.png")
    l5=Label(image=p5)
    l5.place(x=0,y=0)
    E=Entry(win5,font=('Courier New',16))
    E.place(x=155,y=500)
    E.insert(0,"ENTER PASSWORD")
    E.bind("<Button-1>",clear1)
    submit=Button(win5,text="ENTER",command=lambda:a_login(E),font=('Courier',12,"bold"),bg="#F73C57")
    submit.place(x=430,y=500)
    check_show_psw = Checkbutton(win5,text="SHOW PASSWORD",variable=check_var,onvalue=1,offvalue=0,height=0,width=0,fg='black',bg='#13D5D5',command = lambda:show_hide_psd(E))
    check_show_psw.place(x =155,y =534)
    b8=Button(win5,text='BACK',font=('Courier',12),fg='black',bg='#F73C57',command=lambda:leave(win5))
    b8.place(x=250,y=565)
    chp=Button(win5,text='CHANGE PASSWORD',font=('Courier',12,'bold'),fg='black',bg='#F73C57')#,command=lambda:changep(win5)
    chp.place(x=335,y=535)
def leave(win5):
    win5.destroy()
    rootmain()
     
def do():
    global win5,p5,E,check_var,a_b1,a_b2,a_b3,a_2,b8,bbb8,chp,l5,l,submit,win6 
    CHEK=0
    win5.destroy()
    win6=Tk()
    win6.geometry('600x600+0+0')
    ime2=PhotoImage(file="adminlayout.png")
    l6=Label(image=ime2)
    l6.place(x=0,y=0)
    l=Label(win6,text='ADMIN OPTIONS',fg='black',bg='#A4DBE0',font=('segoe script',24))
    l.place(x=150,y=45)
    a_b1=Button(win6,text='SEE MUSEUM LIST',font=('Calibri (Body)',20),fg='blue',bg='white',command=display)
    a_b2=Button(win6,text='ADD MUSEUM',font=('Calibri (Body)',20),fg='blue',bg='white',command=add)
    a_b3=Button(win6,text='DELETE MUSEUM',font=('Calibri (Body)',20),fg='blue',bg='white',command=delete)
    bbb8=Button(win6,text='LOGOUT',font=('Calibri (Body)',12),fg='white',bg='#9B90BA',command=do1)
    a_b1.place(x=160,y=350,width=260,height=50)
    a_b2.place(x=160,y=420,width=260,height=50)
    a_b3.place(x=160,y=490,width=260,height=50)
    bbb8.place(x=530,y=565,width=70,height=35)
    win6.mainloop()
def display():
     win6.destroy()
     print('\t\t\t\t\t\t\t\t\t     ╔╦╗╦ ╦╔═╗╔═╗╦ ╦╔╦╗  ╦  ╦╔═╗╔╦╗')
     print('\t\t\t\t\t\t\t\t\t     ║║║║ ║╚═╗║╣ ║ ║║║║  ║  ║╚═╗ ║ ')
     print('\t\t\t\t\t\t\t\t\t     ╩ ╩╚═╝╚═╝╚═╝╚═╝╩ ╩  ╩═╝╩╚═╝ ╩ ')
     qry="select * from MUSEUM"
     cur.execute(qry)
     rec=cur.fetchall()
     print(tabulate([('MCODE','MUSEUM NAME','ADDRESS','COUNTRY','CHARGES','DAYS OPEN','TIMINGS','TYPE')]+rec,tablefmt='grid',headers='firstrow'))
     ch2=input("RETURN TO ADMIN OPTIONS (Y/N) : ")
     if ch2 in 'Yy':
         doagain()
def ins(typ):
    print("\t","_"*50)
    m_code=int(input  ('\t   ENTER MUSEUM CODE                         : '))
    m_nam=input       ('\t   ENTER MUSEUM NAME                         : ')
    m_add=input       ('\t   ENTER MUSEUM ADDRESS                      : ')
    m_cou=input       ('\t   ENTER MUSEUM COUNTRY                      : ')
    m_charge=int(input('\t   ENTER MUSEUM CHARGES   (Rs.)              : '))
    m_days=input      ('\t   ENTER MUSEUM DAYS OPEN (eg. _day to _day) : ')
    m_timng=input     ('\t   ENTER MUSEUM TIMINGS   (_A.M. to _P.M.)   : ')
    qry='insert into museum values ({},"{}","{}",{},"{}","{}","{}","{}")'.format(m_code,m_nam,m_add,m_cou,m_charge,m_days,m_timng,typ)
    print(qry)
    print("\t","_"*50)
    try:
        cur.execute(qry)
        con.commit()
        print('\t\tSUCCESSFULLY INSERTED !')
    except mysql.connector.errors.integrityerror:
        print('\t\tENTER PROPERLY ')
        ins(typ)
    print("\t","_"*50)
def add():
    global intr
    messagebox.showinfo('','Return To IDLE')
    win6.destroy()
    intr={1:"SCIENCE AND TECH",2:"SPORTS",3:"ART",4:"TOY"}
    print("\t","_"*50)
    print("\t\t   ╔═╗╔╦╗╔╦╗  ╔╦╗╦ ╦╔═╗╔═╗╦ ╦╔╦╗")
    print("\t\t   ╠═╣ ║║ ║║  ║║║║ ║╚═╗║╣ ║ ║║║║") 
    print("\t\t   ╩ ╩═╩╝═╩╝  ╩ ╩╚═╝╚═╝╚═╝╚═╝╩ ╩")
    print("\t","_"*50)
    for i in intr:
        print('\t\t    ','(',i,')',intr[i])
    print("\t","_"*50)
    op=int(input('\t    SELECT THE TYPE OF MUSEUM TO BE ADDED : '))
    print("\t","_"*50)
    CH='Y'
    while CH in 'Yy':
        if op==1:
            ins(intr[1])
        elif op==2:
            ins(intr[2])
        elif op==3:
            ins(intr[3])
        elif op==4:
            ins(intr[4])
        CH=input('\t\t\tADD MORE(Y/N)?  : ')
    ch2=input("RETURN TO ADMIN OPTIONS (Y/N) : ")
    if ch2 in 'Yy':
        doagain()
def dele(m):
    qry='delete museum from museum where mcode = '+str(m)
    cur.execute(qry)
    con.commit()
    print('\t\tRECORD SUCCESSFULLY DELETED')
    print("_"*62)
def delete():
    win6.destroy()
    qry='select mcode,museum_name from museum'
    ch='y'
    print("_"*62)
    print('           ╔╦╗╔═╗╦  ╔═╗╔╦╗╔═╗  ╔╦╗╦ ╦╔═╗╔═╗╦ ╦╔╦╗')
    print('            ║║║╣ ║  ║╣  ║ ║╣   ║║║║ ║╚═╗║╣ ║ ║║║║')
    print('           ═╩╝╚═╝╩═╝╚═╝ ╩ ╚═╝  ╩ ╩╚═╝╚═╝╚═╝╚═╝╩ ╩')
    print("_"*62)
    while ch in 'yY':
        cur.execute(qry)
        rec=cur.fetchall()
        print(tabulate([('MUSEUM CODE','MUSEUM NAME')]+rec,tablefmt="grid",headers="firstrow"))
        print("_"*62)
        mcode=int(input('\t   ENTER MUSEUM CODE TO BE DELETED : '))
        print("_"*62)
        dele(mcode)
        ch=input       ('\t\t   DELETE MORE(Y/N)? : ')
        print("_"*62)
    ch2=input("RETURN TO ADMIN OPTIONS (Y/N) : ")
    if ch2 in  'Yy':
        doagain()
def adm_login1():
    global win5,p5,E,check_var,a_b1,a_b2,a_b3,a_2,b8,bbb8,chp,l5,l,submit,check_show_psw,root
    win5=Tk()
    check_var=IntVar()
    win5.title("||ADMIN LOGIN||")
    win5.geometry("600x600+0+0")
    win5.resizable(width=False,height=False)
    p5=PhotoImage(file="adminlogin.png")
    l5=Label(image=p5)
    l5.place(x=0,y=0)
    E=Entry(win5,font=('Courier New',16))
    E.place(x=155,y=500)
    E.insert(0,"ENTER PASSWORD")
    E.bind("<Button-1>",clear1)
    submit=Button(win5,text="ENTER",command=lambda:a_login(E),font=('Courier',12,"bold"),bg="#F73C57")
    submit.place(x=430,y=500)
    check_show_psw = Checkbutton(win5,text="SHOW PASSWORD",variable=check_var,onvalue=1,offvalue=0,height=0,width=0,fg='black',bg='#13D5D5',command = lambda:show_hide_psd(E))
    check_show_psw.place(x =155,y =534)
    b8=Button(win5,text='BACK',font=('Courier',12),fg='black',bg='#F73C57',command=lambda:leave(win5))
    b8.place(x=250,y=565)
    chp=Button(win5,text='CHANGE PASSWORD',font=('Courier',12,'bold'),fg='black',bg='#F73C57')#,command=lambda:changep(win4)
    chp.place(x=335,y=535)
def do1():
    win6.destroy()
    #rootmain()
    adm_login1()
def do11():
    win3.destroy()
    rootmain()
def doagain():
    global win5,p5,E,check_var,a_b1,a_b2,a_b3,a_2,b8,bbb8,chp,l5,l,submit,win6 
    CHEK=0
    win6=Tk()
    win6.geometry('600x600+0+0')
    ime2=PhotoImage(file="adminlayout.png")
    l6=Label(image=ime2)
    l6.place(x=0,y=0)
    l=Label(win6,text='ADMIN OPTIONS',fg='black',bg='#A4DBE0',font=('segoe script',24))
    l.place(x=150,y=45)
    a_b1=Button(win6,text='SEE MUSEUM LIST',font=('Calibri (Body)',20),fg='blue',bg='white',command=display)
    a_b2=Button(win6,text='ADD MUSEUM',font=('Calibri (Body)',20),fg='blue',bg='white',command=add)
    a_b3=Button(win6,text='DELETE MUSEUM',font=('Calibri (Body)',20),fg='blue',bg='white',command=delete)
    bbb8=Button(win6,text='LOGOUT',font=('Calibri (Body)',12),fg='white',bg='#9B90BA',command=do1)
    a_b1.place(x=160,y=350,width=260,height=50)
    a_b2.place(x=160,y=420,width=260,height=50)
    a_b3.place(x=160,y=490,width=260,height=50)
    bbb8.place(x=530,y=565,width=70,height=35)
    win6.mainloop()    
def show_hide_psd(*a):
    if(check_var.get()):
        for i in a:
            i.config(show="")
    else:
        for i in a:
            i.config(show="*")
rootmain()    