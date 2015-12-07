#!/usr/bin/python2.6

# The CGI module includes various different library to streamline CGI scripting for different mechanisms of interaction.
import cgi
import os
from time import gmtime, strftime
import time

# The CGITB module is a traceback manager for CGI scripts. This allows debugging from the web tier.
# envoked via cgitb.enable()
import cgitb
cgitb.enable()
start = time.time()

# This module provides the various methods needed to communicate with the DB.
import cx_Oracle
host = 'example.co.uk'
sid = 'DBSID'
username = 'DBUser'
#password = 'Tr1pSt1ckT1ck'
password = 'Your-password'

#print strftime("%Y-%m-%d %H:%M:%S", gmtime())

print "Content-type: text/html\n\n"
print "<html>"
print "<head>"

# link the css file
print '<link type="test/css" rel="stylesheet" href="/stylesheet.css" />'

# This is an example of inline styling
#print "<style>"
#print "body {background-color:lightblue}"
#print "</style>"

print "<title>This is a CGI scripts for tablespace in SITST</title>"
#print "<h1>Tablespace in SITST"</h1>"
print "</head>"
print "<body>"
print "<p><b> Tablespace in " + sid + "</b>"

#use this to test that python is seeing the correct path
#print os.environ.get('ORACLE_HOME')

# Creates a connection to the DB
con = cx_Oracle.connect('DBUser/Your-password@example.com/DBSID')
cur = con.cursor()

query = "SELECT * FROM (SELECT OWNER, SEGMENT_NAME, BYTES/1024/1024 SIZE_MB FROM DBA_SEGMENTS WHERE SEGMENT_TYPE = 'TABLE' ORDER BY BYTES/1024/1024  DESC ) WHERE ROWNUM <= 50"

# executes a sql query
cur.execute(query)
#cur.execute('Select * from v$version')

# prints each row retrieved from DB
set = []
# for loop adds each row into an array
for result in cur:
 # print result
 # print "<br>"
 # print "<br>"
 set += result


#contains an array of tablenames
tablenames = set[1::3]

# The below grabs the every 3rd column (disk size) of each table
sizes = set[2::3]

# Since the query variable sorts the results with the highest first the 0 index contains the biggest table.
highest = sizes[0]
print "<br>"

total = 0
# add each item in the array to make a total
for size in sizes:
  total += size

print "<p> This is the total amoungst these tables ", total, "MB"
print "<br><br><br>"

#prints each table name alsong with the percent usuage of that table
count = 0
for size in sizes:
  percentage = float(size) / float(total)
  percent = percentage * 100
  print tablenames[count]," is taking up", '<span style="color:red;display:inline">', sizes[count], '</span>', "MB which is ", ("%.4f" % percent), "% of the total these tables are taking."
  #print float(size) / float(total)
  count += 1
  print "<br><br>"


print 'This script took', time.time() - start, 'seconds to complete.'
print "</body>"
print "</html>"

# closes db connection
cur.close()
con.close()
