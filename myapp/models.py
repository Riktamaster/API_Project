from django.db import models

# Create your models here.
class book_model(models.Model):
    Title=models.CharField(max_length=100)
    Author=models.CharField(max_length=50)
    ISBN=models.CharField(max_length=20, unique=True)
    Publisher=models.CharField(max_length=50)

    def __str__(self):
        return self.Title
