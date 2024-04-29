import psycopg2



conn = psycopg2.connect("dbname=PhoneBook user=postgres password=z9h8i7b6")


cur = conn.cursor()

# search data with following pattern
def search_records(pattern1, pattern2):
    cur.execute("SELECT * FROM phonebook WHERE username LIKE %s AND phone LIKE %s", (pattern1, pattern2))
    print(cur.fetchall())


# Procedure to insert or update a user
def insert_or_update_user(name, phoneNUM):
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s) ON CONFLICT (username) DO UPDATE SET phone = %s", (name, phoneNUM, phoneNUM))
    conn.commit()



# Procedure to delete data by username or phone
def delete_user(username, phone):
    if username:
        cur.execute(("DELETE FROM phonebook WHERE username = %s"), (username,))
    elif phone:
        cur.execute(("DELETE FROM phonebook WHERE phone = %s"), (phone,))
    conn.commit()



pattern1 = 'f%'
pattern2 = '+%'

username = input()
phone = input()

if __name__ == '__main__':
    # search_records(pattern1, pattern2)
    # insert_or_update_user('Someguy','+434238525')
    delete_user(username, phone)

