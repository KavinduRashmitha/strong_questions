nums=input("Enter Values: ").split(",")
nums=list(map(int,nums))
n=int(input("Enter Target Number: "))

left=nums[0]
right=nums[-1]
available=False

while len(nums)>1:
    count=len(nums)//2
    if n==nums[count]:
        available=True
        break
    elif n>nums[count]:
        nums=nums[count:]
    else:
        nums=nums[:count]
if n==nums[0]:
    available=True
print(available)