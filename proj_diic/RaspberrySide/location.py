import twitter
import time
import sys
from enum import Enum
from math import sin, cos, sqrt, atan2, radians
from datetime import timedelta

class DistanceStage(Enum):
    Stopped = 1
    Arriving = 2
    Near = 3
    Far = 4
    Recovering = 5

TagusCoordinates = (38.737109, -9.303306)
distanceStage = DistanceStage.Far
tweetCheckInterval = 15

#If shuttle distance is lower than this, assume Shuttle is stopped
StoppedThreshold = 150
#If shuttle distance is lower than this, assume Shuttle is almost arriving at stop
ArrivingThreshold = 1200
#If shuttle distance is lower than this, assume Shuttle is close
NearThreshold = 4000
Stopped = False

lastTweetSeconds = 0

api = twitter.Api(consumer_key='***',
                consumer_secret='***',
                access_token_key='***',
                access_token_secret='***')

def notifyDistance(color):
    if (color == "RED"):
        print(color)
    if (color == "YELLOW"):
        print(color)
    if (color == "GREEN"):
        print(color)
    if (color == "GRAY"):
        print(color)

notifyDistance("GREEN")

while True:

    t = api.GetUserTimeline(screen_name="IotShuttle", count=2)
    
    if (len(t) > 0):
        newSeconds = t[0].created_at_in_seconds
        if (lastTweetSeconds == 0 or lastTweetSeconds < newSeconds):
            lastTweetSeconds = newSeconds
            #Analyze tweet content
            data = t[0].text
            data ='b38.7476457 -9.3145716'
            TargetCoordinates = t[0].text.split(' ')

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
        else:
            print("No new tweets")
    else:
        print("No tweets to read")
    time.sleep(tweetCheckInterval)
    