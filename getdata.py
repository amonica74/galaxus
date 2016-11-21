from os import listdir
from os.path import isfile, join
import re

mypath = "/Users/ale/galaxus"
myfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and "html" in f]

for f in myfiles:
	with open(join(mypath, f)) as myfile:
	    str = myfile.read()
	    match = re.search(r"Verarbeitungszeit: <strong >(\d+)</strong>ms \((.*)\) Cache: (\d+)ms Esent: (\d+)ms \((\d+)\)\<br /\>Server: <strong >(.*)</strong><br />ES Index: (.*) ES Template: (.*)</H4>", str)
	    if match:
	        datetime = f[:-5].split('_')
	        datetime[1] = datetime[1].replace('-',':')
	        print datetime[0] + ' ' + datetime[1] + ', ' + ', '.join([i for i in match.groups()])
        