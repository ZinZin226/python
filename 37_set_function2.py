setA={1, 2, 5, 6, 7}
setB={5, 6, 7, 8, 9}
print('setA union setB ', setA.union(setB))
print('setA intersection setB ', setA.intersection(setB))
print('setB intersection setA ', setB.intersection(setA))

setC={1, 2, 3, 4}
setD={3, 4, 5, 6}
print('set C difference set D ', setC.difference(setD))
print('set D difference set C ', setD.difference(setC))
print(setC-setD)
print(setD-setC)
print('symmerize difference ', setC.symmetric_difference(setD))