words=input("Enter the Words: ")
words2=input("Enter the Word: ")
if "".join(sorted(words))=="".join(sorted(words2)):
    print(True)
else:
    print(False)