#Inputs
n=input("Enter Values: ").split(",")
#End

#Variables
nums=set(map(int,n))
max=0
num_list=list()
Final_set=set()
#End

#Proceder
for i in nums:
    if (i-1) in nums:
        continue
    else:
        num_list.append(i)
        j=i+1
        while (j) in nums:
            num_list.append(j)
            j=j+1
        num_tuple=tuple(num_list)
        Final_set.add(num_tuple)
        num_list.clear()       
#End

for i in Final_set:
    if len(i)>max:
        max=len(i)
        max_list=i
print(max)
print(max_list)