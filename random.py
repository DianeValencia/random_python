#NOTES FROM UDEMY COURSE: PYTHON MASTERY: 100 DAYS, 100 PROJECTS

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

      
print("\n FOR LOOP \n")

my_games = ["Valorant", "Overcooked", "It Takes Two"]
for game in my_games:
  print(game)

print("\n LIST \n")

print(my_games[0])
print(my_games[2])
print(my_games[1])

#append means add to the list
my_games.append("Flappy Bird")
print(my_games)

my_games[3] = "Candy Crush"
print(my_games)

print("\n FUNCTIONS \n")

def greet(temp_name):
    print("Hello, " + temp_name + " This is a practice!")

greet("Dee!")
greet("Diane!")
greet("Angeline!")

def multiply(a, b):
    return a * b

result = multiply(5, 19)
print(result)
print("Result is ", result)


print()
print()
print("\n Mini Project: Number Guessing Game \n")

import random 

secret_num = random.randint(1,10)#randint means random integer
attempts = 5

print("What number I am thinking between 1-10?")

while attempts > 0:
    guess = int(input("Take a Guess: "))
    if guess == secret_num:
        print("You read my mind!")
    elif guess < secret_num:
        print("Nah. Try higher.")
    else:
        print("Hmm... Try lower.")
    attempts -= 1

if attempts == 0:
    print("That was a good try! But you can't guess anymore.")
    print("For your peace of mind, the secret number was " + str(secret_num) + "!")


# === DAY 1 - 10 NOTES ===
name2 = input("How should I call you? ")
interest = input("What are you currently interested in?")

print(f"Hi, {name2}! I'm also interested to learn about {interest}!") 

# Let user input two numbers
first_num = int(input("Enter First Number: "))
second_num = int(input("Enter Second Number: "))

addition = first_num + second_num
subtraction = first_num - second_num
multiplication = first_num * second_num
division = first_num / second_num  # Note: result will still be float

print("\nThe Results:")
print(f"Addition: {first_num} + {second_num} = {addition}")
print(f"Subtraction: {first_num} - {second_num} = {subtraction}")
print(f"Multiplication: {first_num} * {second_num} = {multiplication}")
print(f"Division: {first_num} / {second_num} = {division}")


print("\n OTHER \n")

import time

#1: asking user from what number to coundown
start = int(input("Enter the number to start the countdown from: "))

#2: application using while loop
print("Starting countdown...")
while start >0:
  print(start)
  time.sleep(1)
  start -= 1

print("Your time is up! Move!")

print()
print()

import random

print("\n QUIZ \n")


# This is Math quiz game (NO CALCULUS!)

# Step 1. define math question function

def generate_question():
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        answer = number1 + number2
    elif operator == '-':
        answer = number1 - number2
    else:
        answer = number1 * number2

    return f"{number1} {operator} {number2}", answer

def math_quiz():
    score = 0
    rounds = 5

    print("Let's solve some math problems!")

    for i in range(rounds):
        question, correct_answer = generate_question()
        print(f"\nQuestion {i + 1}: {question}")
        user_mathanswer = int(input("Your answer: "))

        if user_mathanswer == correct_answer:
            print("You're right!")
            score += 1
        else:
            print("Nice try! The correct answer was", correct_answer)

    print("Quiz is finished!")
    print(f"You final score is: {score}/{rounds}")

    if score == rounds:
        print("You did well! You got everything right!")
    elif score >= 3:
        print("You almost got everything right!")
    else:
        print("Keep learning! You will get better too!")

math_quiz()


print()
print()
print()
# Shopping List Program with View, Add, Remove, Clear

shopping_list = []

def view_list():
    if shopping_list:
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("\nYour shopping list is empty.")

def add_item():
    item = input("Enter item to add: ")
    shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list.")

def remove_item():
    view_list()
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' not found in your shopping list.")

def clear_list():
    shopping_list.clear()
    print("Your shopping list has been cleared.")

def main():
    while True:
        print("\n=== Shopping List Menu ===")
        print("1. View List")
        print("2. Add Item")
        print("3. Remove Item")
        print("4. Clear List")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            view_list()
        elif choice == '2':
            add_item()
        elif choice == '3':
            remove_item()
        elif choice == '4':
            clear_list()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")

main()

