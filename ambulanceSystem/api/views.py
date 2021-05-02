from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Ambulance, Messages

# Create your views here.
def getAmbulances(request):
    ambulances = User.objects.filter(ambulance__hospitalName= request.user.ambulance.hospitalName, ambulance__person = 0)
    res = []
    i = 0
    for ambulance in ambulances:
        name = ambulance.username
        username = ambulance.username
        phoneno = ambulance.ambulance.phoneno
        gmeet = ambulance.ambulance.ambulanceGmeet
        res.append({"name":name, "phoneno":phoneno, "gmeet": gmeet})
        i+=1
    print(res)
    response = {"data": res, "counter":i}
    return JsonResponse(response, safe=False)


# {
#     "data":[
#         'name':sdfsdf
        
#     ]
# }

def getMessages(request):
    hospitalname = str(request.user.ambulance.hospitalName)
    messages = Messages.objects.filter(hospital= hospitalname)
    response = {}
    res = []
    counter = 0
    for i in messages:
        res.append({'driverName':i.driverName, 'meetingLink':i.meetingLink, 'ambulanceName': i.ambulanceName, "disease":i.disease, "oxygen":i.oxygenPatient, "ctv":i.ctv})
        counter+=1
    response['data'] = res
    return JsonResponse(response, safe=False)
