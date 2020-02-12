class Artist:
    
    def __init__(self, name, email, id):
        self.name = name
        self.email = email
        self.id = id


class Artwork:

    def __init__(self, artwork, price, is_sold, artist_id):
        self.artwork = artwork
        self.price = price
        self.is_sold = is_sold
        self.artist_id = artist_id

