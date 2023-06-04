'''
this description lambda
'''

def test(x,y):
    return x + y
print(test(1,2))

# square in lambda
x = lambda x : x * 2
print(x(3))


a=[1,2,3,4]
b=[item for item in a if item % 2 ==0]
print(b)