from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']    
        last_name = request.POST['last_name']  
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists ' )
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password2,email=email,first_name=first_name,last_name=last_name)
                user.save()
                
                return redirect('signin')
        else:
            messages.info(request, 'password not matching......')
            return redirect('register') 

    else:    
            return render(request, 'core/signup.html')


def signin(request):
    return render(request, 'core/signin.html')