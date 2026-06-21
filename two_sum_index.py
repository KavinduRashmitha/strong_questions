x=input("Enter Values: ").split(",")
x=list(map(int,x))
y=set(x)
n=int(input("Enter Target Number: "))
new=dict()

for i in x:
    num=n-i
    if num in y and x.index(num) in new.values():
        print(new[num],x.index(i))
    new[i]=x.index(i)