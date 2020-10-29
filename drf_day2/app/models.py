from django.db import models

# Create your models here.

class Teacher(models.Model):
    gender_choice = (
        (0,'男'),
        (1,'女')
    )
    name = models.CharField(max_length=20)
    age = models.IntegerField
    gender = models.SmallIntegerField(choices=gender_choice,default=0)
    ke = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    pic = models.ImageField(upload_to='pic/',default='pic/1.jpg')

    class Meta:
        db_table = 'teacher'
        verbose_name = '教师'
        verbose_name_plural = verbose_name