from django.db import models

# Create your models here.
class Secret(models.Model):
    code = models.CharField(max_length=4)
