my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

def calculate_average(list):
    sum = 0
    i = 0
    for numb in list:
        sum += numb
        i += 1
    avg = sum/i
    return avg
print(calculate_average(my_list))


