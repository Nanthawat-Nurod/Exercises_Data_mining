
def input_username(name) :
    print("Hello, " + name + "!")
def input_age(age) :
    print('You are ' +str(age) +' years old.')
    birth_year = 2024 - age
    print("You were born in the year " + str(birth_year) + ".")


name = input("Enter your name: ")
input_username(name)
age = int(input("Enter your age: "))
input_age(age)


