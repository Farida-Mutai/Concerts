from sqlalchemy import Column, String, Integer
from database_setup import Base



class Band(Base):
    __tablename__ = 'bands'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    concerts = relationship("Concert", back_populates="band")

    # Method to get all concerts for this Band
    def get_concerts(self):
        return self.concerts

    # Method to get all venues where this Band has performed
    def get_venues(self):
        return [concert.venue for concert in self.concerts]
