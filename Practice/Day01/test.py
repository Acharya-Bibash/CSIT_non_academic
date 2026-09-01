expenses = input("Enter your expenses: ")
exp = expenses.split(",")
new = []
for i in range(0,len(exp)):
    new.append(int(exp[i]))
print(new)
