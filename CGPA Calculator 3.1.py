from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter.ttk import Progressbar
from tkinter import Menu
from tkinter import Image



window=Tk()
window.geometry('1350x700')
window.resizable(0,0)
window.title("CGPA Calculator")
window.configure(background="#505050")

def base():
       f=Frame(window, width='1000', height='1000', background="black")
       f.place(x=350, y=0) #Login Page Black Background 


#BACKGROUND --------------------------------------------------------------

bcg=PhotoImage(file="bcg1.gif") #Red Wallpaper
blabel=Label(window,image=bcg)
blabel.place(x=0, y=0, width=500, height=700)



base()



#LOGIN -------------------------------------------------------------------

def page(event):
       f2=Frame(window, width='1000', height='1000', background="black")
       f2.place(x=350, y=0) #Login Page Black Background Frame

       
              

       
       

     
       
       icon=PhotoImage(file="login.gif") #Login Page Icon
       iconlabel=Label(f2,image=icon)
       iconlabel.image=icon
       iconlabel.place(x=458, y=130, width=100,height=100)
     
       
       label1=Label(f2, text=" CGPA Calculator ",font=("Arial Bold",15))
       label1.place(x=0, y=50)
      
       
       #Progress Bars Function
       def fill(event):
              a=username.get()
              b=password.get()
              f2.after(3000,fill,"<1>")
              if((a=="")and(b=="")):
                     style = ttk.Style() 
                     style.theme_use('clam')
                     style.configure("bar1.Horizontal.TProgressbar",
                       troughcolor='black', background='red')
                     bar1=Progressbar(f2,length=20, value=100, style="bar1.Horizontal.TProgressbar")
                     bar1.place(x=600, y=255)
                     bar2=Progressbar(f2,length=20, value=100, style="bar1.Horizontal.TProgressbar")
                     bar2.place(x=600, y=290)
              
              elif((a=="")and(not(b==""))):
                     style = ttk.Style() 
                     style.theme_use('clam')
                     style.configure("bar1.Horizontal.TProgressbar",
                       troughcolor='black', background='#00AA00')
                     style.configure("bar2.Horizontal.TProgressbar",
                       troughcolor='black', background='red')
                     bar1=Progressbar(f2,length=20, value=100, style="bar2.Horizontal.TProgressbar")
                     bar1.place(x=600, y=255)
                     bar2=Progressbar(f2,length=20, value=100, style="bar1.Horizontal.TProgressbar")
                     bar2.place(x=600, y=290)
              
              elif((b=="")and(not(a==""))):
                     style = ttk.Style() 
                     style.theme_use('clam')
                     style.configure("bar1.Horizontal.TProgressbar",
                       troughcolor='black', background='red')
                     style.configure("bar2.Horizontal.TProgressbar",
                       troughcolor='black', background='#00AA00')
                     bar1=Progressbar(f2,length=20, value=100, style="bar2.Horizontal.TProgressbar")
                     bar1.place(x=600, y=255)
                     bar2=Progressbar(f2,length=20, value=100, style="bar1.Horizontal.TProgressbar")
                     bar2.place(x=600, y=290)

              elif((not(a==""))and(not(b==""))):
                     style = ttk.Style() 
                     style.theme_use('clam')
                     style.configure("bar1.Horizontal.TProgressbar",
                       troughcolor='black', background='#00AA00')
                     style.configure("bar2.Horizontal.TProgressbar",
                       troughcolor='black', background='#00AA00')
                     bar1=Progressbar(f2,length=20, value=100, style="bar2.Horizontal.TProgressbar")
                     bar1.place(x=600, y=255)
                     bar2=Progressbar(f2,length=20, value=100, style="bar1.Horizontal.TProgressbar")
                     bar2.place(x=600, y=290)
              
       

       #Username Label
       label3=Label(f2, text=" Username ",font=("calibri Bold",14), bg="black", fg="white")
       label3.place(x=305, y=250)


       #Username Input Box

       username=Entry(f2, width=23, bd=3, bg="#101010", fg="red",justify="left",
              font=("arial Bold",12),selectbackground="red", selectforeground="white")
       username.bind("<1>",fill)
       username.place(x=410, y=250)


       #Password Label
       label4=Label(f2, text=" Password  ",font=("calibri Bold",14), bg="black", fg="white")
       label4.place(x=305, y=285)

       #Password Input Box
       password=Entry(f2, width=23, bd=3, bg="#101010",show="x", fg="red", justify="left",
              font=("arial Bold",12),selectbackground="red", selectforeground="white")
       password.bind("<1>",fill)
       password.place(x=410, y=285)
              
       def log():
              a=username.get()     #username extracted
              b=password.get()     #password extracted
              if((a=="100100")and(b=="1998")):
                     messagebox.showinfo("Message", "Successful Login")
                     
                     t1=Frame(window, width='1500', height='1000', background="black")
                     t1.place(x=0, y=0)

                     canvas=Canvas(t1, width="500", height=35, bg="#D6D6D6",
                                          highlightthickness=0, relief="ridge" )
                     canvas.place(x=400, y=430)

                     page.colo="red"         
                     page.z=50
                     def increase():
                            increase.pp=canvas.create_rectangle(0,35,page.z,0,fill=page.colo)
                            page.z=page.z+1.4                   
                                          
                     increase()

                     def one():
                            cal=Label(t1, bg="#D6D6D6", font=("arial Bold",20),
                                text="  CGPA Calculator  ", fg="black", )
                            cal.place(x=520,y=140)

                            icon=PhotoImage(file="login.gif") #Login Page Icon
                            iconlabel=Label(t1,image=icon)
                            iconlabel.image=icon
                            iconlabel.place(x=600, y=250, width=100,height=100)
                            
                            load=Label(t1, bg="black", font=("arial Bold",14),
                                text="Loading ... ", fg="white", )
                            load.place(x=400,y=400)
                            window.after(1,increase)
                            if(page.z>250):
                                   page.colo="red"
                                   #canvas.itemconfigure(increase.pp,fill="red")
                                   
                                        
                            if(page.z<500):
                                   
                                   window.after(1,two)
                            else:
                                   load['text']="Login Successful"
                                   window.update()
                                   
                                   t1.destroy()
                                   f2.destroy()
                                   calculator("<1>")
                                   
                                          

                     def two():
                            window.after(1,increase)
                            window.after(1,one)                                        

                     a=one()


                     
                     
              
              elif((a=="")or(b=="")):
                     messagebox.showwarning("Warning", "Please fill all Details")
              else:
                     messagebox.showerror("Error", "Invalid Login")

              
       #Login BUTTON
       button=Button(f2, width=10, text="Login", bd=2, font=("arial Bold",9),
              command=log)
       button.place(x=470, y=325)

       #Forgot Passowrd
       def req(event):
              messagebox.showinfo("Forgot Password", "Go to Official Site and Request for new password")
       
       lbl6=Label(f2, text=" Forgot Password ? ",font=("Arial Bold",9), bg="black", fg="red")
       lbl6.place(x=420,y=360)

       lbl8=Label(f2, text="_________ ",font=("Arial Bold",9), bg="black", fg="white")
       lbl8.bind("<1>",req)
       lbl8.place(x=541,y=365)

       lbl7=Label(f2, text=" Click here ",font=("Arial Bold",9), bg="black", fg="white")
       lbl7.bind("<1>",req)
       lbl7.place(x=540,y=360)

       #temporary Button
       def temp2():             
              f2.destroy()
              calculator("<1>")
                            
                                   

              
       
       #button2=Button(f2, width=10, text="Calculator", bd=2, font=("arial Bold",9),
              #command=temp2)
       #button2.place(x=700, y=500)
page("<1>")


#------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------


#CGPA Calculator Frame Function

def calculator(event):

       def destroy3(event):
              f3.destroy()
              calculator("<1>")

       def destroy2(event):
              f3.destroy()
              avg("<1>")

       def destroy1(event):
              a=messagebox.askyesno("Logout","Are you sure you want to logout")
              if(a==True):
                     f3.destroy()
                     page("<1>")    
       

       
       #Black Background for CGPA Calculator Frame 
       f3=Frame(window, width='1500', height='1000', background="black")
       f3.place(x=0, y=0)          

       bcg2=PhotoImage(file="bcg1.gif") #Red Wallpaper
       blabel2=Label(f3,image=bcg2)
       blabel2.place(x=0, y=0, width=150, height=700)       
       blabel2.image=bcg2
              
       #LABEL CGPA Calculator (ACTIVE TAB)
       lbl1=Label(f3, text=" CGPA Calculator ",font=("arial Bold",11), bg="#FFA07A",
                  width=18)
       lbl1.place(x=150,y=20)
       lbl1.bind("<1>",destroy3)
       
       #Label AVG Calculator
       lbl2=Label(f3, text=" About ",font=("arial Bold",11), width=15)
       lbl2.place(x=329,y=20)
       lbl2.bind("<1>",destroy2)
       
       #Label LOG OUT
       lbl3=Label(f3, text=" Logout ",font=("arial Bold",11), width=15)
       lbl3.place(x=480,y=20)
       lbl3.bind("<1>",destroy1)

                         
        
#------------------------------------------------------------------------------------

       

       class calculate:
              def __init__(self):
                     self.sno="-"
                     self.subject="--"
                     self.credit="--"
                     self.marks="--"
                     self.grade="--"
                     self.gmeaning="--"
                     
                     

              #r1.onerow(x,y, sno, subject, marks, credits, grade, gmeaning, color)
              def onerow(self,a,b,c,d,e,f,g,h,i):
                     
                    
                     
                     self.sno=Label(f3, text="", font=("arial Bold",10), bg=i,
                         justify="left", width="5")
                     self.sno['text']=c
                     self.sno.place(x=a,y=b)     

                     
                           
                     self.subject=Entry(f3, width=20, bg=i,font=("arial Bold",12), bd=0,
                              justify="left")
                     self.subject.place(x=a+80, y=b)
                     self.subject.insert(1,d)       

                     self.marks=Entry(f3, width=18, bg=i,font=("arial Bold",12), bd=0,
                                            justify="center")
                     self.marks.place(x=a+280, y=b)
                     self.marks.insert(1,e)

                     self.credit=Entry(f3, width=20, bg=i,font=("arial Bold",12), bd=0,
                                            justify="center")
                     self.credit.place(x=a+480, y=b)
                     self.credit.insert(1,f)

                     self.grade=Label(f3, text="", font=("arial Bold",10), bg=i,
                                       justify="left", width="15")
                     self.grade['text']=g
                     self.grade.place(x=a+700,y=b)

                     self.gmeaning=Label(f3, text="", font=("arial Bold",10), bg=i,
                                       justify="left", width="15")
                     self.gmeaning['text']=h
                     self.gmeaning.place(x=a+840,y=b)

                     

              def subjectcheck(self,a):
                     try:                     
                            
                            b=int(a)
                            if(b>=0):
                                   return(-1)
                            else:
                                   return(-1)
                                          
                                              
                     except ValueError:
                            if((a=="")or(a==" ")or(a=="  ")or(a=="   ")):
                                   return(-1)
                            else:
                                   return(a)
                            

              def markscheck(self,a):

                     try:                            
                            b=int(a)
                            if((b>=0)and(b<=100)):
                                   if(b<40):
                                          return(0)
                                   elif(b<45):
                                          return(4)
                                   elif(b<55):
                                          return(5)
                                   elif(b<60):
                                          return(6)
                                   elif(b<70):
                                          return(7)
                                   elif(b<80):
                                          return(8)
                                   elif(b<90):
                                          return(9)
                                   else:
                                          return(10)
                                                        
                            else:
                                   return(-1)                                   
                                              
                     except ValueError:
                            return(-1)


              def creditcheck(self,a):
                                   
                     try:                            
                            b=int(a)
                            if((b>=0)and(b<=100)):
                                   return(b)
                            else:
                                   return(-1)
                                          
                                              
                     except ValueError:
                            return(-1)


              def gradecheck(self,a,r):                     
                     if(a==0):
                            r.grade['text']="F"
                            r.gmeaning['text']="Fail"
                            return(a)

                     if(a==4):
                            r.grade['text']="D"
                            r.gmeaning['text']="Pass"

                     if(a==5):
                            r.grade['text']="C"
                            r.gmeaning['text']="Average"

                     if(a==6):
                            r.grade['text']="B"
                            r.gmeaning['text']="Fair"

                     if(a==7):
                            r.grade['text']="B+"
                            r.gmeaning['text']="Good"

                     if(a==8):
                            r.grade['text']="A"
                            r.gmeaning['text']="Very Good"

                     if(a==9):
                            r.grade['text']="A+"
                            r.gmeaning['text']="Excellent"

                     if(a==10):
                            r.grade['text']="O"
                            r.gmeaning['text']="Outstanding"                    
                     
                     
                     
              
              def defaultrows1(self):
                     
                     global r1
                     global r2
                     global r3
                     global r4
                     global r5
                     global r6
                     
                     r1=calculate() #Objects created of class calculate
                     r2=calculate()
                     r3=calculate()
                     r4=calculate()
                     r5=calculate()
                     r6=calculate()
                     
                     #r1.onerow(x,y, sno, subject, marks, credits, grade, gmeaning, color)
                     r1.onerow(230,107,"1."," Subject 1","00","01","--","--","white")
                     r2.onerow(230,130,"2."," Subject 2","00","01","--","--","#D6D6D6")
                     r3.onerow(230,153,"3."," Subject 3","00","01","--","--","white")
                     r4.onerow(230,176,"4."," Subject 4","00","01","--","--","#D6D6D6")
                     r5.onerow(230,199,"5."," Subject 5","00","01","--","--","white")
                     r6.onerow(230,222,"6."," Subject 6","00","01","--","--","#D6D6D6")
                     

              def defaultrows2(self):
                     
                     global rr1
                     global rr2
                     global rr3
                     global rr4
                     global rr5
                     global rr6
                     
                     rr1=calculate() #Objects created of class calculate
                     rr2=calculate()
                     rr3=calculate()
                     rr4=calculate()
                     rr5=calculate()
                     rr6=calculate()
                     
                     #r1.onerow(x,y, sno, subject, marks, credits, grade, gmeaning)
                     rr1.onerow(230,317,"1."," Subject 1","00","01","--","--","white")
                     rr2.onerow(230,340,"2."," Subject 2","00","01","--","--","#D6D6D6")
                     rr3.onerow(230,363,"3."," Subject 3","00","01","--","--","white")
                     rr4.onerow(230,386,"4."," Subject 4","00","01","--","--","#D6D6D6")
                     rr5.onerow(230,409,"5."," Subject 5","00","01","--","--","white")
                     rr6.onerow(230,432,"6."," Subject 6","00","01","--","--","#D6D6D6")


       #Semester 1 Heading LABEL
       heading=Label(f3, text="SEMESTER 1\t\t\t\t            Marks     \t\t               Credits\t\t\tGrade\t             TGPA =\t\t",
                     font=("arial Bold",11), bg="#E9967A")
       heading.place(x=200,y=80)

       tgpa1=Label(f3, text="0.00", font=("arial Bold",11), bg="#E9967A",
                         justify="left", width="4", fg="black")
       tgpa1.place(x=1145,y=80)

       #Semester 2 Heading LABEL
       heading2=Label(f3, text="SEMESTER 2\t\t\t\t            Marks    \t\t               Credits\t\t\tGrade\t             TGPA =\t\t",
                     font=("arial Bold",11), bg="#E9967A")
       heading2.place(x=200,y=290)

       tgpa2=Label(f3, text="0.00", font=("arial Bold",11), bg="#E9967A",
                         justify="left", width="4")
       tgpa2.place(x=1145,y=290)
       
       #OVERALL RESULT Heading 
       heading3=Label(f3, text=" OVERALL  RESULT\t\t\t\t\t\t\t\t\t\t\t            CGPA = \t\t",
                     font=("arial Bold",11), bg="darkred", fg="white")#E9967A
       heading3.place(x=200,y=500)

       valuecgpa=Label(f3, text="0.00", font=("arial Bold",11), bg="darkred",
                         justify="left", width="4", fg="white")
       valuecgpa.place(x=1145,y=500)
       
       #COLOR MEANINGS
       missing=Label(f3, bg="orange", width=3, font=("Arial Bold",11),relief="ridge")
       missing.place(x=230, y=528)

       missingtext=Label(f3, bg="white",  font=("Arial Bold",11),
                                text=" INVALID FIELD \t\t")
       missingtext.place(x=267, y=528)

       fail=Label(f3, bg="red", width=3, font=("Arial Bold",11),relief="ridge")
       fail.place(x=230, y=553)

       failtext=Label(f3, bg="#D6D6D6", font=("Arial Bold",11),
                                text=" FAILED\t\t                ")
       failtext.place(x=267, y=553)

       sem1=Label(f3, bg="royalblue", width=3, font=("Arial Bold",11),relief="ridge")
       sem1.place(x=230, y=578)
              
       sem1text=Label(f3, bg="white", font=("Arial Bold",11),
                                text=" SEMESTER 1\t                ")
       sem1text.place(x=267, y=578)
              
       sem2=Label(f3, bg="lime", width=3, font=("Arial Bold",11),relief="ridge")
       sem2.place(x=230, y=603)
              
       sem2text=Label(f3, bg="#D6D6D6", font=("Arial Bold",11),
                                text=" SEMESTER 2\t                ")
       sem2text.place(x=267, y=603)
             
       # PERCENTAGE SEMESTER 1

       sem1colo=Label(f3, bg="royalblue", width=3, font=("Arial Bold",11),relief="ridge")
       sem1colo.place(x=490, y=528)
        
       per1label=Label(f3, bg="white",  font=("Arial Bold",11),
                                text=" PERCENTAGE %  ")
       per1label.place(x=527, y=528)

       pervalue=Label(f3, bg="white", font=("Arial Bold",11), fg="black",
                             text=" 0.00 ",width=5)
       pervalue.place(x=665, y=528)

       tgpa1colo=Label(f3, bg="royalblue", width=3, font=("Arial Bold",11),relief="ridge")
       tgpa1colo.place(x=490, y=553)

       tgpalabel1=Label(f3, bg="#D6D6D6",  font=("Arial Bold",11),
                                text=" TGPA\t\t ")
       tgpalabel1.place(x=527, y=553)

       tgpavalue1=Label(f3, bg="#D6D6D6", font=("Arial Bold",11), fg="black",
                             text=" 0.00 ",width=5)
       tgpavalue1.place(x=665, y=553)
       
       # PERCENTAGE SEMESTER 2

       sem2colo=Label(f3, bg="lime", width=3, font=("Arial Bold",11),relief="ridge")
       sem2colo.place(x=745, y=528)
              
       per2label=Label(f3, bg="white",  font=("Arial Bold",11),
                                text=" PERCENTAGE %  ")
       per2label.place(x=782, y=528)

       pervalue2=Label(f3, bg="white", font=("Arial Bold",11), fg="black",
                             text=" 0.00 ",width=5)
       pervalue2.place(x=920, y=528)

       tgpa2colo=Label(f3, bg="lime", width=3, font=("Arial Bold",11),relief="ridge")
       tgpa2colo.place(x=745, y=553)

       tgpalabel2=Label(f3, bg="#D6D6D6",  font=("Arial Bold",11),
                                text=" TGPA\t\t ")
       tgpalabel2.place(x=782, y=553)

       tgpavalue2=Label(f3, bg="#D6D6D6", font=("Arial Bold",11), fg="black",
                             text=" 0.00 ",width=5)
       tgpavalue2.place(x=920, y=553)

       #OVERALL RESULT BOXES
       overallP=Label(f3, bg="#E9967A",  font=("Arial Bold",11),
                                text=" PERCENTAGE %   ")
       overallP.place(x=1000, y=528)

       overallPvalue=Label(f3, bg="#E9967A", font=("Arial Bold",11), fg="black",
                             text=" 0.00 ", width=5)
       overallPvalue.place(x=1140, y=528)

       overallCGPA=Label(f3, bg="#E9967A",  font=("Arial Bold",11),
                                text=" CGPA\t\t  ")
       overallCGPA.place(x=1000, y=553)

       overallCvalue=Label(f3, bg="#E9967A", font=("Arial Bold",11), fg="black",
                             text=" 0.00 ",width=5)
       overallCvalue.place(x=1140, y=553)

       #--------------------------------------------------------              
       row=calculate()
       row.defaultrows1()
       row.defaultrows2()
                     


       
       def result():
              #Functions Made for Semester 1
              def creditcolorcheck1(c,p):
                     k=84+(23*p)
                     if(c==-1):
                            orange=Label(f3, bg="orange", width=3,font=("Arial Bold",10))
                            orange.place(x=896, y=k)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=896, y=k)

              def markscolorcheck1(m,p):
                     k=84+(23*p)
                     if(m==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=677, y=k)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=677, y=k)

              def gradecolorcheck1(g,p):
                     k=84+(23*p)
                     if(g==0):
                            red=Label(f3, bg="red", width=3, font=("Arial Bold",10))
                            red.place(x=1200, y=k)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=k)

              def subjectcolorcheck1(s,p):
                     k=84+(23*p)
                     if(s==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=278, y=k)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=278, y=k)
                     

              
              #Function Calling For Semester 1
              s1=r1.subjectcheck(r1.subject.get())
              s2=r2.subjectcheck(r2.subject.get())
              s3=r3.subjectcheck(r3.subject.get())
              s4=r4.subjectcheck(r4.subject.get())
              s5=r5.subjectcheck(r5.subject.get())
              s6=r6.subjectcheck(r6.subject.get())
              
              m1=r1.markscheck(r1.marks.get())
              m2=r2.markscheck(r2.marks.get())
              m3=r3.markscheck(r3.marks.get())
              m4=r4.markscheck(r4.marks.get())
              m5=r5.markscheck(r5.marks.get())
              m6=r6.markscheck(r6.marks.get())

              c1=r1.creditcheck(r1.credit.get())              
              c2=r2.creditcheck(r2.credit.get())
              c3=r3.creditcheck(r3.credit.get())
              c4=r4.creditcheck(r4.credit.get())              
              c5=r5.creditcheck(r5.credit.get())
              c6=r6.creditcheck(r6.credit.get())          
              
              creditcolorcheck1(c1,1)
              creditcolorcheck1(c2,2)
              creditcolorcheck1(c3,3)
              creditcolorcheck1(c4,4)
              creditcolorcheck1(c5,5)
              creditcolorcheck1(c6,6)

              markscolorcheck1(m1,1)
              markscolorcheck1(m2,2)
              markscolorcheck1(m3,3)
              markscolorcheck1(m4,4)
              markscolorcheck1(m5,5)
              markscolorcheck1(m6,6)

              subjectcolorcheck1(s1,1)
              subjectcolorcheck1(s2,2)
              subjectcolorcheck1(s3,3)
              subjectcolorcheck1(s4,4)
              subjectcolorcheck1(s5,5)
              subjectcolorcheck1(s6,6)
              

              
              #Functions Made for Semester 2
              def creditcolorcheck2(c,p):
                     k=294+(23*p)
                     if(c==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=896, y=k)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=896, y=k)

              def markscolorcheck2(m,p):
                     k=294+(23*p)
                     if(m==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=677, y=k)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=677, y=k)

              def gradecolorcheck2(g,p):
                     k=294+(23*p)
                     if(g==0):
                            red=Label(f3, bg="red", width=3, font=("Arial Bold",10))
                            red.place(x=1200, y=k)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=1200, y=k)

              def subjectcolorcheck2(s,p):
                     k=294+(23*p)
                     if(s==-1):
                            orange=Label(f3, bg="orange", width=3, font=("Arial Bold",10))
                            orange.place(x=278, y=k)
                     else:
                            black=Label(f3, bg="black", width=3, font=("Arial Bold",10))
                            black.place(x=278, y=k)
              
              
              #Function Calling for Semester 2


              ss1=rr1.subjectcheck(rr1.subject.get())
              ss2=rr2.subjectcheck(rr2.subject.get())
              ss3=rr3.subjectcheck(rr3.subject.get())
              ss4=rr4.subjectcheck(rr4.subject.get())
              ss5=rr5.subjectcheck(rr5.subject.get())
              ss6=rr6.subjectcheck(rr6.subject.get())
              
              mm1=rr1.markscheck(rr1.marks.get())
              mm2=rr2.markscheck(rr2.marks.get())
              mm3=rr3.markscheck(rr3.marks.get())
              mm4=rr4.markscheck(rr4.marks.get())
              mm5=rr5.markscheck(rr5.marks.get())
              mm6=rr6.markscheck(rr6.marks.get())

              cc1=rr1.creditcheck(rr1.credit.get())              
              cc2=rr2.creditcheck(rr2.credit.get())
              cc3=rr3.creditcheck(rr3.credit.get())
              cc4=rr4.creditcheck(rr4.credit.get())              
              cc5=rr5.creditcheck(rr5.credit.get())
              cc6=rr6.creditcheck(rr6.credit.get())

              creditcolorcheck2(cc1,1)
              creditcolorcheck2(cc2,2)
              creditcolorcheck2(cc3,3)
              creditcolorcheck2(cc4,4)
              creditcolorcheck2(cc5,5)
              creditcolorcheck2(cc6,6)

              markscolorcheck2(mm1,1)
              markscolorcheck2(mm2,2)
              markscolorcheck2(mm3,3)
              markscolorcheck2(mm4,4)
              markscolorcheck2(mm5,5)
              markscolorcheck2(mm6,6)

              subjectcolorcheck2(ss1,1)
              subjectcolorcheck2(ss2,2)
              subjectcolorcheck2(ss3,3)
              subjectcolorcheck2(ss4,4)
              subjectcolorcheck2(ss5,5)
              subjectcolorcheck2(ss6,6)
              
              if(-1 in(s1,s2,s3,s4,s5,s6,ss1,ss2,ss3,ss4,ss5,ss6)):
                     messagebox.showwarning("Invalid","Please Enter Valid Subject Name")                       

              elif(-1 in (c1,c2,c3,c4,c5,c6,cc1,cc2,cc3,cc4,cc5,cc6)):
                     messagebox.showwarning("Invalid","Please Enter Valid Credits")
              else:
                     if(-1 in (m1,m2,m3,m4,m5,m6,mm1,mm2,mm3,mm4,mm5,mm6)):
                            messagebox.showwarning("Invalid","Please Enter Valid Marks")
                     else:
                            m=(m1*c1)+(m2*c2)+(m3*c3)+(m4*c4)+(m5*c5)+(m6*c6)
                            c=c1+c2+c3+c4+c5+c6

                            mm=(mm1*cc1)+(mm2*cc2)+(mm3*cc3)+(mm4*cc4)+(mm5*cc5)+(mm6*cc6)
                            cc=cc1+cc2+cc3+cc4+cc5+cc6

                            g1=r1.gradecheck(m1,r1)
                            g2=r2.gradecheck(m2,r2)
                            g3=r3.gradecheck(m3,r3)
                            g4=r4.gradecheck(m4,r4)
                            g5=r5.gradecheck(m5,r5)
                            g6=r6.gradecheck(m6,r6)                     

                            gradecolorcheck1(g1,1)
                            gradecolorcheck1(g2,2)
                            gradecolorcheck1(g3,3)
                            gradecolorcheck1(g4,4)
                            gradecolorcheck1(g5,5)
                            gradecolorcheck1(g6,6)

                            gg1=rr1.gradecheck(mm1,rr1)
                            gg2=rr2.gradecheck(mm2,rr2)
                            gg3=rr3.gradecheck(mm3,rr3)
                            gg4=rr4.gradecheck(mm4,rr4)
                            gg5=rr5.gradecheck(mm5,rr5)
                            gg6=rr6.gradecheck(mm6,rr6)

                            gradecolorcheck2(gg1,1)
                            gradecolorcheck2(gg2,2)
                            gradecolorcheck2(gg3,3)
                            gradecolorcheck2(gg4,4)
                            gradecolorcheck2(gg5,5)
                            gradecolorcheck2(gg6,6)
                            
                            t=round((m/c),2)
                            tt=round((mm/cc),2)                            
                            
                            tgpa1.configure(bg="darkred", fg="white", text=t)
                            tgpa2.configure(bg="darkred", fg="white", text=tt)

                            tgpavalue1['text']=t
                            pervalue['text']=round((t*10),2)

                            tgpavalue2['text']=tt
                            pervalue2['text']=round((tt*10),2)

                            cgpa=round(((t+tt)/2),2)
                            percentage=round((cgpa*10),2)

                            valuecgpa.configure(text=cgpa, bg="#F9967A", fg="black")
                            
                            overallPvalue.configure(text=percentage, bg="white")
                            overallCvalue.configure(text=cgpa, bg="#D6D6D6")

                            generated=Label(f3, font=("calibri bold",13), width=20, bg="orange")
                            generated.place(x=1003,y=610)
                            generated['text']=" Generated "
              
              
              
       btn=Button(f3, text="Generate", command=result, font=("arial bold",11),
                         width=10, bd=0)
       btn.place(x=1095, y=580)

       btn2=Button(f3, text="Reset", font=("arial bold",11),
                         width=10, bg="white", bd=0)
       btn2.place(x=1000, y=580)
       btn2.bind("<1>",destroy3)     
       

       
#------------------------------------------------------------------------------------
       
# About Frame Function


def avg(event):      # Destroys Previous Frames while Changing Tabs
       def destroy3(event):
              f3.destroy()
              calculator("<1>")

       def destroy2(event):
              f3.destroy()
              avg("<1>")
              
       def destroy1(event):
              a=messagebox.askyesno("Logout","Are you sure you want to logout")
              if(a==True):
                     f3.destroy()
                     page("<1>")
       
       # Black Wallpaper for AVG Calculator
       
       f3=Frame(window, width='1500', height='1000', background="black")
       f3.place(x=150, y=0)

       
       #Label CGPA Calculator
       lbl1=Label(f3, text=" CGPA Calculator ",font=("arial Bold",11),
                  width=18)
       lbl1.place(x=0,y=20)
       lbl1.bind("<1>",destroy3)
       
       #Label About
       lbl2=Label(f3, text=" About ",font=("arial Bold",11), width=15, bg="#F9967A")
       lbl2.place(x=179,y=20)
       lbl2.bind("<1>",destroy2)
       
       #Label LOG OUT
       lbl3=Label(f3, text=" Logout ",font=("arial Bold",11), width=15)
       lbl3.place(x=330,y=20)
       lbl3.bind("<1>",destroy1)

       

       #----------------------------------------------------------
       headingCGPA=Label(f3, text=" What is CGPA ? \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",
                     font=("arial Bold",11), bg="#E9967A")
       headingCGPA.place(x=50,y=80)

       CGPApoint1=Label(f3, font=("calibri",13))
       CGPApoint1.place(x=50,y=110)
       CGPApoint1['text']=" - CGPA is defined as Cumulative Grade Point Average.\t\t\t\t\t\t\t\t\t    "

       CGPApoint2=Label(f3, font=("calibri",13))
       CGPApoint2.place(x=50,y=140)
       CGPApoint2['text']=''' - CGPA is the measurement of average grade points obtained by a student in all the semesters excluding additional subject as per study scheme.    '''
       
       CGPApoint3=Label(f3, font=("calibri",13))
       CGPApoint3.place(x=50,y=170)
       CGPApoint3['text']=''' - Semester grade point average is obtained by dividing the total points by total credits.\t\t\t\t\t\t    '''
       
       headingTGPA=Label(f3, text=" What is TGPA ? \t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",
                     font=("arial Bold",11), bg="#E9967A")
       headingTGPA.place(x=50,y=230)

       TGPApoint1=Label(f3, font=("calibri",13))
       TGPApoint1.place(x=50,y=260)
       TGPApoint1['text']=" - TGPA is defined as Term Grade Point Average.\t\t\t\t\t\t\t\t\t\t    "

       TGPApoint2=Label(f3, font=("calibri",13))
       TGPApoint2.place(x=50,y=290)
       TGPApoint2['text']=''' - TGPA is the measurement of average grade points obtained by a student in single semester excluding additional subject as per study scheme.       '''

       TGPApoint3=Label(f3, font=("calibri",13))
       TGPApoint3.place(x=50,y=320)
       TGPApoint3['text']=''' - Semester grade point average is obtained by dividing the total points by total credits.\t\t\t\t\t\t    '''

       headingGRADE=Label(f3, text=" GRADE DETAILS\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",
                     font=("arial Bold",11), bg="#E9967A")
       headingGRADE.place(x=50,y=380)

       grade1=Label(f3, font=("calibri bold",13), width=10, bg="darkred", fg="white")
       grade1.place(x=50,y=410)
       grade1['text']=" O "
       
       grade1=Label(f3, font=("calibri bold",13), width=20)
       grade1.place(x=140,y=410)
       grade1['text']=" Outstanding "

       grade2=Label(f3, font=("calibri bold",13), width=10, bg="darkred", fg="white")
       grade2.place(x=50,y=440)
       grade2['text']=" A+ "
       
       grade2=Label(f3, font=("calibri bold",13), width=20)
       grade2.place(x=140,y=440)
       grade2['text']=" Excellent "

       grade3=Label(f3, font=("calibri bold",13), width=10, bg="darkred", fg="white")
       grade3.place(x=50,y=470)
       grade3['text']=" A "
       
       grade3=Label(f3, font=("calibri bold",13), width=20)
       grade3.place(x=140,y=470)
       grade3['text']=" Very Good "

       grade4=Label(f3, font=("calibri bold",13), width=10, bg="darkred", fg="white")
       grade4.place(x=435,y=410)
       grade4['text']=" B+ "
       
       grade4=Label(f3, font=("calibri bold",13), width=20)
       grade4.place(x=525,y=410)
       grade4['text']=" Good "

       grade5=Label(f3, font=("calibri bold",13), width=10, bg="darkred", fg="white")
       grade5.place(x=435,y=440)
       grade5['text']=" B "
       
       grade5=Label(f3, font=("calibri bold",13), width=20)
       grade5.place(x=525,y=440)
       grade5['text']=" Fair "

       grade6=Label(f3, font=("calibri bold",13), width=10, bg="darkred", fg="white")
       grade6.place(x=435,y=470)
       grade6['text']=" C "
       
       grade6=Label(f3, font=("calibri bold",13), width=20)
       grade6.place(x=525,y=470)
       grade6['text']=" Average "

       grade7=Label(f3, font=("calibri bold",13), width=10, bg="darkred", fg="white")
       grade7.place(x=804,y=410)
       grade7['text']=" D "
       
       grade7=Label(f3, font=("calibri bold",13), width=20)
       grade7.place(x=894,y=410)
       grade7['text']=" Pass "

       grade8=Label(f3, font=("calibri bold",13), width=10, bg="darkred", fg="white")
       grade8.place(x=804,y=440)
       grade8['text']=" F "
       
       grade8=Label(f3, font=("calibri bold",13), width=20)
       grade8.place(x=894,y=440)
       grade8['text']=" Fail "
       
window.mainloop()
