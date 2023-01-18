from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Todo,Completed
# Create your views here.
@login_required(login_url='signin')
def index(request):
    upcom = Todo.objects.all()
    compl = Completed.objects.all()
    context = {
        'upcom':upcom,
        'compl':compl,
    }
    return render(request, 'core/index.html',context)


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
    if request.method == 'POST':
        print('call cammed')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        user = authenticate(username=username, password=password)
        # print(user)
    
        if user is not None:
            login(request, user)
            # auth.login(request, user)
            print('not found')
            # return redirect('/')
            # return render(request, 'core/index.html')
            return HttpResponseRedirect(reverse('index'))
            # return render(request, 'core/signin.html')
            
        else:
            print('hey')
            # return reverse('index')
            # print('user found')
            # return render(request, 'core/index.html')
        # No backend authenticated the credentials
        # return render(request, 'core/index.html')
    else:
        # return HttpResponse('Hello')
        return render(request, 'core/signin.html')
        # return redirect('/')
        # return HttpResponse('jgasdfkjh')


def logout_view(request):
    logout(request)
    return redirect('signin')


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date-picker')

        if title is None or title == "":
            raise ValueError('Title is required')
        
        if description is None or description == "":
            raise ValueError('Description is required')
        
        if date is None or date == "":
            raise ValueError('Date is required')

        obj = Todo.objects.create(name=title,description=description,date=date)

        print(title,description,date)
    return render(request, 'core/add-task.html')


def completed(request,id):
    # print(id)
    obj = Todo.objects.get(id=id)
    compl = Completed.objects.create(name=obj.name,description=obj.description,date=obj.date)
    # print(compl)
    obj.delete()

    print(obj)
    return redirect('/')