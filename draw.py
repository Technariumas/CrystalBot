from __future__ import division
import sys
import MySQLdb
import wget
import os 
import subprocess

db = MySQLdb.connect(host="sql.crystallography.net",    
                     user="cod_reader", db="cod")        

cur = db.cursor()
#select the latest added structure
#cur.execute('select file, formula, date, time from data where flags like "%has Fobs%" order by date desc, time  DESC  limit 1')

#select random structure
cur.execute('select file, formula, date, time from data where flags like "%has Fobs%" order by rand() limit 1')


for row in cur.fetchall():
    cifId = str(row[0])
    formula = str(row[1])
    date = str(row[2])    
    time = str(row[3])
    print date, time
db.close()

cifFile = "http://www.crystallography.net/cod/"+cifId+".cif"

wget.download(cifFile, "cif/"+cifId+".cif")
#os.system("jmol cif/"+cifId+".cif")

file = open("scripts/"+cifId+".spt","w") 
file.write("load cif/"+cifId+".cif;\n")
#imgFilename = cifId+".png"
#file.write("select all;")
#file.write("label %a;")
file.write("set echo example 0% 5%;\n")
file.write("font echo 63 serif bold;\n") 
file.write("echo " +formula+ " ("+cifId+");\n" )

file.write('write IMAGE 842 595 PNG n "png";') 
file.close() 
os.system("jmol scripts/"+cifId+".spt &&")
os.system("convert png -negate  -threshold 80% output.bmp")
os.system("potrace --svg output.bmp -t 10 -a 3 -u 10 -P A4 --group -o vect.svg")

# call the plotter:
subprocess.check_output(['axibot', 'plot', 'vect.svg'])


