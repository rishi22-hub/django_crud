from django import forms
from .models import Company,Employee
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


class CompanyNameForm(forms.Form):
    company = forms.ModelChoiceField(queryset=Company.objects.all())


class EmployeeNameForm(forms.Form):
    employee = forms.CharField(max_length=100)


class updateCompanyForm(forms.Form):
    name=forms.CharField(max_length=100)
    description=forms.CharField(max_length=100,required=False)
    industry=forms.CharField(max_length=100,required=False)
    phoneno=forms.CharField(max_length=100,required=False)
    est_date=forms.DateField(required=True)
    address=forms.CharField(max_length=100,required=False)


class updateEmployeeForm(forms.Form):
    cmp_name=forms.ModelChoiceField(queryset=Company.objects.all())
    emp_name=forms.CharField(max_length=100,required=False)
    join_date=forms.DateField()
    emp_address=forms.CharField(max_length=100,required=False)
    designation=forms.CharField(max_length=100,required=False)




    