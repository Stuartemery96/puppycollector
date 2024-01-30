from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Puppy
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
  feeding_form = FeedingForm()
  return render(request, 'puppies/detail.html', { 'puppy': puppy, 'feeding_form': feeding_form })

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