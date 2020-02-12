import sqlite3
from sqlite3 import Error

artist_details_table_sql = '''CREATE TABLE IF NOT EXISTS artist_tbl(
                artist_name TEXT, 
                email_address TEXT,
                artist_id INTEGER PRIMARY KEY ) '''


artwork_details_table_sql = '''CREATE TABLE IF NOT EXISTS artwork_tbl(
                artwork TEXT UNIQUE, 
                price NUMERIC,
                isSold BOOLEAN,
                artist_id INTEGER,
                FOREIGN KEY(artist_id) REFERENCES artist_tbl(artist_id) ) '''


def db_connection():
    conn = None
    try:
        conn= sqlite3.connect('artwork_db.sqlite')
        conn.execute('PRAGMA foreign_keys = ON')
    except Error as e:
        print(e)
    return conn

#add artist to database artist table
def add_artist(conn, table, name, email, artistid):
    conn = db_connection()
    table = artist_details_table_sql
    conn.execute(table)

    name = input('Enter artist name: ')
    email = input('Enter artist email: ')
    artistid = int (input('Enter artist id: '))

    sql = 'INSERT INTO artist_tbl values(?, ?, ?)'
    cur = conn.cursor()
    try:
        cur.execute(sql, (name, email, artistid))
    except sqlite3.DatabaseError as err:
        print(f'data cannot be commited, {err}')
    conn.commit()
    
#add artwork database artwork table
def add_artwork(conn, table, artwork, price, isSold, artistid):
    
    conn = db_connection()
    table = artwork_details_table_sql
    conn.execute(table)
    

    artwork = input('Enter the name of artwork: ')
    price = float(input('Enter price of artwork: '))
    available = input('is artwork available: Yes/No?')
    available = available.lower()
    if available == 'yes':
        isSold = True
    elif available == 'no':
        isSold =False
    else:
        print("Invalid! Response is either 'Yes' or 'No': ")

    artistid = int (input('Enter artist id: '))

    sql = 'INSERT INTO artwork_tbl values(?, ?, ?, ?)'
    cur = conn.cursor()
    try:
        cur.execute(sql, (artwork, price, isSold, artistid))
    except sqlite3.DatabaseError as err:
        print(f'data cannot be commited, {err}')
    conn.commit()


    #def delete_artist_artwork(artist_id):
      


if __name__ == "__main__":
    add_artist('con', 'tbl', 'name', 'email', artistid = 1)
    #add_artwork('conn', 'table', 'artwork', price = 0.00, isSold=False, artistid=1)