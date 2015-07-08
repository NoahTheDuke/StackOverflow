import random

apoints, bpoints, cpoints, dpoints = 5, 2, 1, 8
# attempting to sort using a dictionary (works assuming no teams have equal points)
pointsdict = {"a": apoints, "b": bpoints, "c": cpoints, "d": dpoints}
pointsdictsorted = sorted(pointsdict, key=pointsdict.__getitem__, reverse=True)

for idx, elem in enumerate(pointsdictsorted):
    pointsdictsorted[idx] = (elem, idx + 1)

ranks = sorted(pointsdictsorted)
arank = ranks[0][1]
brank = ranks[1][1]
crank = ranks[2][1]
drank = ranks[3][1]

print(arank, brank, crank, drank)
