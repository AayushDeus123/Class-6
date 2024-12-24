#Checking if user input is an alphabet or not
a = input("Enter a single character: ")
if a.isalpha() and len(a) == 1:
    print(a, 'is an alphabet.')
else:
    print(a, 'is not an alphabet.')