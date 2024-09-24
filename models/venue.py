from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database_setup import Base

class Venue(Base):
    __tablename__ = 'venues'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    city = Column(String) 
    
    
    concerts = relationship("Concert", back_populates="venue")
    
    def bands(self):
        return {concert.band for concert in self.concerts}
    
    def concert_on(self, date):
        return next((concert for concert in self.concerts if concert.date == date), None)
    
    def most_frequent_band(self):
        band_counts = {}
        for concert in self.concerts:
            band_counts[concert.band] = band_counts.get(concert.band, 0) + 1
        return max(band_counts, key=band_counts.get)
