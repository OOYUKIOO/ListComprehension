def intersect(a,b):
    return [x for x in a if x in b]

def setDifference(a,b):
    return [x for x in a if x not in b]

def cartesian(a,b):
    return [(x,y) for x in a for y in b]

def union(a,b):
    return []

print cartesian([1,2,3],[1,4])
