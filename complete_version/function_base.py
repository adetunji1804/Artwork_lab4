from art import *

# function add artist to table
def create_artist(name, email):
    #instanciate an object of artist class
    obj_artist = Artist(name, email)
    #prompt for object attributes value
    name = input('Enter artist name: ')
    email = input('Enter artist email: ')
    try:
        obj_artist.name = name #initialize name
        obj_artist.email = email #initialize email
        row_added = obj_artist.save() #commit to table in database
    except:
        print('Invalid operation!')
    return row_added #return number of row/s added

    
#Check for artwork sale status
def check_available(is_available):
    is_available = is_available.lower() #input to lower case before
    if is_available== 'yes':
        return True
    elif is_available == 'no':
        return False 
    else:
        raise ValueError (f'invalid input!')

#function to add artwork to table
def create_artwork(artwork, price, isSold, artistId):
    #prompt user for data
    artwork = input('Enter artwork: ')
    price =float(input('Enter the price: '))
    is_available = input('Enter either ["YES" or "NO"] for availability: ')
    artistId =int(input('Enter artist ID: '))
    isSold = check_available(is_available)

    try:
        #instanciate object of artwork class
        object_artwork = Artwork(artwork, price, isSold, artistId)
        object_artwork.artwork = artwork.upper()
        object_artwork.price = price
        object_artwork.isSold = isSold
        object_artwork.artistId = artistId
        row_added = object_artwork.save() #added /commit data to table
    except:
        print('Invalid operation!')
    return row_added #return number of row/s added


def search_all_artwork(artist_id):
    record = [] #empty list to hold recored/s
    try: #guard error 
        artist_id = int(input('Enter artist ID: ')) #user input
        object_artwork = Artwork('artwork', 1, True, artist_id) #object created

        object_artwork.artistId = artist_id #value pass to object attribute
        #iterate over record fetched
        for potrait in Artwork.select().join(Artist).where(Artist.id == object_artwork.artistId):
            record.append(potrait) #added each record to list
    except:
        print('Error! Data cannot be retrieved') # message if error
    return record #return record list
    

def search_available_artwork(artist_id):
    record = []
    try:
        artist_id = int(input('Enter artist ID: '))
        #instaciate class object 
        object_artwork = Artwork('artwork', 1, True, artist_id)

        object_artwork.artistId = artist_id
        object_artwork.isSold = True
        #for potrait in Artwork.select().join(Artist).where((Artwork.artistId_id == object_artwork.artistId) and (Artwork.isSold == object_artwork.isSold)):
        for potrait in Artwork.select().where(Artwork.artistId_id == artist_id and Artwork.isSold == object_artwork.isSold):
            record.append(potrait)
    except:
        print('Error! Data cannot be retrieved')
    return record
    
#function to delete object take artwork attribute as parameter
def delete_artwork(obj_name):

    obj_name = input('Enter artwork to delete: ')
    obj_artwork = Artwork(obj_name, 1, True, 1)
    obj_artwork.artwork = obj_name.upper()
    deleted = Artwork.delete().where(Artwork.artwork == obj_artwork.artwork)
    row_deleted = deleted.execute() #commit to database
    return  row_deleted

# function to update
def update_art_sale(obj_name):
    
    obj_name = input('Enter artwork name: ')

    # call function to transalte and assign user response to available artwork
    is_available = input('Is artwork availabe ["Yes" or "No"]?: ')
    is_sold = check_available(is_available)
    try:
        obj_artwork = Artwork(obj_name, 1, True, 1)
        obj_artwork.artwork = obj_name.upper()
        obj_artwork.isSold =is_sold

        updated = Artwork.update(isSold = obj_artwork.isSold).where(Artwork.artwork == obj_artwork.artwork)
        row_updated = updated.execute()
    except:
        print('Invalid operation!')
    return row_updated #return number of row/s affected