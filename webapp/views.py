from django.shortcuts import render, redirect
from .forms import ExtendedUserCreationForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import EmployeeDetails, Tickets

from django.contrib import messages



# Home

def home(request):

    return render(request, 'webapp/home.html')

# - Index page 

def index(request):

    return render(request, 'webapp/index.html')


# - Register a user

def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('my-login')  # or wherever you want to redirect to
    else:
        form = ExtendedUserCreationForm()
    return render(request, 'webapp/register.html', {'form': form})



# - Login a user

def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("home")

    context = {'form':form}

    return render(request, 'webapp/my-login.html', context=context)


# - Dashboard

@login_required(login_url='my-login')
def dashboard(request):

    my_records = EmployeeDetails.objects.all()

    context = {'records': my_records}

    return render(request, 'webapp/home.html', context=context)


# - Create a record 

@login_required(login_url='my-login')
def create_record(request):

    form = CreateRecordForm()

    if request.method == "POST":

        form = CreateRecordForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("home")

    context = {'form': form}

    return render(request, 'webapp/create-record.html', context=context)


# - Update a record 

@login_required(login_url='my-login')


# - Read / View a singular record

@login_required(login_url='my-login')
def singular_record(request, pk):

    all_records = EmployeeDetails.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'webapp/view-record.html', context=context)


# - Delete a record

@login_required(login_url='my-login')
def delete_record(request, pk):

    record = EmployeeDetails.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("home")



# - User logout

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("my-login")

