from django.shortcuts import render,redirect
from django.http import HttpResponse
from .formss import CompanyForm,EmployeeForm,CompanyNameForm,EmployeeNameForm,updateCompanyForm,updateEmployeeForm
from .models import Company,Employee
def first_page(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_done')  # Redirect after POST
    else:
        form = CompanyForm()  # An empty form

    return render(request, 'first.html', {'form': form})
   

def second_page(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('request_done')  # Redirect after POST
    else:
        form = EmployeeForm()  # An empty form

    return render(request, 'second.html', {'form': form})

def demo(request):
    context={}
    return render(request,'demo.html',context)

def success(request):
    return HttpResponse("Request Successfull!!")


def show_data(request):
    companies=None
    company = None
    form = CompanyNameForm(request.POST)
    if form.is_valid():
        company = request.POST.get('company')
        companies = Company.objects.filter(name=company) 
    
    context={
        'heading':"Show Company Data",
        'form':form,
        'data':companies
    }
    return render(request,'show.html',context)

def show_data_emp(request):
    employees=None
    company = None
    form = CompanyNameForm(request.POST)
    if form.is_valid():
        company = request.POST.get('company')
        employees = Employee.objects.filter(cmp_name=company)      
    
    context={
        'heading':"Show Employee Data",
        'form':form,
        'cmpny_name':company,
        'data':employees
    }
    return render(request,'show_emp.html',context)



def update_data(request):
    context={}
    form=updateCompanyForm(request.POST)
    try:
        if form.is_valid():

            company=Company.objects.filter(name=request.POST.get('name'))
            for c in company:
                for field, value in request.POST.items():
                    value=form.cleaned_data.get(field)
                    if value != "":
                        print("value changed", field,value)
                        if value:
                            setattr(c, field, value)
                c.save()
            
                
            context={
                'form':form,
            }
            
    except Company.DoesNotExist:
        print(request.POST)
        context={'form':form}
        print("company with name does not exist")
    return render(request,'update_company_form.html',context)
    
    

def delete_data(request):
    companies=None
    company = None
    form = CompanyNameForm(request.POST)
    if form.is_valid():
        company = request.POST.get('company')
        companies = Company.objects.filter(name=company) 
    if companies:
        for cmp in companies:
            cmp.delete()
    context={'form':form,'data':Company.objects.all(),'heading':"Delete Company"}
    return render(request,'show.html',context)


def update_data_emp(request):
    form = updateEmployeeForm(request.POST)
    employee=Employee.objects.filter(cmp_name=request.POST.get('cmp_name'),emp_name=request.POST.get('emp_name'))
    try:
        if form.is_valid():

            
            for c in employee:
                for field, value in request.POST.items():
                    value=form.cleaned_data.get(field)
                    if value != "":
                        print("value changed", field,value)
                        if value:
                            setattr(c, field, value)
                c.save()
            
                
            context={
                'form':form,
            }
            
    except Company.DoesNotExist:
        print(request.POST)
        context={'form':form}
        print("company with name does not exist")
    return render(request,'update_company_form.html',context)
    return render(request,'update_employees.html',context)





def delete_data_emp(request):
    company=None
  
    form = CompanyNameForm(request.POST)
    form1 = EmployeeNameForm(request.POST)
    if form.is_valid() and form1.is_valid():
        company=request.POST.get("company")      
        employee=request.POST.get('employee')
        emp=Employee.objects.filter(cmp_name=company,emp_name=employee)
        print(company,employee,emp,len(emp))
        for e in emp:
            e.delete()
        
    context={
        'form':form,
        'form1':form1,
        'data':Employee.objects.filter(cmp_name=company)
    }
    return render(request,'delete_emp.html',context)



def delete(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('show2')

def edit(request,id):
    emp=Employee.objects.get(id=id)
    print("id is",id)
    return redirect('show2')