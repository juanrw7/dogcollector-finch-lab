from django.shortcuts import render, redirect
from .models import Dog, Snack
# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import WalkForm


# Create your views here.

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dog_index(request):
  dogs = Dog.objects.all()
  return render(request, 'dogs/index.html', { 'dogs': dogs })

def dog_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  walk_form = WalkForm()
  return render(request, 'dogs/detail.html', { 
    'dog': dog, 
    'walk_form' : walk_form
    })

class DogCreate(CreateView):
  model = Dog
  fields= '__all__'

class DogUpdate(UpdateView):
  model = Dog
  # Let's disallow the renaming of a Dog by excluding the name field!
  fields = ['breed', 'description', 'age']

class DogDelete(DeleteView):
  model = Dog
  success_url = '/dogs/'

def add_walk(request, dog_id):
  form = WalkForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_walk = form.save(commit=False)
    new_walk.dog_id = dog_id
    new_walk.save()
  return redirect('dog-detail', dog_id=dog_id)

class SnackCreate(CreateView):
  model = Snack
  fields = '__all__'



class SnackList(ListView):
  model = Snack

class SnackDetail(DetailView):
  model = Snack

class SnackUpdate(UpdateView):
  model = Snack
  fields = ['name']

class SnackDelete(DeleteView):
  model = Snack
  success_url = '/snacks/'