#!/usr/bin/python3
print("content-type: text/html")
print()
import subprocess
command="sudo systemctl start docker"
output=subprocess.getstatusoutput(command)
status=output[0]
info=output[1]
if status==0:
  print("docker started succesfully....")
else:
  print("some error: {}".format(info))

