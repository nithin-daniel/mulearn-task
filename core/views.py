from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Todo
from datetime import date
# Create your views here.
@login_required(login_url='signin')
def index(request):
    incomplete_todos = Todo.objects.filter(is_completed=False)
    completed_todos = Todo.objects.filter(is_completed=True)
    active_todos = []
    expired_todos = []
    print(date.today())
    for todo in incomplete_todos:
        print(todo.date)
        # if todo.is_expired:
        #     print(todo)
        #     expired_todos.append(todo)
        # else:
        #     active_todos.append(todo)
        if todo.date.date() < date.today():
            print('expired')
            expired_todos.append(todo)
        else:
            print('active')
            active_todos.append(todo)
    
    print(active_todos)
    print(expired_todos)



    # compl = Completed.objects.all()
    context = {
        # 'upcom':upcom,
        # 'compl':compl,
        'upcom_false' :active_todos,
        'upcom_true': completed_todos,
        'expired_todos':expired_todos

    }
    return render(request, 'core/index.html',context)


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')  
        last_name = request.POST.get('last_name')  
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

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
    if request.user.is_authenticated:
        return redirect('/') # or somewhere else or last url
    else:
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

        # print(title,description,date)
        return redirect('/')
    else:
        return render(request, 'core/add-task.html')


def completed(request,id):
    # print(id)
    obj = Todo.objects.get(id=id)
    # print(obj)
    obj.is_completed = True
    # print(obj.is_completed)
    obj.save()
    # print(obj)
    return redirect('/')

def delete_task(request,id):
    # print(id)
    obj = Todo.objects.get(id=id)
    # print(obj)
    # obj.is_completed = True
    # print(obj.is_completed)
    print('logging')
    obj.delete()
    print('deleted')
    # print(obj)
    return redirect('/')

def time_expired(request,id):
    print(id)
    