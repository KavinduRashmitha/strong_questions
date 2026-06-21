text_1=input("Enter the first Word: ")
text_2=input("Enter the second Word: ")

new_1=dict()
new_2=dict()

for i in text_1:
    new_1[i]=new_1.get(i,0)+1
for i in text_2:
    new_2[i]=new_2.get(i,0)+1

if new_1==new_2:
    is_anagrame=True
else:
    is_anagrame=False

print(is_anagrame)