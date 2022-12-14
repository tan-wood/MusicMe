from unicodedata import decimal
from django.db import models
from datetime import datetime, timedelta

# Create your models here.
class Artist(models.Model):
    # the id is autogenerated when we migrate to the table
    artist_name = models.CharField(max_length=50)
    

    def __str__(self):
        return (self.artist_name)

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=50)
    album_photo = models.ImageField(upload_to='photos')

    def __str__(self) :
        return self.album_name

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=13, blank=True)
    album = models.ManyToManyField(Album, blank=True)

    def __str__(self) :
        return (self.full_name)
    
    @property # attribute of a model but does not get stored to the database 
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
        # string (space) string and then put in these values 

    def save(self):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        super(User, self).save() # so we modified the save method that already existed so we want to do the above code and then after call the rest of the default save