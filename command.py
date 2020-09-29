#!/usr/bin/python3
print("content-type: text/html")
print()
import subprocess
import cgi
form=cgi.FieldStorage()
p=form.getvalue("c")
print(p)
cmd="sudo {}".format(p)
print(cmd)
out=subprocess.getstatusoutput(cmd)
status=out[0]
output=out[1]
if status==0:
    print("{}".format(output))
else:
    print("some error:{}".format(output))    
