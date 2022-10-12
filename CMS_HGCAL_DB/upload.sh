#!/bin/bash
#first kill process on port 10131
lsof -ti:10131 | xargs kill -9
ssh -fNL 10131:itrac1609-v.cern.ch:10121 -L 10132:itrac1601-v.cern.ch:10121 aalkadhi@lxplus.cern.ch
#scp $1 aalkadhi@dbloader-hgcal.cern.ch:/home/dbspool/spool/hgc/int2r
