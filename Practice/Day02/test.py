def str_to_int(self):
    x = []
    for i in self:
        x.append(int(i))
    return x

s = input().split(",")
print(str_to_int(s))
