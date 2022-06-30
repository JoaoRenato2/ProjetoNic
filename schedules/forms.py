from django import forms
from schedules.models import Usuario
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class EditProfileForm(UserChangeForm):
    template_name='editProfile.html'

    class Meta:
        model = Usuario
        fields = (
            'email',
            'first_name',
            'last_name',
            'picture',
            'telefone',
            'curso',
            'periodo',
            'bio'

        )