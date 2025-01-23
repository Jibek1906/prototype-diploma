from django.shortcuts import render
from .models import Workout

def workout_list(request):
    workouts = Workout.objects.all()
    return render(request, 'workouts.html', {'workouts': workouts})