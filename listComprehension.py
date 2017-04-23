def union (a,b):
    return a+[x for x in b if x not in a]

def intersect(a,b):
    return [x for x in a if x in b]

def setDifference(a,b):
    return [x for x in a if x not in b]

def cartesian(a,b):
    return [(x,y) for x in a for y in b]

def symmetricDifference(a,b):
    return [x for x in a if x not in b] + [y for y in b if y not in a]

print symmetricDifference([1,2,3],[1,4,2,5])
