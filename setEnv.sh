#!/bin/sh

LD_LIBRARY_PATH=/u01/siapp/vision/test/uniface/lib:/u01/app/oracle/product/11.2.0/client_1/lib:/usr/lib64

ORACLE_SID=SITST

ORACLE_HOME=/u01/app/oracle/product/11.2.0/client_1

PATH=$PATH:$ORACLE_HOME/bin

export LD_LIBRARY_PATH
export ORACLE_HOME
export PATH

python tablespace.py

