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




