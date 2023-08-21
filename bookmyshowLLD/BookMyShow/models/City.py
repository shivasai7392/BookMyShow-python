from django.db import models

from bookmyshowLLD.BookMyShow.models.BaseModel import BaseModel


class City(BaseModel):
    def __init__(self):
        self._name = models.CharField(max_length=255)
        ##self._theatres = None
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def theatres(self):
        return self._theatres

    @theatres.setter
    def theatres(self, value):
        self._theatres = value
