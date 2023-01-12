from django.db import models
from django.contrib.auth.models import User
from isbn_field import ISBNField


# Create your models here.

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    creator_user = models.ForeignKey(User,
                                     on_delete=models.PROTECT)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Author(BaseModel):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255,
                               null=True,
                               blank=True)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255,
                             null=True,
                             blank=True)
    address = models.CharField(max_length=255,
                               null=True,
                               blank=True)
    description = models.TextField(max_length=2048,
                                   null=True,
                                   blank=True)
    enabled = models.BooleanField(default=True)


class Book(BaseModel):
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author',
                               on_delete=models.PROTECT)
    count = models.IntegerField()
    isbn = ISBNField(null=True,
                     blank=True)
    price = models.DecimalField(max_digits=6,
                                decimal_places=2)
    size = models.SmallIntegerField(default=0,
                                    blank=True)
    pages = models.SmallIntegerField(default=0,
                                     blank=True)
    description = models.TextField(max_length=2048,
                                   null=True,
                                   blank=True)
    enabled = models.BooleanField(default=True)
