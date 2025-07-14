from django.shortcuts import render,redirect
from django.urls import reverse
from .models import UserProfile,Experience,Education
from django.contrib.auth import authenticate,login as django_login,logout as django_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def addeducation(request):
    if request.method == 'POST':
        school = request.POST.get('school')
        degree = request.POST.get('degree')
        field = request.POST.get('field')
        start = request.POST.get('start')
        end = request.POST.get('end')
        description = request.POST.get('description')
        education = Education(school=school,degree=degree,field=field,start=start,end=end,description=description)
        education.save()
        return redirect(dashboard)    
    return render(request,'accounts/addeducation.html',{})

def addexperience(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        company = request.POST.get('company')
        location = request.POST.get('location')
        start = request.POST.get('start')
        end = request.POST.get('end')
        description = request.POST.get('description')
        experience = Experience(title = title , company=company,location=location,start=start,end=end,description=description)
        experience.save()
        return redirect(dashboard)
    elif request.method == 'GET':
      return render(request,'accounts/addexperience.html',{})

def createprofile(request):
    return render(request,'accounts/createprofile.html',{})

def dashboard(request):
        return render(request,'accounts/dashboard.html',{})

def login(request):
     if request.method == 'POST':
          name = request.POST['name']
          password = request.POST.get('password')
          user = authenticate(request,username=name,password=password)
          if user is not None:
               django_login(request,user)
               return redirect(reverse('profile',kwargs={'pk':user.pk}))
          error = 'User or Password Incorrect'
          return render(request,'accounts/login.html',{'error':error})
     elif request.method =='GET':
       return render(request,'accounts/login.html',{})
   
def logout(request):
    django_logout(request)
    return redirect(reverse('index'))

@login_required
def profile(request,pk):
    user_profile = UserProfile.objects.get(pk=pk)
    return render(request,'accounts/profile.html',{'user_profile':user_profile})

def profiles(request):
    return render(request,'accounts/profiles.html',{})

def register(request):
    if request.method == 'POST':
       form = UserCreationForm(request.POST)
       if form.is_valid():
           form.save()
           messages.add_message(request,messages.SUCCESS,'Signed Up successfully')
           return redirect(reverse('login'))
       return render(request,'accounts/register.html',{'form':form})
    elif request.method == 'GET':
        form = UserCreationForm()
        return render(request,'accounts/register.html',{'form':form})
       
