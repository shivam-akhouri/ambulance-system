from django.contrib.auth.models import User
def checkPassword(pass1, pass2):
    if pass1 == pass2:
        return True
    return False

def getHospitalAmbulances(hospitalName):
    profiles = User.objects.filter(ambulance__person = 0)
    return profiles