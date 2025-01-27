from django.contrib import admin
from django.urls import path, include
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='main'),
    path('workouts/', include('workouts.urls')),
    path('nutrition/', include('nutrition.urls')),
    path('users/', include('users.urls')),
]