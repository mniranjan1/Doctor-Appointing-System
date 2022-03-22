from django.db import models
# Create your models here.

class doc(models.Model) :
    name = models.CharField(max_length=200)
    qualification = models.CharField(max_length=100)
    experience = models.IntegerField()
    job = models.CharField(max_length=200)
    like = models.IntegerField()
    patient_experience = models.IntegerField()
    address = models.CharField(max_length=200)
    available = models.CharField(max_length=200)
    img = models.ImageField(upload_to='pics')






