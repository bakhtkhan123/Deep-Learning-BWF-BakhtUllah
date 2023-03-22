#introducing to set
S={1,2,3,4}
print(type(S))

S.pop()
print(S)

S.add(1)
print(S)


#Union
s1={1,2,3,4,5}
s2={6,7,2,9,5}
Union=s1.union(s2)
print('union = ',Union)

#Intersection
s1.add(7)
common=s1.intersection(s2)
print('intersection = ',common)

#Difference
diff=s2.difference(s1)
print('difference = ',diff)

#symetric difference
sym_diff=s1.symmetric_difference(s2)
print("symeteric_difference = ",sym_diff)

#making data unique with set
S1={1,2,4,2,1,5,4,8,5,3,5,8}
uni_Que=set(S1)
print('unique set = ',uni_Que)
