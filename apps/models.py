from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField,  Model,  FloatField, \
    ImageField


class User(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    profession = CharField(max_length=255)
    image = ImageField(upload_to='rasm')
    address = CharField(max_length=255)
    rating = FloatField()

#
# class User1(AbstractUser):
#     username = ForeignKey('auth.User', CASCADE)
#     email = ForeignKey('auth.User', CASCADE)

