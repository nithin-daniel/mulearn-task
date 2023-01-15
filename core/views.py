from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth

# Create your views here.
def index(request):
    return render(request, 'core/signup.html')


def register(request):
    if request.method == 'POST':
        full_name = request.POST['first_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username,password1=password1,password2=password2)
        user.save()
        print('user created')