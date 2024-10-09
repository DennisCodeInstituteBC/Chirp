from django.shortcuts import render
from .forms import ChirpForm
from .models import Profile
from django.shortcuts import render, redirect

# Create your views here.
def dashboard(request):
     if request.method == "POST":
        form = ChirpForm(request.POST or None)
        if form.is_valid():
            chirp = form.save(commit=False)
            chirp.user = request.user
            chirp.save()
            return redirect("chirpsocial:dashboard")
        return render(request, "chirpsocial/dashboard.html", {"form": form})

def profile_list(request):
    profiles = Profile.objects.all()
    return render(
        request, "chirpsocial/profile_list.html", {"profiles": profiles})


def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()


    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
    return render(request, "chirpsocial/profile.html", {"profile": profile})

def dashboard(request):
    return render(request, "chirpsocial/dashboard.html")