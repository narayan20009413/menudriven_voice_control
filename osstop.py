#!/usr/bin/python3
print("content-type: text/html")
print()
import subprocess
import cgi
form=cgi.FieldStorage()
osname=form.getvalue("x")
command="sudo docker stop {}".format(osname)
output=subprocess.getstatusoutput(command)
status=output[0]
info=output[1]
if status==0:
  print("{} OS is stopped succesfully....".format(osname))
else:
  print("some error: {}".format(info))
