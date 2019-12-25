from math import sin, cos, sqrt, atan2, radians
# CALCULATE DISTANCE IN METERS

def calcDist(alpha, beta): # pass in two strings and calculate distance between them

    R = 6373.0 # radius of the earth in KM

    # alpha = "52.2296756 21.0122287" # point one
    # beta = "52.406374 16.9251681" # point two 

    P1 = [radians(float(x)) for x in alpha.split(", ")]
    P2 = [radians(float(x)) for x in beta.split(", ")]

    dlat = P1[0] - P2[0]
    dlon = P1[1] - P2[1]

    a = sin(dlat / 2)**2 + cos(P1[0]) * cos(P2[0]) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distanceKM = R * c
    distanceM = (distanceKM*1000.0)
    
    return distanceM