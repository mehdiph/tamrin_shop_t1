from django.db import models

# Create your models here.
class coment (models.Model):
    name =models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    created= models.DateTimeField(auto_now_add=True)
    