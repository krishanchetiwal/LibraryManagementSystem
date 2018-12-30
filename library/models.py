from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    genre = models.CharField(max_length=100, default='')
    author = models.CharField(max_length=100, default='')
    section = models.CharField(max_length=100, default='')
    shelf_no = models.IntegerField(default=0)


