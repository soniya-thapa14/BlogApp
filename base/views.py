from django.shortcuts import render,redirect, get_object_or_404
from .models import *
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def test(request):
    return redirect('home')


def loginn(request):
    if request.method == 'POST':
        name= request.POST.get('uname')
        password= request.POST.get('upassword')
        user = authenticate(request, username=name, password =password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:            
            messages.error(request, "Invalid username or password.")
            return redirect('/loginn')
    return render(request,'base/loginn.html')

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('uemail')
        password =request.POST.get('upassword')
        
        newuser = User.objects.create_user(username= name,email=email,password=password, first_name= first_name, last_name= last_name)
        newuser.save()
        return redirect('/loginn')
    return render(request,'base/signup.html')

def home(request):
    context = {
        'posts': Posts.objects.all(),
    }
    return render(request,'base/home.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description= request.POST.get('description')
        npost=Posts.objects.create(
            author=request.user,
            Title=title,
            description=description
        )
        return redirect('/home')
    return render(request, 'base/create_post.html')

@login_required
def update_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id, author=request.user)
    
    if request.method == 'POST':
        post.Title = request.POST.get('title')
        post.description = request.POST.get('description')
        post.save()
        return redirect('home')
    return render(request, 'base/update_post.html', {'post': post})

@login_required
def my_blog(request):
    context = {
        'posts': Posts.objects.filter(author= request.user)
    }
    return render(request, 'base/my_blog.html', context)

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id, author=request.user)
    post.delete()
    return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    posts = Posts.objects.filter(author=request.user)
    if request.method == 'POST':
        user=request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        if request.FILES.get('image'):
            profile.image = request.FILES['image']
            profile.save()
        user.save()

        return redirect('profile')
    return render(request, 'base/profile.html', {'posts': posts, 'profile': profile})


def update_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user=request.user
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')
        if request.FILES.get('image'):
            profile.image = request.FILES['image']
            profile.save()
        user.save()
        return redirect('profile')
    return render(request, 'base/update_profile.html',{'profile': profile})