import socket
import sys
from enum import Enum
from math import sin, cos, sqrt, atan2, radians
class DistanceStage(Enum):
    Stopped = 1
    Arriving = 2
    Near = 3
    Far = 4
    Recovering = 5

UDP_IP = "194.210.221.224"
UDP_PORT = 5500
TagusCoordinates = (38.737109, -9.303306)
distanceStage = DistanceStage.Far

#If shuttle distance is lower than this, assume Shuttle is stopped
StoppedThreshold = 100
#If shuttle distance is lower than this, assume Shuttle is almost arriving at stop
ArrivingThreshold = 1200
#If shuttle distance is lower than this, assume Shuttle is close
NearThreshold = 4000
Stopped = False

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

def notifyDistance(color):
    if (color == "RED"):
        1
    if (color == "YELLOW"):
        1
    if (color == "GREEN"):
        1
    if (color == "GRAY"):
        1

notifyDistance("RED")

while True:
    data, addr = sock.recvfrom(128) # buffer size is 1024 bytes
    TargetCoordinates = (data[1:len(data)]).split(';')

    lat2 = radians(float(TargetCoordinates[0]))
    lon2 = radians(float(TargetCoordinates[1]))
    
    lat1 = radians(TagusCoordinates[0])
    lon1 = radians(TagusCoordinates[1])

    R = 6373.0

    dlon = lat2 - lat1
    dlat = lon2 - lon1

    a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c * 1000

    print(distance)

    if (distanceStage == DistanceStage.Recovering) :
        #When shuttle exits NEAR radius
        if (distance > NearThreshold) :
            distanceStage = DistanceStage.Far
            notifyDistance("GREEN")
    elif (distanceStage == DistanceStage.Far) :
        #When shuttle enters the NEAR radius
        if (distance < NearThreshold) :
            distanceStage = DistanceStage.Near
            notifyDistance("YELLOW")
    elif (distanceStage == DistanceStage.Near) :
        #When shuttle enters the ARRIVING radius
        if (distance < ArrivingThreshold) :
            distanceStage = DistanceStage.Arriving
            notifyDistance("RED")
    elif (distanceStage == DistanceStage.Arriving) :
        #When shuttle enters the STOPPED radius
        if (distance < StoppedThreshold) :
            distanceStage = DistanceStage.Stopped
    elif (distanceStage == DistanceStage.Stopped) :
        #When shuttle exits the STOPPED radius
        if (distance > StoppedThreshold) :
            distanceStage = DistanceStage.Recovering
            notifyDistance("GRAY")
