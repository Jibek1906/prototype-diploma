from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserDetailsForm
from django.contrib.auth.models import User
from .models import UserDetails, WeightRecord

def main(request):
    return render(request, 'main.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Создаем объект UserDetails
            UserDetails.objects.create(
                user=user,
                height=170,
                weight=70,
                goal='maintain',
                training_level='beginner'
            )
            return redirect('user_details', user_id=user.id)
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Перенаправляем на личный кабинет
            return redirect('personal_office', user_id=user.id)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_details(request, user_id):
    user = get_object_or_404(User, id=user_id)

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
        return redirect('login')  # Redirect to login after user details
    return render(request, 'user_details.html', {'form': form, 'user_details': user_details})

@login_required
def personal_office(request, user_id):
    user_details = get_object_or_404(UserDetails, user__id=user_id)
    weight_records = WeightRecord.objects.filter(user=user_details).order_by('date')

    labels = [record.date.strftime('%d.%m.%Y') for record in weight_records]
    weights = [record.weight for record in weight_records]

    context = {
        'user_details': user_details,
        'labels': labels,
        'weights': weights,
    }

    return render(request, 'personal_office.html', context)
