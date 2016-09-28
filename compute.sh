#!/bin/bash
# Runs Scuff and compiles the epfiles

#find . -name '*.epfile*' -exec echo {}; ls \;
export OMP_NUM_THREADS="8"
export GOMP_CPU_AFFINITY="0-7"
export SCUFF_INTERPOLATION_TOLERANCE=1.0e-3
export SCUFF_LOGLEVEL="NONE"

for i in *.epfile*; 
do 
echo "Running file: $i";
scuff-rf --geometry trap.scuffgeo --portfile trap.ports --portcurrentfile trap.portcurrents --EPFile "$i" --Cache trap.cache
done
cat *.field* > input.csv
