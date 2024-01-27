import heapq
import numpy as np

def heap_sort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    
    return [heapq.heappop(h) for _ in range(len(h))]

def find_min_sum(arr):
    sorted_arr = heap_sort(arr)

    shortest_way = list()

    while len(sorted_arr) > 1:
        sum = 0
        sum = sorted_arr[0] + sorted_arr[1]
        shortest_way.append(sum)
        heapq.heappop(sorted_arr)
        heapq.heapreplace(sorted_arr, sum)
        sorted_arr = heap_sort(sorted_arr)

    res = np.sum(shortest_way)

    return res
