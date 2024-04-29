import psycopg2



conn = psycopg2.connect("dbname=PhoneBook user=postgres password=z9h8i7b6")


cur = conn.cursor()

# search data with following pattern
def search_records(pattern1, pattern2):
    cur.execute("SELECT * FROM phonebook WHERE username LIKE %s AND phone LIKE %s", (pattern1, pattern2))
    print(cur.fetchall())




pattern1 = 'f%'
pattern2 = '+%'



if __name__ == '__main__':
    search_records(pattern1, pattern2)
    

cur.close()
conn.close()