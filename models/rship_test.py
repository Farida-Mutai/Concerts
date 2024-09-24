from database_setup import session
from models.band import Band
from models.venue import Venue
from models.concert import Concert



first_band = session.query(Band).first()
print("First Band:", first_band.name)
print("Venues for this band:", [venue.name for venue in first_band.venues()])
print("Concerts for this band:", [concert.date for concert in first_band.concerts])

first_venue = session.query(Venue).first()
print("First Venue:", first_venue.name)
print("Bands at this venue:", [band.name for band in first_venue.bands()])
print("Concert on 2024-10-01:", first_venue.concert_on('2024-10-01'))
