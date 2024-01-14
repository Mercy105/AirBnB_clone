#!/usr/bin/python3
'''This module defines a class to manage file storage for hbnb project
'''
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    '''Serialize and deserialize instances to a JSON file
    Attr:
        - __file_path(str): path to our JSON file
        -__objects(dict): empty dictionary we will use
        to store our objects
    '''
    __file_path = 'file.json'
    __objects = {}
    classes = {
        "BaseModel": BaseModel, "User": User, "State": State,
        "City": City, "Amenity": Amenity, "Place": Place,
        "Review": Review
    }

    def all(self):
        '''Return a dictionary of all objects currently stored
        '''
        return FileStorage.__objects

    def new(self, obj):
        '''Fills in __objects with key <obj class name>.id
        The values will be corresponding dict representations
        '''
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        '''serializes __objects to our JSON file
        '''
        json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(json_objects, f)

    def reload(self):
        '''Deserializes json_string to __objects
        Raises:
            Nothing if JSON file does not exist
        '''
        try:
            with open(FileStorage.__file_path, 'r') as g:
                objs_dict = json.load(g)
                for k in objs_dict:
                    self.__objects[k] =\
                      self.classes[objs_dict[k]['__class__']](**objs_dict[k])
        except FileNotFoundError:
            pass
