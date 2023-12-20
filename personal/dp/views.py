from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth, messages

from .forms import PersonForm
from .models import Person


class AddPersonView(View):
    def get(self, request):
        form = PersonForm()
        return render(request, 'add_person.html', {'form': form})

    def post(self, request):
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dp:view_persons')
        return render(request, 'add_person.html', {'form': form})


class ViewPersonsView(View):
    def get(self, request):
        persons = Person.objects.all()
        return render(request, 'view_persons.html', {'persons': persons})


def index(request):
    return render(request,'index.html')



def register(request, username=None):

    if request.method == 'POST':
        name = None
        email = None
        password = None
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password']

            
        if password == password1:
            if User.objects.filter(username=name).exists():
                    messages.info(request, 'username already taken')
                    return redirect('register')
            elif User.objects.filter(email=email).exists():
                    messages.info(request, 'email already taken')
                    return redirect('register')
            elif User.objects.filter(password=password).exists():
                    messages.info(request, 'password not matching')
                    return redirect('dp:register')

            else:
                    user = User.objects.create_user(username=name, email=email, password=password)
                    user.save()
                    print("user created")
                    return redirect('dp:login')

        else:
                messages.info(request, 'password arent matching')
                return redirect('dp:register')

    return render(request, "register.html")

def login(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=name, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('dp:login')
    else:
        return render(request, 'login.html')

def logout(request):
     auth.logout(request)
     return redirect('/')


# Create your views here.
