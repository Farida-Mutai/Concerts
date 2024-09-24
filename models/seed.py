from database_setup import session
from band import Band
from venue import Venue
from concert import Concert

# Add your seeding logic here
band1 = Band(name='The Rockers', hometown='New York')
band2 = Band(name='Jazz Hands', hometown='Chicago')

venue1 = Venue(name='Madison Square Garden', city='New York')
venue2 = Venue(name='Chicago Theatre', city='Chicago')

# Add bands and venues to the session
session.add_all([band1, band2, venue1, venue2])
session.commit()

# Create concerts
concert1 = Concert(band_id=band1.id, venue_id=venue1.id, date='2024-10-01')
concert2 = Concert(band_id=band2.id, venue_id=venue2.id, date='2024-10-02')
concert3 = Concert(band_id=band1.id, venue_id=venue2.id, date='2024-10-03')

# Add concerts to the session
session.add_all([concert1, concert2, concert3])
session.commit()

print("Database seeded with initial data.")
