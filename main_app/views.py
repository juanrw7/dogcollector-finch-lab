from django.shortcuts import render, redirect
from .models import Dog, Snack
# Add the following import
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import WalkForm

from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import UserCreationForm
# Import the login_required decorator
from django.contrib.auth.decorators import login_required
# Import the mixin for class-based views
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

# Define the home view
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def dog_index(request):
  dogs = Dog.objects.filter(user=request.user)
  return render(request, 'dogs/index.html', { 'dogs': dogs })

@login_required
def dog_detail(request, dog_id):
  dog = Dog.objects.get(id=dog_id)
  snacks_dog_doesnt_have = Snack.objects.exclude(id__in = dog.snacks.all().values_list('id'))
  walk_form = WalkForm()
  return render(request, 'dogs/detail.html', { 
    'dog': dog, 
    'walk_form' : walk_form,
    'snacks': snacks_dog_doesnt_have,
    })

class DogCreate(LoginRequiredMixin, CreateView):
  model = Dog
  fields= ['name', 'breed', 'description', 'age']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class DogUpdate(LoginRequiredMixin, UpdateView):
  model = Dog
  # Let's disallow the renaming of a Dog by excluding the name field!
  fields = ['breed', 'description', 'age']

class DogDelete(LoginRequiredMixin, DeleteView):
  model = Dog
  success_url = '/dogs/'

@login_required
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

class SnackCreate(LoginRequiredMixin, CreateView):
  model = Snack
  fields = '__all__'


class SnackList(LoginRequiredMixin, ListView):
  model = Snack

class SnackDetail(LoginRequiredMixin, DetailView):
  model = Snack

class SnackUpdate(LoginRequiredMixin, UpdateView):
  model = Snack
  fields = ['name']

class SnackDelete(LoginRequiredMixin, DeleteView):
  model = Snack
  success_url = '/snacks/'

@login_required
def assoc_snack(request, dog_id, snack_id):
  # Note that you can pass a toy's id instead of the whole object
  Dog.objects.get(id=dog_id).snacks.add(snack_id)
  return redirect('dog-detail', dog_id=dog_id)


def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('dog-index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})