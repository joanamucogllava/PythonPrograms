# This function takes a list and returns a new list that contains all the 
# elements of the first list despite the ones that are duplicated.
# This is a practice program.

def dedupe_v1(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y

def dedupe_v2(x):
    return list(set(x))

a = [1,2,3,4,3,2,1]
print (a)
print (dedupe_v1(a))
print (dedupe_v2(a))
