try:
    member_count = int(input("""
<=== Welcome to family Expenses Analyzer ===>
.... We are always here to assist you ....
________________________________________
How many family member you have: """))
except:
    print("Enter a valid number!!")
    quit()

master_list = []
def func():
    if member_count == 0:
        print("Your family has 0 member to work with..!!")
        quit()
    for i in range(0,member_count):
        try:
            ind = input(f"Expenses for member {i+1}: ").split(",")
            master_list.append(str_to_int(ind))
        except:
            print("Enter a proper expenses.. plz try again!!")
            quit()

    return master_list

def str_to_int(inp):
    x = []
    for i in inp:
        x.append(int(i))
    return x

def highest(x):
    h = x[0]
    for i in x :
        if i > h:
            h = i
    return h

def lowest(x):
    l= x[0]
    for i in x :
        if i < l:
            l = i
    return l

def total(x):
    t = 0
    for i in x:
        t += i
    return t

def average(x):
    t = 0
    a = 0
    for i in x:
        t += i
    a = t/len(x)
    return a



master_list_ = func()
total_family_exp = 0
average_family_exp = 0
list_of_totals = []
for i in master_list_:
    total_family_exp += total(i)
    average_family_exp += average(i)
    list_of_totals.append(total(i))
    print("_"*40)
    print(f"Highest expenses of member {master_list_.index(i)+1}:",highest(i))
    print(f"Lowest expenses of member {master_list_.index(i)+1}:",lowest(i))
    print("_"*40)

print(f"Total family expenses: {total_family_exp}")
print(f"Average family expenses: {average_family_exp/len(master_list_)}")

for i in range(0,len(list_of_totals)):
    if list_of_totals[i] == max(list_of_totals):
        print(f"Member {i+1} spent the most.")
    if list_of_totals[i] == min(list_of_totals):
        print(f"Member {i+1} spent the least.")


