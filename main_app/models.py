from django.db import models
from django.urls import reverse
from datetime import date

STATUS = (
  ('H', 'Healthy'),
  ('N', 'Under Half'),
  ('L', 'Low'),
  ('U', 'Unconcious'),
  ('D', 'Dead')
)

class Weapon(models.Model):
  name = models.CharField(max_length=50)
  damage = models.TextField(max_length=100)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('weapons_detail', kwargs={'pk': self.id})

class Character(models.Model):
  name = models.CharField(max_length=100)
  race = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  weapons = models.ManyToManyField(Weapon)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'character_id': self.id})

  # def healed_for_today(self):
  #   return self.healing_set.filter(date=date.today()).count() >= len(STATUS)

class Healing(models.Model):
  date = models.DateField('healing date')
  status = models.CharField(
    max_length = 1,
    choices=STATUS,
    default=STATUS[0][0][0][0]
  )
  character = models.ForeignKey(Character, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_status_display()} on {self.date}"

  class Meta:
    ordering = ['-date']