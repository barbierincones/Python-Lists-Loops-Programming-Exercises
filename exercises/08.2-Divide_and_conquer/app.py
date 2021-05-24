list_of_numbers = [4,	80,	85,	59,	37,25,	5,	64,	66,	81,20,	64,	41,	22,	76,76,	55,	96,	2,	68]


def merge_two_list(list):
    odd_list = []
    even_list = []
    for numb in list:
        if numb % 2 == 0:
            even_list.append(numb)
        else:
            odd_list.append(numb)
    even_list.extend(odd_list)
    return (even_list)
    
print(merge_two_list(list_of_numbers))
