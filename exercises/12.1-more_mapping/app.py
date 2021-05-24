my_numbers = [23,234,345,4356234,243,43,56,2]
new_list = []

def increment_by_one(x):
    x = x * 3
    return x
    
new_list = list(map(increment_by_one, my_numbers))

print(new_list)
