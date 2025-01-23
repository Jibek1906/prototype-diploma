from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='main.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user_details/<int:user_id>/', views.user_details, name='user_details'),  # Убедитесь, что это есть
    path('profile/<int:user_id>/', views.personal_office, name='personal_office'),
    # path('edit/', views.update_user_info, name='update_user_info'),
    # path('update_user_info/', views.update_user_info, name='update_user_info'),
]
