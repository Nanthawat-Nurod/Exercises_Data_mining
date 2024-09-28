course = 'Data Mining!'
print (course) # Prints complete string
print (course[0]) # Prints first character of the string
print (course[2:5]) # Prints characters starting from 3rd to 5th
print (course[2:]) # Prints string starting from 3rd character
print (course * 2) # Prints string two times
print (course + "TEST ") # Prints concatenated string


# list
print()
print('List')
exlist1 = ['abcd', 999 , 55.55, 'Jirapond', 83.25]
exlist2 = ['Hello' ,'my' , 'student']
print (exlist1) # Prints complete list
print (exlist1[0]) # Prints first element of the list
print (exlist1[1:3]) # Prints elements starting from 2nd till3rd (end-1 คือ 3-1=2)

print (exlist1[2:]) # Prints elements starting from 3rd element
print (exlist2 * 2) # Prints list two times
print (exlist1 + exlist2) # Prints concatenated lists

#(Operators)
#ตัวดําเนินการทางคณิตศาสตร- (Arithmetic Operators)
print()
print('Operators')
print('Arithmetic Operators')
x = 10
y = 3
print(x + y) # ผลลัพธ์ คือ 13
print(x - y) # ผลลัพธ์ คือ 7
print(x * y) # ผลลัพธ์ คือ 30
print(x / y) # ผลลัพธ์ คือ 3.3333333333333335
print(x % y) # ผลลัพธ์ คือ 1
print(x ** y) # ผลลัพธ์ คือ 1000
print(x // y) # ผลลัพธ์ คือ 3

#(Comparison Operators)
print()
print('Comparison Operators')
x = 10
y = 3
print(x == y) # ผลลัพธ์ที-ได้ คือ False
print(x != y) # ผลลัพธ์ที-ได้ คือ True
print(x > y) # ผลลัพธ์ที-ได้ คือ True
print(x < y) # ผลลัพธ์ที-ได้ คือ False
print(x >= y) # ผลลัพธ์ที-ได้ คือ True
print(x <= y) # ผลลัพธ์ที-ได้ คือ False

#(Assignment Operators)
print()
print('Assignment Operators')
x = 10
x += 5 # ผลลัพธ์เกิดจาก x = x + 5
print(x) # 15
x -= 3 # ผลลัพธ์เกิดจาก x = x - 3
print(x) # 12
x *= 2 # ผลลัพธ์เกิดจาก x = x * 2
print(x) # 24
x /= 4 # ผลลัพธ์เกิดจาก x = x / 4
print(x) # 6.0

#(Logical Operators)
print()
print('Logical Operators')
x = True
y = False
print(x and y) # False
print(x or y) # True
print(not x) # False

#(Bitwise Operators)
print()
print('Bitwise Operators')
x = 5 # 0101
y = 3 # 0011
print(x & y) # 0001 -> 1
print(x | y) # 0111 -> 7
print(x ^ y) # 0110 -> 6
print(~x) # 1010 -> -6
print(x << 2) # 010100 -> 20
print(x >> 2) # 0001 -> 1

#(Membership Operators)
print()
print('Membership Operators')
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits) # True
print("grape" not in fruits) # True

#(Identity Operators)
print()
print('Identity Operators')
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) # True
print(x is y) # False
print(x == y) # True
print(x is not y) # True

print()
print('6540011030 Nanthawat Nurod')