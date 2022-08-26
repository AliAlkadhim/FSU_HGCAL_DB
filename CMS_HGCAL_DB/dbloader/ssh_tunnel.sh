#!/bin/bash
ssh -fN -L 10131:itrac1609-v.cern.ch:10121 -L 10132:itrac1601-v.cern.ch:10121 aalkadhi@lxplus.cern.ch

#then the dbloader command is scp <file.xml> <user>@dbloader-hgcal.cern.ch:/home/dbspool/spool/hgc/int2r
