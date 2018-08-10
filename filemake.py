import os
import sys

MAXSMALL =  26214400
MAXMED = 52428800
MAXLARGE = 104857600

count = 0
with open('filesS.dat','w') as fn:
    count = 0
    while count < MAXSMALL:
        fn.write('A')
        count = count + 1

count = 0
with open('filesM.dat','w') as fn:
    count = 0
    while count < MAXMED:
        fn.write('A')
        count = count + 1


count = 0
with open('filesL.dat','w') as fn:
    count = 0
    while count < MAXLARGE:
        fn.write('A')
        count = count + 1
