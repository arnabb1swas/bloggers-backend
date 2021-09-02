from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.


def register_(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        userObj = form.save()
        return redirect('/login')
    context = {'form': form}
    return render(request, "authors/register.html", context)


def login_(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            userObj = form.get_user()
            login(request, userObj)
            return redirect('/')
        else:
            return render(request, 'authors/login.html')

    else:
        form = AuthenticationForm(request)

    context = {'form': form}
    return render(request, 'authors/login.html', context)


def logout_(request):
    if request.method == "POST":
        logout(request)
        return redirect('/login')

    return render(request, "authors/logout.html", {})
