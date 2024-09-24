class Concert(Base):
    __tablename__ = 'concerts'
    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    band_id = Column(Integer, ForeignKey('bands.id'), nullable=False)
    venue_id = Column(Integer, ForeignKey('venues.id'), nullable=False)

    band = relationship("Band", back_populates="concerts")
    venue = relationship("Venue", back_populates="concerts")

    # Method to get the associated Band instance for a Concert
    def get_band(self):
        return self.band

    # Method to get the associated Venue instance for a Concert
    def get_venue(self):
        return self.venue
