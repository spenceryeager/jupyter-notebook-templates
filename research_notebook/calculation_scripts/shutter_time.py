highV = 0.8 #V
lowV = -0.4 #V
deltaV = highV - lowV
v = 0.05 # V/s

time = deltaV / v # getting run time

print(str(round(time, 4))+' seconds')