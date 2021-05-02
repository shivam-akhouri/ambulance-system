from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login,logout,authenticate
from . import utils
from . import meetautomatic
from django.contrib.auth.models import User
from api.models import Ambulance, Messages


# Create your views here.

# @login_required(login_url='/home/signIn/')
def ambulanceRegister(request):
    if request.method == "POST":
        ambno = request.POST.get("AmbulanceNo")
        drivName = request.POST.get("DriverName")
        phone = request.POST.get("PhoneNo")
        healthWork = request.POST.get("HealthWorker")
        hosName = request.POST.get("Hospital")
        pass1 = request.POST.get("Password")
        pass2 = request.POST.get("ConfirmPassword")
        gmeet = request.POST.get("gmeetLink")
        print(drivName, phone, hosName, pass1, pass2)
        if utils.checkPassword(pass1, pass2):
            user = User.objects.create_user(username = ambno, password = pass1)
            user.save()
            user.ambulance.driverName = drivName
            user.ambulance.phoneno = phone
            user.ambulance.hospitalName = hosName
            user.ambulance.status = 0
            user.ambulance.posLatitude = 0.0
            user.ambulance.posLongitude = 0.0
            user.ambulance.sevirity = 0
            user.ambulance.healthWorker= 0
            user.ambulance.oxyCylinderMeter = 0
            user.ambulance.ambulanceGmeet = gmeet
            user.ambulance.save()
            messages.success(request, "Congo! You have registered Successfully.")
        template = loader.get_template('index.html')
        return HttpResponse(template.render({}, request))
    if request.method == 'GET':
        template = loader.get_template('registerAmbulance.html')
        return HttpResponse(template.render({}, request))

def homepage(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))

def contactUs(request):
    template = loader.get_template("contacts.html")
    return HttpResponse(template.render({}, request))

def searchPage(request):
    #Processing to be done
    template = loader.get_template("search.html")
    return HttpResponse(template.render({}, request))

def signIn(request):
    if request.method=="GET":
        if request.user.is_authenticated:
            template = loader.get_template("index.html")
            return HttpResponse(template.render({}, request))
        template = loader.get_template("signIn.html")
        return HttpResponse(template.render({}, request))
    if request.method=="POST":
        username = request.POST.get("Username")
        password = request.POST.get("Password")                             
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.warning(request, "Invalid Username or Password")
            template = loader.get_template("signIn.html")
            return HttpResponse(template.render({}, request))
        login(request, user)
        template = loader.get_template("index.html")
        return HttpResponse(template.render({}, request))


def signOut(request):
    logout(request)
    template = loader.get_template("index.html")
    return HttpResponse(template.render({}, request))
        

def signUp(request):
    if request.method == 'POST':
        username = request.POST['Username']
        firstName = request.POST['FirstName']
        lastName = request.POST['LastName']
        phone = request.POST.get("PhoneNo")
        pass1 = request.POST['Password']
        pass2 = request.POST['ConfirmPassword']
        if utils.checkPassword(pass1, pass2):
            print(username, firstName, lastName, phone, pass1, pass2)
            user = User.objects.create_user(username = username, password = pass1)
            user.save()
            user.first_name = firstName
            user.last_name = lastName
            user.ambulance.phoneno = phone
            user.ambulance.person = 1
            user.save()
            messages.success(request, "Your Profile has been created Successfully. Click Below to login.")
        else:
            messages.warning(request, "There was some mishappening during account creation")
        template = loader.get_template("index.html")
        return HttpResponse(template.render({}, request))
    if request.method == "GET":
        template = loader.get_template("signUp.html")
        return HttpResponse(template.render({}, request))
    

def showAmbulances(request):
    #To be done
    profiles = User.objects.filter(ambulance__person = 0)
    template = loader.get_template("ambulanceList.html")
    return HttpResponse(template.render({"ambulances": profiles}, request))

def joinMeeting(request):
    if request.method == "GET":
        meetautomatic.mainFunc(request.user.ambulance.ambulanceGmeet)
        template = loader.get_template("index.html")
        return HttpResponse(template.render({}, request))          

@login_required(login_url='/home/signIn')
def sendMessage(request):
    if request.method=='POST':
        hospital = request.user.ambulance.hospitalName
        gmeetLink = request.user.ambulance.ambulanceGmeet
        driverName = request.user.ambulance.driverName
        ambulanceName = request.user.username
        oxygen = request.POST.get('OxygSatu')
        ctv = request.POST.get('CTV')
        disease = request.POST.getlist('Disease')
        diseases = ""
        for i in disease:
            diseases += i+" "
        print(oxygen, ctv, diseases)
        m = Messages.objects.create(driverName=driverName, meetingLink=gmeetLink, hospital= hospital, ambulanceName=ambulanceName, disease=diseases, oxygenPatient=oxygen, ctv=ctv)
        m.save()
        meetautomatic.mainFunc(request.user.ambulance.ambulanceGmeet)
        template = loader.get_template("index.html")
        return HttpResponse(template.render({}, request))

def location(request):
    template = loader.get_template('location.html')
    return HttpResponse(template.render({}, request))
    


def isAmbulance(user):
    if user.ambulance.person == 0:
        return True
    return False

@login_required(login_url='/home/signIn')
def patientUpdate(request):
    if request.user.ambulance.person == 1 :
        messages.warning(request, "Kindly login from an Ambulance Compitable Account.")
        template = loader.get_template("index.html")
        return HttpResponse(template.render({}, request))
    template = loader.get_template('patientUpdate.html')
    return HttpResponse(template.render({}, request))    

@login_required(login_url='/home/signIn')
def doctorSide(request):
    if request.user.ambulance.person == 0:
        messages.warning(request, "Kindly login from an Doctors Compitable Account.")
        template = loader.get_template("index.html")
        return HttpResponse(template.render({}, request))
    ambulances = User.objects.filter(ambulance__hospitalName= request.user.ambulance.hospitalName, ambulance__person = 0)
    template = loader.get_template('doctorSide.html')
    return HttpResponse(template.render({"result": ambulances}, request))   

def todelete(request):
    template = loader.get_template('todelete.html')
    return HttpResponse(template.render({}, request))   
