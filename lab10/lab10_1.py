import psycopg2
import csv

conn = psycopg2.connect(
    dbname="mydatabase",
    user="postgres",
    password="2303",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def crtab():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook2 (
            id SERIAL PRIMARY KEY,
            name VARCHAR(30) NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    """)
    conn.commit()

def ins_csv():
    file_path = input("Enter CSV file path: ")
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            cur.execute("INSERT INTO phonebook2 (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    conn.commit()
    print("CSV data inserted successfully")

def ins_cons():
    name1 = input("Enter name: ")
    phone1 = input("Enter phone number: ")
    cur.execute("INSERT INTO phonebook2 (name, phone) VALUES (%s, %s)", (name1, phone1))
    conn.commit()
    print("Contact added")

def upd():
    old_name = input("Enter the name of the user to update: ")
    update_name = input("Enter new name: ")
    update_phone = input("Enter new phone number: ")

    if update_name:
        cur.execute("UPDATE phonebook2 SET name = %s WHERE name = %s", (update_name, old_name))
    if update_phone:
        cur.execute("UPDATE phonebook2 SET phone = %s WHERE name = %s", (update_phone, update_name or old_name))
    conn.commit()
    print("Contact updated")

def query():
    filter_type = input("Filter by (n)ame, (p)hone, or show (a)ll? ").lower()
    if filter_type == 'n':
        name = input("Enter name to search: ")
        cur.execute("SELECT * FROM phonebook2 WHERE name ILIKE %s", ('%' + name + '%',))
    elif filter_type == 'p':
        phone = input("Enter phone number to search: ")
        cur.execute("SELECT * FROM phonebook2 WHERE phone = %s", (phone,))
    else:
        cur.execute("SELECT * FROM phonebook2")
    results = cur.fetchall()
    for row in results:
        print(row)

def delus():
    choice = input("Delete by (n)ame or (p)hone? ").lower()
    if choice == 'n':
        name = input("Enter name to delete: ")
        cur.execute("DELETE FROM phonebook2 WHERE name = %s", (name,))
    elif choice == 'p':
        phone = input("Enter phone number to delete: ")
        cur.execute("DELETE FROM phonebook2 WHERE phone = %s", (phone,))
    conn.commit()
    print("Contact deleted")

crtab()
print(""" 
    1. Insert from csv
    2. Insert from console
    3. Update 
    4. Query
    5. Delete
""")
n = input("Select: ")
if n == '1':
    ins_csv()
elif n == '2':
    ins_cons()
elif n == '3':
    upd()
elif n == '4':
    query()
elif n == '5':
    delus()