P =[13, 2, 7, 21, 16, 16, 5, 13, 37]
Q= [14, 29, 23, 31, 26, 23, 7, 28, 72]
outlier= []







from lab5 import symmMeasure,mean_sampleP,stdev_sampleP



upCoeff =mean_sampleP - 3*stdev_sampleP
print("outCoeff",upCoeff)

downCoeff = mean_sampleP + 3*stdev_sampleP
print("outCoeff",downCoeff)

a,b = upCoeff,downCoeff
print(a,b)



def outliersSigma():
    if symmMeasure == True:
        for i in P:
            if i<=upCoeff:
                return("its a outCOeff")
            else:
                return("return check your code")
        
    else:
        for i in P:
            if i>= upCoeff:
                outlier.append(i)
                return(i,outlier)

        

print(outliersSigma())




#outlier using quartiles

import numpy as np

Q1 = np.percentile(P,25)
print("first quartile", Q1)


Q2 = np.percentile(P,50)
print("inter 2nd quartile", Q2)


Q3 = np.percentile(P,75)
print("third quartile", Q3)


lowerFence = Q1-1.5*(Q3-Q1)

upperFence = Q1+1.5*(Q3-Q1)

print("lowerFence , upperFence", lowerFence , upperFence)


def outlierQuartile():
    if symmMeasure == True:
        for i in P:
            if i<=lowerFence:
                return("its a outCOeff")
            else:
                return("return check your code")
        
    else:
        for i in P:
            if i>= upperFence:
                outlier.append(i)
                return(i,outlier)

        

print(outliersSigma())
print(outlierQuartile())





    
    
    
