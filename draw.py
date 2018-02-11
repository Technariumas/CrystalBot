#!/usr/bin/python3

import sys
import MySQLdb
import wget
import os 
import subprocess

#Access MySQL via Python..
db = MySQLdb.connect(host="sql.crystallography.net",    
                     user="cod_reader", db="cod")        

cur = db.cursor()
#select the latest added structure from COD
cur.execute('select file, formula, date, time from data where flags like "%has Fobs%" order by date desc, time  DESC  limit 1')

#select random structure
#cur.execute('select file, formula, date, time from data where flags like "%has Fobs%" order by rand() limit 1')

for row in cur.fetchall():
    cifId = str(row[0])
    formula = str(row[1])
db.close()

cifFile = "http://www.crystallography.net/cod/"+cifId+".cif"

#Downloads the CIF file
wget.download(cifFile, "cif/"+cifId+".cif")
#os.system("jmol cif/"+cifId+".cif")

#Creates Jmol script that generates an annotated 2D molecule snapshot 
file = open("scripts/"+cifId+".spt","w") 
file.write("load cif/"+cifId+".cif;\n")
file.write("set echo example 0% 5%;\n")
file.write("font echo 63 serif bold;\n") 
file.write("echo " +formula+ " ("+cifId+");\n" )
file.write('write IMAGE 842 595 PNG n "png";') 
file.close() 

#Runs Jmol script
os.system("jmol scripts/"+cifId+".spt &&")

#Runs ImageMagick's convert utility to invert image colours and convert it to black and white
os.system("convert png -negate  -threshold 80% output.bmp")

#Runs potrace to vectorize the generated bmp file
os.system("potrace --svg output.bmp -t 10 -a 3 -u 10 -P A4 --group -o vect-grib.svg")

#This is a shell script that corrects the output svg measurements -- thanks to ffwd!
os.system("./grib.sh")

# calls the plotter:
subprocess.check_output(['axibot', 'plot', 'vect.svg'])


