#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship


merge_table = Table("place_amenity", Base.metadata,
                    Column("place_id", String(60), ForeignKey('places.id'),
                           primary_key=True, nullable=False),
                    Column("amenity_id", String(60),
                           ForeignKey('amenities.id'),
                           primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    @property
    def reviews(self):
        """ list of linked reviews """
        from models import storage
        return [r for r in storage.all(Review).values()
                if r.place_id == self.id]

    @property
    def amenities(self):
        """ list of all linked amenities """
        from models import storage
        return [a for a in storage.all(Amenity).values()
                if a.id in self.amenity_ids]

    @amenities.setter
    def amenities(self, param):
        """ linked amenities """
        if isinstance(param, Amenity):
            self.amenity_ids.append(param.id)
