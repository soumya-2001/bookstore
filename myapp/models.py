from django.db import models

# Create your models here.

class Book(models.Model):
    book_title=models.CharField(max_length=200,unique=True)
    ISBN_No=models.IntegerField()
    author_name=models.CharField(max_length=200)
    publisher=models.CharField(max_length=200)
    year_of_publication=models.IntegerField()
    genre=models.CharField(max_length=200)
    price=models.IntegerField()
    
    def __str__(self):
        return self.book_title