from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    # age = models.IntegerField
    hoddy = models.CharField(max_length=20)

    class Meta:
        db_table = "user"