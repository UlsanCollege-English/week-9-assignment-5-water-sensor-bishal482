import heapq

def streaming_median(nums):
    """
    Compute running medians using two heaps.
    :param nums: List[int] -- input numbers
    :return: List[float] -- running medians
    """
    if not nums:
        return []

    min_heap = []  # min-heap for upper half
    max_heap = []  # max-heap for lower half (store negatives)
    result = []

    for num in nums:
        # Push into max_heap (lower half)
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

        # Balance heaps
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        elif len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))

        # Compute median
        if len(max_heap) == len(min_heap):
            median = (-max_heap[0] + min_heap[0]) / 2.0
        else:
            median = -max_heap[0]

        result.append(median)

    return result


# Optional manual test
if __name__ == "__main__":
    print(streaming_median([1,2,3]))            # [1,1.5,2]
    print(streaming_median([5,15,1,3]))         # [5,10.0,5,4.0]
    print(streaming_median([-1,-2,-3]))         # [-1,-1.5,-2]
