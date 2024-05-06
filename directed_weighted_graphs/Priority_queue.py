import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0  # This variable ensures that elements with the same priority are ordered according to the order they were inserted.

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def remove(self, item):
        for i in range(len(self._queue)):
            if self._queue[i][-1] == item:
                del self._queue[i]
                # heapq.heapify(self._queue)
                return
        raise ValueError("Item " + str(item)+ " not found in the priority queue")
    
    def pop(self):
        return heapq.heappop(self._queue)[-1]

    def is_empty(self):
        return len(self._queue) == 0

