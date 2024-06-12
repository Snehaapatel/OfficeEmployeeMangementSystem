from django.shortcuts import render,HttpResponse
from . models import Employee,Role,Department
from datetime import datetime
from . forms import EmpForm
from django.db.models import Q

# Create your views here.

def index (request):
    return render (request,'index.html')

def all_emp (request):
    emps=Employee.objects.all()
    context={
        'emps' :emps
    }
    print (context)

    return render (request,'view_all_emp.html',context)

def add_emp (request):
    if request.method == 'POST' :
        #emps=EmpForm(request.POST)
        #if emps.is_valid():



            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            salary=(request.POST['salary'])
            dept=(request.POST['dept'])
            bonus=(request.POST['bonus'])
            phone=(request.POST['phone'])
            role=(request.POST['role'])

            new_emp=Employee (first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,dept_id=dept,phone=phone,role_id=role,hire_date=datetime.now())
            new_emp.save()
            #emps=EmpForm()
            return HttpResponse('Employee Added Successfully')
    elif request.method=='GET' :
        return render (request,'add_emp.html')
    
    else :
        return HttpResponse("An exception Occured ! An employe has not been added")

        

    return render (request,'add_emp.html')

def remove_emp (request,emp_id=0):
    if emp_id :
         try :
              emp_to_be_removed=Employee.objects.get(id=emp_id)
              emp_to_be_removed.delete()
              return HttpResponse ("Employee Removed Successfully")
         except :
              return HttpResponse("Please Enter a valid Emp_id")
    emps=Employee.objects.all()
    
    return render (request,'remove_emp.html',{'emps':emps})

def filter_emp (request):
    if request.method=='POST' :
         name=request.POST['name']
         dept=request.POST['dept']
         role=request.POST['role']
         emps=Employee.objects.all()
         if name:
              emps=emps.filter(Q(first_name__icontains=name) |Q(last_name__icontains=name))

         if dept :
              emps=emps.filter(dept__name=dept)
         if role :
              emps=emps.filter (role__name=role)

         return render (request,'view_all_emp.html',{'emps':emps})
    
    elif request.method=='GET' :
        return render (request,'filter_emp.html')
    
    else :
        return HttpResponse("An exception Occured ! An employe has not been filtered")


         

            
        

    return render (request,'filter_emp.html')

