from models.band import Band
from models.venue import Venue
from models.concert import Concert
from database_setup import session  # Assuming you have a session defined in database_setup.py

# Example of seeding the database
def seed_database():
    # Create some example data
    band1 = Band(name="The Beatles")
    venue1 = Venue(name="Madison Square Garden")
    concert1 = Concert(date="2024-10-01", band=band1, venue=venue1)

    # Add and commit to the session
    session.add(band1)
    session.add(venue1)
    session.add(concert1)
    session.commit()

if __name__ == "__main__":
    seed_database()
