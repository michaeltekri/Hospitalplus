from django.shortcuts import render,redirect


from hospitalapp.models import *
# Create your views here.
def index(request):
    return render(request,'index.html')

def services(request):
    return render(request,'service-details.html')



def starter(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'services.html')


def doctor(request):
    return render(request,'doctors.html')

def dep(request):
    return render(request,'departments.html')

def appoints(request):
    if request.method =="POST":
        myappointments=appointment(
            name= request.POST['name'],
            email= request.POST['email'],
            phone= request.POST['phone'],
            date= request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message']
        )
        myappointments.save()
        return redirect('/appointment')
    else:
        return render(request,'appointment.html')

def con(request):
    if request.method =="POST":
        mycontacts=contact(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message']
        )
        mycontacts.save()
        return redirect('/contact')
    else:
        return  render(request,'contact.html')
