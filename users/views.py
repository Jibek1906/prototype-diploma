from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User  # Убедись, что эта строка есть
from .models import UserDetails
from .forms import UserDetailsForm
from .models import UserDetails, WeightRecord
from .forms import UserDetailsForm

def main(request):
    return render(request, 'main.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user_details', user_id=user.id)  # Передаем ID пользователя в URL
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def user_details(request, user_id):
    user = get_object_or_404(User, id=user_id)

    # Попытка получить UserDetails
    try:
        user_details = UserDetails.objects.get(user=user)
    except UserDetails.DoesNotExist:
        user_details = UserDetails.objects.create(
            user=user,
            height=170,
            weight=70,
            goal='maintain',
            training_level='beginner'
        )

    form = UserDetailsForm(request.POST or None, instance=user_details)

    if form.is_valid():
        form.save()
        return redirect('personal_office', user_id=user.id)  # Передаем user_id в редирект

    return render(request, 'user_details.html', {'form': form, 'user_details': user_details})

@login_required
def personal_office(request, user_id):  # Добавляем user_id в параметр
    # Получаем UserDetails для текущего пользователя по user_id
    user_details = get_object_or_404(UserDetails, user__id=user_id)  # Используем user_id для фильтрации

    # Получаем записи по весу для этого пользователя
    weight_records = WeightRecord.objects.filter(user=user_details).order_by('date')

    # Подготовим данные для графиков
    labels = [record.date.strftime('%d.%m.%Y') for record in weight_records]
    weights = [record.weight for record in weight_records]

    context = {
        'user_details': user_details,
        'labels': labels,
        'weights': weights,
    }

    return render(request, 'personal_office.html', context)

def update_user_info(request):
    if request.method == 'POST':
        user_details_form = UserDetailsForm(request.POST, instance=request.user.details)
        user_profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        
        if user_details_form.is_valid() and user_profile_form.is_valid():
            user_details_form.save()  # Обновляем данные пользователя
            user_profile_form.save()  # Сохраняем аватар (если был загружен)
            return redirect('profile')  # Перенаправление на страницу профиля
    else:
        user_details_form = UserDetailsForm(instance=request.user.details)
        user_profile_form = UserProfileForm(instance=request.user.profile)

    return render(request, 'personal_office.html', {
        'user_details_form': user_details_form,
        'user_profile_form': user_profile_form,
    })