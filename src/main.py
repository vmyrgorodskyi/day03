#lesson27

'''print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120:
    print("You can ride the rollercoaster!")
else:
    print("Sorry, you are not good for the rollercoaster!")

'''

#lesson28

'''# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 1:
    print("Your number is odd")
else:
    print("Your number is even")
'''

#lesson29

'''print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    age = int(input("You can ride the rollercoaster! What is your age? "))
    if age < 12:
        print("You will have to pay $5")
    elif age <= 18:
        print("You will have to pay 7")
    else:
        print("You will have to pay $12")
else:
    print("Sorry, you are not good for the rollercoaster!")
'''

#lesson30
'''
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / (height ** 2), 2)

if bmi < 18.5:
    print(f"You are underweight{bmi}")
elif bmi < 25:
    print("You have normal weight")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are clinically obese")
'''

'''
#lesson31
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print("This year is Leap")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap")
'''
#lesson32
'''
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    age = int(input("You can ride the rollercoaster! What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are for $5")
    elif age <= 18:
        bill = 7
        print("Youth tickers are for 7")
    else:
        bill = 12
        print("Adult tickets are for $12")
    wants_photo = input("Do you want your photo taken? Y or N ")
    if wants_photo == "Y":
        #Add $3 to the bill
        bill += 3
        print (f"Your total bill is {bill}")
    else:
        print(f"Your total bill is {bill}")
else:
    print("Sorry, you are not good for the rollercoaster!")

'''

#lesson33
'''
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

"""bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
    print(f"Your total bill for the small pizza is ${bill}")

if size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your total bill for the medium pizza is ${bill}")

if size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
    print(f"Your total bill for the large pizza is ${bill}")
"""
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is ${bill}")
'''
#lesson 34

'''
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    age = int(input("You can ride the rollercoaster! What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are for $5")
    elif age <= 18:
        bill = 7
        print("Youth tickers are for 7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("You are in crisi, tickets are for $0")
    else:
        bill = 12
        print("Adult tickets are for $12")
    wants_photo = input("Do you want your photo taken? Y or N ")
    if wants_photo == "Y":
        #Add $3 to the bill
        bill += 3
        print (f"Your total bill is {bill}")
    else:
        print(f"Your total bill is {bill}")
else:
    print("Sorry, you are not good for the rollercoaster!")
'''
'''
#lesson35
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your full name? \n")
name2 = input("What is their full name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1 + name2
lowercase_srtring = combined_string.lower()

t = lowercase_srtring.count("t")
r = lowercase_srtring.count("r")
u = lowercase_srtring.count("u")
e = lowercase_srtring.count("e")

true = t + r + u + e

l = lowercase_srtring.count("l")
o = lowercase_srtring.count("o")
v = lowercase_srtring.count("v")
e = lowercase_srtring.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your love score is {love_score}. You go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is lovescore is {love_score}. You are alright together")
else:
    print(f"Your score is {love_score}")
'''

#lesson36

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

side_choice1 = input("You are the crossroad. Where do you want to go: left or right? ")
side_choice = side_choice1.lower()
if side_choice == "left":
    action_choice1 = input("You come to a lake. There is an island you see in front of you. What do you want to do: swim or wait? ")
    action_choice = action_choice1.lower()
    if action_choice == "wait":
        door_choice = input("You arrive to the island. You see houses with different doors. Which door do you want to open: red, yellow or blue? ")
        door_choice.lower()
        if door_choice == "yellow":
            print("You won the game")
        else:
            print("Your died")
    else:
        print("Your died")
else:
    print("Your died")
