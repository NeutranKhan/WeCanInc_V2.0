from django.shortcuts import redirect, render
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            redirect_url = form.save()
            return redirect(redirect_url)

        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect to a success page.
            return redirect('home')
        else:
            # Return an 'invalid login' error message.
            pass
    return render(request, "accounts/login.html")


def logout(request):
    
    auth_logout(request)

    return redirect('home')