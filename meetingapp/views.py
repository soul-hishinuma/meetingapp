from django.http.response import HttpResponse
from meetingapp.models import MeetingModel
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from .models import MeetingModel
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
def signupfunc(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    try:
      user = User.objects.create_user(username, '', password)
      return render(request,'signup.html',{'some':100})
    except IntegrityError:
      return render(request,'signup.html',{'error':'このユーザーは既に登録されています。'})
  return render(request,'signup.html',{'some':100})

def loginfunc(request):
  if request.method == "POST":
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
      login(request, user)
      return redirect('list')
    else:
      return render(request,'login.html',{})
  return render(request,'login.html',{})

@login_required
def listfunc(request):
  objects = MeetingModel.objects.all()
  return render(request, 'list.html', {'objects':objects})

def logoutfunc(request):
  logout(request)
  return redirect('login')

def detailfunc(request, pk):
  object_detail = get_object_or_404(MeetingModel, pk=pk)
  return render(request, 'detail.html', {'object_detail':object_detail})

def goodfunc(request, pk):
  object_good = MeetingModel.objects.get(pk=pk)
  object_good.good = object_good.good + 1
  object_good.save()
  return redirect('list')

def readfunc(request, pk):
  object_read = MeetingModel.objects.get(pk=pk)
  username = request.user.get_username()
  if username in object_read.readtext:
    return redirect('list')
  else:
    object_read.read = object_read.read + 1
    object_read.readtext = object_read.readtext + ' ' + username
    object_read.save()
    return redirect('list')

class MeetingCreate(CreateView):
  template_name = 'create.html'
  model = MeetingModel
  fields = ('title','content','author','snsimage')
  success_url = reverse_lazy('list')

def mapfunc(request):
  return render(request, 'map.html', {})