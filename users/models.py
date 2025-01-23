from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.IntegerField()
    goal_choices = [
        ('lose-weight', 'Lose Weight'),
        ('gain-muscle', 'Gain Muscle'),
        ('maintain', 'Maintain Fitness'),
    ]
    goal = models.CharField(max_length=50, choices=goal_choices)
    training_level_choices = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    training_level = models.CharField(max_length=50, choices=training_level_choices)

    def __str__(self):
        return self.user.username


class WeightRecord(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    weight = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.user.username} - {self.date} - {self.weight} kg"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    goal = models.CharField(max_length=50, choices=[
        ('Lose Weight', 'Lose Weight'),
        ('Gain Muscle', 'Gain Muscle'),
        ('Maintain', 'Maintain')
    ])
    training_level = models.CharField(max_length=50, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ])
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    def __str__(self):
        return self.user.username