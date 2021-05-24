the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

def yes_and_no(item):
    if item == 0:
        return "woko"
    else:
        return "wiki"

trailing_booleans = list(map(yes_and_no, the_bools))
print(trailing_booleans)

