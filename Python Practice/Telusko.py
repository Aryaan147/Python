'''
for i in range(1,5):
  for j in range(1,i+1):
    print(chr(j + 64), end=" ")
  for k in range(i,4):
    print(chr(k + 79), end=" ")
  print()
'''

'''x = int(input())
for i in range(2,x**2):
 if x%i == 0 :
  print("not prime")
  break
else:
 print("prime no.")

from array import *
'''

'''
vals = array('i', [4,3,6,8,9,2,7,1,5])

arr = array(vals.typecode, (a*a for a in vals))

for i in arr:
 print(i, end=" ")
'''

'''
arr = array('i', [5,7,3,1,5,7,9,8,4,3,2,1])
ascarr = sorted(arr)
print(ascarr)
dscarr = sorted(arr,reverse=True)
print(dscarr)
'''
import math as m

'''
num = int(input("No.- "))
print(m.factorial(num))
'''
from numpy import *
'''
arr = array([[1, 2, 3], [4, 5, 6]])
print(arr)
'''


'''
arr = linspace(1,12,10)
print(arr)

arr = logspace(0,9,6)
print('%.2f' %arr[2]) #to get the specific output in integer
arr = arr.astype(int) #to get all the outputs in integer
print(arr)

arr = arange(0,10,2)
print(arr)

arr = zeros(5,int)
# arr = ones(5,int)
print(arr)
'''

'''
arr1 = array([1,2,3,4])
arr2 = arr1 + 5
arr3 = arr1 + arr2
print(arr3)
print(sin(arr3))
print(log(arr3))
print(sqrt(arr3))
print(sum(arr3))
print(max(arr3))
print(min(arr3))
print(concatenate([arr1,arr2,arr3]))

arr1 = arr2 #assignment
print(id(arr1))
print(id(arr2)) #addres(id) is same as arr1
print(id(arr3))
arr1[0] = 2
print(arr1) #same values
print(arr2)

arr2 = arr1.view() #shallow copy
print(id(arr1))
print(id(arr2)) #now addreses of arr1 and arr2 is diff
arr1[0] = 2
print(arr1) #but values of both the arrays are same
print(arr2)

arr1 = arr2.copy() #deep copy
print(id(arr1))
print(id(arr2)) #here addreses of arr1 and arr2 are also is diff
arr1[0] = 5
print(arr1) #and the values are also diff
print(arr2)
'''

'''
arr1 = array([1,2,3,4,5])
arr2 = array([3,4,5,6,7])
for i in range(len(arr1)) :
 print(arr1[i]+arr2[i])


arr = [1, 7, 3, 9, 5]

max_value = arr[0]  # Assume the first element is the max

for i in arr:
    if i > max_value:
        max_value = i

print("Maximum value is:", max_value)
'''


'''
arr1 = array([

  [1,2,3,4,2,7],
  [5,6,7,3,1,6],
])

# print(arr1.dtype)
# print(arr1.ndim)
# print(arr1.shape)
# print(arr1.size)

arr2 = arr1.flatten()
# print(arr2)

arr3 = arr2.reshape(3,4)
print(arr3)

print()

arr4 = arr2.reshape(2,2,3)
print(arr4)
'''

'''
arr = array([
  [1,2,3,4],
  [5,6,7,8]
])
arr = arr
m1 = matrix(arr)

m2 = matrix('1 2 3 4; 5 6 7 8').transpose()
# print(m2)
# print(diagonal(m2))
# print(m2.max())


m = m1 * m2

print(m)
'''
 
'''
def greet():
 print("Hey!")
 print("Good Morning")
greet()

def add(x,y):
  c = x+y
  print(c)
add(4,5)

def add_sub(x,y):
  c = x+y
  d = x-y
  return c, d #return does not give any output but instead it stores the value so i can use it in anyway i want
# result = add_sub(6,7)
# print(result)
result1, result2 = add_sub(6,7)
print(result1,  result2) 
'''

'''
def update(x):
  print("a2", id(a))

  x[0] = 5
  print("val2",x)
  print("a3", id(a))

a =[10, 20, 30]
print("a1",id(a))
print("val1",a)
update(a)
print("val3", a)
'''
'''
# def person(name, age):
#   print("Name:", name)
#   print("Age:", age)
# person(age=18, name="Aryan")

def sum(a,*b):
  c= a
  for i in b:
    c= c + i
  print(c)

sum(1,2,3,4,5,6,7,8)
'''

'''
# def person(name, *data):
#   print(name)
#   for i in data:
#     print(i)

# person('aryan', 18, 'abohar')

#OR

def person(name, **data):
  print(name)
  for i,j in data.items():
    print(i,j)

person('aryan', age=18, city='abohar')
'''

# a = 10 #Global
# def something():
#   global a #by using this the value which was supposed to be changed Localy, now can be changed Gloabaly (it let you access it globaly)
#   a = 5 #Local
#   print("inner", a)

# something()
# print("outer", a)

#Changing the Value of Global a without effecting Local a
a = 10 
def something():
  a = 5
  x = globals()['a']
  globals()['a'] = 15
  print("inner", a)

something()
print("outer", a)































