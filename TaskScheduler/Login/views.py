
# Create your views here.

from django.shortcuts import render, redirect,reverse
from .models import LoginUser


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if LoginUser.objects.filter(UserName=username ,password = password).exists():
            #print("User name exists")
            return redirect('dashboard')
        else:
            #print("User name does not exists" )       
            return render(request, 'Login.html',{'invalid_login': True})
    return render(request, 'Login.html',{'invalid_login': False})


def logout_view(request):
     return redirect('login')

def dashboard_view(request):
    app2_url = reverse('task_list')  
    return redirect(app2_url)