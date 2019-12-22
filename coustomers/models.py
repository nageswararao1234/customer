from django.db import models

# Create your models here.


class Coustomer(models.Model):
    """
    create a customer table
    """
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    age = models.IntegerField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name

