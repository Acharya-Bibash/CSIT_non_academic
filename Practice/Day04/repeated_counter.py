# numbers = [4, 7, 2, 7, 9, 4, 2, 7]
# numbers = [1, 1, 1, 1, 1]
numbers = [4, 7, 2, 7, 9, 4, 2, 7]

def count(num):
    c = 0
    for i in numbers:
        if i == num:
            c += 1
    return c

unique_number = list(set(numbers))

def count_num_from_list(num_list):
    for i in num_list:
        print(f"{i} appears {count(i)} times.")


def frequency(num_list):
    high = count(unique_number[0])
    m = unique_number[0]
    
    for i in num_list:
        if count(i) > high:
            high = count(i)
            m = i
    return m , high

fq = frequency(unique_number)
count_num_from_list(unique_number)
print(f"""{"-"*40}
Most frequency : {fq[0]}
Frequency : {fq[1]}
""")
