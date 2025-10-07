from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm, UserProfileForm
from django.contrib import messages
from django.contrib.auth.models import User

# Registration - custom view
def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally, log the user in immediately after registration:
            login(request, user)
            messages.success(request, "Registration successful. You are now logged in.")
            return redirect("home")  # change to your homepage url name
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = CustomUserCreationForm()
    return render(request, "blog/register.html", {"form": form})


# Login using Django's generic LoginView (we can subclass only to set template)
class CustomLoginView(LoginView):
    template_name = "blog/login.html"


# Logout using Django's LogoutView (set redirect)
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("home")


# Profile view - view & edit the logged-in user's profile
@login_required
def profile_view(request):
    user = request.user
    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated.")
            return redirect("profile")
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = UserProfileForm(instance=user)
    return render(request, "blog/profile.html", {"form": form})
