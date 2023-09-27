from django.shortcuts import render, redirect , get_object_or_404
from .forms import ExtendedUserCreationForm, LoginForm, CreateTicketRecordForm, UpdateRecordForm, UpdateTicketRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import EmployeeDetails, Tickets

from django.contrib import messages



# Home - admin
def home(request):

    return render(request, 'admin_webapp/admin-home.html')

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
            return redirect('my-login') 
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


# - employee records

@login_required(login_url='my-login')
def employee_records(request):

    my_records = EmployeeDetails.objects.all()

    context = {'records': my_records}

    return render(request, 'admin_webapp/employee-records.html', context=context)


# - Create a record 

#@login_required(login_url='my-login')
#def create_employee_record(request):

#    form = CreateRecordForm()

#    if request.method == "POST":

#        form = CreateRecordForm(request.POST)

#        if form.is_valid():

#            form.save()

#            messages.success(request, "Your record was created!")

#            return redirect("home")

#    context = {'form': form}

#    return render(request, 'webapp/create-record.html', context=context)


# - Update a record 

@login_required(login_url='my-login')
def update_employee_record(request, pk):

    record = get_object_or_404(EmployeeDetails, pk=pk)
    print(record, record.id)  # Debug print statement

    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=record)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("view-employee-record",pk=record.id)
        
    context = {'form': form, 'record': record}
    return render(request, 'webapp/update-employee-record.html', context=context)


# - Read / View a singular record

@login_required(login_url='my-login')
def singular_employee_record(request, pk):

    all_records = EmployeeDetails.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'webapp/view-employee-record.html', context=context)


# - Delete a record

@login_required(login_url='my-login')
def delete_record(request, pk):

    record = EmployeeDetails.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("view-employee-record",pk=record.id)



# - Tickets

#view ticket record

@login_required(login_url='my-login')
def ticket_records(request):

    ticket_records = Tickets.objects.all()

    context = {'ticket_records': ticket_records}
  
    return render(request, 'admin_webapp/tickets.html', context=context)

# - View single ticket

@login_required(login_url='my-login')
def singular_ticket_record(request, pk):

    ticket_records= Tickets.objects.get(id=pk)

    context = {'ticket_records': ticket_records}

    return render(request, 'webapp/view-ticket.html', context=context)



# - Create Ticket record

def create_ticket_record(request):

    if request.method == 'POST':
        form = CreateTicketRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tickets') # Replace 'tickets_list' with the name of the view that lists all tickets
    else:
        form = CreateTicketRecordForm()
    return render(request, 'webapp/create-ticket-record.html', {'form': form})

# - Update ticket record

@login_required(login_url='my-login')
def update_ticket_record(request, pk):

    ticket_record = get_object_or_404(Tickets, pk=pk)
    print(ticket_record,ticket_record.id)  # Debug print statement

    form = UpdateTicketRecordForm(instance=ticket_record)

    if request.method == 'POST':

        form = UpdateRecordForm(request.POST, instance=ticket_record)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("view-ticket",pk=ticket_record.id)
        
    context = {'form': form, 'ticket_records': ticket_record}
    return render(request, 'webapp/update-ticket-record.html', context=context)


# - User logout

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("my-login")

