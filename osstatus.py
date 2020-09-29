#!/usr/bin/python3
print("content-type: text/html")
print()
import subprocess
command="sudo docker ps"
output=subprocess.getstatusoutput(command)
status=output[0]
info=output[1]
if status==0:
  print("currently running OS....{}".format(info))
else:
  print("some error: {}".format(info))


