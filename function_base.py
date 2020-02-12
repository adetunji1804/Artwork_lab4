# refernces to modules
from art_class import Artist
from art_class import Artwork
import sqlite3
from sqlite3 import Error

# query string to create ARTIST table
artist_details_table_sql = '''CREATE TABLE IF NOT EXISTS artist_tbl(
                artist_name TEXT, 
                email_address TEXT,
                artist_id INTEGER PRIMARY KEY ) '''

# query string to create ARTWORK table
artwork_details_table_sql = '''CREATE TABLE IF NOT EXISTS artwork_tbl(
                artwork TEXT UNIQUE, 
                price NUMERIC,
                isSold BOOLEAN,
                artist_id INTEGER,
                FOREIGN KEY(artist_id) REFERENCES artist_tbl(artist_id) ) '''

# Query string. Join table Artwork_tbl and Artist_tbl to search all artwork related to artist
search_artwork_details = '''SELECT a.rowid, a.artwork, a.price, a.isSold
                FROM artwork_tbl AS a JOIN artist_tbl AS b
                ON a.artist_id = b.artist_id
                WHERE b.artist_name = ?
                '''

# Query string. Join table Artwork_tbl and Artist_tbl to search all available artwork related to artist
search_available_artwork = '''SELECT a.rowid, a.artwork, a.price
                FROM artwork_tbl AS a JOIN artist_tbl AS b
                ON a.artist_id = b.artist_id
                WHERE b.artist_name = ? AND a.isSold = ?
                '''

# function create database, connection, and enforced the foreign key policy
def db_connection():
    conn = None #return none if connection is not established
    try:
        conn= sqlite3.connect('artwork_db.sqlite')
        conn.execute('PRAGMA foreign_keys = 1')
    except Error as e: # capture connection error
        print(e)
    return conn

#add artist to database artist table
def add_artist(conn, table, artist_obj):
    conn = db_connection()
    table = artist_details_table_sql
    conn.execute(table)

#prompt for artist object attribute values
    name = input('Enter artist name: ')
    email = input('Enter artist email: ')
    id = int (input('Enter artist id: '))

# instanciate an object of artist class
    artist_obj = Artist(name, email, id)
    sql = 'INSERT INTO artist_tbl values(?, ?, ?)' #parameterized query
    cur = conn.cursor() # row cursor created
    try:
        cur.execute(sql, (artist_obj.name.upper(), artist_obj.email, artist_obj.id))
        return cur.rowcount 
    except sqlite3.DatabaseError as err: #capture database error
        return f'data cannot be commited, {err}'
    conn.commit()

    
    
#function to add artwork to database table
def add_artwork(conn, table, artwork_obj):
    conn = db_connection()
    table = artwork_details_table_sql
    conn.execute(table)
    cur = conn.cursor()

    artist_id = int (input('Enter artist Id: '))
    artwork = input('Enter the name of artwork: ')
    price = float(input('Enter price of artwork: '))
    is_available = input('is artwork available: Yes/No?: ')
    
    is_available = is_available.lower()
    if is_available== 'yes':
        is_sold = True
    elif is_available == 'no':
        is_sold =False 
    else:
        print("Invalid! check if available response['Yes' or 'No']")

    artwork_obj = Artwork(artwork, price, is_sold, artist_id)
    sql = 'INSERT INTO artwork_tbl values(?, ?, ?, ?)'
    
    try:
        cur.execute(sql, (artwork_obj.artwork.upper(), artwork_obj.price, artwork_obj.is_sold, artwork_obj.artist_id))
        return cur.rowcount
    except sqlite3.DatabaseError as err:
        return f'data cannot be commited, {err}'
    conn.commit()
    

# function to remove artwork       
def delete_artwork(artwork_obj):
    conn = db_connection()
    sql_query = 'DELETE FROM artwork_tbl WHERE artwork = ?'
    artwork_name = input('Enter artwork to delete: ')
    artwork_obj = Artwork(artwork_name, 0.00, True, 1)
    cur = conn.cursor()
    try:
       cur.execute(sql_query, (artwork_obj.artwork.upper(), ))
       return f'deleted {cur.rowcount} row'
    except sqlite3.DatabaseError as err:
        return f'data cannot be commited, {err}'
    conn.commit()
    

# function to retrieve all artwork
def search_all_record(conn, join_table, artist_obj):
    conn = db_connection()
    join_table = search_artwork_details
    cur = conn.cursor()
    search_artwork = input('Enter artist name: ')
    artist_obj = Artist(search_artwork, 'email', id=1)
    try:
        artwork_detail = cur.execute(join_table, (artist_obj.name.upper(), ))
        print(f'\nRECORD OF {artist_obj.name.upper()} ARTWORK')
        return artwork_detail
    except sqlite3.DatabaseError as err:
        return f'data cannot be commited, {err}'
    conn.commit()
    

# function to retrieve each artist artwork
def search_available_record(conn, join_table, artist_obj, artwork_obj):
    conn = db_connection()
    join_table = search_available_artwork
    cur = conn.cursor()
    search_artwork = input('Enter artist name: ')
    artist_obj = Artist(search_artwork, 'email', id=1)
    artwork_obj = Artwork("artwork", price=0.00, is_sold =True, artist_id=1)
    try:
        artwork_detail = cur.execute(join_table, (artist_obj.name.upper(), artwork_obj.is_sold ))
        print(f'\nAVAILABLE ARTWORK FOR {artist_obj.name}')
        return artwork_detail
    except sqlite3.DatabaseError as err:
        return f'data cannot be commited, {err}'
    conn.commit()
    
    
# function to update artwork
def update_artwork(artwork_obj):
    conn = db_connection() # connection returned the connection string to open database
    cur = conn.cursor() 
    sql_query = 'UPDATE artwork_tbl SET isSold = ? WHERE artwork = ?'
    artwork_name = input('Enter artwork to update: ')
    available =input('Update availability [Yes or No]: ')

    available = available.lower()
    if available == 'yes':
        isSold = True
    elif available == 'no':
       isSold = False
    artwork_obj = Artwork(artwork_name, 0.00, isSold, 1)
    artwork_obj.is_sold = isSold
    
    try:
       cur.execute(sql_query, (artwork_obj.is_sold, artwork_obj.artwork.upper()))
       return f'Updated {cur.rowcount} row/s'
    except sqlite3.DatabaseError as err:
        return f'data cannot be commited, {err}'
    conn.commit()
