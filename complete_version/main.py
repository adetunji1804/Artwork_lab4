from function_base import *
import sqlite3

def main():
    # command execution guide manual
    print('\nINSTRUCTION MANUAL\n-----------------------')
    print('To ADD ARTIST - artist\nTo Add ARTWORK  - artwork')
    print('To SEARCH ALL ARTWORK IN DATABASE  - all')
    print('To SEARCH AVAILABLE ARTWORK  - unsold')
    print('To UPDATE AVAILABILITY STATUS  - u')
    print('To DELETE ART WORK  - del')
    print('To EXIT APPLICATION  - ex')

    db.connect() # established connection to datavase
    db.create_tables([Artist, Artwork]) #peewee auto generate tables
    

    check = True

    while check: # continue prompt for operation if criteria below are met
        
        choice = input('\nEnter choice of operation: ')
        print('\n')
        choice = choice.upper()
        #try:
            
            # identify operation symbol
        if choice == 'ARTIST': # add artist
            result = create_artist('name', 'email')
            print(f'successfully added {result} row') 

        elif choice == 'ARTWORK': # add artwork
                result = create_artwork('Artwork', 1, True, 1)
                print(f'sucessfully added {result} row')       

        elif choice == 'ALL': # search all artwork by artist
            result = search_all_artwork(artist_id=1)
            for items in result:
                print(items)

        elif choice == 'UNSOLD': # search all unsold artwork by artist
            result = search_available_artwork('artist_id')
            for items in result:
                print(items)
            
        elif choice == 'U': # update artwork availability status
            result = update_art_sale('obj_name')
            print(result)

        elif choice == 'DEL': # delete artwork  
            result = delete_artwork('obj_name')
            print(f'{result} row/s deleted')

        elif choice == 'EX': # Exit application
            raise SystemExit(f'application terminated.......bye!')

        else:
            print('Invalid operation sign!') # message displayed when operation sign is not on list
        db.close()
    #except: # handle error
        #print('Error! Operation aborted')
    #finally:
        
        
if __name__ == "__main__":
    main()