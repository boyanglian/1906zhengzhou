from django.db import models

# Create your models here.
class Host(models.Model):
    id = models.AutoField(primary_key=True)
    press_name = models.CharField(max_length=35, null=False)