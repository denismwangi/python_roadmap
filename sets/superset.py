setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
setc = {90,80}

print(setA.issubset(setB))
print(setB.issubset(setA))
print(setB.issuperset(setA))

#disjoint
print(setA.isdisjoint(setc))