#!/usr/bin/python3
print("content-type: text/html")
print()
import subprocess
command="sudo systemctl stop docker"
output=subprocess.getstatusoutput(command)
status=output[0]
info=output[1]
if status==0:
  print("docker stopped succesfully....")
else:
  print("some error: {}".format(info))
