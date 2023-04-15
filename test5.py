
P= [13, 2, 7, 21, 16, 16, 5, 13, 37]
Q=[14, 29, 23, 31, 26, 23, 7, 28, 72]
import math
def stats(P,Q):
    vol = len(P)
    summ_of_sampleP = sum(P)
    P_mean = summ_of_sampleP/vol
    m=(vol+1)/2
    a= int(m-1 ) #num start from 0 
    
    P_median = P[a]
    print("median of P", P_median)  
  
    stdevP = math.sqrt(sum((i-P_mean)**2 for i in P)/vol-1)
    
    print("the stdevP",stdevP)


    P_para = print( vol,summ_of_sampleP,P_mean)
    vol = len(Q)
    summ_of_sampleQ = sum(Q)
    Q_mean = summ_of_sampleQ/vol

    mq=(vol+1)/2
    b= int(mq-1 ) #num start from 0 
    
    Q_median = Q[b]

    print("median of q", Q_median)


    

    stdevQ = math.sqrt(sum((i- Q_mean)**2 for i in Q)/vol-1)
    
    print("the stdevQ",stdevQ)
    
    Q_para=print( vol,summ_of_sampleQ,Q_mean)
    return(vol,P_mean, Q_mean, P_median, Q_median, stdevP, stdevQ)
    
    

print(stats(P,Q))

stats_result = stats(P, Q)
vol, P_mean, Q_mean, P_median, Q_median, stdevP, stdevQ = stats_result

def symmMeasure(P_mean,P_median,stdevP):
    if (P_mean - P_median) <= 3*stdevP :
        return ("symmetric")
    else:
        return("non symmetric")
#print ("check symmetric",symmMeasure(P_mean,P_median,stdevP))
print("check symmetric", symmMeasure(P_mean, P_median, stdevP))




# correlation coefficient

def corrCoeff():
    corr = sum((i-P_mean)*(j-Q_mean)for i,j in zip(P,Q))/math.sqrt(sum((i-P_mean)**2 for i in P)*sum((j-Q_mean)**2 for j in Q))
    return corr
print("the correlation coefficient is",corrCoeff())
    
    






    
    #print(stdevP)

#print(corrCoeff())
    
    

    
