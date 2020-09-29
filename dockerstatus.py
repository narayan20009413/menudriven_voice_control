#!/usr/bin/python3
print("content-type: text/html")
print()
import subprocess
command="sudo systemctl status docker"
output=subprocess.getstatusoutput(command)
status=output[1]
print(" docker status {} ".format(status))

