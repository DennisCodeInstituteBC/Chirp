from django.shortcuts import render
from .forms import ChirpForm
from .models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.
def dashboard(request):
    form = ChirpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            chirp = form.save(commit=False)
            chirp.user = request.user
            chirp.save()
            return redirect("chirp:dashboard")
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


def search_profiles(request):
    query = request.GET.get('q')
    profiles = Profile.objects.filter(user__username__icontains=query) if query else []
    return render(request, 'chirpsocial/search_results.html', {'profiles': profiles, 'query': query})



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Ensure that the Profile is created only if it does not exist
            Profile.objects.get_or_create(user=user)
            login(request, user)  # Automatically log the user in after registration
            messages.success(request, "Registration successful.")
            return redirect("chirp:dashboard")
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = RegisterForm()

    return render(request, "chirpsocial/register.html", {"form": form})