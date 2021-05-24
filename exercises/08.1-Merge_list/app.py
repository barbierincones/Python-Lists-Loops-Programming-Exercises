chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']

def merge_list(list1, list2):
    chunk_final = []
    for i in range(len(chunk_one)-1):
        list1.extend(list2)
        chunk_final.append(list1)
        return chunk_final[i]
    
print(merge_list(chunk_one, chunk_two))
