from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Company(models.Model):
    cname=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    ceo=models.CharField(max_length=100)
    def __str__(self):
        return self.cname
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})

class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=64)
    esal=models.FloatField()
    company=models.ForeignKey(Company,related_name='employees')
    def get_absolute_url(self):
        return reverse('detail',kwargs={'pk':self.pk})
