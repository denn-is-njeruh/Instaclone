from django.test import TestCase
from .models import Image, Profile

# Create your tests here.
class TestProfileClass(TestCase):
  def setUp(self):
      self.new_profile = Profile(name = 'the_phi', profile_photo = 'image.jpg', bio = 'Dedicated coder')

  def test_instance(self):
    self.assertTrue(isinstance(self.new_profile,Profile))

  def test_save_method(self):
    self.new_profile.save_profile()
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles) > 0)


