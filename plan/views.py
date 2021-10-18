from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import  messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import  User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import *
from .models import Plan, Userprofile
# Create your views here.


def login_page(request):
    if request.user.is_authenticated:
        return redirect(dashboard)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except :
            messages.error(request, "user name does not exist")

        user = authenticate(request, username=username, password=password)
        
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Incorrect Password")

    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    messages.success(request,"logout successfully" )
    return redirect('login')


@login_required(login_url="login")
def dashboard(request):
    search_qurery = ' '
    if request.GET.get('search_query'):
        search_qurery = request.GET.get('search_query')

    users = Userprofile.objects.filter(user__icontains=search_qurery)
    user = Userprofile.objects.all()
    plans = Plan.objects.all()
    u = Userprofile.objects.all()
    total_user = u.count()
    page = request.GET.get('page')
    results = 5
    paginator = Paginator(user,results)
    try:
        user = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        user = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        user = paginator.page(page)

    left = (int (page) -  1)
    if left < 1 :
        left = 1
    right = (int (page) + 2)
    if right >paginator.num_pages:
        right = paginator.num_pages+1
    custom_range = range(left, right)
    total_plan = plans.count()
    context = {'plans':plans, 
    'total_plan':total_plan,
     'users':users,
    'user':user,
    'search_qurery':search_qurery,
    'paginator':paginator, 
    'custom_range':custom_range,
    'total_user':total_user
   
    
    }
    return render(request,'dashboard.html',context)

@login_required(login_url="login")
def plans(request):
    plans = Plan.objects.all()
    context = {'plans':plans}
    return render(request,'plans.html',context)

@login_required(login_url="login")
def create_plan(request):
    if request.method == 'POST':
        form= planform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"plan added successfully")
            return redirect('/')
    else:
        form = planform()
    return render(request,"create-plan.html",{'form':form})

@login_required(login_url="login")
def delete_plan(request,pk):
    if request.method == 'POST':
        pi = Plan.objects.get(id=pk)
        pi.delete()
        messages.warning(request, 'plan deleted successfully')
        return redirect('/')
    else:
        messages.error(request,'Oopse something went wrong!!!')

@login_required(login_url="login")
def update_plan(request,pk):
    pi = Plan.objects.get(id=pk)
    form = planform(instance=pi)
    if request.method == 'POST':
        form =planform(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            messages.info(request,'Plan updated successfully')
            return redirect('/')
    context = {'form':form}



    return render(request,'update-plan.html',context)

@login_required(login_url="login")
def users(request):
    search_qurery = ' '
    if request.GET.get('search_query'):
        search_qurery = request.GET.get('search_query')

    users = Userprofile.objects.filter(user__icontains=search_qurery)
    user = Userprofile.objects.all()

    page = request.GET.get('page')
    results = 5
    paginator = Paginator(user,results)
    try:
        user = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        user = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        user = paginator.page(page)

    left = (int (page) -  1)
    if left < 1 :
        left = 1
    right = (int (page) + 2)
    if right >paginator.num_pages:
        right = paginator.num_pages+1
    custom_range = range(left, right)
    



    context = {'users':users,'user':user, 'search_qurery' : search_qurery, 'paginator':paginator, 'custom_range':custom_range}
    return render(request,'users.html',context)

@login_required(login_url="login")
def create_user(request):
    if request.method == 'POST':
        form= clientform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'user added successfully')
            return redirect('/')
    else:
        form = clientform()
        
    return render(request,"create-user.html",{'form':form})

@login_required(login_url="login")
def edit_user(request, pk):
    try:
        user = Userprofile.objects.get(user=pk)
        form = clientform(instance=user)
        if request.method == 'POST':
            form = clientform(request.POST,  request.FILES, instance=user )
            if form.is_valid():
                form.save()
            messages.info(request,'User updated successfully')
            return redirect('/users')
    except :
        print("somthing went wrong")
    

    return render(request,'update-user.html',{'form':form})

@login_required(login_url="login")
def delete_user(request,pk):
    if request.method == 'POST':
        pi = Userprofile.objects.get(pk=pk)
        pi.delete()
        messages.warning(request, 'User deleted successfully')
        return redirect('/users')
    else:
        messages.error(request,"oops something went wrong!!!")



@login_required(login_url="login")
def view_user(request,pk):
    user = Userprofile.objects.filter(user=pk)
    context = {'user':user}
    return render(request,"view-user.html",context)

@login_required(login_url="login")
def bill(request):
    user = Userprofile.objects.all()
    plan = Plan.objects.all()
    context = {'user':user, 'plan':plan }

    return render(request,"bill.html",context)

