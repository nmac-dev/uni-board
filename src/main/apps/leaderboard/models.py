from django.db                  import models
from django.contrib.auth.models import User

# Create your models here.

class Leaderboard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    points = models.PositiveIntegerField(default = 0)

    def __str__(self):
        x = self.points
        return str(x)