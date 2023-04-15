my_lst = [True,"ram",783, "raj","roshan",-33,3.09]
other_lst = [123,"rajroshan"]

print(my_lst)
print(my_lst[0])
print(my_lst[4])
print(my_lst[1:4])
print(my_lst[3:7])
print(other_lst[2: ])
print(other_lst *5)
print("this is addition of two lsl",my_lst + other_lst)


#using append()

lst=[]
raj = [43,"x"]
lst.append("a")
lst.append(raj)
lst.append("rajroshan")
lst.append(True)

print(lst)


#tuple

my_tuple = (False,"rajroshan",343,"life",24,-232.23)
other_tuple= (124,"eveing")

print(my_tuple)
print(my_tuple[1])
print(my_tuple[1:3])
print(my_tuple * 2)
print(my_tuple + other_tuple)


#differences of tuple and list
details = ["voronezh",23,["eggs","potatoes"],True,29993,2.32]
my_tuple = ("voronezh",23,["eggs","potatoes"],True,29993,2.32)

details[0] = "rajroshan"
#my_tuple[0] = "rajroshan"   tuples can't be changed

print(details)
#print("my tuples file",my_tuple)


#searching tuple and lst

fruits = ["mango","banana","apple","ornage","pineapple"]

if "mango" in fruits:
    print("I got mango")
else:
    print("mango is not avilable")


#loops

word = "kathmandu nepal"

kitchen = ["knife","cuttingpad","vegetables","fruits","glass"]

for i in word:
    print(i)
for i in kitchen:
    print(i)

#Otherways

weekDays = ["sun","mon","tue","wed","thu","fri","sat"]
for i in range(len(weekDays)):
    print(weekDays[i])

for i in range(2,5):
    print(weekDays[i])

for num in range(2,22):
    print(num)


#python generator
hrs = [x for x in range(23,43)]
print(hrs)

#sequence for random

from random import randint

sample = [randint(1,10) for i in range(10)]
print (sample)

sound = "hummingbird"

new_lst = [word for word in sound]
print (new_lst)  

#zip
lst=[]
A = [2,34,142]
B = [4,43,113]

for p,q in zip(A,B):
    lst.append(p-q)
print(lst)

#max and min
A = [randint(1,893) for i in range(10)]
print(A)
maximum = max(A)
print(maximum)
minimum = min(A)
print(minimum)
    
    
    
    



    


      
