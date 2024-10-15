from django.shortcuts import render, HttpResponseRedirect
from . forms import StudentRegistration
from . models import User
# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fname = fm.cleaned_data['First_Name']
            lname = fm.cleaned_data['Last_Name']
            pnumber = fm.cleaned_data['Phone_Number']
            email = fm.cleaned_data['Email_ID']
            address = fm.cleaned_data['Address']
            reg = User(First_Name=fname,Last_Name=lname,Phone_Number=pnumber,Email_ID=email, Address=address  )
            reg.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    user = User.objects.all()

    return render(request, 'addandshow.html', {'form':fm, 'users':user})

def delete_data(request, id):
    if request.method == 'POST':
        sd = User.objects.get(pk=id)
        sd.delete()
        return HttpResponseRedirect('/')
    
def delete_all_data(request):
    if request.method == 'POST':
        da = User.objects.all()
        da.delete()
        User.truncate()
    else:
        print('Not with Post request, just for debug the function')
    return HttpResponseRedirect('/')

def update_data(request, id):
    if request.method == 'POST':
        sd = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=sd)
        if fm.is_valid():
            fm.save()
    else:
        sd = User.objects.get(pk=id)
        fm = StudentRegistration(instance=sd)
    return render(request, 'updatestudent.html', {'form':fm})

