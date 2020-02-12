from function_base import *

if __name__ == "__main__":
    # command execution guide manual
    print('\nINSTRUCTION MANUAL\n-----------------------')
    print('To ADD ARTIST - Add AR\nTo Add ARTWORK  - Add AW')
    print('To SEARCH ALL ARTWORK IN DATABASE  - S AAW')
    print('To SEARCH EACH ARTIST WORK  - S EAW')
    print('To UPDATE AVAILABILITY STATUS  - U')
    print('To DELETE ART WORK  - DEL')
    print('To EXIT APPLICATION  - EX')

    check = True

    while check: # continue prompt for operation if criteria below are met
        choice = input('\nEnter choice of operation: ')
        print('\n')
        choice = choice.upper()
        try:
            # identify operation symbol
            if choice == 'ADD AR': # add artist
                result = add_artist('con', 'tbl', 'name')
                print(f'successfully added {result} row') 

            elif choice == 'ADD AW': # add artwork
                 result = add_artwork('conn', 'table', 'artwork_obj') 
                 print(f'sucessfully added {result} row')       

            elif choice == 'S AAW': # search all artwork
                result = search_all_record('con', 'join_table', 'artist_obj')
                for items in result:
                    print(items)

            elif choice == 'S EAW': # search all artwork by artist
                result = search_available_record('con', 'join_table', 'artist_obj','artwork_obj')
                for items in result:
                    print(items)
                
            elif choice == 'U': # update artwork availability status
               result = update_artwork('artwork_obj')
               print(result)

            elif choice == 'DEL': # delete artwork  
                result = delete_artwork('artwork_obj')
                print(result)

            elif choice == 'EX': # Exit application
                raise SystemExit(f'application terminated.......bye!')

            else:
                print('Invalid operation sign!') # message displayed when operation sign is not on list
        except sqlite3.Error as err: # handle database error
            print(f'Error! Operation aborted. {err}')
        finally:
            connection = db_connection()
            connection.close()