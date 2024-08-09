from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
#from django.http import HttpResponse


def signup(request):
    if request.method == "POST":
        get_first_name = request.POST.get('first_name')
        get_last_name = request.POST.get('last_name')
        get_email = request.POST.get('email')
        get_current_address = request.POST.get('current_address')
        get_permanent_address = request.POST.get('permanent_address')
        get_password = request.POST.get('pass1')
        get_confirm_password = request.POST.get('pass2')

        # Check if passwords match
        if get_password != get_confirm_password:
            messages.info(request, 'Passwords do not match.')
            return redirect('/auth/signup/')
        
        # Check if email already exists
        if User.objects.filter(username=get_email).exists():
            messages.warning(request, "Email is already taken.")
            return redirect('/auth/signup/')
        
        # Create the user
        try:
            myuser = User.objects.create_user(
                username=get_email,
                email=get_email,
                password=get_password
            )
            myuser.first_name = get_first_name
            myuser.last_name = get_last_name
            myuser.save()
            messages.success(request, "User created successfully. Please log in.")
            return redirect('/auth/login/')
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('/auth/signup/')
    
    return render(request, 'signup.html')

def handlelogin(request):
    if request.method == "POST":
        get_email = request.POST.get('email')
        get_password = request.POST.get('pass1')
        myuser = authenticate(username=get_email, password=get_password)
        if myuser is not None:
            login(request, myuser)
            messages.success(request, "Login successfully")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials")
    return render(request, 'login.html')
def handlelogout(request):
    logout(request)
    messages.success(request,"logged out successfully")
    return render(request, 'login.html')
