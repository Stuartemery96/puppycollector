from django.shortcuts import render

puppies = [
  {'name': 'Hazel', 'breed': 'chocolate lab', 'description': 'Rambunctious little bird dog', 'age': '1'},
  {'name': 'Remmy', 'breed': 'mini austrailian shephard', 'description': 'little fur ball', 'age': '5'},
]

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def puppies_index(request):
  return render(request, 'puppies/index.html', {'puppies': puppies})