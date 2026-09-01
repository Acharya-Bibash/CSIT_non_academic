# expenses = [250, 120, 500, 80, 300, 150]
# expenses = list(input("Enter your expenses: "))
# print(expenses)
expenses_ = input("Enter your expenses seperated with comma',' : ")
exp_split = expenses_.split(",")
expenses = []
for i in range(0,len(exp_split)):
    expenses.append(int(exp_split[i]))

# Total expense
# Average expense
# Highest expense
# Lowest expense
# Number of expenses above the average
# Whether the user stayed within a budget of 1200

total = 0
highest = expenses[0]
lowest = expenses[0]
for i in range(0,len(expenses)):
    total += expenses[i]
    if expenses[i] > highest:
        highest = expenses[i]

    if expenses[i] < lowest:
        lowest = expenses[i]    

average = total/len(expenses)
count = 0
for i in range(0,len(expenses)):
    if expenses[i] > average:
        count += 1

if total > 1200 :
    print("Out of budget!!")
else:
    print("You are in the budget..")

print(f"Total : {total}")
print(f"Average : {average}")
print(f"Highest : {highest}")
print(f"Lowest : {lowest}")
print(f"Expenses above average : {count}")
