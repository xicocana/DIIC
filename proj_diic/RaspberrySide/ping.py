import sys, subprocess, platform

def usage():
    print "DIIC T3 ping script"
    print ""
    print "usage:"
    print "    ping <ip_address>"
    print ""

def main(host):
    import subprocess, platform
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True
    if subprocess.call(args, shell=need_sh)==0:
        print ""
        print "send message to arduino!"
    else:
        print "no need to change light..."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
    else:
        main(str(sys.argv[1]))