
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

hello = []

for item in range(0,len(my_list), 1):
    if type(my_list[item]) == dict:
        hello.append(my_list[item])

print(hello)
