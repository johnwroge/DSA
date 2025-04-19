''''
Priority queue: abstract description of data structure heap

Orders elements by priority. 

Heap: concrete data structure

'''


import heapq
# 1 creating Min heap and removing min, heapq offers min heap by default

data = [10, 20, 43, 1, 2, 65, 17, 44, 2, 3, 1]
heapq.heapify(data)

# print(heapq.heappop(data))

# pushing value to heap
# print(data)
heapq.heappush(data, 4)
# print(data)

# 2 max heap, 2 ways:  negate each value in a  minimum heap, or use heapq.heapify_max()

# data = [-x for x in data]

# heapq._heapify_max(data)
# print(data)


# 3 combining two lists into a heap

l1 = [10,20,30,40,50]
l2 = [15,25,35,45,55]

l3 = heapq.merge(l1,l2)
print(list(l3))

