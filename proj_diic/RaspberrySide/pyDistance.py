from math import sin, cos, sqrt, atan2, radians
import sys

def main(lat, lon):
	lat2 = radians(float(lat))
	lon2 = radians(float(lon))

	lat1 = radians(38.737109)
	lon1 = radians(-9.303306)

	R = 6373.0

	dlon = lat2 - lat1
	dlat = lon2 - lon1

	a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
	c = 2 * atan2(sqrt(a), sqrt(1-a))
	distance = R * c

	print "Result", distance, "km"

def usage():
	print ""
	print "IOT Shuttle -- T3"
	print ""
	print "python script that calculates distance between two locations"
	print ""
	print "python pyDistance.py <lat> <lon>"
	print ""

if __name__ == "__main__":
	if(len(sys.argv) < 2):
		usage()
	else:
		main(sys.argv[1], sys.argv[2])