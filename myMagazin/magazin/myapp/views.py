from django.shortcuts import render
from django.contrib.auth.models import User


def index(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        new = User.objects.create_user(data["log"],data["email"],data["pass"])
        new.save()
        
    return render(request,'main.html')

# Create your views here.
