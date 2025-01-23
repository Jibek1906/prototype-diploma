from django import forms
from .models import UserDetails, UserProfile

class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ['height', 'weight', 'goal', 'training_level']  # Все необходимые поля для редактирования данных
    
    # Если вы хотите добавить поле для пароля
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False,  # Если не обязательно, можно сделать необязательным
        error_messages={
            'required': 'Password is required.',
            'min_length': 'Your password must contain at least 8 characters.',
            'max_length': 'Your password can’t be more than 128 characters.',
            'invalid': 'Your password is invalid.',
        }
    )

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['avatar']  # Поле для загрузки аватара

    # Дополнительно можно добавить валидаторы для файла аватара
    avatar = forms.ImageField(
        required=False,  # Если аватар не обязательно загружать
        error_messages={
            'invalid': 'The uploaded file is not a valid image.',
        }
    )