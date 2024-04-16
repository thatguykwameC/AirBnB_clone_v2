#!/usr/bin/python3
""" database storage """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.review import Review
from models.place import Place
from models.amenity import Amenity


class DBStorage:
    """ Databse Storage Class """
    __engine = None
    __session = None

    def __init__(self):
        """ Init DBStorage """
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query objs depending of the class name """
        cls_list = [User, State, City, Amenity, Place, Review]

        if cls:
            cls_list = [cls] if isinstance(cls, str) else [cls]
        obj_list = []
        for cls in cls_list:
            cls_objs = self.__session.query(cls).all()
            obj_list.extend(cls_objs)
        return {f"{type(o).__name__}.{o.id}": o for o in obj_list}

    def new(self, obj):
        """ Adds the obj to the current db session """
        self.__session.add(obj)

    def save(self):
        """ Commits all the current db session's changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current db session obj if not None """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all the tables and loads them to db """
        Base.metadata.create_all(self.__engine)
        new_session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(new_session)
