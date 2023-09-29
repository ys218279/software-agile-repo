from django.shortcuts import render, redirect , get_object_or_404
from .forms import ExtendedUserCreationForm, LoginForm, CreateTicketRecordForm, UpdateRecordForm, UpdateTicketRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required

from .models import EmployeeDetails, Tickets

from django.contrib import messages

def index(request):
    if not request.user.is_authenticated:
        return redirect('my-login')
    elif request.user.is_staff:
        return redirect('admin-home')
    else:
        return redirect('user-home')

# Home - admin
def admin_home(request):
    return render(request, 'admin_webapp/admin-home.html')
@login_required
def user_home(request):
    try:
        record = EmployeeDetails.objects.get(user=request.user)
    except EmployeeDetails.DoesNotExist:
        record = None
    
    context = {'record': record}
    return render(request, 'user_webapp/user-home.html', context)

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
                if user.is_staff:
                    return redirect("admin-home")
                else:
                    return redirect("user-home")

    context = {'form':form}

    return render(request, 'webapp/my-login.html', context=context)


# - employee records

@login_required(login_url='my-login')
def employee_records(request):

    my_records = EmployeeDetails.objects.all()

    context = {'records': my_records}

    return render(request, 'admin_webapp/employee-records.html', context=context)

# - Read / View a singular record
@login_required(login_url='my-login')
def singular_employee_record(request, pk):
    all_records = EmployeeDetails.objects.get(id=pk)
    context = {'record':all_records}
    return render(request, 'webapp/view-employee-record.html', context=context)

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


def user_tickets(request):
    tickets = Tickets.objects.filter(user=request.user)  # Correctly using 'user' field here
    return render(request, 'user_webapp/user-tickets.html', {'tickets': tickets})
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
            ticket = form.save(commit=False)
            ticket.user = request.user  # Assign the currently logged-in user to the user field of the Ticket model.
            ticket.save()
            messages.success(request, 'Ticket created successfully!')
            return redirect('tickets')  # Redirect to the ticket_records view
    else:
        form = CreateTicketRecordForm()
    return render(request, 'webapp/create-ticket-record.html', {'form': form})  # Render the form in the specified template


# - Update ticket record

@login_required(login_url='my-login')
def update_ticket_record(request, pk):

    ticket_record = get_object_or_404(Tickets, pk=pk)
    print(ticket_record,ticket_record.id)  # Debug print statement

    form = UpdateTicketRecordForm(instance=ticket_record)

    if request.method == 'POST':

        form = UpdateTicketRecordForm(request.POST, instance=ticket_record)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("view-ticket",pk=ticket_record.id)
        
    context = {'form': form, 'ticket_record': ticket_record}
    return render(request, 'webapp/update-ticket-record.html', context=context)

# - Delete Ticket record

@login_required(login_url='my-login')
def delete_ticket_record(request, pk):

    record = Tickets.objects.get(id=pk)

    record.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("tickets")
# - User logout

def user_logout(request):

    auth.logout(request)

    messages.success(request, "Logout success!")

    return redirect("my-login")

