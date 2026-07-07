words=input("Enter the Words: ").split(",")

new=dict()

for i in words:
    new[''.join(sorted(i))]=new.get(''.join(sorted(i)),[])+[i]

for i in new.values():
    print(i)