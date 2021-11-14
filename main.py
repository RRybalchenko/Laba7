import heapq
erste_list = sorted([1,4,5,8,10,11])
zweite_list = sorted([1,3,4,5,6,7,9,12,14])
dritte_list = sorted([1,7,8,9,13,14,15,16])
abschliessend_list = list(heapq.merge(erste_list, zweite_list, dritte_list))
print(abschliessend_list)
