from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Image,Comment,Profile

class NewUserForm(UserCreationForm):
  email = forms.EmailField()

  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")


  def save(self,commit=True):
    user = super(NewUserForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
      user.save()
    return user


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['user', 'body']


class UploadImageForm(forms.ModelForm):
  class Meta:
    model = Image
    exclude = ['comments', 'likes', 'profile',]


class ProfileEditForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['',]

