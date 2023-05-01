#creating tuples 
names = ("hatim", "maha", "zakaria") # we have create a tuple 
print(len(names)) # determine how many items in a tuples
ones = ("mehdi",) # we have create one item tuple
#to make a modification, we can convert tuple to list then make it back
# we have problem to use list() method cause i have list variable upper
#so i use seconde method
names_list=[]
for i in names: 
    names_list.append(i)
names_list.append("mehdi") 
names_list.sort(key = str.lower)
names= tuple(names_list) # back to tuples
print("this list of names \n:", names)
#to add tuple to tuple 
new_name = ("shaherazad",)
names +=new_name
names_list=[]
for i in names: 
    names_list.append(i)
names_list.sort(key = str.lower)
names= tuple(names_list) # back to tuples
print(names)
#remove element from tuple, can not be directly 
#first method : using slicing
new_names = names[1:]
print("after removing the first name: \n", new_names)
#seconde method: using filtering
new_names= tuple(x for x in names if x!="zakaria")
print("after removing a name: \n", new_names)
#third method: convert to list then back to tuple
names_list=[]
for i in names: 
    names_list.append(i)
names_list.remove("mehdi")
names=tuple(names_list)
print("after removing a name: \n", names)
#packing tuple
(a, b, c, d)=names #number of variables must match the number of values in tuple
print("this name of the first element in list :",a)
print("this name of the last element in list :",d)
(a,b,*c)= names #* to assign a list c inside the tuple
print("this a list of names : ",c)

