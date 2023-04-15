sampleP =[13, 2, 7, 21, 16, 16, 5, 13, 37]
sampleQ= [14, 29, 23, 31, 26, 23, 7, 28, 72]

import statistics as st
mean_sampleP = st.mean(sampleP)
print(mean_sampleP)
mean_sampleQ = st.mean(sampleP)
print(mean_sampleQ)

median_sampleP = st.median(sampleP)
print(median_sampleP)
median_sampleQ = st.median(sampleQ)
print(median_sampleQ)

stdev_sampleP = st.stdev(sampleP)
print(stdev_sampleP)
stdev_sampleQ = st.stdev(sampleQ)
print(stdev_sampleQ)


def symmMeasure():
    mean = mean_sampleP
    median= median_sampleP
    stdev = stdev_sampleP

    if (mean - median)<=(3*(stdev**2)/2):
        print (True)
    else:
        print(False)

print(symmMeasure())

def symmMeasure():
    mean = mean_sampleQ
    median= median_sampleQ
    stdev = stdev_sampleQ

    if (mean - median)<=(3*(stdev**2)/2):
        print (True)
    else:
        print(False)

print(symmMeasure())

import numpy as np

corrCoeffPQ = np.corrcoef(sampleP,sampleQ) [0,1]
print(corrCoeffPQ)







        


