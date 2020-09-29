#!/usr/bin/python3
print("content-type: text/html")
print()
import cgi
import subprocess
form=cgi.FieldStorage()
osname=form.getvalue("x")
osimage=form.getvalue("y")
command="sudo docker run -d -i -t --name {0} {1}".format(osname,osimage)
output=subprocess.getstatusoutput(command)
status=output[0]
info=output[1]
if status==0:
  print("{} OS is launched succesfully....".format(osname))
else:
  print("some error: {}".format(info))

