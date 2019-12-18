from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
        return render(request, 'home/home.html')
def login2(request):
        return render(request, "home/login2.html")
        
def stock(request):
        return render(request, "home/stock.html")

def addmedi(request):
        return render(request, "home/addmedi.html")



def register(request):
        
        if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                        form.save()
                        return redirect('login2')
        else:
                form = UserCreationForm()

        return render(request, "home/register.html", {'form': form}) 