from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
