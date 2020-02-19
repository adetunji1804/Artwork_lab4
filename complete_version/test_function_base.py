from unittest import TestCase
from function_base import *


class TestArtistArtwork(TestCase):
    # check available artwork, accept a paramater, to return true or false
    def test_check_available(self):
        #pass
        self.assertFalse(False, check_available('no'))
        self.assertTrue(True, check_available('yes'))

        with self.assertRaises(Exception):
            check_available("not")
        
        with self.assertRaises(Exception):
            check_available(1)

        # function add artist accept object parameter and return 1
    def test_add_artist(self):
        self.assertEqual(1, create_artist('name', 'email'))
        #failed
        with self.assertRaises(Exception):
            create_artist('artist', 'email')
    
    # add artwork accept object parameter and return number of row affected
    def test_create_artwork(self):
        self.assertEqual(1, create_artwork('artwork', price=1, isSold=True, artistId=1))

        with self.assertRaises(Exception):
            create_artwork('artwork', price=1, isSold=True, artistId=1)

     # test update function
    def test_update_artwork(self):
        self.assertEqual(1, update_art_sale('obj_name'))

        with self.assertRaises(Exception):
            update_art_sale('obj_name')


    #delete function
    def test_delete_artwork(self):
        self.assertEqual(1, delete_artwork('obj_name'))

        with self.assertRaises(Exception):
             delete_artwork('obj_name')


    def test_search_all_artwork(self):
        row = []
        self.assertListEqual(row, search_all_artwork(artist_id=1))

        with self.assertRaises(Exception):
             search_all_artwork(artist_id=1)

    
    def test_search_available_artwork(self):
        row = []
        self.assertListEqual(row, search_available_artwork(artist_id=1))

        with self.assertRaises(Exception):
             search_available_artwork(artist_id=1)

   