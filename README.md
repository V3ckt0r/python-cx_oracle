######How to use this CGI

Simply configure your web server to serve start.py, this is a wrapper script that goes on to configure the system environment in setEnv.sh before starting the main oracle interaction in tablespace.py. 

This example code is just to demonstrate using cx_Oracle to connect to a Oracle database. In this example, once connected python runs an SQL query to get the table space size for all the tables within your database.

######example 
www.example.com/start.py

