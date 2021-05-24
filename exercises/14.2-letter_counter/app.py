par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

par_lower = par.lower()

def letter_count(string):
    counts = {}
    for i in string:
        counts[i] = counts.get(i,0)+1
    return counts

print(letter_count(par_lower.replace(" ", "")))