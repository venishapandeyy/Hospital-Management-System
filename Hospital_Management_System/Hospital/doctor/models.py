
from django.db import models

# Create your models here.
class Doctor(models.Model):
    doc_id = models.IntegerField(primary_key = True)
    doc_name = models.CharField(max_length=20)
    doc_email = models.EmailField()
    specialisation = models.CharField(max_length=20)
    qualification = models.CharField(max_length=20)
    image = models.ImageField(upload_to='uploads/', null=True)

    def __str__(self):
        return self.doc_name
