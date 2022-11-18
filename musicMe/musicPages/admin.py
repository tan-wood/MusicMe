from django.contrib import admin
from .models import Album, User, Artist
# Register your models here.

# We can give the admin users access to whatever we want or as little as we want
admin.site.register(Album)
admin.site.register(Artist)
admin.site.register(User)