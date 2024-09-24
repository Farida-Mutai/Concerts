from database_setup import session
from models.band import Band
from models.venue import Venue
from models.concert import Concert

# Check if tables are created and retrieve counts
band_count = session.query(Band).count()
venue_count = session.query(Venue).count()
concert_count = session.query(Concert).count()

print(f"Number of Bands: {band_count}")
print(f"Number of Venues: {venue_count}")
print(f"Number of Concerts: {concert_count}")
