expenses_ = input("Enter your expenses seperated with comma',' : ")

exp_split = expenses_.split(",")

expenses = []
for i in range(0,len(exp_split)):
    try:
        expenses.append(float(exp_split[i]))
    except:
        print(f"Invalid Expenses: {exp_split[i]}\n"\
              "Enter your expenses again!!")
        quit()

def total():
    x = 0
    for i in range(0,len(expenses)):
        x += expenses[i]
    return x

def highest():
    highest = expenses[0]
    for i in range(0,len(expenses)):
        if expenses[i] > highest:
            highest = expenses[i]
    return highest

def lowest():
    lowest = expenses[0]
    for i in range(0,len(expenses)):
        if expenses[i] < lowest:
            lowest = expenses[i]    
    return lowest

def average():
    x = total()
    x = x/len(expenses)
    return x

def expenses_above_counter():
    count = 0
    for i in range(0,len(expenses)):
        if expenses[i] > average():
            count += 1
    return count 

def budget_info():
    if total > 1200 :
        print("Out of budget!!")
    else:
        print("You are in the budget..")

def print_receipt():
    print(f"Total : {total()}")
    print(f"Average : {average()}")
    print(f"Highest : {highest()}")
    print(f"Lowest : {lowest()}")
    print(f"Expenses above average : {expenses_above_counter()}")

print_receipt()