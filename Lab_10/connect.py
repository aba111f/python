import psycopg2 
import config 
# connection = psycopg2.connect(host = "localhost", port = "5432", database = "suppliers", user = "postgres", password = "z9h8i7b6")


def connect():
    connection = None 
    try:
        my_config = config.config()
        print('connection to the database...')
        print(my_config)
        connection = psycopg2.connect(**my_config)

        crsr = connection.cursor()
        print('pastgresql database version:')
        crsr.execute('SELECT version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally: 
        if connection is not None:
            connection.close()

if __name__ == "__main__":
    connect()