
import math
import random
normalized_sample=[]
def normalization(sample):
    for i in sample:
        norm_Sample = (i-min(sample))/(max(sample)-min(sample))
        normalized_sample.append(round(norm_Sample,2))
    return(normalized_sample)
  
sample = [random.randint(11,45) for i in range(50)]

print(normalization(sample))







