x=input("Enter Values: ").split(",")
x=set(map(int,x))
n=int(input("Enter Target Number: "))
new=set()

for i in x:
    num=n-i
    if num in new:
        print(i,",",num)
    new.add(i)