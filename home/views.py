from django.shortcuts import render,HttpResponse,redirect
from datetime import datetime
from home.models import Contact,Sign
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate



# Create your views here.
def index(request):
    context={
        'variable1':"this is sent",#calling a variable
        'variable2':"this is recieved"
    }
    # if request.user.is_anonymous:
    #     return redirect ("/sign.html")
    return render(request,'index.html',context)




def about(request):
    return render(request,'about.html')
    

def services(request):
    return render(request,'services.html')
    

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        msg=request.POST.get('msg')
        contact=Contact(name=name,email=email,phone=phone,msg=msg,date=datetime.today())
        contact.save()
        messages.success(request, "your message has been sent")

    return render(request,'contact.html')

# def logout(request):
#     logout()
#     return render(request,'proceed.html')
def physics(request):
    return render(request,'physics.html')

def maths(request):
    return render(request,'maths.html')

def chemistry(request):
    return render(request,'chemistry.html')

def physics2(request):
    return render(request,'physics2.html')

def maths2(request):
    return render(request,'maths2.html')

def chemistry2(request):
    return render(request,'chemistry2.html')

def physics3(request):
    return render(request,'physics3.html')

def maths3(request):
    return render(request,'maths3.html')

def chemistry3(request):
    return render(request,'chemistry3.html')

def physics4(request):
    return render(request,'physics4.html')

def maths4(request):
    return render(request,'maths4.html')

def chemistry4(request):
    return render(request,'chemistry4.html')

def services(request):
    return render(request,'services.html')

def boardpps(request):
    return render(request,'boardpps.html')

def mhtcetpps(request):
    return render(request,'mhtcetpps.html')

def collegelist(request):
    return render(request,'collegelist.html')

def mhtcet(request):
    return render(request,'mhtcet.html')

def boards(request):
    return render(request,'boards.html')