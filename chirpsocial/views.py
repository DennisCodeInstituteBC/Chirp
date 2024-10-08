from django.shortcuts import render
from .models import Profile

# Create your views here.
def dashboard(request):
    return render(request, "chirpsocial/base.html")

def profile_list(request):
    profiles = Profile.objects.exclude()
    return render(
        request, "chirpsocial/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    profile = Profile.objects.get(pk=pk)
    return render(request, "chirpsocial/profile.html", {"profile": profile})