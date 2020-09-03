import pymysql as db
import os
import sys

def sign_in():
    cnct=db.connect("127.0.0.1","root","srijan4799","BDS")
    c=cnct.cursor()
    empcode=input("Enter Employee Code:-")
    emppassword=input("Enter Password:-")
    q="select empname,role from employee where empcode=%s and emppassword=%s"
    c.execute(q,(empcode,emppassword))
    a=c.fetchone()
    if(c.rowcount==1):
        if a[1]=="admin" or a[1]=="ADMIN" or a[1]=="Admin":
            admenu(a[0],a[1],cnct,c)
        elif a[1]=="MANAGER" or a[1]=="Manager" or a[1]=="manager":
            mnmenu(a[0],a[1],cnct,c)
        elif a[1]=="Developer" or a[1]=="developer" or a[1]=="DEVELOPER" or a[1]=="Tester" or a[1]=="TESTER" or a[1]=="tester":
            emenu(a[0],a[1],cnct,c)
    else:
        print("\n USERNAME OR PASSWORD NOT CORRECT.\nLOGIN FAILED.\tPLEASE TRY AGAIN LATER.")
    c.close()
    cnct.close()

def admenu(eid,role,cnct,c):
     print(eid)
     c.close()
     while True:
        os.system("cls")
        print("Welcome Administrator".center(50))
        print("\nMain Menu".center(50))
        print("\n 1->Manager".center(50))
        print("\n 2->Employee".center(50))
        print("\n 3->View Project".center(50))
        print("\n 4->View Bug Report".center(50))
        print("\n 5->Exit".center(50))
        b=int(input("Enter Your Choice"))
            
        if b==1:
            while True:
                os.system("cls")
                print("WELCOME TO THE ADMINISTRATOR's HOME PAGE".center(50))
                print("\n1:Create Manager".center(50))
                print("\n2:Update Manager".center(50))
                print("\n3:Delete Manager".center(50))
                print("\n4:View All Managers".center(50))
                print("\n5:Exit".center(50))
                e=0
                d=int(input("Enter Your Choice"))
                if d==1:
                    create_new_employee(cnct,c,e)
                elif d==2:
                    update_employee(cnct,c,e)
                elif d==3:
                    delete_employee(cnct,c,e)
                elif d==4:
                    view_all_employees(cnct,c,e)
                elif d==5:
                    break;
                else:
                    print("Wrong Choice")
                    
                
        elif b==2:
            e=int(input("Enter type of employee 1:Developer 2:Tester"))
            while True:
                print("Main Menu\n1:Create Employee\n2:Update Employee Record\n3:Delete Employee Record\n4:View All Employees\n5:Back")
                d=int(input("Enter Your Choice"))
                if d==1:
                    create_new_employee(cnct,c,e)
                elif d==2:
                    update_employee(cnct,c,e)
                elif d==3:
                    delete_employee(cnct,c)
                elif d==4:
                    view_all_employees(cnct,c,e)
                elif d==5:
                    break;
                else:
                    print("Wrong Choice")
        elif b==3:
            view_project(cnct,c)
        elif b==4:
            view_bug_report(cnct,c)
        elif b==5:
            BugTracker()
        else:
            print("Invalid choice")

def mnmenu(eid,role,cnct,c):
    os.system("cls")
    
    while True:
        print("\n Welcome Manager".center(50))
        print("Main Menu".center(50))
        print("\n1:Update Profile".center(50))
        print("\n2:Manage Project".center(50))
        print("\n3:Manage Bug".center(50))
        print("\n4:Back".center(50))
        b=int(input("Enter Your Choice"))
        if b==1:
            update_manager(cnct,c)
        elif b==2:
            mngproject(eid,cnct,c)
        elif b==3:
            bugs(cnct,c)
        elif b==4:
            BugTracker()
        else:
            print("Invalid choice")



def emenu(eid,role,cnct,c):
    os.system("cls")
    if(role=='developer'):
        print("Welcome Developer\n\n")
    else:
        print("Welcome tester\n\n")
    
    while True:
        print("Main Menu\n1:Update Profile\n2:Add Bug Report\n3:Update Bug Status\n4:VIew Bug's\n5:Bug's Details\n6:Back")
        b=int(input("Enter Your Choice"))
        if b==1:
            update_emp_employee(cnct,c,role)
        elif b==2:
            abr(cnct,c,role)
        elif b==3:
            ubgs(cnct,c,role)
        elif b==4:
            vbgs(cnct,c,role)
        elif b==5:
            sbgd(cnct,c,role)
        elif b==6:
            BugTracker()
        else:
            print("Invalid choice")


def create_new_employee(cnct,c,e):
    if e==0:
        role="manager"
    elif e==1:
        role="developer"
    elif e==2:
        role="tester"
    else:
        return 0
    
    empcode=input("Enter Employee id:-")
    empname=input("Enter Name:-")
    empemail=input("Enter Email:-")
    emppassword=input("Enter Password:-")
    gender=input("Enter Gender:-")
    dob=input("Enter dob:-")
    mobileno=input("Enter mobileno:-")
    
    
    c=cnct.cursor()
    qry="insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s)"
    if(c.execute(qry,(empcode,empname,empemail,emppassword,gender,dob,mobileno,role))):
        cnct.commit()
        print("Employee created")
        c.close()
        return 1
    else:
        print("some error")
        c.close()
        return 0


def update_employee(cnct,c,e):

    if e==0:
        role="manager"
    elif e==1:
        role="developer"
    elif e==2:
        role="tester"
    else:
        return 0
    
    empcode=input("Enter Employee id:-")
    empname=input("Enter Name:-")
    empemail=input("Enter Email:-")
    emppassword=input("Enter Password:-")
    gender=input("Enter Gender:-")
    dob=input("Enter dob:-")
    mobileno=input("Enter mobileno:-")
    
    
    c=cnct.cursor()
    qry="update employee set empname=%s,empemail=%s,emppassword=%s,gender=%s,dob=%s,mobileno=%s,role=%s where empcode=%s"
    if(c.execute(qry,(empname,empemail,emppassword,gender,dob,mobileno,role,empcode))):
        cnct.commit()
        print("Employee's Record updated")
        c.close()
        return 1
    else:
        print("CANNOT UPDATE RECORD.\n NO USER FOUND WITH THE GIVEN EMPLOYEE ID")
        c.close()
        return 0
    
def delete_employee(cnct,c):
    
    empcode=input("Enter Employee id:-")
    c=cnct.cursor()
    qry="delete from employee where empcode=%s"
    if(c.execute(qry,(empcode,))):
        cnct.commit()
        print("Employee deleted")
        c.close()
        return 1
    else:
        print("UNABLE TO FIND ANY EMPLOYEE WITH THE GIVEN EMPLOYEE CODE")
        c.close()
        return 0    


def view_all_employees(cnct,c,e):
    if e==0:
        role="manager"
    elif e==1:
        role="developer"
    elif e==2:
        role="tester"
    else:
        return 0
    c=cnct.cursor()
    qry="select empcode,empname,empemail,gender,dob,mobileno,role from employee where role=%s"
    c.execute(qry,role)
    if(c.rowcount>0):
        s=c.fetchall()
        for i in s:
            for j in i:
                print(j,end="\t")
            print()
    else:
        print("\nNO RECORD FOUND")
    c.close()
    os.system("pause")
    return 0

def view_project(cnct,c):
    c=cnct.cursor()
    qry="select * from project"
    c.execute(qry)
    if(c.rowcount>0):
        s=c.fetchall()
        for i in s:
            for j in i:
                print(j,end="\t")
            print()
    else:
        print("\nNO RECORD FOUND")
    c.close()
    os.system("pause")
    return 0


def view_bug_report(cnct,c):
    c=cnct.cursor()
    qry="select * from bugreport"
    c.execute(qry)
    if(c.rowcount>0):
        s=c.fetchall()
        for i in s:
            for j in i:
                print(j,end="\t")
            print()
    else:
        print("\nNO RECORD FOUND!")
    c.close()
    os.system("pause")
    return 0

def update_manager(cnct,c):
    role="manager"
    empcode=input("Enter Employee id:-")
    empname=input("Enter Name:-")
    empemail=input("Enter Email:-")
    emppassword=input("Enter Password:-")
    gender=input("Enter Gender:-")
    dob=input("Enter dob:-")
    mobileno=input("Enter mobileno:-")

    c=cnct.cursor()
    qry="update employee set empname=%s,empemail=%s,emppassword=%s,gender=%s,dob=%s,mobileno=%s,role=%s where empcode=%s"
    if(c.execute(qry,(empname,empemail,emppassword,gender,dob,mobileno,role,empcode))):
        cnct.commit()
        print("Employee's Record updated")
        c.close()
        return 1
    else:
        print("CANNOT UPDATE RECORD.\n NO USER FOUND WITH THE GIVEN EMPLOYEE ID")
        c.close()
        return 0

def update_emp_employee(cnct,c,role):
    r=role
    empcode=input("Enter Employee id:-")
    empname=input("Enter Name:-")
    empemail=input("Enter Email:-")
    emppassword=input("Enter Password:-")
    gender=input("Enter Gender:-")
    dob=input("Enter dob:-")
    mobileno=input("Enter mobileno:-")

    c=cnct.cursor()
    qry="update employee set empname=%s,empemail=%s,emppassword=%s,gender=%s,dob=%s,mobileno=%s,role=%s where empcode=%s"
    if(c.execute(qry,(empname,empemail,emppassword,gender,dob,mobileno,r,empcode))):
        cnct.commit()
        print("Employee's Record updated")
        c.close()
        return 1
    else:
        print("CANNOT UPDATE RECORD.\n NO USER FOUND WITH THE GIVEN EMPLOYEE ID")
        c.close()
        return 0

def mngproject(eid,cnct,c):
    print("\n WELCOME TO THE PROJECT MANAGEMENT WINDOW")
    print("1: Add Project\n 2:View Projects\n3:Delete Project\n4:Update Project\n5:Back")
    ch=int(input("\n ENTER YOUR CHOICE:- "))
    if ch==1:
        ecode=input("\n ENTER YOUR EMPLOYEE CODE:- ")
        pid=input("Enter Project id:-")
        pname=input("Enter Project Name:-")
        sd=input("Enter Start Date:-")
        ed=input("Enter End Date:-")
        desc=input("Enter Project Description:-")
    
        c=cnct.cursor()
        qry="insert into project values(%s,%s,%s,%s,%s)"
        if(c.execute(qry,(pid,pname,sd,ed,desc))):
            cnct.commit()
            print("Project created")
        qry1="insert into assignproject values(%s,%s)"
        if(c.execute(qry1,(pid,ecode))):
            print("\n PROJECT ASSIGNED")
            c.close()
        else:
            print("some error")
        c.close()
        
    elif ch==2:
        c=cnct.cursor()
        qry="select * from project"
        c.execute(qry)
        if(c.rowcount>0):
            s=c.fetchall()
            for i in s:
                for j in i:
                    print(j,end="\t")
            print()
        else:
            print("\nNO RECORD FOUND!")
        c.close()
        os.system("pause")
        return 0
    elif ch==3:
        pid=input("Enter Project id:-")
        c=cnct.cursor()
        qry="delete from project where projectid=%s"
        if(c.execute(qry,(pid,))):
            cnct.commit()
            print("Project deleted")
            c.close()
            return 1
        else:
            print("UNABLE TO FIND ANY EMPLOYEE WITH THE GIVEN EMPLOYEE CODE")
            c.close()
            return 0    
    elif ch==4:
        w=eid
        ecode="select empcode from employee where empname=w"
        pid=input("Enter Project id:-")
        pname=input("Enter Project Name:-")
        sd=input("Enter Start Date:-")
        ed=input("Enter End Date:-")
        desc=input("Enter Project Description:-")

        c=cnct.cursor()
        qry="update project set projectname=%s,sdate=%s,edate=%s,projectdec=%s where projectid=%s"
        if(c.execute(qry,(projectname,sdate,edate,projectdec,pid))):
            cnct.commit()
            print("Project's Record updated")
            c.close()
            return 1
        else:
            print("CANNOT UPDATE RECORD.\n NO USER FOUND WITH THE GIVEN EMPLOYEE ID")
            c.close()
            return 0

    elif ch==5:
        mnmenu()

def bugs(cnct,c):
    print("\n WELCOME TO BUGGING WINDOW")
    print("\n1:Add New Bug\n2:View All Bug's\n3:Update Bug\n4:Delete Bug")
    d=int(input("\n ENTER YOUR CHOICE:- "))
    if d==1:
        bid=input("\n Enter Bug ID:- ")
        bcg=input("\n Enter Bug Category:- ")
        bsv=input("\n Enter Bug Severty:- ")
        c=cnct.cursor()
        qry="insert into bugtype values(%s,%s,%s)"
        if(c.execute(qry,(bid,bcg,bsv))):
            cnct.commit()
            print("\n BUG ADDED TO THE DATABASE")
            c.close()
            return 1
        else:
            print("\n SOME ERROR")
            c.close()
            return 0
    if d==2:
        c=cnct.cursor()
        qry="select * from bugtype"
        c.execute(qry)
        if(c.rowcount>0):
            s=c.fetchall()
            for i in s:
                for j in i:
                    print(j,end="\t")
            print()
        else:
            print("\nNO RECORD FOUND!")
        c.close()
        os.system("pause")
        return 0
    if d==3:
         bid=input("\n Enter Bug ID:- ")
         bcg=input("\n Enter Bug Category:- ")
         bsv=input("\n Enter Bug Severty:- ")
         c=cnct.cursor()
         qry="update bugtype set bugCatgory=%s,bugSeverty=%s where bugcode=%s"
         if(c.execute(qry,(bugCatgory,bugSeverty,bid))):
            cnct.commit()
            print("Bug's Record updated")
            c.close()
            return 1
         else:
            print("CANNOT UPDATE RECORD.\n NO USER FOUND WITH THE GIVEN EMPLOYEE ID")
            c.close()
            return 0
    if d==4:
        bid=input("Enter Bug id:-")
        c=cnct.cursor()
        qry="delete from bugtype where bugcode=%s"
        if(c.execute(qry,(bid,))):
            cnct.commit()
            print("Bug deleted")
            c.close()
            return 1
        else:
            print("UNABLE TO FIND ANY EMPLOYEE WITH THE GIVEN EMPLOYEE CODE")
            c.close()
            return 0    
         
def abr(cnct,c,role):
    if role=="tester":
        bno=input("\n ENTER BUG NUMBER:- ")
        bcode=input("\n ENTER BUG CODE:- ")
        pid=input("\n ENTER PROJECT ID:- ")
        tc=input("\n ENTER TCODE:- ")
        eid=input("\n ENTER EMPLOYEE CODE:- ")
        st=input("\n ENTER STATUS OF THE BUG:- ")
        bdes=input("\n ENTER BUG DESCRIPTION:- ")
        c=cnct.cursor()
        qry="insert into bugreport values(%s,%s,%s,%s,%s,%s,%s)"
        if(c.execute(qry,(bno,bcode,pid,tc,eid,st,bdes))):
            cnct.commit()
            print("\n BUG REPORT ADDED TO THE DATABASE")
            c.close()
            return 1
        else:
            print("\n SOME ERROR")
            c.close()
            return 0

def ubgs(cnct,c,role):
    bno=input("\n ENTER BUG NUMBER:- ")
    st=input("\n ENTER STATUS OF THE BUG:- ")
    c=cnct.cursor()
    qry="update bugreport set status=%s where bugcode=%s"
    if(c.execute(qry,(status,empcode))):
        cnct.commit()
        print("Bug's Report updated")
        c.close()
        return 1
    else:
        print("CANNOT UPDATE RECORD.\n NO USER FOUND WITH THE GIVEN EMPLOYEE ID")
        c.close()
        return 0

def vbgs(cnct,c,role):
    c=cnct.cursor()
    qry="select * from bugtype"
    c.execute(qry)
    if(c.rowcount>0):
        s=c.fetchall()
        for i in s:
            for j in i:
                print(j,end="\t")
            print()
        c.close()
    else:
        print("\nNO RECORD FOUND!")
    c.close()
    os.system("pause")
    return 0

def sbgd(cnct,c,role):
     bno=input("\n ENTER BUG NUMBER:- ")
     c=cnct.cursor()
     qry="select * from bugreport where bugcode=%s"
     c.execute(qry,(bno,))
     if(c.rowcount>0):
        s=c.fetchall()
        for i in s:
            for j in i:
                print(j,end="\t")
            print()
        c.close()
     else:
        print("\nNO RECORD FOUND!")
     c.close()
     os.system("pause")
     return 0
     
     
    
    
        
def BugTracker():
    print("WELCOME TO BUG TRAKING SYSTEM AND ANALYSIS".center(50))
    print("1 LOGIN".center(50))
    print("2 EXIT".center(50))
    choice=int(input("Enter choice:-"))
    if(choice==1):
        sign_in()
    else:
        print("THANK YOU FOR VISITING THIS PAGE. SEE YOU LATER")
        sys.exit()
        

if __name__=="__main__":
    BugTracker()
