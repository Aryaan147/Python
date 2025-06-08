#project 2: Calculator
"""
operator = input("enter an operatpr(+ - * /): ")
num1 = float(input("enter a no.: "))
num2 = float(input("enter another no.: "))

if operator == "+":
 print(round((num1 + num2),4))
elif operator == "-":
 print(round((num1 - num2),4))
elif operator == "*":
 print(round((num1 * num2),4))
elif operator == "/":
 print(round((num1 / num2),4))
else:
 print(f"{operator} is not a valide operator")
"""

#project 3: Weight Conversion(Kg,Lbs)
"""
to = input("What do you want to convert from(Kg or Lbs): ")
if to not in ["Kg", "Lbs"]:
  print("Invalid unite")
elif to == "Kg":
  value=float(input("Enter the Weight(in Lbs): "))
  value = round(value*2.20462,3)
  print(f"{value}Kg")
elif to == "Lbs":
  value=float(input("Enter the Weight(in Kg): "))
  value = round(value/2.20462,3)
  print(f"{value}Lbs")
"""

#project 4: Tempertaure Conversion(C,F,K)
"""
unit = input("What do you want to convert from(C,F,K): ")

if unit not in ["C","F","K"]:
  print(f"{unit} is Invalid")

elif unit == "C":
  unit = input("what do you wanna convert into(F or K): ")
  
  if unit not in ["F","K"]:
    print(f"{unit} is Invalid")
  elif unit == "F":
    temp=float(input("Enter the Temprature: "))
    temp= (temp * 9/5) + 32
    print(f"{temp}°F")
  elif unit == "K":
    temp=float(input("Enter the Temprature: "))
    temp= temp + 273.15
    print(f"{temp}K")
  
elif unit == "F":
  unit = input("what do you wanna convert into(C or K): ")
  
  if unit not in ["C","K"]:
    print(f"{unit} is Invalid")
  elif unit == "C":
    temp=float(input("Enter the Temprature: "))
    temp= (temp - 32) * 5/9 
    print(f"{temp}°C")
  elif unit == "K":
    temp=float(input("Enter the Temprature: "))
    temp= (temp - 32) * 5/9 + 273.15
    print(f"{temp}K")

elif unit == "K":
  unit = input("what do you wanna convert into(C or F): ")
  
  if unit not in ["C","F"]:
    print(f"{unit} is Invalid")
  elif unit == "C":
    temp=float(input("Enter the Temprature: "))
    temp= temp - 273.15  
    print(f"{temp}°C")
  elif unit == "F":
    temp=float(input("Enter the Temprature: "))
    temp= ((temp - 273.15) * 9/5) + 32
    print(f"{temp}°F")
"""

#Exercise(1:35:30):
"""
usnm=input("Enter your username: ")
name = usnm.isalpha()
if len(usnm)<=12 and name:
  print(f"Hi! {usnm}")
else:
  print("Invalide Username")
"""

#project 5: Compound intrest calculator
"""
principle = 0
rate = 0
time = 0

while principle <= 0 :
  principle = float(input("Enter your Principle Amount: "))
  if principle <= 0:
    print("Invalid input")

while rate <= 0 :
  rate = float(input("Enter your Rate of Intrest: "))
  if rate <= 0:
    print("Invalid input")

while time <= 0 :
  time = float(input("Enter Time period(in years): "))
  if time <= 0:
    print("Invalid input")

total = round(principle* (1+ rate/100)**time,2)
print(f"The total amount is: ${total}")
"""

#project 6: Countdown Timer programe
import time
"""
times = int(input("Enter Time in seconds: "))
for x in range(times,0,-1):
  seconds = x%60
  minutes = int(x/60) % 60
  hours = int(x/3600) % 24
  print(f"{hours}:{minutes}:{seconds}")
  time.sleep(1)
print("TIMES UP!")
"""

#project 7: shopping cart program
"""
foods = []
prices = []
total = 0.0
while True :
 food = input("Enter your food name(q to Quit): ")
 if food.lower() == "q":
  break
 else:
  price = float(input(f"Enter the price of the {food}: $"))
  foods.append(food)
  prices.append(price)
print("------YOUR CART-----")
for food in foods:
 print(food)

for price in prices:
 total += price

print(f"Total price is: ${total}")
"""

#project 8 : quiz game
"""
questions = ["What is the capital of India?",
             "What is 10 + 5?",
             "Which animal is known as The King of Jungle?",
             "What colour do yo get wehn you mix red and blue?",
             "What is the tallest mountain in the world?"]

options = [["A. Mumbai", "B. Delhi","C. Chennai","D. Kolkata"],
           ["A. 12", "B. 15","C. 16","D. 20"],
           ["A. Tiger", "B. Elephant","C. Lion","D. Cheetah"],
           ["A. Green", "B. Yellow","C. Purple","D.Orange"],
           ["A. Mount Kilimanjaro", "B. Mount Everest","C. Mount Fuji","D. Mount McKinley"]]

score = 0
ans = ["B","B","C","C","B"]
question_num = 0
guesses = []

for question in questions:
  print(question)
  for option in options[question_num]:
    print(option)
  print("------------------------------------------------")
  guess = input("Answer(A/B/C/D): ").capitalize()
  guesses.append(guess)
  if guess == ans[question_num]:
    print("Correct answer!")
    score += 1
  else:
    print("Incorrect answer")
    print(f"Correct answer is {ans[question_num]}")

  question_num += 1

print("----------------------------RESULT----------------------------")
print("Correct Answers: ",end="")
for x in ans:
  print(x,end=(" "))
print()
print("Your Answers: ",end="")
for x in guesses:
  print(x,end=(" "))
print()
print(f"Total score: {score}/5")
"""

#project 9: conssesion stand program
"""
menu = {"popcorn": 50,
        "soda": 40,
        "nachos": 30,
        "pizza": 210,
        "burger": 150,
        "sandwich": 120,
        "icecream": 40}

cart = []
total = 0
print("--------MENU--------")
for key, value in menu.items() :
  print(f"{key:10} : ₹{value}")
print("--------------------")

while True :
  item = input("What would you like to buy (q to quit): ").lower()
  if item == "q":
    break
  elif item not in menu:
    print(f"{item} is unavlaible")
  else:
    cart.append(item)

print("--------YOUR ORDER--------")
for item in cart:
  total += menu.get(item)
  print(item)
print(f"Total: ₹{total}")
print("--------------------------")
"""

#project 12: Banking program
"""
def deposite():
  amount = input("Enter the amount you would like to deposite: ")
  if amount > 0:
    return amount
  else :
    print("Invalide Input")

def withdraw():
  amount = float(input("Enter the amount you would like to withdraw: "))
  if amount > 0 and amount < balance:
    return amount
  else :
    print("Invalide Input")


balance = 0.00
run = True

while run:
  print("------Banking Program------")
  print("How can i help you?")
  print("1. Show Balance")
  print("2. Deposite")
  print("3. Withdraw")
  print("4. Exit")
  option = input("Enter your choice(1/2/3/4): ")

  if option == "1":
    print(f"Your balance is: ${balance}")
  elif option == "2":
    balance += deposite()
  elif option == "3":
    balance -= withdraw()
  elif option == "4":
    run = False
  else:
    print("Invalid input")
"""

#project 13: Encryption program
import random
import string
"""
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)

"##Encryption"
plain_text = input("Enter the text you want to encrypt: ")
cipher_text = ""
for letter in plain_text:
  index = chars.index(letter)
  cipher_text += key[index]

print(f"Encrypted text: {cipher_text}")

"##Decryption"
plain_text = ""
cipher_text = input("Enter the text you want to decrypt: ")
for letter in cipher_text:
  index = key.index(letter)
  plain_text += chars[index]

print(f"Decrypted text: {plain_text}")
"""

def get_sprinkles(func):
  def wrapper():
    print("Would you liked sprinkles")
    func('Vanilla')
  return wrapper

@get_sprinkles
def ice_cream(flavor):
  print(f"Here's your {flavor} ice cream")

ice_cream()