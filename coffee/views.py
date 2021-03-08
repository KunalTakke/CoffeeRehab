from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages 
from django.contrib.auth import authenticate,login as dj_login,logout
from django.contrib.auth.models import User
from .models import Product,Contact

# Create your views here.
def index(request):
    return render(request,'coffee/index.html')

def about(request):
    return render(request,'coffee/about.html')

def menu(request):
    products=Product.objects.all()
    print(products)
    params={'product':products}
    return render(request,'coffee/menu.html',params)

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        msg=request.POST.get('msg','')
        # print(name,email,phone,msg) 
        contact=Contact(name=name,email=email,phone=phone,msg=msg)
        contact.save()
    return render(request,'coffee/contact.html')

def login(request):
    return render(request,'coffee/login.html')

def handleSignup(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        #Check for errors
        if pass1 != pass2:
            messages.warning(request,"Passwords do not match")
            return redirect("Login")

        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.username= username
        myuser.email= email
        myuser.save()
        messages.success(request, " Your Account has been successfully created !")
        return redirect('Login')
    else:
        return HttpResponse("You need to login first to access !!!")

def handleLogin(request):
    signedusername=request.POST['signedusername']
    signedpassword=request.POST['signedpassword']
    
    user=authenticate(username=signedusername,password=signedpassword)  
    
    if user is not None:
        dj_login(request, user)
        messages.success(request,"Successfully Logged In")
        return redirect('Menu')
    else:
        messages.warning(request,"Invalid Credentials !")
        return redirect("Login")
    return HttpResponse('Login') 

