from sqlalchemy import Column, String, Integer
from database_setup import Base


class Venue(Base):
    __tablename__ = 'venues'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    concerts = relationship("Concert", back_populates="venue")

    # Method to get all concerts for this Venue
    def get_concerts(self):
        return self.concerts

    # Method to get all bands who performed at this Venue
    def get_bands(self):
        return [concert.band for concert in self.concerts]
