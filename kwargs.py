def sum(**kwargs):
    sum = 0
    for x,y in kwargs.items():
        sum+=y
    return sum

print(sum(pizza = 5.40,coke = 2.99))