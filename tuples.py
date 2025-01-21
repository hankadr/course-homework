#task1 - You have three tuples of integers. Find elements present in all tuples.
#na konci všech tasků už nepřevádím zpět na tuply
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)
tuple3 = (5, 6, 7, 8, 9)
common_elements = []
for element in tuple1:
    if tuple1.count(element) > 0 and tuple2.count(element) > 0 and tuple3.count(element) > 0:
        if element not in common_elements:
            common_elements.append(element)
            print(common_elements)

#task2 - You have three tuples of integers. Find elements unique for each list.
tuple1 = (1, 2, 3, 4)
tuple2 = (3, 4, 5, 6)
tuple3 = (6, 7, 8, 1)

set1 = set(tuple1)
set2 = set(tuple2)
set3 = set(tuple3)

unique1 = set1 - set2 - set3  
unique2 = set2 - set1 - set3  
unique3 = set3 - set1 - set2  

print("Unique to tuple1:", unique1)
print("Unique to tuple2:", unique2)
print("Unique to tuple3:", unique3)

#task3 - You have three tuples of integers. Find elements that are present in each tuple and at the same position in each tuple.
tuple1 = (1, 2, 3, 4)
tuple2 = (1, 5, 3, 6)
tuple3 = (1, 9, 3, 8)
min_length = min(len(tuple1), len(tuple2), len(tuple3))#minimum length to avoid indexerror if tuples are of different lenght

common_elements = [
    tuple1[i]
    for i in range(min_length)
    if tuple1[i] == tuple2[i] == tuple3[i]
]
common_elements = tuple(common_elements)
print("Elements present in all tuples at the same position:", common_elements)