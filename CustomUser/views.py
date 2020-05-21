from django.shortcuts import render

# Create your views here.
from CustomUser.forms import SignUpForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from .models import Customuser


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='/login/')
def home(request):
    instance = Customuser.objects.get(username=request.user.username)
    user = {
        'username': request.user.username,
        'displayname': instance.Display_name
    }
    return render(request, 'home.html', {'user': user})


def login_view(request):
    html = "login.html"
    form = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data["username"], password=data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )
    else:
        form = LoginForm()
    return render(request, html, {"form": form})


def logout_action(request):
    logout(request)
    return redirect(request.GET.get("next", reverse('login')))
