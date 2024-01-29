from django.shortcuts import render
from .models import Puppy

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def puppies_index(request):
  puppies = Puppy.objects.all()
  return render(request, 'puppies/index.html', {'puppies': puppies})

def puppies_detail(request, puppy_id):
  puppy = Puppy.objects.get(id=puppy_id)
  return render(request, 'puppies/detail.html', { 'puppy': puppy})