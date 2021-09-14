from django.db import models
from cloudinary.models import CloudinaryField
from django.db.models.deletion import CASCADE

# Create your models here.
class Image(models.Model):
  name = models.CharField(max_length=35)
  caption = models.TextField(default='caption')
  comments = models.TextField(default='comment here')
  photo = CloudinaryField('image',default='photo.jpeg')
  likes = models.PositiveIntegerField(default=0)
  profile = models.ForeignKey('Profile', on_delete=models.CASCADE, default='photo&bio')

  def __str__(self):
    return self.name

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()

class Profile(models.Model):
  name = models.CharField(max_length=70, default='Phi')
  profile_photo = CloudinaryField('image', default='img.jpg')
  bio = models.TextField(default='Add Bio here')

  def __str__(self):
    return self.name

  def save_profile(self):
    self.save()

  def delete_profile(self):
    self.delete()

  
