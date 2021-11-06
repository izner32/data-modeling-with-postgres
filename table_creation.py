import psycopg2 # to connect to postgres database 
from table_queries import drop_table_queries,create_table_queries# importing sql queries

# connecting to database then using this connection to execute sql queries
def create_database():
    # connect to default database 
    conn = psycopg2.connect("")
    conn.set_session(autocommit = True) # we need to commit every query execution, but with this we don't have to anymore
    cur = conn.cursor() # creating a cursor to execute queries

    # create database(sparkifydb) we want with UTF8 encoding 
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database so we could connect to the database(sparkifydb) we want
    conn.close()

    # connect to database(sparkifydb) we just created 
    conn = psycopgy2.connect("")
    conn.set_session(autocommit = True) 
    cur = conn.cursor()

    return conn, cur

# dropping each of the tables 
def drop_tables(conn,cur):
    for i in drop_table_queries:
        cur.execute(i)
        conn.commit() # commit every time we drop a table 

# creating each of the tables 
def create_tables(conn,cur):
    for i in create_table_queries:
        cur.execute(i)
        conn.commit() # commit every time we drop a table 
