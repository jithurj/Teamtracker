from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Trackerdata
from .forms import TrackerdataForm
# Create your views here.

def home(request):
    if request.method == 'GET':
        return render(request,'tracker/index.html',{})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'tracker/index.html',{'error':'Username and password did not match'})
        else:
            login(request,user)
            return redirect('trackerhome')
@login_required
def trackerhome(request):
    team = Trackerdata.objects.filter(user =request.user)
    return render(request,'tracker/trackerhome.html',{'trackerdata':team})

@csrf_exempt
def savetracker(request):
    id=request.POST.get('id','')
    type=request.POST.get('type','')
    value=request.POST.get('value','')
    tracker=Trackerdata.objects.get(id=id)
    if type=="automation":
       tracker.automation=value

    if type == "task":
        tracker.task = value

    if type == "stardate":
        tracker.stardate = value

    if type == "enddate":
        tracker.status = value

    if type == "blockers":
        tracker.hobbies = value

    if type == "spoc":
        tracker.spoc = value

    tracker.save()
    return JsonResponse({"success":"Updated"})

def update_tracker(request,trackerid):
    tracker=Trackerdata.objects.get(id=trackerid)
    form = TrackerdataForm(instance=tracker)
    if request.method == "POST":
        form = TrackerdataForm(request.POST,instance=tracker)
        if form.is_valid():
            form.save()
            return redirect('trackerhome')
    context ={'form':form}
    return render(request,'tracker/update_tracker.html',{'form':form})

def passwordreset(request):
    if request.method == 'GET':
        return render(request,'tracker/password_reset.html',{})
    else:
        uname = request.POST['username']
        user_name= User.objects.get(username=uname)
        if user_name is  None:
            return render(request,'tracker/password_reset.html',{'error':'Username does not exist'})
        else:
            pw1 =request.POST['password1']
            pw2 =request.POST['password2']
            if pw1 == pw2 :
                user_name.set_password(pw1)
                user_name.save()
                return render(request,'tracker/index.html',{'error':'Password changed successfully'})
            else:
                return render(request,'tracker/password_reset.html',{'error':'Passwords did not match'})

def logoutuser(request):
    #if request.method =='POST':
        print('loging out')
        logout(request)
        return redirect('home')
        #return HttpResponse("Item Not Found")

        #tracker.save(update_fields=['automation','task','stardate','enddate','status','blockers','spoc','finished'])
        #return redirect('trackerhome')
        #team = Trackerdata.objects.all()
        #return render(request,'tracker/trackerhome.html',{'trackerdata':team})
        #return render(request,"student_edit.html",{'student':student})
