from django.db import models

# Create your models here.
class Image(models.Model):
  name = models.CharField(max_length=35)
  caption = models.TextField(default='caption')
  comments = models.TextField(default='comment here')
  photo = CloudinaryField('image',default='photo.jpeg')
  likes = models.PositiveIntegerField(default=0)
