#!/bin/bash
# Runs the S and Z parameter feature on Scuff. Frequency in units of GHz
scuff-rf --geometry trap.scuffgeo --portfile trap.ports --frequency 0.02 --Cache trap.cache --Zparameters --Sparameters

