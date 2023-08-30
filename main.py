import mysql.connector

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Execute SQL queries
query = "show databases"
cursor.execute(query)
for i in cursor:
    print(i)
conn.commit()

def create_database():
    n=input("Enter the database name: ")
    query=f"create database {n}"
    cursor.execute(query)
    conn.commit()

def delete_database():
    m=input("Enter the database name : ")
    query=f"drop database {m}"
    cursor.execute(query)
    conn.commit()

def create_table():
    m=input("Enter the database_name : ")
    cursor.execute(f"USE {m}")
    n=input("Enter the table name : ")
    query=f"create table {m}.{n} ( Id int primary key, Name varchar(20), Age int, Year int )"
    cursor.execute(query)
    conn.commit()

def dispaly_data():
    
    # Select display query
    m=input("Enter the database name : ")
    n=input("Enter teh table name : ")
    # to count the datas
    # cursor.execute(f"select count(*) from {m}.{n}")
    # to disaplay the datas
    cursor.execute(f"select * from {m}.{n}")
    result = cursor.fetchall()
    if result:
        print("Table datas are : ")
        for row in result:
            print(row)
    else:
        print("Table is Empty")


def insert_data():

    #insert data
    # query="insert into student_list (id,name) values(%s,%s)"
    # value=(1,"gokul")
    # value=(2,"gokul")
    # cursor.execute(query,value)
    # conn.commit()

    #insert data using for loop
    m=input("Enter the database name : ")
    n=input("Enter the table name : ")
    a=int(input("Enter the number of data you need to enter : "))
    values=[]
    for i in range(a):
        value1=input("Id : ")
        value2=input("Name : ")
        value3=input("Age : ")
        value4=input("year  : ")
        values.append((value1,value2,value3,value4))
    query= f"insert into {m}.{n} (Id, Name, Age, Year) values (%s,%s,%s)"
    for j in values:
        cursor.execute(query,j)
    conn.commit()

    #end of insert query

def delete_data():
    #delete data in table
    n=input("id to delete: ")
    query =f"delete from student_list where id={n}"
    cursor.execute(query)
    conn.commit()

def truncate_table():
    #delete all datas in the table
    m=input("Enter the database name : ")
    n=input("Enter the table name : ")
    query = f"truncate {m}.{n}"
    cursor.execute(query)
    conn.commit()
    dispaly_data()

def drop_table():
    #to delete the table
    n=input("Enter the table name : ")
    query =f"drop {n}"
    cursor.execute()
    conn.commit()



# insert_data()
# delete_data()
# truncate_table()
# dispaly_data()
# drop_table()
# create_table()
# delete_database()
# create_database()


# Close the cursor and connection
cursor.close()
conn.close()
