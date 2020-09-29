#!/usr/bin/python3
print("content-type: text/html")
print()
import subprocess
command="sudo systemctl status httpd"
output=subprocess.getstatusoutput(command)
status=output[1]
print("httpd status: {}".format(status))
