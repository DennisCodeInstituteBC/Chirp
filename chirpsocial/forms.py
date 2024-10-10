from django import forms
from .models import chirp

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