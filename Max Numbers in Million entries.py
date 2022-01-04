import heapq
entries = [3, 2, 5, 61, 8, 7, 12, 9, 56 , 1, 0, -54, 23, -45 , 97]

negative_entries = [-x for x in entries]



import heapq
def Greater_elements(negative_entries):
    heapq.heapify(negative_entries)

    for _ in range(10):
        print(-1 * (heapq.heappop(negative_entries)))

Greater_elements(negative_entries)
