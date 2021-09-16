from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey


# Create your models here.
class Image(models.Model):
  name = models.CharField(max_length=35)
  caption = models.TextField(default='caption')
  comments = models.TextField(default='comment here')
  photo = CloudinaryField('image',default='photo.jpeg')
  author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, related_name='the_phi')
  likes = models.PositiveIntegerField(default=0)
  time_created = models.DateTimeField(auto_now=True, auto_now_add=False)
  profile = models.ForeignKey('Profile', on_delete=models.CASCADE, default='photo&bio')

  def __str__(self):
    return self.name

  def save_image(self):
    self.save()

  def delete_image(self):
    self.delete()

  def update_image(self):
    fetched_object = Image.objects.filter()

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


class Comment(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey('Image', null=True, on_delete=models.CASCADE)
  comment = models.TextField(default='Comment Here')
  posted_on = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.comment

  def save_comment(self):
    self.save()

  def delete_comment(self):
    self.delete()


class Like(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey('Image', on_delete=models.CASCADE)

  class Meta:
    unique_together = ("user","post")

    def __str__(self):
      return 'Like: '+self.user.username+''+self.post.name


class Followers(models.Model):
  user = models.CharField(max_length=50, default='')
  follower = models.CharField(max_length=50, default='')


