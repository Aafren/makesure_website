from django.shortcuts import render
from .models import RF_Services,WM_Services,AC_Services 
from .models import Users
from django.contrib.auth.models import User, auth
# import pywhatkit as kit
import datetime
# Create your views here.


def website(request):

   
    # serv1=Services()
    # serv1.name='Lite AC Servicesx'
    # serv1.price=700

    # serv2=Services()
    # serv2.name='usama'
    # serv2.price=300

    # serv3=Services()
    # serv3.name='Hudhaifa'
    # serv3.price=200

    rf_servs=RF_Services.objects.all()
   
    ac_servs=AC_Services.objects.all()
    wm_servs=WM_Services.objects.all()
    servs=[rf_servs,ac_servs,wm_servs]
    return render(request,'website.html',{'rf_servs':rf_servs,'ac_servs':ac_servs,'wm_servs':wm_servs})


def submit(request):
    
    if request.method == 'POST':
        name=request.POST['name']
        address=request.POST['address']
        mobile=request.POST['mobile']
        user=Users(name=name,address=address,mobile=mobile)
        # save(username='name',address='address',mobile='mobile')
        user.save();
        # number='+919003912073'
        test=[name,address,mobile]
        # kit.sendwhatmsg(number,'Hi',23, 48)
        # kit.sendwhatmsg("+919003912073",'Aafren', datetime.datetime.now().hour,datetime.datetime.now().minute+1)
        print('User Created')
    
    return render(request,'submit.html')

def booking_details(request):
    result=Users.objects.all()

    # servs=[serv1,serv2,serv3]
    return render(request,'booking_details.html',{'result':result})

def home(request):
    return render(request,'website.html')

def privacy(request):
    return render(request,'privacy.html')

def terms(request):
    return render(request,'terms.html')