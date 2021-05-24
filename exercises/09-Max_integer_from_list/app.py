my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

def calculate_maximum(list):
    max = 0
    for numb in list:
        if numb > max:
            max = numb
    return max
print(calculate_maximum(my_list))
