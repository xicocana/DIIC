import sys, subprocess, platform, os

def usage():
	print "DIIC T3 IOT SHUTTLE"
	print ""
	print "usage: "
	print "   SendColor <value>"
	print ""
	print "possible values are: red, yellow, green and off"
	print ""

def main(value):
	args = "mosquitto_pub -h raspberrypi -t '/leds/esp8266' -m "
	if value == "red":
		command = args + " 'a'"
		os.system(command)
	if value == "yellow":
		command = args + " 'aa'"
		os.system(command)
	if value == "green":
		command = args + " 'aaa'"
		os.system(command)
	if value == "off":
		command = args + " 'aaaa'"
		os.system(command)

if __name__ == "__main__":
	if len(sys.argv) < 2:
		usage()
	else:
		main(str(sys.argv[1]))

