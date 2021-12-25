import matplotlib.pyplot as plt
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="NAV_hospitals")
mycursor=mydb.cursor()

#ADDING PATIENT RECORDS
def patientadd():
    mycursor.execute("select ID from patient")
    v=mycursor.fetchall()
    A=[]
    for i in v:
        H=list(i)
        A.append(H)
    if len(A)==0:
        print("TABLE EMPTY")
    else:
        print("THE PATIENT ID'S THAT WERE AVAILABLE IN THE TABLE ARE:",A)
    
    ID=input("Enter the patient's id([PX(X=1,2,3...)]):")
    Name=input("Enter the patient's name:")
    Gender=input("Enter the patient's gender(in capital letter):")
    Age=int(input("Enter the patient's age:"))
    Phone=input("enter the patient's phone number:")
    Address=input("Enter the patient's address(E.g:CHENNAI):")
    Disease=input("disease:")
    check_in=input("Enter the patient's admit date(YYYY-MM-DD):")
    Blood_Group=input("Enter the patient's blood group:")
    Doctor_name=input("Doctor name:")
    Room_no=int(input("Enter the patient's room number(XXX(X=1,2,3...):"))
    add="insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(ID,Name,Gender,Age,Phone,Address,Disease,check_in,Blood_Group,Doctor_name,Room_no)
    mycursor.execute(add,val)
    mydb.commit()
    print("patient's record added successfully")

#DISPLAYING PATIENT RECORDS
def patientdis():
    mycursor.execute("select * from patient")
    a=mycursor.fetchall()
    for i in a:
         s=list(i)
         print("ID=",s[0])
         print("NAME=",s[1])
         print("GENDER=",s[2])
         print("AGE=",s[3])
         print("PHONE=",s[4])
         print("ADDRESS=",s[5])
         print("DISEASE=",s[6])
         print("CHECK_IN=",s[7])
         print("BLOOD GROUP=",s[8])
         print("DOCTOR NAME=",s[9])
         print("ROOM NUMBER=",s[10])
         print("+++++++++++++++++++++++")
         print("+++++++++++++++++++++++")
         
#SEARCHING FOR PATIENT'S ID WHOSE DETAILS TO BE DISPLAYED
def patientsearch():
    ID=input("Enter the patient's id to be searched(PX(X=1,2,3...)):")
    SEARCH="select * from patient where ID=%s"
    mycursor.execute(SEARCH,(ID,))
    a=mycursor.fetchone()
    while True:
        try:
            print("ID=",a[0])
            print("NAME=",a[1])
            print("GENDER=",a[2])
            print("AGE=",a[3])
            print("PHONE=",a[4])
            print("ADDRESS=",a[5])
            print("DISEASE=",a[6])
            print("CHECK_IN=",a[7])
            print("BLOOD GROUP=",a[8])
            print("DOCTOR NAME=",a[9])
            print("ROOM NUMBER=",a[10])
            break
        except TypeError:
                print("RECORD NOT FOUND")
                break

#UPDATING PATIENT'S RECORD WHEN PATIENT'S ID IS GIVEN
def patientupdate():
    print("----------------------------------------")
    print("    1.Patient's Gender to be updated    ")
    print("----------------------------------------")
    print(" 2.Patient's phone number to be updated ")
    print("----------------------------------------")
    print("    3.Patient's address to be updated   ")
    print("----------------------------------------")
    print("              4.Exit                   ")
    print("----------------------------------------")
    s="select ID from patient"
    mycursor.execute(s)
    n=mycursor.fetchall()
    N=[]
    for i in n:
         f=list(i)
         N.append(f)
    print("the patient IDs that are found in the table:",N )

    while True:
          ID=input("Enter the patient's id to be updated(PX(X=1,2,3...)):")
          ch=int(input("enter the number that corresponds to the details that need to be updated:"))
          if ch==1:
               gender=input("enter the patient's gender(in capital letter):")
               up1="update patient set Gender=%s where id=%s"
               b=(gender,ID)
               mycursor.execute(up1,b)
               print("PATIENT'S GENDER UPDATED SUCCESSFULLY")
               mydb.commit()
               break
          elif ch==2:
               number=input("enter the patient's new mobile number:")
               up3="update patient set Phone=%s where id=%s"
               d=(number,ID)
               mycursor.execute(up3,d)
               print("PATIENT'S PHONE NUMBER UPDATED SUCCESSFULLY")
               mydb.commit()
               break
          elif ch==3:
               address=input("enter the patient's correct address(Eg:CHENNAI,TUTICORIN):")
               up4="update patient set Address=%s where id=%s"
               e=(address,ID)
               mycursor.execute(up4,e)
               print("PATIENT'S ADDRESS UPDATED SUCCESSFULLY")
               mydb.commit()
               break
          elif ch==4:
               print("EXIT")
               break
          else:
             print("ENTER THE CORRECT CHOICE")
             continue

#DELETING PATIENT RECORDS WHEN PATIENT'S ID IS GIVEN
def patientdelete():
    j=[]
    mycursor.execute("select ID from patient")
    g=mycursor.fetchall()
    for i in g:
        h=list(i)
        j.append(h)
    print("the patient IDs that are found in the table :",j)
    ID=input("Enter the Patient's ID whose details is to be deleted:")
    DEL="delete from patient where id= %s"
    q=(ID,)
    mycursor.execute(DEL,q)
    print("record deleted successfully")
    mydb.commit()

#GENERATING BILL 
def billing():
    ID=input("Enter the patient's id to be searched for generating bill(PX(X=1,2,3...)):")
    SEARCH="select * from patient where ID=%s"
    mycursor.execute(SEARCH,(ID,))
    a=mycursor.fetchone()
    while True:
        try:
            b=input("Enter the bill number(0000XX):")
            c=input("Enter the bill date(YYYY-MM-DD):")
            d=input("Discharge date(YYYY-MM-DD):")
            doc=float(input("Enter the Doctor's fees:"))
            n=float(input("Enter the Lab test Charges:"))
            l=float(input("Enter the Room Rent:"))
            y=float(input("Enter the Treatment Charges:"))
            z=float(input("Enter the Medicine Charges:"))
            k=float(input("Enter the Miscellaneous Charges:"))
            total=doc+n+l+y+z+k
           
            print("************************************************************NAV GROUP OF HOSPITALS*********************************************************************************************************")
            print("Tel:+(91)-80-26304050/33345551",end='                                                                                                                        ')
            print("Fax:+(91)-80-43215789")
            print("***************************************************************INPATIENT BILL**************************************************************************************************************")
            print("ID=",a[0],end='   ')
            print("NAME=",a[1],end='   ')
            print("GENDER=",a[2],end='   ')
            print("AGE=",a[3],end='   ')
            print("PHONE=",a[4],end='   ')
            print("ADDRESS=",a[5],end='   ')
            print("DISEASE=",a[6],end='   ')
            print("CHECK_IN=",a[7],end='   ')
            print("BLOOD GROUP=",a[8],end='   ')
            print("DOCTOR NAME=",a[9],end='   ')
            print("ROOM NUMBER=",a[10])
            print("********************************************************************BILL*******************************************************************************************************************")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Bill NO:",b,end='  ')
            print("Bill Date:",c,end='  ')
            print("Admission Date:",a[7],end='  ')
            print("Discharge Date:",d)
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("Service Name",end='                                                                                                                                                    ')
            print("Amount(Rs)")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("ROOM RENT",end='                                                                                                                                                                ')
            print(l)
            print("DOCTOR CHARGES",end='                                                                                                                                                           ')
            print(doc)
            print("TREATMENT CHARGES",end='                                                                                                                                                        ')
            print(y)
            print("LABTEST CHARGES",end='                                                                                                                                                          ')
            print(n)
            print("MISCELLANEOUS CHARGES",end='                                                                                                                                                    ')
            print(k)
            print("MEDICINES",end='                                                                                                                                                                ')
            print(z)
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("BILL AMOUNT",end='                                                                                                                                                              ')
            print(total)
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            break
    

        except TypeError:
            print("Record not found")
            break
while True:
    print("                         ++++++++++++++++++++++++++++")
    print("                              PATIENT RECORDS        ")
    print("                         ++++++++++++++++++++++++++++")
    print("                         ----------------------------")
    print("                           1.ADD PATIENT'S RECORDS   ")
    print("                         ----------------------------")
    print("                         2.DISPLAY PATIENT'S RECORDS ")
    print("                         ----------------------------")
    print("                          3.SEARCH PATIENT'S RECORDS ")
    print("                         ----------------------------")
    print("                         4.UPDATE PATIENT'S RECORDS  ")
    print("                         ----------------------------")
    print("                         5.DELETE PATIENT'S RECORDS  ")
    print("                         ----------------------------")
    print("                               6.GENERATE BILL       ")
    print("                         ----------------------------")
    print("                             7.EXIT THE PROGRAM      ")       
    print("                         ----------------------------")
    choice=int(input("Enter your choice:"))
    if choice==1:
         patientadd()
    elif choice==2:
         patientdis()
    elif choice==3:
         patientsearch()
    elif choice==4:
         patientupdate()
    elif choice==5:
         patientdelete()
    elif choice==6:
         billing()
    elif choice==7:
         print("EXIT")
         break
    else:
         print("Enter the correct choice")
         
#STAFF RECORDS
         
#ADDING STAFF RECORDS
         
def STAFFadd():
    mycursor.execute("select ID from staff")
    v=mycursor.fetchall()
    A=[]
    for i in v:
        H=list(i)
        A.append(H)
    if len(A)==0:
        print("TABLE EMPTY")
    else:
        print("THE PATIENT ID'S THAT WERE AVAILABLE IN THE TABLE ARE:",A)
    
    ID=input("Enter the staff's id(e.g,SX(X=1,2,..):")
    Name=input("Enter the staff's name:")
    Gender=input("Enter the staff's gender:")
    Department=input("Enter the staff's department:")
    Phone=input("enter the staff's phone number:")
    Address=input("Enter the staff's address(Eg:CHENNAI):")
    Timing=input("Enter the staff's available timing(TYPE:X-Y AM/PM):")
    add="insert into staff values(%s,%s,%s,%s,%s,%s,%s)"
    val=(ID,Name,Gender,Department,Phone,Address,Timing)
    mycursor.execute(add,val)
    mydb.commit()
    print("staff's record added successfully")
     
#DISPLAYING STAFF RECORDS
def STAFFdis():
    mycursor.execute("select * from staff")
    a=mycursor.fetchall()
    for i in a:
        G=list(i)
        print("ID=",G[0])
        print("NAME=",G[1])
        print("GENDER=",G[2])
        print("DEPARTMENT=",G[3])
        print("PHONE=",G[4])
        print("ADDRESS=",G[5])
        print("AVAILABLE TIMINGS=",G[6])
        print("+++++++++++++++++++++++")
        print("+++++++++++++++++++++++")
        

#SEARCHING STAFF RECORDS
def STAFFsearch():
    print("1.To search by ID(e.g,SX(X=1,2,..)")
    print("2.To search by NAME(in capital letters)")
    print("3.To search by DEPARTMENT(in capital letters)")
    ch=int(input("enter your choice to search from the above details:"))
    if ch==1:
            ID=input("Enter the staff's id to be searched(e.g,SX(X=1,2,..):")
            SEARCH="select * from staff where ID=%s"
            mycursor.execute(SEARCH,(ID,))
            a=mycursor.fetchone()
            while True:
                try:
                    print("ID:",a[0])
                    print("NAME:",a[1])
                    print("GENDER:",a[2])
                    print("DEPARTMENT:",a[3])
                    print("PHONE:",a[4])
                    print("ADDRESS:",a[5])
                    print("AVAILABLE_TIM",a[6])
                    break
                except TypeError:
                    print("STAFF'S RECORD NOT FOUND")
                    break
    elif ch==2:
            NAME=input("Enter the staff's name to be searched:")
            SEARCH="select * from staff where NAME=%s"
            mycursor.execute(SEARCH,(NAME,))
            a=mycursor.fetchone()
            while True:
                try:
                    print("ID:",a[0])
                    print("NAME:",a[1])
                    print("GENDER:",a[2])
                    print("DEPARTMENT:",a[3])
                    print("PHONE:",a[4])
                    print("ADDRESS:",a[5])
                    print("AVAILABLE_TIM",a[6])
                    break
                except TypeError:
                    print("STAFF'S RECORD NOT FOUND")
                    break
    elif ch==3:
            DEPARTMENT=input("Enter the department to be searched:")
            SEARCH="select * from staff where DEPARTMENT=%s"
            mycursor.execute(SEARCH,(DEPARTMENT,))
            a=mycursor.fetchone()
            while True:
                try:
                    print("ID:",a[0])
                    print("NAME:",a[1])
                    print("GENDER:",a[2])
                    print("DEPARTMENT:",a[3])
                    print("PHONE:",a[4])
                    print("ADDRESS:",a[5])
                    print("AVAILABLE_TIM",a[6])
                    break
                except TypeError:
                    print("STAFF'S RECORD NOT FOUND")
                    break

#DELETING STAFF RECORDS
def STAFFdelete():
     j=[]
     mycursor.execute("select ID from staff")
     g=mycursor.fetchall()
     for i in g:
          h=list(i)
          j.append(i)
     print(j)
     ID=input("Enter the staff's ID details to be deleted(from above IDs):")
     DEL="delete from staff where ID= %s"
     mycursor.execute(DEL,(ID,))
     mydb.commit()
     print("record deleted succesfully")
while True:
    print("                         ++++++++++++++++++++++++++++")
    print("                              STAFF'S RECORDS        ")
    print("                         ++++++++++++++++++++++++++++")
    print("                         ----------------------------")
    print("                             1.ADD STAFF'S RECORDS   ")
    print("                         ----------------------------")
    print("                           2.DISPLAY STAFF'S RECORDS ")
    print("                         ----------------------------")
    print("                            3.SEARCH STAFF'S RECORDS ")
    print("                         ----------------------------")
    print("                           4.DELETE STAFF'S RECORDS  ")
    print("                         ----------------------------")
    print("                            5.EXIT THE PROGRAM       ")
    print("                         ----------------------------")
    choice=int(input("Enter your choice:"))
    if choice==1:
         STAFFadd()
    elif choice==2:
          STAFFdis()
    elif choice==3:
         STAFFsearch()
    elif choice==4:
         STAFFdelete()
    elif choice==5:
         print("EXIT")
         break
    else:
         print("ENTER THE CHOICE from above")
    
def piechart():
    mycursor.execute(" select disease,count(*) from patient group by disease")
    r=mycursor.fetchall()
    #DATA TO PLOT
    Disease=[]
    patient=[]
    for i in r:
        a=list(i)  #CONVERSION OF TUPLE IN WHICH THE RECORDS ARE STORED
    
        #Appending the record to a list as PIECHART accepts the values only in a list
        Disease.append(a[0])
        patient.append(a[1])

    #PLOT
    plt.pie(patient,labels=Disease,startangle=90,shadow=True,radius=1.2,autopct='%1.1f%%')
    plt.title("PATIENT ANALYSIS")
    plt.show()

def bargraph():
    #DATA TO PLOT
    Age=[]
    Patient=[]
    mycursor.execute(" select Age,count(*) from patient group by Age")
    r=mycursor.fetchall()
    for i in r:
        a=list(i)
        Age.append(a[0])
        Patient.append(a[1])
    
    plt.bar(Age,Patient,align='center',width=0.9,color='b')
    plt.xlabel('AGE OF PATIENTS')  #LABELLING  X-AXIS
    plt.ylabel('NUMBER OF PATIENTS OF RESPECTIVE AGE')#LABELLING Y-AXIS
    plt.title("PATIENT ANALYSIS ON AGE DISTRIBUTION")
    plt.show()
    
while True:
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("     1.PIECHART PRESENTATION OF AFFECTED PATIENTS ON RESPECTIVE DISEASE    ")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("         2.BAR GRAPH PRESENTATION OF PATIENTS ON AGE DISTRIBUTION          ")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("                         3.EXIT THE PROGRAM                                ")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    ch=int(input("Enter your choice:"))
    if ch==1:
        piechart()
    elif ch==2:
        bargraph()
    elif ch==3:
        print("EXIT THE PROGRAM")
        break
    else:
        print("ENTER THE CORRECT CHOICE")
        




    

    
