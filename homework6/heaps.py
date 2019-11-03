class min_heap(object):
    def __init__(self, A):
        # heap array has empty first element
        self.heap = self.build_min_heap(A)
        self.size = len(self.heap) - 1

    def heapify(self, A, i):
        # i is the root to heapify from
        n = len(A)
        smallest = i
        l = 2 * i
        r = 2 * i + 1

        if (l < n) and (A[l] < A[smallest]):
            smallest = l
        if (r < n) and (A[r] < A[smallest]):
            smallest = r
        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]
            self.heapify(A, smallest)

    def build_min_heap(self, A):
        A = [None] + A
        n = len(A)//2
        for i in range(n, 0, -1):
            self.heapify(A, i)
        return A

    def bubble_up(self, i):
        # i is the index of node to bubble up
        parent = i // 2
        while (parent > 0) and (self.heap[parent] > self.heap[i]):
            self.heap[parent], self.heap[i] = \
            self.heap[i], self.heap[parent]
            i = parent
            parent = i // 2

    def push(self, i):
        # add to end of heap
        self.heap.append(i)
        self.size += 1

        # bubble up to restore heap invariants
        i = self.size
        self.bubble_up(i)

    def pop(self):
        if self.size >= 1:
            # swap root and bottom-most, right-most child and remove last element
            child = self.size
            self.heap[1], self.heap[child] = self.heap[child], self.heap[1]
            min = self.heap.pop()
            self.size -= 1

            # restore heap invariants
            self.heapify(self.heap, 1)
            return min
        else:
            return None

    def peek(self):
        return self.heap[1]

class max_heap(object):
    def __init__(self, A):
        # heap array has empty first element
        self.heap = self.build_max_heap(A)
        self.size = len(self.heap) - 1

    def heapify(self, A, i):
        # i is the root to heapify from
        n = len(A)
        largest = i
        l = 2 * i
        r = 2 * i + 1

        if (l < n) and (A[l] > A[largest]):
            largest = l
        if (r < n) and (A[r] > A[largest]):
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.heapify(A, largest)

    def build_max_heap(self, A):
        A = [None] + A
        n = len(A)//2
        for i in range(n, 0, -1):
            self.heapify(A, i)
        return A

    def bubble_up(self, i):
        # i is the index of node to bubble up
        parent = i // 2
        while (parent > 0) and (self.heap[parent] < self.heap[i]):
            self.heap[parent], self.heap[i] = \
            self.heap[i], self.heap[parent]
            i = parent
            parent = i // 2

    def push(self, i):
        # add to end of heap
        self.heap.append(i)
        self.size += 1

        # bubble up to restore heap invariants
        i = self.size
        self.bubble_up(i)

    def pop(self):
        if self.size >= 1:
            # swap root and bottom-most, right-most child and remove last element
            child = self.size
            self.heap[1], self.heap[child] = self.heap[child], self.heap[1]
            max = self.heap.pop()
            self.size -= 1

            # restore heap invariants
            self.heapify(self.heap, 1)
            return max
        else:
            return None

    def peek(self):
        return self.heap[1]
