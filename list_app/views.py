from django.shortcuts import render,redirect
from django.contrib import messages
from .models import userdetails
from django.contrib.auth import authenticate,login
from .models import Task
from django.contrib.auth import logout
from django.contrib.auth import logout


# Create your views here.
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm-password')
     

        if password1 != password2:
            messages.error(request,'Password does not match')
            return render(request, 'register.html')

        if userdetails.objects.filter(name=username).exists():
            messages.error(request,'user name already exist')
            return render(request, 'register.html')

        if userdetails.objects.filter(email=email).exists():
            messages.error(request,'email already exist')
            return render(request, 'register.html')
        
        userdetails.objects.create(name=username, email=email, password=password1)
        messages .success(request,'registered successfully')
        return redirect('login')

    return render(request, 'register.html')
        
       

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = userdetails.objects.get(name=username, password=password)
            messages.success(request,'login successfully')
            return redirect('home',username=user.name)
        except userdetails.DoesNotExist:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')


def homepage_view(request, username):
    user = userdetails.objects.get(name=username)

    total_task = Task.objects.count()

    # ✅ Delete task logic
    delete_id = request.GET.get('delete_task_id')
    if delete_id:
        Task.objects.filter(id=delete_id).delete()
        return redirect('home', username=user.name)

    # ✅ Add task logic
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        if title and due_date:
            Task.objects.create(title=title, due_date=due_date)
            return redirect('home', username=user.name)

    tasks = Task.objects.all()
    return render(request, 'home.html', {'user': user, 'tasks': tasks, 'total_task': total_task})




from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    messages.success(request,'Logged out succesfully')
    return redirect('login')


def adminlogin_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Need admin credentials to access this page.")
                
    return render(request, "admin.html")










        
        