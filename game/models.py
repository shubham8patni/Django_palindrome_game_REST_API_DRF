from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Boards(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    game_string = models.TextField(max_length = 6, default = "")


    def __str__(self):
        return self.id


    class Meta:
        db_table = 'Boards'