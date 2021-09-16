from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.
def index(request):
  message = 'Welcome to PhiInsta'
  return(request, 'index.html', {"message": message})

def register_new_user(request):
  if request.method == "POST":
    form = NewUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request,user)
      messages.success(request, 'Registration Successful.')
      return redirect('index.html')
    messages.error(request, 'Unsuccessful registration. Invalid information.')
  form = NewUserForm()
  return render(request, 'django_registration/registration_form.html', {"registration_form": form} )
