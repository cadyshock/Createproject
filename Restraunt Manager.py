# Cady Shock
# CSCI 101- Section A
# Create Project

# A python program that can keep track of seating at a restraunt

import random
random.seed()
from collections import Counter

hours=6
count=0
tables=12

def arrive():
    arrive=0
    arriving=[]
    arrive=random.randint(1, tables)
    for i in range(arrive):
        x=random.randint(1, 8)
        arriving.append(x)
    return Counter(arriving)
    


while hours*4 > count:
    if count % 4 == 0:
        # This code will make customers arrive every hour.
        arr=arrive()
        for key, val in arr.items():
            print ('Table Size:',key,'| Number of Tables:', val)
    count=count+1
