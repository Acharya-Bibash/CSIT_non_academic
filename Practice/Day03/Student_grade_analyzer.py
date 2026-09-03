marks = input("Enter marks: ").split(",")

def str_to_float(num):
    try:
        h = []
        for i in num:
            h.append(float(i))
        return h
    except:
        print("Wrong input try again.")
        quit()

float_marks = str_to_float(marks)

def total(num):
    t = 0 
    for i in num:
        t+= i
    return t

def average(num):
    t = 0
    a = 0
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

def pass_sub_counter(num):
    count = 0
    for i in num:
        if i >= 40:
            count += 1
    return count


def failed_sub_counter(num):
    count = 0
    for i in num:
        if i < 40:
            count += 1
    return count

def grade(avg):
    if avg < 40:
        return "F"
    elif avg >= 90:
        return "A+"
    elif avg >= 80 and avg <= 89.99:
        return "A"
    elif avg >= 70 and avg <= 79.99:
        return "B+"
    elif avg >= 60 and avg <= 69.99:
        return "B"
    elif avg >= 50 and avg <= 59.99:
        return "C+"
    elif avg >= 40 and avg <= 49.99:
        return "C"


def print_result(num):
    return f"""
========== RESULT ==========

Total: {total(num)}
Average: {average(num)}
Highest: {highest(num)}
Lowest: {lowest(num)}
Passed subjects: {pass_sub_counter(num)}
Failed subjects: {failed_sub_counter(num)}
Grade: {grade(average(num))}
============================
"""


print(print_result(float_marks))