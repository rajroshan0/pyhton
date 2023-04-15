P =[13, 2, 7, 21, 16, 16, 5, 13, 37]
Q= [14, 29, 23, 31, 26, 23, 7, 28, 72]
outlier= []




import numpy as np


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
                outlier.append(i)
                return("list of outliers", i,outlier)
            else:
                return("return check your code")
        
    else:
        for i in P:
            if i>= downCoeff:
                outlier.append(i)
                return(i,outlier)
            else:
                return("there is no outliers in the list")

        

print(outliersSigma())
    
    
    
    
