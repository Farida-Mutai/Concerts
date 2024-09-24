from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database_setup import Base

class Band(Base):
    __tablename__ = 'bands'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hometown = Column(String)  # Added hometown field
    
    # Relationships
    concerts = relationship("Concert", back_populates="band")
    
    def venues(self):
        return {concert.venue for concert in self.concerts}
    
    def play_in_venue(self, venue, date):
        new_concert = Concert(band_id=self.id, venue_id=venue.id, date=date)
        session.add(new_concert)
        session.commit()
    
    def all_introductions(self):
        return [
            f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            for concert in self.concerts
        ]

    @classmethod
    def most_performances(cls):
        bands = session.query(Band).all()
        return max(bands, key=lambda band: len(band.concerts))
