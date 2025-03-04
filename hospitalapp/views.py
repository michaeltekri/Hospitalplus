from django.shortcuts import render,redirect,get_object_or_404


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
        return redirect('/show')
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

def show(request):
    all=appointment.objects.all()
    return render(request,'show.html',{'all':all})

def delete(request,id):
    deleteappointment=appointment.objects.get(id=id)
    deleteappointment.delete()
    return redirect('/show')

def edit(request,id):
    appointments=get_object_or_404(appointment,id=id)
    if request.method=='POST':
        appointments.name=request.POST.get('name')
        appointments.email=request.POST.get('email')
        appointments.phone=request.POST.get('phone')
        appointments.date=request.POST.get('date')
        appointments.department=request.POST.get('department')
        appointments.doctor=request.POST.get('doctor')
        appointments.message=request.POST.get('message')
        appointments.save()
        return redirect('/show')

    else:
        return render(request,'edit.html',{'appointments':appointments})




