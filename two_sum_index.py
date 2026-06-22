x=input("Enter Values: ").split(",")
x=list(map(int,x))
n=int(input("Enter Target Number: "))
new=dict()
count=-1

for i in x:
    count+=1
    num=n-i
    if num in new:
        print(count,",",new.get(num))
    new[i]=count