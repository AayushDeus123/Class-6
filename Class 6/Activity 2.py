#NOT EQUAL and EQUAL operator usind OR
a = 5
b = 10
c = 15
if a != b or b == c:
    print('The above statement is true')
else:
    print('The above statement if false')
    
#NOT EQUAL and EQUAL operator using AND
if a != b and b == c:
    print('The above statement is true')
else:
    print('The above statement is false')
    
#NOT EQUAL and EQUAL operator using AND and OR
if a != b and b==c or a!=b:
    print('The above statement is true')
else:
    print('The above statement is false')