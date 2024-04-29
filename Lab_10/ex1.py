import psycopg2
import csv

# Connect to your postgres DB
conn = psycopg2.connect("dbname=PhoneBook user=postgres password=z9h8i7b6")

# Open a cursor to perform database operations
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS PhoneBook (
    username VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL
)
""")
conn.commit()

# Insert data from CSV file
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # Skip the header row
    for row in reader:
        cur.execute(
            "INSERT INTO PhoneBook VALUES (%s, %s)",
            row
        )
conn.commit()

# Insert data from console
# run = True
# while run:
#     username = input("Enter username: ")
#     phone = input("Enter phone: ")
#     cur.execute(
#         "INSERT INTO PhoneBook VALUES (%s, %s)",
#         (username, phone)
#     )
#     conn.commit()
#     run = False
# Query data
# cur.execute("SELECT * FROM PhoneBook WHERE username like 'A%'")
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# Update data
# new_phone = input("Enter new phone for user: ")
# cur.execute(
#     "UPDATE PhoneBook SET phone = %s WHERE username = %s",
#     (new_phone, 'Alice')
# )

# Delete data
# username_to_delete = input("Enter username to delete: ")
# cur.execute("DELETE FROM PhoneBook WHERE username = %s", (username_to_delete,))

# Close communication with the database
cur.close()
conn.close()
