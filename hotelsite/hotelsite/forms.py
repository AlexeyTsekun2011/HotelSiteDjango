from .models import CustomUser,Booking
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.forms import Form, ModelForm


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', "password2")


class CustomUserLoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ('room','coming_date','leaving_date','guest_count')



