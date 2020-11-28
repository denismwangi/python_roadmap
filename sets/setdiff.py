
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB)
print(diff)
dif2 = setB.difference(setA)
print(dif2)

#retun all different but not in both
diffsy = setA.symmetric_difference(setB)
print(diffsy)

#combine no duplicates
setA.update(setB)
print(setA)

#intersection both
setA.intersection_update(setB)
print(setA)