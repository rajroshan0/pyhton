P =[13, 2, 7, 21, 16, 16, 5, 13, 37]
Q= [14, 29, 23, 31, 26, 23, 7, 28, 72]
A= sorted(P)
B=sorted(Q)



normA = []
for i in P:
    normP = (i-min(A))/(max(A)-min(A))
   # print(round(normP,2))
    normA.append(round(normP,2))  #rounding off float after decimal

print("here is it normA",normA)



normB = []
for i in Q:
    normQ = (i-min(A))/(max(A)-min(A))
   # print(round(normP,2))
    normB.append(round(normQ,2))  #rounding off float after decimal

print("here is it normB",normB)

