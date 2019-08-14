from django.shortcuts import render,redirect
from . forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
       
    return render(request, "home.html")
    
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =UserRegistrationForm()
    return render(request,'registration/registration_form.html',{'form':form}) 