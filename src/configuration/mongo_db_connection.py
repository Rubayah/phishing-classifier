import os
import sys
import certifi
import pymongo

from src.constant import *
from src.exception import CustomException

ca = certifi.where()

class MongoDBClient:
    clinet = None

    def __init__(self, database_name = MONGO)