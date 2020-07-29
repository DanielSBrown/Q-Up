from django.db import models


class Room(models.Model):
  code = models.CharField(max_length=4)
  group_name = models.CharField(max_length=100)
  created_date = models.DateTimeField('date created')

  def __str__(self):
    return f"Room code: {self.code}"
