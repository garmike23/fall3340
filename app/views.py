from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
# Create your views here.
def home(request):
    return render(request, 'home.html',{})
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None: 
            login(request, user)
            message.success(request, "Login Successful")
        else:
            messages.success(request, "Login Error")
            return redirect('home')
    else:
        return render(request, 'home.html',{})
