

def getInstances(userPositionLat, userPositonLon, distance):
    profiles = User.objects.filter(ambulance__person = 0)  
    possibilities = []
    for profile in profiles:
        if profile.ambulace.posLatitude is not None and profile.ambulance.posLongitude is not None:
            ambLat = profile.ambulance.posLatitude
            ambLon = profile.ambulance.posLongitude
            calcDist = ((ambLat-userPositionLat)**2)+((ambLon-userPositonLon)**2)
            if calcDist < distance**2:
                possibilities.append(profile) 
    return possibilities