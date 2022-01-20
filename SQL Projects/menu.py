import os
import time
def menu_func(host_name, user_name, user_password) :
     """Funcion to operate menu

     Args:
         host_name (str): hostname of your MySQL machine (example:localhost)
         user_name (str): username of MySQL instance
         user_password (str): passord of MySQL instance

     Raises:
         Exception: covered all the exceptions
     """
     import datetime as dt
     import mysql.connector as sql
     from loging_func import log_thisError

     DB_NAME = "STUDENTDATA"
     # conn = sql.connect(host = "localhost", user="root", passwd="mysql8976", use_pure= True)
     conn = sql.connect(host = host_name, user=user_name, passwd=user_password, use_pure= True)
     cur = conn.cursor()
     conn.database = DB_NAME
          

     conn.autocommit = True
     c = 'n'
     while c == 'n'or c=="N":
                              clearconsole = lambda:os.system('cls' if os.name in ('nt','dos') else 'clear')
                              # clearconsole()
                              print()
                              print('1.CREATE NEW STUDENT')
                              print()
                              print('2.UPDATE COURSE')
                              print()
                              print('3.STUDENT DETAILS')
                              print()
                              print('4.COURSE DETAILS')
                              print()
                              print('5.DELETE STUDENT')
                              print()
                              print('6.QUIT')

                              print()
                              while True:
                                   try:
                                        n = input("Enter your choice :")
                                        if n == '1':
                                             n= int(n)
                                             break
                                        elif n == '2':
                                             n= int(n)
                                             break
                                        elif n == '3':
                                             n= int(n)
                                             break
                                        elif n == '4':
                                             n= int(n)
                                             break
                                        elif n == '5':
                                             n= int(n)
                                             break
                                        elif n == '6':
                                             n= int(n)
                                             break
                                        else :
                                             raise Exception("INVALID INPUT : Enter From menu only !!")
                                             
                                        #break
                                   except Exception as e:
                                        print(e)
                                        log_thisError(e)

                              print()

                              if n == 1:

                                        acc_no=int(input('Enter your ROLL NUMBER='))
                                        print()
                                        acc_name=input('Enter your  NAME=')
                                        print()
                                        ph_no=int(input('Enter your phone number='))
                                        print()
                                        add=input('Enter your address=')
                                        print()
                                        cr_amt=input('Enter your Standard=')
                                        print()
                                        course=input('Enter your course name=')
                                        V_SQLInsert="INSERT  INTO student_details values (" +  str (acc_no) + ",' " + acc_name + " ',"+str(ph_no) + ",' " +add + " ',"+" '"+ cr_amt +"',"+"'"+ course+"'" + " ) "
                                        cur.execute(V_SQLInsert)
                                        print()
                                        print('Account Created Succesfully!!!!!')
                                        conn.commit()
                                        time.sleep(10)
                                        clearconsole()

                              if n == 2:
                                   clearconsole()
                                   acct_no=int(input('Enter Your Roll Number='))
                                   cur.execute('select * from student_details where roll_no='+str (acct_no) )
                                   data=cur.fetchall()
                                   count=cur.rowcount
                                   conn.commit()
                                   if count == 0:
                                        print()
                                        print('Roll Number Invalid Sorry Try Again Later')
                                        print()
                                   else:
                                        print()
                                        for row in data:
                                             print("Previous course of "+str(acct_no)+" is "+str(row[5]))
                                        string1 = input("Enter the course name:- ")
                                        # final = value+' '+string1
                                        print((string1))
                                        print("update student_details set course_name= '"+string1+"' where roll_no="+str(acct_no))
                                        cur.execute("update student_details set course_name= '"+string1+"' where roll_no="+str(acct_no))
                                        conn.commit()
                                        print("record updated")
                                        
                                        print()
                                        print("Do u want to print:- Y/N")
                                        x = input()
                                        if x == "Y" or x=="y":
                                             for row in data:
                                                  print('ROLL NO=',acct_no)
                                                  print()
                                                  print('STUDENT NAME=',row[1])
                                                  print()
                                                  print(' PHONE NUMBER=',row[2])
                                                  print()
                                                  print('ADDRESS=',row[3])
                                                  print()
                                                  print('Standard=',row[4])
                                                  print()
                                                  print('Course=',row[5])
                                             time.sleep(60)
                                                  
                                        
                              if n == 3:
                                   clearconsole()
                                   acct_no=int(input('Enter your Roll number='))
                                   print()
                                   cur.execute('select * from student_details where roll_no='+str(acct_no) )
                                   if cur.fetchone() is  None:
                                        print()
                                        print('Invalid Roll number')
                                   else:
                                        cur.execute('select * from student_details where roll_no='+str(acct_no) )
                                        data=cur.fetchall()
                                        for row in data:
                                             print('ROLL NO=',acct_no)
                                             print()
                                             print('STUDENT NAME=',row[1])
                                             print()
                                             print(' PHONE NUMBER=',row[2])
                                             print()
                                             print('ADDRESS=',row[3])
                                             print()
                                             print('Standard=',row[4])
                                             print()
                                             print("course name=",row[5])
                                             
                              if n == 4:
                                   clearconsole()
                                   acct_no=int(input('Enter your Roll number='))
                                   print()
                                   cur.execute('select * from student_details where roll_no='+str(acct_no) )
                                   if cur.fetchone() is  None:
                                        print()
                                        print('Invalid Roll number')
                                   else:
                                        cur.execute('select * from student_details where roll_no='+str(acct_no) )
                                        data=cur.fetchall()
                                        for row in data:
                                             print('Roll NO=',acct_no)
                                             print()
                                             print("Course Details= ",row[5])
                                             print()
                                   

                              if n == 5:
                                   clearconsole()
                                   print('DELETE YOUR ACCOUNT')
                                   acct_no=int(input('Enter your account number='))
                                   
                                   cur.execute('delete from student_details where roll_no='+str(acct_no) )
                                   print('ACCOUNT DELETED SUCCESFULLY')

                              if n == 6:
                                   print('DO YO WANT TO EXIT(y/n)')
                                   c=input ('enter your choice=')
                              

                              
                              
     else:
          print('THANK YOU PLEASE VISIT AGAIN')
          quit()
          
     
                               
                              
                              
                              

                                        
               
     


