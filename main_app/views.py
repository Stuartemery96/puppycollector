import os
import uuid
import boto3
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Puppy, Toy, Photo
from .forms import FeedingForm

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
  id_list = puppy.toys.all().values_list('id')
  unpossessed_toys = Toy.objects.exclude(id__in=id_list)
  feeding_form = FeedingForm()
  return render(request, 'puppies/detail.html', { 'puppy': puppy, 'feeding_form': feeding_form, 'toys': unpossessed_toys })

class PuppyCreate(CreateView):
  model = Puppy
  fields = '__all__'
  
class PuppyUpdate(UpdateView):
  model = Puppy
  fields = '__all__'

class PuppyDelete(DeleteView):
  model = Puppy
  success_url = '/puppies'  
  
def add_feeding(request, puppy_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.puppy_id = puppy_id
    new_feeding.save()
  return redirect('detail', puppy_id=puppy_id)

class ToyList(ListView):
  model = Toy
  
class ToyDetail(DetailView):
  model = Toy

class ToyCreate(CreateView):
  model = Toy
  fields = '__all__'
  
class ToyUpdate(UpdateView):
  model = Toy
  fields = ['name', 'color']
  
class ToyDelete(DeleteView):
  model = Toy
  success_url = '/toys'
  
def assoc_toy(request, puppy_id, toy_id):
  Puppy.objects.get(id=puppy_id).toys.add(toy_id)
  return redirect('detail', puppy_id=puppy_id)

def unassoc_toy(request, puppy_id, toy_id):
  Puppy.objects.get(id=puppy_id).toys.remove(toy_id)
  return redirect('detail', puppy_id=puppy_id)

def add_photo(request, puppy_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      bucket = os.environ['S3_BUCKET']
      s3.upload_fileobj(photo_file, bucket, key)
      url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
      Photo.objects.create(url=url, puppy_id=puppy_id)
    except Exception as e:
      print('An error occurred upliading file to S3')
      print(e)
  return redirect('detail', puppy_id=puppy_id)