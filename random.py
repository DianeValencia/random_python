print ("Hello Github")

name = "Diane Angeline M. Valencia"
birthday = "May 19, 2003"
age = 22
#integers = whole numbers; float = decimals
is_CS_student = True
#boolean value = True or False

print(name)
print(birthday)
print(age)
print(is_CS_student)

print("\n===Other ways===\n")

print("Name: ", name)
print("Birthday: ", birthday)
print("Age: ", age)
print("Computer Science student? ", is_CS_student)

print("\n===Other ways===\n")
print("\n===Input Function===\n")

my_name = input("How should I call you?")
print("Wecome to my program, " + my_name + "! Nice to meet you!")


print("\n = = = OPERATIONS = = = \n")
a = 5
b = 19

print(a + b)    # 13 (addition)
print(a - b)    # 7 (subtraction)
print(a * b)    # 30 (multiplication)
print(a / b)    # 3.333... (division, returns float)
print(a // b)   # 3 (floor division, drops decimal part)
print(b % a)    # 3 (modulo, remainder when b is divided by a)
print(a ** b)   # 1000 (exponentiation, 10 to the power of 3)

print("\n OTHER \n")
age1 = int(input("Enter your age: "))

if age1 >= 18:
  print("Congrats! You're old with the weight of life's responsibilities now!")
elif  age1 >= 13:
  print("Enjoy your remaining happy days")
else:
  print("What are you doing here?")


print()
print()
print()

print("\n LOOP \n")

count = 0
while count <5:
  print("Count is: ", count)
  count += 1

      

