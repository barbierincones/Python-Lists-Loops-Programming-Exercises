people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def deletePerson(person_name):
    new_people = []
    for item in people:
        if item == person_name:
            continue
        else:
            new_people.append(item)
    return (new_people)

print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))
