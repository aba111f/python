import psycopg2


conn = psycopg2.connect("dbname=PhoneBook user=postgres password=z9h8i7b6")


cur = conn.cursor()

# Call the stored procedure
cur.execute("CALL insert_update_user('Someone', '123-456-7890')")


conn.commit()


cur.close()
conn.close()

