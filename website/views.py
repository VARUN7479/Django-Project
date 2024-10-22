from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) 
            messages.success(request, "You have been logged in!")
            return redirect('home')  # Redirect to the home page after successful login
        else:
            messages.error(request, "There was an error logging in, please try again.")
            return redirect('home')  # Redirect back to the home page for another attempt

    else:
        return render(request, 'home.html', {})

def logout_user(request):
    logout(request)  # Log out the user
    messages.success(request, "You have been logged out!")
    return redirect('home')  # Redirect to home after logout

def register_user(request):
    return render(request, 'register.html', {})
