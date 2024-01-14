#!/usr/bin/python3
'''This module defines class User
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Define user by various attributes
    Attr:
        -email (str): user email
        -password (str): user password
        -first_name (str): first name of user
        -last_name (str): last name of user
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
