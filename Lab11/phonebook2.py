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

cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
)
""")
con.commit()

def insert_console():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (name, phone))
    con.commit()
    print("Data inserted!")

def insert_csv():
    with open('/Users/nurdanam/Desktop/all_labs_pp2/Lab10/data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            cur.execute("INSERT INTO phonebook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
        con.commit()
        print("Data from CSV inserted!")

def update_data():
    name = input("Enter the name to update: ")
    new_phone = input("Enter the new phone number: ")
    cur.execute("UPDATE phonebook SET phone = %s WHERE name = %s", (new_phone, name))
    con.commit()
    print("Data updated!")
 
def search():
    keyw = input("Enter part of name or phone to search: ")
    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s OR phone ILIKE %s", (f'%{keyw}%', f'%{keyw}%'))
    rows = cur.fetchall()
    for row in rows:
        print(row)

def delete():
    target = input("Enter name or phone to delete: ")
    cur.execute("DELETE FROM phonebook WHERE name = %s OR phone = %s", (target, target))
    con.commit()
    print("Data deleted!")

# Procedure: insert or update user
def insert_or_update_user():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    cur.execute("CALL insert_or_update_user(%s, %s)", (name, phone))
    con.commit()
    print("User inserted or updated!")

# Procedure: insert many users
def insert_many_users():
    n = int(input("Enter number of users to add: "))
    names = []
    phones = []
    for i in range(n):
        name = input(f"Name {i+1}: ")
        phone = input(f"Phone {i+1}: ")
        names.append(name)
        phones.append(phone)
    cur.execute("CALL insert_many_users(%s, %s)", (names, phones))
    con.commit()
    print("Users inserted (check terminal for incorrect data)")

# Function: search by pattern
def search_by_pattern():
    pattern = input("Enter search pattern: ")
    cur.execute("SELECT * FROM search_by_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Function: paginated results
def paginate():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))
    cur.execute("SELECT * FROM paginate(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Procedure: delete by name or phone
def delete_user():
    target = input("Enter name or phone to delete: ")
    cur.execute("CALL delete_user(%s)", (target,))
    con.commit()
    print("User deleted.")

def menu():
    while True:
        print("""
1. Insert manually
2. Insert from CSV
3. Update
4. Search
5. Delete
6. Insert or update user (procedure)
7. Insert many users (procedure)
8. Search by pattern (function)
9. Paginated results (function)
10. Delete by name/phone (procedure)
11. Exit
""")
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
            insert_or_update_user()
        elif choice == '7':
            insert_many_users()
        elif choice == '8':
            search_by_pattern()
        elif choice == '9':
            paginate()
        elif choice == '10':
            delete_user()
        elif choice == '11':
            break

menu()
cur.close()
con.close()