
lst=[]
val="raj"
lst.append(2)
lst.append(True)
lst.append(23)
lst.append(5)
lst.append(14)
lst.append(345)
lst.append(45)
lst.append("apple")
print(lst)
arr = ["one","two","three"]
arr_sec = ["sun","mon","tue","web","thu","fri","sat"]
lst.append("apple")
lst.append("orange")
lst.append(arr)
lst.append("pineapple")
lst.append("pomogranate")
lst.append("turnip")
lst.append("grapes")
lst.append(arr_sec)
print(lst)


lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in lst:
    if i<5:
        print(i)

    # if i<5:
    #    print(i)

import random
lst = [random.randint(1,10) for i in range(10)]
print(lst)
sort = sorted(lst)
print(sort)

newLst = []
lstFirst = [random.randint(1,10) for i in range(10)]
lstSecond = [random.randint(1,10) for i in range(10)]

for p,q in zip(lstFirst,lstSecond):
    newLst.append(p-q)
print(newLst)
    


