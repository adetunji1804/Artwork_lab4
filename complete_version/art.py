from peewee import *
#import sqlite3

# create an instance of a database, establish connection and enforce foreignkey constraints
db = SqliteDatabase('art_db.sqlite', pragmas={'foreign_keys': 1})

class Artist(Model):
    # class attributes
    name = CharField()
    email = CharField()

    def __str__(self):
        return f'Name: {self.name}, email: {self.email} '

    class Meta:
        database = db #model use the art_db.sqlite database


class Artwork(Model):
    #class attributes
    artwork = CharField(unique=True) 
    price = DecimalField(2, 0)
    isSold = BooleanField()
    artistId = ForeignKeyField(Artist, backref='artworks')


    def __str__(self):
        return f'Artwork: {self.artwork}, Price: {self.price}, Available: {self.isSold}'

    class Meta:
        database = db #model use the art_db.sqlite database

