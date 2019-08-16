from django.shortcuts import render,redirect
from . forms import UserRegistrationForm,profileForm
from django.contrib.auth.decorators import login_required
from.models import Item,Profile,Order,OrderItem
# Create your views here.

def home(request):
    context ={
        "items":Item.objects.all()
    }
    return render(request, "home.html",context)
    
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form =UserRegistrationForm()
    return render(request,'registration/registration_form.html',{'form':form}) 
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    id = current_user.id
  
    return render(request, "profile/profile.html")

@login_required(login_url='/accounts/login/')
def add_profile(request):
    try:
        current_user = request.user
    except DoesNotExist:
        raise Http404()
    if request.method == 'POST':
        form = profileForm(request.POST, request.FILES)
        if form.is_valid():
            myprofile = form.save(commit=False)
            myprofile.username = current_user
            myprofile.save()
            return redirect('details')
    else:
        form = profileForm()
    return render(request, 'profile/profileupdate.html', {"form": form})

@login_required(login_url='/accounts/login/')
def search_item(request):
    
    if 'items' in request.GET and request.GET["items"]:
        name = request.GET.get("items")
        items = Item.search_item(name)
        print(items)
        message = f"{name}"

        return render(request, 'search.html', {"message": message, "categories": items})

    else:
        message = "You haven't searched for any item"
        return render(request, 'search.html', {"message": message})
    