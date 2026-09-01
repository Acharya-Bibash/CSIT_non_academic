import random

print("<=== Welcome to Number guessing Game ===>")

number1 = random.randint(1,50)
number2 = random.randint(1,100)
number3 = random.randint(1,500)

level = int(input("Select difficulty: Easy: 1-50 (1)| Medium 1-100 (2)| Difficult: 1-500 (3): "))


if level == 1 :
    number = number1
elif level == 2:
    number = number2
elif level ==3:
    number = number3
else:
    print("Enter valid number!!")
    quit()


def check(guess):
    if guess == number:
        print("Correct!!!!!")
        print(f"You got it in {attempt} attempt.")
        quit()
        
    if guess < number:
        warmness = number - guess
    else:
        warmness = guess - number
        
    if warmness <= 5:
        print("Too hot....")
    elif warmness <= 20:
        print("Getting Warmer outside...") 
    elif warmness <= 50:
            print("Cold...")
    else:
        print("Its freezing..") 

attempt = 0
while True:
    try:
        guess = int(input("Enter your Guess: "))
    except:
        print("Enter a valid number:")
        quit()
    attempt += 1
    check(guess)
  
    

