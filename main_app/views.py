from django.shortcuts import render
# Add the following import
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
class Dog:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dogs = [
  Dog('Enzo', 'Border Collie', 'A gentleman.', 8),
  Dog('Hela', 'Dachshund', 'Crazy but adorable.', 1),
  Dog('Nicky', 'Chihuahua', 'Shy but likes to bark.', 1),
  Dog('Milo', 'Chihuahua', 'Helas minion.', 0)
]

# Create your views here.

# Define the home view
def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def about(request):
  return render(request, 'about.html')

def dog_index(request):
  return render(request, 'dogs/index.html', { 'dogs': dogs })