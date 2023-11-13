from django.db import models
# Create your models here.
class Person(models.Model):
    p_id = models.AutoField(primary_key=True)
    p_firstname = models.CharField(max_length=50)
    p_lastname = models.CharField(max_length=50)
    p_tel = models.CharField(max_length=20,null=True)
    p_regisyear = models.DateField(null=True)
    p_picture = models.ImageField(upload_to='images/')
    def __str__(self):
        return f'{self.p_firstname} {self.p_lastname}'