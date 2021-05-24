import random

my_list = [4,5,734,43,45]

for i in range(0,10):
    random_list = random.randint(0, 10)
    my_list.append(random_list)

print(my_list)
