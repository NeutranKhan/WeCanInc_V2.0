#import modules
from django import forms
from django.shortcuts import reverse
from .models import Profile
from django.contrib.auth.models import User


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    profile_picture = forms.ImageField()

    def save(self):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        profile = Profile.objects.create(
            user=user,
            profile_picture=self.cleaned_data['profile_picture']
        )

        redirect_url = reverse('home')
        return redirect_url



