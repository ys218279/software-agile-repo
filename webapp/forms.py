from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import EmployeeDetails, Tickets
from django import forms
from django.contrib.auth.forms import AuthenticationForm
#from django.forms.widgets import PasswordInput, TextInput


#Employee

# - Register/Create a user

class EmployeeDetailsForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'postcode', 'country']


class ExtendedUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    address = forms.CharField(required=True)
    country = forms.CharField(required=True)
    city = forms.CharField(required=True)
    postcode = forms.CharField(required=True)
    

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            employee_details = EmployeeDetails(
                user=user,
                first_name=self.cleaned_data['first_name'],
                last_name=self.cleaned_data['last_name'],
                email=self.cleaned_data['email'],
                phone=self.cleaned_data['phone'],
                address=self.cleaned_data['address'],
                city=self.cleaned_data['city'],
                country=self.cleaned_data['country'],
                postcode=self.cleaned_data['postcode']
            )
            employee_details.save()
        return user


class LoginForm(AuthenticationForm):
    pass  # No need to explicitly define username and password fields


#class CreateRecordForm(forms.ModelForm):
#    class Meta:
#        model = EmployeeDetails
#        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'postcode', 'country']


class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = EmployeeDetails
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'postcode', 'country']


#Tickets 
class CreateTicketRecordForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ['item', 'location_use', 'date_hired', 'date_returned']
        widgets = {
            'date_hired': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'date_returned': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
            }


class UpdateTicketRecordForm(forms.ModelForm):
    class Meta:
        model = Tickets
        fields = ['date_returned']
        widgets = {
            'date_returned': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'})
        }
        

