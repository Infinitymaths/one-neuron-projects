



def Database_Create(host_name, user_name, user_password):
    """Function to activate database or Grant access to database if it already exist

     Args:
         host_name (str): hostname of your MySQL machine (example:localhost)
         user_name (str): username of MySQL instance
         user_password (str): passord of MySQL instance
    """
    from loging_func import log_thisError 
    import  mysql.connector as sql
    DB_NAME = "STUDENTDATA" #Name of the database
    try:
        # conn = sql.connect(host = "localhost", user="root", passwd="mysql8976", use_pure= True)
        conn = sql.connect(host = host_name, user=user_name, passwd=user_password, use_pure= True)
        #if conn.is_connected():
            #print('connected succesfully')
        cur = conn.cursor()
        try:
            cur.execute(f"CREATE DATABASE {DB_NAME}")
        except sql.Error as e:
            print(f"Failed creating Database {e}")
            log_thisError(e)
    except Exception as e:
        print(e)
        log_thisError(e)





def student_table(host_name, user_name, user_password) :
     """Funcion to create customer's details' table

     Args:
         host_name (str): hostname of your MySQL machine (example:localhost)
         user_name (str): username of MySQL instance
         user_password (str): passord of MySQL instance

     Raises:
         Exception: covered all the exceptions
     """
     import  mysql.connector as sql
     from loging_func import log_thisError
     # conn = sql.connect(host = "localhost", user="root", passwd="mysql8976", use_pure= True)
     conn = sql.connect(host = host_name, user=user_name, passwd=user_password, use_pure= True)
     #if conn.is_connected():
          #print('connected succesfully')
     cur = conn.cursor()
     DB_NAME = "STUDENTDATA" #Name of the database
     try:
        cur.execute(f"USE {DB_NAME}")
     except sql.Error as e:
        print(f"Database {DB_NAME} does not exist!")
        if e.errno == sql.errorcode.ER_BAD_DB_ERROR:
            Database_Create(host_name, user_name, user_password)
            print("Database Created Successfully")
            log_thisError("Database didn't exist, created successfully")
            
            conn.database = DB_NAME
        else:
            print(e)
            log_thisError(e)
             
     table_name = 'STUDENT'
     try:
        cur.execute('create table student_details(roll_no int primary key check(roll_no>7),name varchar(25) ,phone_no bigint(25) check(phone_no>11),address varchar(400),standard varchar(20),course_name varchar(50) )')
        print(f"{table_name} Data Table Checked (Created)")
     except sql.Error as e:
         if e.errno == sql.errorcode.ER_TABLE_EXISTS_ERROR:
             log_thisError(f"{table_name} Data table already existed {e}")
             print(f"{table_name} Data Table Checked")
         else:
             log_thisError(e)
             print(e)


def user_table(host_name, user_name, user_password) :
     """Funcion to initialize the user table

     Args:
         host_name (str): hostname of your MySQL machine (example:localhost)
         user_name (str): username of MySQL instance
         user_password (str): passord of MySQL instance

     Raises:
         Exception: covered all the exceptions
     """
     import  mysql.connector as sql
     from loging_func import log_thisError
     # conn = sql.connect(host = "localhost", user="root", passwd="mysql8976", use_pure= True)
     conn = sql.connect(host = host_name, user=user_name, passwd=user_password, use_pure= True)
     #if conn.is_connected():
          #print('connected succesfully')
     cur = conn.cursor()
     DB_NAME = "STUDENTDATA" #Name of the database
     try:
        cur.execute(f"USE {DB_NAME}")
     except sql.Error as e:
        print(f"Database {DB_NAME} does not exist!")
        if e.errno == sql.errorcode.ER_BAD_DB_ERROR:
            Database_Create(host_name, user_name, user_password)
            print("Database Created Successfully")
            log_thisError("Database didn't exist, created successfully")
            
            conn.database = DB_NAME
        else:
            print(e)
            log_thisError(e)
     table_name = 'USER'
     try:
        cur.execute('create table user_table(username varchar(25) primary key,passwrd varchar(25) not null )')
        print(f"{table_name} Data Table Checked (Created)")
     except sql.Error as e:
         if e.errno == sql.errorcode.ER_TABLE_EXISTS_ERROR:
             log_thisError(f"{table_name} Data table already existed {e}")
             print(f"{table_name} Data Table Checked")
         else:
             log_thisError(e)
             print(e)
