#!/bin/python3
print("content-type: text/html")
print()

import cgi,json
#import requests,xmltodict
import subprocess as sp
import os
#import requests
#from xml_to_dict import XMLtoDict
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
# Get filename here.
fileitem = form['filename']
#filename="sample.jpg"
#file = open('filename', 'wb')
#try:
 #   file.write('fileitem')
#finally:
 #   file.close()
#print(fileitem.file.read())
# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename.replace("\\", "/" ))
   open('/test/'+fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully...Now please click Submit and wait for sometime till we give you the output!!...\nAlso dont click submit again and again...press only once and wait for sometime..approx 10-15 seconds'
else:
   message = 'No file was uploaded'

print(message)
sp.getoutput("mv /test/* /var/www/cgi-bin/images/task8.jpeg")
#print("Now please click Submit and wait for sometime till we give you the output!!...Also dont click submit again and again...press only once and wait for sometime..approx 10-15 seconds")

