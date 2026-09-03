# def double(number):
#     return number*2

# print(double(45))

# def calculate_discount(price, percentage):
#     discount_amount = price*(percentage/100)
#     total = price - discount_amount
#     return total

# discount = calculate_discount(1000,20)
# print(discount)

# number = input("Enter a number: ")
# def digit_count(number):
#     digit = 0
#     for i in number :
#         digit += 1
#         if i == "-" or i == "+" or i == " ":
#             digit -= 1

#     if digit == 0 or digit < 0:
#         print("No number entered.")
#         quit()
#     elif digit == 1:
#         print("Single digit number.")
#     else:
#         print("Multidigit number.")

# def check_positive(number):
#     number = int(number)
#     if number < 0:
#         print("Your number is negative.")
#     elif number == 0:
#         print("your number is 0.")
#     else:
#         print("Your number is positive:")

# def check_even(number):
#     number = int(number)
#     if number % 2 == 0:
#         print("Your number is Even.")
#     else:
#         print("Your number is Odd.")

# check_even(number)
# check_positive(number)
# digit_count(number)

numbers = [4, 7, 2, 9, 5]

def analyze(num):
    return total(num) , average(num) , highest(num) , lowest(num) , count_even(num) , count_odd(num)

def total(num):
    t = 0 
    for i in num:
        t += i
    return t

def average(num):
    a = 0 
    t = 0
    for i in num:
        t += i
    a = t/len(num)
    return a

def highest(num):
    h = num[0]
    for i in num:
        if i > h:
            h = i
    return h

def lowest(num):
    l = num[0]
    for i in num:
        if i < l:
            l = i
    return l

def count_odd(num):
    odd = 0
    for i in num:
        if i % 2 != 0:
            odd += 1
    return odd

def count_even(num):
    even = 0
    for i in num:
        if i % 2 == 0:
            even += 1
    return even

print(analyze(numbers))