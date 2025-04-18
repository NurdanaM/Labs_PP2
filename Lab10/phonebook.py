import psycopg2
import csv

con = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="nurdana205!",
    host="localhost",
    port="5432"
)
cur = con.cursor()

# create table
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
)
""")
con.commit()

# insert data from console
def insert_console():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    con.commit()
    print("Data inserted!")

# insert from csv
def insert_csv():
    with open('/Users/nurdanam/Desktop/all_labs_pp2/Lab10/data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
        con.commit()
        print("Data from CSV inserted!")

# update
def update_data():
    name = input("Enter the name to update: ")
    new_phone = input("Enter the new phone number: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    con.commit()
    print("Data updated!")

# search 
def search():
    keyw = input("Enter part of name or phone to search: ")
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", (f'%{keyw}%', f'%{keyw}%'))
    rows = cur.fetchall()
    for row in  rows:
        print(row)
    
# delete 
def delete():
    target = input("Enter name or phone to delete: ")
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (target, target))
    con.commit()
    print("Data deleted!")

def menu():
    while True:
        print("\n1. Insert manually\n2. Insert from CSV\n3. Update\n4. Search\n5. Delete\n6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            insert_console()
        elif choice == '2':
            insert_csv()
        elif choice == '3':
            update_data()
        elif choice == '4':
            search()
        elif choice == '5':
            delete()
        elif choice == '6':
            break
menu()
cur.close()
con.close()