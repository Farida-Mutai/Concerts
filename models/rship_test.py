from Models import Band, Venue, Concert
from database_setup import session

# Test 1: Get the band for the first concert
first_concert = session.query(Concert).first()
print(f"Concert on {first_concert.date} is performed by: {first_concert.get_band().name}")

# Test 2: Get the venue for the first concert
print(f"Concert on {first_concert.date} is held at: {first_concert.get_venue().name}")

# Test 3: Get all concerts at the first venue
first_venue = session.query(Venue).first()
print(f"Venue: {first_venue.name} hosted concerts on: {[concert.date for concert in first_venue.get_concerts()]}")

# Test 4: Get all bands that performed at the first venue
bands_at_first_venue = [band.name for band in first_venue.get_bands()]
print(f"Bands that performed at {first_venue.name}: {bands_at_first_venue}")

# Test 5: Get all concerts for the first band
first_band = session.query(Band).first()
print(f"Band: {first_band.name} played on the following dates: {[concert.date for concert in first_band.get_concerts()]}")

# Test 6: Get all venues where the first band performed
venues_for_first_band = [venue.name for venue in first_band.get_venues()]
print(f"Band: {first_band.name} performed at: {venues_for_first_band}")
