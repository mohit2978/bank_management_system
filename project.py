from tkinter import *
import sqlite3
import time
import datetime
from time import strftime
db=sqlite3.connect('Bank.db')


def read():
     
     pin=e2.get()
     passw=e212.get()
     m=db.execute('''select * from records where pin=(?) and password=(?)''',(pin,passw))
     for record in m:
                global na
                pos1.configure(text='You are logged in as {}'.format(record[0]) ,font=(30))
                pos2.configure(text='Your Current Balance is {}'.format(record[2]),font=(30))


     if (pin=='')|(passw==''):
          pos5.configure(text='Please fill the correct PIN or Password',font=(30),bg='red',fg='yellow') 


def loan():
     pin=e2.get()
     passw=e212.get()
     m=db.execute('''select * from records where pin=(?) and password=(?)''',(pin,passw))
     for record in m:
                global na
                na=record[0]
     s=e1.get()
     y=loant.get()
     t=loany.get()
     if (y==1)&(t==6):
          n=(int(s)*9)/100
          total=int(s)+n
          payable=total/6
          pos3.configure(text='Your payable interest is :{}'.format(n),font=(24))
          pos4.configure(text='Total amount:{}'.format(total),font=(24))
          pos5.configure(text='Total amount every month:{}'.format(payable),font=(24))

     if (y==1)&(t==12):
          n=(int(s)*9)/100
          total=int(s)+n
          payable=total/12
          pos3.configure(text='Your payable interest is :{}'.format(n),font=(24))
          pos4.configure(text='Total amount:{}'.format(total),font=(24))
          pos5.configure(text='Total amount every month:{}'.format(payable),font=(24))

          
     if (y==1)&(t==18):
          n=(int(s)*9)/100
          total=int(s)+n
          payable=total/18
          pos3.configure(text='Your payable interest is :{}'.format(n),font=(24))
          pos4.configure(text='Total amount:{}'.format(total),font=(24))
          pos5.configure(text='Total amount every month:{}'.format(payable),font=(24))

          
     if (y==1)&(t==24):
          n=(int(s)*9)/100
          total=int(s)+n
          payable=total/24
          pos3.configure(text='Your payable interest is :{}'.format(n),font=(24))
          pos4.configure(text='Total amount:{}'.format(total),font=(24))
          pos5.configure(text='Total amount every month:{}'.format(payable),font=(24))

     if (y==2)&(t==6):
          n=(int(s)*10)/100
          total=int(s)+n
          payable=total/6
          pos3.configure(text='Your payable interest is :{}'.format(n),font=(24))
          pos4.configure(text='Total amount:{}'.format(total),font=(24))
          pos5.configure(text='Total amount every month:{}'.format(payable),font=(24))


     if (y==2)&(t==12):
          n=(int(s)*10)/100
          total=int(s)+n
          payable=total/12
          pos3.configure(text='Your payable interest is :{}'.format(n),font=(24))
          pos4.configure(text='Total amount:{}'.format(total),font=(24))
          pos5.configure(text='Total amount every month:{}'.format(payable),font=(24))


     if (y==2)&(t==18):
          n=(int(s)*10)/100
          total=int(s)+n
          payable=total/18
          pos3.configure(text='Your payable interest is :{}'.format(n),font=(24))
          pos4.configure(text='Total amount:{}'.format(total),font=(24))
          pos5.configure(text='Total amount every month:{}'.format(payable),font=(24))

          
     if (y==2)&(t==24):
          n=(int(s)*10)/100
          total=int(s)+n
          payable=total/24
          pos3.configure(text='Your payable interest is :{}'.format(n),font=(24))
          pos4.configure(text='Total amount:{}'.format(total),font=(24))
          pos5.configure(text='Total amount every month:{}'.format(payable),font=(24))

         
     if (y==3)&(t==6):
          n=(int(s)*7)/100
          total=int(s)+n
          payable=total/6
          pos3.configure(text='Your payable interest is :{}'.format(n),font=(24))
          pos4.configure(text='Total amount:{}'.format(total),font=(24))
          pos5.configure(text='Total amount every month:{}'.format(payable),font=(24))


     if (y==3)&(t==12):
          n=(int(s)*7)/100
          total=int(s)+n
          payable=total/12
          pos3.configure(text='Your payable interest is :{}'.format(n),font=(24))
          pos4.configure(text='Total amount:{}'.format(total),font=(24))
          pos5.configure(text='Total amount every month:{}'.format(payable),font=(24))


     if (y==3)&(t==18):
          n=(int(s)*7)/100
          total=int(s)+n
          payable=total/18
          pos3.configure(text='Your payable interest is :{}'.format(n),font=(24))
          pos4.configure(text='Total amount:{}'.format(total),font=(24))
          pos5.configure(text='Total amount every month:{}'.format(payable),font=(24))


     if (y==3)&(t==24):
          n=(int(s)*7)/100
          total=int(s)+n
          payable=total/24
          pos3.configure(text='Your payable interest is :{}'.format(n),font=(24))
          pos4.configure(text='Total amount:{}'.format(total),font=(24))
          pos5.configure(text='Total amount every month:{}'.format(payable),font=(24))

     if (y==4)&(t==6):
          n=(int(s)*10)/100
          total=int(s)+n
          payable=total/6
          pos3.configure(text='Your payable interest is :{}'.format(n),font=(24))
          pos4.configure(text='Total amount:{}'.format(total),font=(24))
          pos5.configure(text='Total amount every month:{}'.format(payable),font=(24))


     if (y==4)&(t==12):
          n=(int(s)*10)/100
          total=int(s)+n
          payable=total/12
          pos3.configure(text='Your payable interest is :{}'.format(n),font=(24))
          pos4.configure(text='Total amount:{}'.format(total),font=(24))
          pos5.configure(text='Total amount every month:{}'.format(payable),font=(24))

     if (y==4)&(t==18):
          n=(int(s)*10)/100
          total=int(s)+n
          payable=total/18
          pos3.configure(text='Your payable interest is :{}'.format(n),font=(24))
          pos4.configure(text='Total amount:{}'.format(total),font=(24))
          pos5.configure(text='Total amount every month:{}'.format(payable),font=(24))

     if (y==4)&(t==24):
          n=(int(s)*10)/100
          total=int(s)+n
          payable=total/24
          pos3.configure(text='Your payable interest is :{}'.format(n),font=(24))
          pos4.configure(text='Total amount:{}'.format(total),font=(24))
          pos5.configure(text='Total amount every month:{}'.format(payable),font=(24))
         
     db.execute('''insert into loan values(?,?,?,?,?,?,?)''',(pin,na,s,n,total,t,payable,))
     db.commit()
def trans():

     pin=e2.get()
     passw=e212.get()
     m=db.execute('''select * from records where pin=(?) and password=(?)''',(pin,passw))
     for record in m:
                nt=record[2]


     if (pin=='')|(passw==''):
          pos5.configure(text='Please fill the correct PIN or Password',font=(30),bg='red',fg='yellow') 

     nt=int(nt)-2000
     x=int(e4.get())
     if(x<nt):
         an=e3.get()
         na=e32.get()
         n=db.execute('''select * from records where name=(?) and pin=(?) ''',(na,an,))
         for record in n:
                de=int(record[2])
                de=de+x
                passwod=record[3]
                db.execute('''delete from records where pin=(?) and name=(?)''',(an,na,))
                db.execute('''insert into records  values(?,?,?,?)''',(na,an,de,passwod,))
         m=db.execute('''select * from records where pin=(?) and password=(?)''',(pin,passw))
         for record in m:
                name=record[0]
                mj=int(record[2])
                mj=mj-x
                db.execute('''delete from records where pin=(?) and password=(?)''',(pin,passw,))
                db.execute('''insert into records  values(?,?,?,?)''',(name,pin,mj,passw,))
         pos5.configure(text='Your transfer is done,Thanks',font=(27))
         pos6.configure(text='Your balance is now {}'.format(mj),font=(27))
     else:
          pos5.coonfigure(text='You are not eligible for this transaction',font=(27))
     db.commit()
def clr():
     e2.delete(0,END)
     e212.delete(0,END)
     e4.delete(0,END)
     e3.delete(0,END)
     e32.delete(0,END)
     e1.delete(0,END)
     pos1.configure(text='')
     pos2.configure(text='')
     pos3.configure(text='')
     pos4.configure(text='')
     pos5.configure(text='')
     pos6.configure(text='')





          
   
def newly():        
     mn=e21.get()
     mn2=e22.get()
     zx=f2.get()
     zx1=f22.get()
     if(zx!=zx1):
          pos1.configure(text='Your both password does not match',font=(30))
     else:
          
          mn3=db.execute('''select max(PIN) from records''')
          for record in mn3:
                ns=record[0]+1
          db.execute('''insert into records values (?,?,?,?)''',(mn,ns,mn2,zx,))
          pos3.configure(text='Thanks for joining A.B.C. Bannk',font=(40),fg='blue',bg='yellow')
          db.commit()            
root=Tk()
root.title("A.B.C.B.")
root.geometry('1350x720+0+0')
root.configure(background='yellow')
#Frames
leftfr=Frame(root,width=800,height=750,bd=8,relief="raise")

leftfr.pack(side=LEFT)

rightfr=Frame(root,width=550,height=750,bd=8,relief="raise")
rightfr.pack(side=RIGHT)


leftfr1=Frame(leftfr,width=800,height=100,bd=8,relief="raise")

leftfr1.pack(side=TOP)
leftfr2=Frame(leftfr,width=800,height=100,bd=8,relief="raise")
leftfr2.pack(side=TOP)
leftfr3=Frame(leftfr,width=800,height=100,bd=8,relief="raise")
leftfr3.pack(side=TOP)
leftfr4=Frame(leftfr,width=800,height=450,bd=8,relief="raise")
leftfr4.pack(side=TOP)


rightfr1=Frame(rightfr,width=550,height=50,bd=8,relief="raise")
rightfr1.pack(side=TOP)
rightfr2=Frame(rightfr,width=550,height=200,bd=8,relief="raise")
rightfr2.pack(side=TOP)
rightfr3=Frame(rightfr,width=550,height=450,bd=8,relief="raise")
rightfr3.pack(side=TOP)
rightfr4=Frame(rightfr,width=550,height=50,bd=8,relief="raise")
rightfr4.pack(side=TOP)
##components
DateofOrder=StringVar()
DateofOrder.set(time.strftime("%d /%m /%y"))
t=StringVar()

t.set(time.strftime("%H:%M:%S"))



 #Labels
m=Label(leftfr1,text='A.B.C. BANK', font=('High Tower Text',32,'bold'),bg='green',fg='yellow')
m.grid(row=0,column=2,columnspan=1)

b=Label(leftfr1,text='A.B.C.Bank Management System', font=('High Tower Text',32,'bold'),bg='white',fg='black')
b.grid(row=1,column=0,columnspan=4)


b=Label(leftfr1,textvariable=DateofOrder,bd=2, font=('High Tower Text',32,'bold'),bg='white',fg='black')
b.grid(row=0,column=3,columnspan=2)
c=Label(leftfr1,textvariable=t,bd=2, font=('High Tower Text',32,'bold'),bg='white',fg='black')
c.grid(row=0,column=0,columnspan=2)
a=Label(leftfr2,text='Welcome', font=('High Tower Text',32,'bold'),bg='yellow',fg='blue')
#New Account
a.grid(row=1,column=1,columnspan=4,sticky=W)
new=Label(leftfr3,text='Create new Account', font=('High Tower Text',32,'bold'),bg='blue',fg='yellow')

new.grid(row=0,column=0,columnspan=2,sticky=W)
n1=Label(leftfr3,text='Enter Name:' ,font=(20 ))
n1.grid(row=1,column=0)
e21=Entry(leftfr3)
e21.grid(row=1,column=1)
b1=Label(leftfr3,text='Enter Balance:',font=(20 ) )
b1.grid(row=2,column=0)
e22=Entry(leftfr3)
e22.grid(row=2,column=1)
p1=Label(leftfr3,text='Enter Password:',font=(20 ) )
p1.grid(row=3,column=0)
f22=Entry(leftfr3,show='*')
f22.grid(row=3,column=1)
b1=Label(leftfr3,text='Reenter Password:',font=(20 ) )
b1.grid(row=4,column=0)
f2=Entry(leftfr3,show='*')
f2.grid(row=4,column=1)
ps=Label(leftfr3,text='PIN will be  autogenerated by bank and we will inform you',font=(30),bg='red',fg='yellow' )
ps.grid(row=5,column=0,columnspan=2)
con=Button(leftfr3,text='Confirm',width=14,command=newly)
con.grid(row=6,column=1)
p1=Label(leftfr3,text='Password must be a 4 length string containing only uppercase and lowercase letters and must have atleast one',font=(30 ) )
p1.grid(row=7,column=0,columnspan=3)
p1=Label(leftfr3,text='numeric value',font=(30 ) )
p1.grid(row=8,column=0,columnspan=3)


submit12=Button(leftfr2,text='Log In',width=14,command=read)
submit12.grid(row=4,column=1)
#Label Services
service=Label(rightfr1,text='Services', font=('High Tower Text',28,'bold'),bg='blue',fg='yellow')

service.grid(row=0,column=0,columnspan=2,sticky=W)

#Loan

Loan=Label(rightfr2,text='Loan' , font=('Modern No. 20',42,'underline'),bg='red',fg='yellow')
Loan1=Label(rightfr2,text='Enter amount',font=(20 ) )
Loan.grid(row=1,column=0)
Loan1.grid(row=1,column=1)
e1=Entry(rightfr2)
e1.grid(row=2,column=1)
Loant=Label(rightfr2,text='Type of Loan',font=(25 ) )
Loant.grid(row=3,column=1)
loant=IntVar()
hl=Radiobutton(rightfr2,text='Home Loan',var=loant,value=1,font=(20 ))
hl.grid(row=4,column=1)
hli=Label(rightfr2,text='For Home Loan interest is 9 percent per annum' , font=(15))
hli.grid(row=4,column=0)
cl=Radiobutton(rightfr2,text='Car Loan',var=loant,value=2,font=(20 ))
cl.grid(row=5,column=1)
cli=Label(rightfr2,text='For Car Loan interest is 10 percent per annum' , font=(15))
cli.grid(row=5,column=0)
el=Radiobutton(rightfr2,text='Education Loan',var=loant,value=3,font=(20 ))
el.grid(row=6,column=1)
eli=Label(rightfr2,text='For Education Loan interest is 7 percent per annum' , font=(15))
eli.grid(row=6,column=0)
pl=Radiobutton(rightfr2,text='Personal Loan',var=loant,value=4,font=(20 ))
pl.grid(row=7,column=1)
pli=Label(rightfr2,text='For Personal Loan interest is 10 percent per annum' , font=(15))
pli.grid(row=7,column=0)
Loan_d=Label(rightfr2,text='Duration of Loan',font=(25 ) )
Loan_d.grid(row=8,column=1)


loany=IntVar()
t1=Radiobutton(rightfr2,text='6 months',var=loany,value=6,font=(20 ))
t1.grid(row=9,column=0)
t2=Radiobutton(rightfr2,text='12 months',var=loany,value=12,font=(20 ))
t2.grid(row=9,column=1)
t3=Radiobutton(rightfr2,text='18 months',var=loany,value=18,font=(20 ))
t3.grid(row=10,column=0)
t4=Radiobutton(rightfr2,text='24 months',var=loany,value=24,font=(20 ))
t4.grid(row=10,column=1)
s=Button(rightfr2,text='Submit',width=14,command=loan)
s.grid(row=13,column=1)
#Transaction
t=Label(rightfr3,text='Transaction' , font=('Modern No. 20',42,'underline'),bg='red',fg='yellow')
t11=Label(rightfr2,text='Amount is entered in INR',font=(15))
t11.grid(row=14,column=0)
t1=Label(rightfr3,text='Enter amount',font=(20 ) )
t.grid(row=15,column=0)
t1.grid(row=16,column=1)
e4=Entry(rightfr3)
e4.grid(row=17,column=1)
t21=Label(rightfr3,text='Account number where you want to transfer',font=(15))
t21.grid(row=18,column=0)
t2=Label(rightfr3,text='Enter account no',font=(20 ) )
t2.grid(row=18,column=1)
e3=Entry(rightfr3)
e3.grid(row=19,column=1)
t231=Label(rightfr3,text='Enter the name of person to whom you want to transfer',font=(15))
t231.grid(row=20,column=0)
t23=Label(rightfr3,text='Enter payee name',font=(20 ) )
t23.grid(row=20,column=1)
e32=Entry(rightfr3)
e32.grid(row=21,column=1)
s1=Button(rightfr3,text='Submit',width=14,command=trans)
s1.grid(row=22,column=1)
#Already exists
passwrd=Label(leftfr2,text='Enter PIN:',font=(20 ))
passwrd.grid(row=2,column=0)
e2=Entry(leftfr2,show='*')
e2.grid(row=2,column=1)
passwrd11=Label(leftfr2,text='Enter Password:',font=(20 ),width=12)
passwrd11.grid(row=2,column=3)
e212=Entry(leftfr2,show='*')
e212.grid(row=2,column=4)
ap1=Label(leftfr2,text='', )
ap1.grid(row=2,column=5)
submit=Button(leftfr2,text='Log In',width=14,command=read)
submit.grid(row=4,column=1)

#Information
pos=Label(leftfr4,text='Information',font=(50))
pos.grid(row=1,column=0)
ton=Button(leftfr4,text='Logout',command=clr)
ton.grid(row=1,column=1)
pos1=Label(leftfr4,text='')
pos1.grid(row=2,column=0)
pos2=Label(leftfr4,text='')
pos2.grid(row=3,column=0)
pos3=Label(leftfr4,text='')
pos3.grid(row=4,column=0)
pos4=Label(leftfr4,text='')
pos4.grid(row=5,column=0)
pos5=Label(leftfr4,text='')
pos5.grid(row=6,column=0)
pos6=Label(leftfr4,text='')
pos6.grid(row=7,column=0)
pos7=Label(leftfr4,text='All the information will appear here regarding account ,loans and transactions',font=(20))
pos7.grid(row=8,column=0)
mainloop()
