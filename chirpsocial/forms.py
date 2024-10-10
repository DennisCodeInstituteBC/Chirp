from django import forms
from django.db import models
from .models import chirp
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class ChirpForm(forms.ModelForm):
    body = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "Chirp something...",
                "class": "form-control is-success is-medium", 
                "rows": 4, 
                "style": "resize: vertical;",
            }
        ),
        label="",
    )

    class Meta:
        model = chirp
        exclude = ("user", )



class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"placeholder": "Email"}))
    name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs={"placeholder": "Full Name"}))
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], required=True)
    age = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={"placeholder": "Age"}))
    bio = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Write something about yourself..."}), required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Create or update the Profile object
            Profile.objects.update_or_create(
                user=user,
                defaults={
                    'name': self.cleaned_data['name'],
                    'gender': self.cleaned_data['gender'],
                    'age': self.cleaned_data['age'],
                    'bio': self.cleaned_data['bio'],
                }
            )
        return user