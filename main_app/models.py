from django.db import models
# Import the reverse function
from django.urls import reverse
from datetime import date


TIMES = (
  ('M', 'Morning'),
  ('A', 'Afternoon'),
  ('N', 'Night')
)


class Snack(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('snack-detail', kwargs={'pk': self.id})


# Create your models here.
class Dog(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  snacks = models.ManyToManyField(Snack)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('dog-detail', kwargs={'dog_id': self.id})
  
  def walked_today(self):
    return self.walk_set.filter(date=date.today()).count() >= 1
  

class Walk(models.Model):
  date = models.DateField('Date of the Walk')
  type = models.CharField(
    max_length=1,
    choices=TIMES,
    default=TIMES[0][0]
    )
  
  dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

  def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
    return f"{self.get_type_display()} walk on {self.date}"
  
  class Meta:
    ordering = ['-date']
