#Calcuator
"""
run = True
while run:
  total = input("Enter a number: ")
  if total.isdigit():
    total = int(total)
    run = False
  else:
    print("Invalid input")

run = True

while run:
  no = input("Enter a number(q to quit): ")
  if no.isdigit():
    oprt = input("Enter the operation you want to perform(+ - * /): ")

    if oprt in ["+","-","*","/"]:
      if oprt == "+":
        total += int(no)
      elif oprt == "-":
        total -= int(no)
      elif oprt == "*":
        total *= int(no)
      elif oprt == "/":
        total /= int(no)
      print(f"Total: {total}")
    else:
      print("Invalid input")
  elif no.lower() == "q":
    run = False
  else:
    print("Invalid input")
"""

import random

#Number Guessing Game
"""
numb = random.randint(1,99)
print("-------Welcome to Number Guessing Game-------")
print("You have to gues a no. between 0 to 100")
print("and you will get 10 tries to guess the no.")
print()
for i in range(0,10):
  guess = input("Enter your no. here: ")

  while not (guess.isdigit() and 0< int(guess) <100):
    if not guess.isdigit():
      print(f'"{guess}" is not a no.')
    elif not 0< int(guess) <100:
      print("no. should be between 0 to 100")
    guess = input("Enter your no. here: ")

  guess = int(guess)
  x = guess - numb

  if guess == numb:
    print("Congratulations, you have guessed the correct no.!!!!")
    break

  elif x > 0:
    if x < 4:
      print("Try for just a little smaller no.")
    elif x < 11:
      print("Try for a smaller no.")
    else:
      print("Too high")

  elif x < 0:
    if x > -4:
      print("Try for just a little bigger no.")
    elif x > -11:
      print("Try for a bigger no.")
    else:
      print("Too low")
  print(f"You have {9 - i} tries left.")
"""

#Todo List
"""
tasks = []

def Add():
    task = input("Enter the task: ")
    tasks.append(task)

def View():
    if not tasks:
        print("No tasks to show.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def Delete():
    if not tasks:
        print("No tasks to delete.")
        return

    View()
    numb = input("Enter the number of the task you want to delete: ")
    
    if numb.isdigit():
        numb = int(numb)
        if 1 <= numb <= len(tasks):
            removed = tasks.pop(numb - 1)
            print(f"Deleted: {removed}")
        else:
            print("Number out of range.")
    else:
        print("Please enter a valid number.")

while True:
    print("\n--- To-Do List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    c = input("Choose an option (1-4): ").strip()
    
    while not (c.isdigit() and 1 <= int(c) <= 4):
        print("Invalid input. Please enter a number between 1 and 4.")
        c = input("Choose an option (1-4): ").strip()

    if c == "1":
        Add()
    elif c == "2":
        View()
    elif c == "3":
        Delete()
    elif c == "4":
        break

print("Goodbye 👋👋")
"""

