from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from myblog.settings import LOGIN_REDIRECT_URL
from .forms import UserRegistrationForm


def register(request):
    # to register use POST method
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            context = {'title': 'Registration is successful', 'new_user': new_user}
            return render(request, template_name='users/register_done.html', context=context)

    user_form = UserRegistrationForm()
    context = {'title': 'Registration', 'register_form': user_form}
    return render(request, template_name='users/register.html', context=context)


def log_in(request):
    form = AuthenticationForm(request, request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            url = request.GET.get('next', LOGIN_REDIRECT_URL)
            return redirect(url)
    context = {'form': form}
    return render(request, template_name='users/login.html', context=context)



def log_out(request):
    logout(request)
    return redirect('blog:index')

def user_detail(request):
    pass


def change_password(request):
    pass


