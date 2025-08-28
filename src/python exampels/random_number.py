import random

list=['green','blue','blue','green','yellow']
print(set(list))

print(type(set(list)))

list_lengith= len(list)

num = random.randint(0, (len(list)-1))

print(f"the random number: {list[num]}")

x= lambda list : list
print(x(list))

def a(a,b):
     return a+b,a-b

c,b=a(5,3)
print(c,b)