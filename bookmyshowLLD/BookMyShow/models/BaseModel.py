from django.db import models


class BaseModel(models.Model):
    def __init__(self):
        self._id = models.AutoField(primary_key=True)
        self._createdAt = models.DateTimeField()
        self._lastUpdatedAt = models.DateTimeField()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def createdAt(self):
        return self._createdAt

    @createdAt.setter
    def createdAt(self, value):
        self._createdAt = value

    @property
    def lastUpdatedAt(self):
        return self._lastUpdatedAt

    @lastUpdatedAt.setter
    def lastUpdatedAt(self, value):
        self._lastUpdatedAt = value
