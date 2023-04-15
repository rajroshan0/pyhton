raj = "i love {}".format("mango")
print(raj)
var = "{} is my girlfriend"
print(var.format("rita"))
      #pair of curely bracket
varr = "i have {}"
print(varr.format("3 pencil"))
fruits = "there are {} and {} in the bucket"
print(fruits.format("apple","orange"));

#several bracket
my_str = "I love {}, {} and have {} dogs"
print(my_str.format("cat","dog", 3))


print("my friend {} has a pet {}!".format("sam","german buffet"))

#tuples can be called with index
print("my friend {0} has a pet {1}!".format("sam","german buffet"))
print("my friend {1} has a pet {0}!".format("sam","german buffet"))

#position arguments with name
print("Tom {0} an {var}.".format("has","made",var ="car"))
print("Tom {1} an {var}.".format("has","made",var ="car"))

#using codes with data types
print("sam ate {0:f} percent of a {1}!".format(75, "melon")) #don't forget .after: to add decimal(0:.2f) 
print("sam ate {0:.4f} percent of a {1}!".format(75.73648364, "melon"))
print("sam ate {0:.1f} percent of a {1}!".format(75.723648364, "melon"))
print("sam ate {0:.0f} percent of a {1}!".format(75.723648364, "melon"))


#visuall organize large amount of data
print ("I have {0:4} red {1:10}!".format(5,"apple"))

#aligning the objects to right left and center <- ^- >-

print("sam ate {0:<24} percent of a {1:^14}!".format(75.723648364, "melon"))
print("sarojni ate {0} percent of a {1}!".format(75.723648364, "melon"))
print("sarojni ate {0:} percent of a {1:>14}!".format(75.723648364, "melon"))



#creating table using str.format
num = "|{0:^10}|".format("Number")
col ="{0:^20}|".format("Color")
food = "{0:^20}|".format("Food")
print("-"*56)
print(num , col, food)

aum = "|{0:^10}|".format("")
aol ="{0:^20}|".format("")
aood = "{0:^9}| {1:^9}|".format("Fruits", "vegs")
print(aum , aol, aood)
print("-"*56)
print("|{0:^10}|{1:^21}|{2:^10}|{3:^10}|".format(1,"green","apple"," "))
print("-"*56)
print("|{0:^10}|{1:^21}|{2:^10}|{3:^10}|".format(2,"red","","rajroshan "))
print("-"*56)








