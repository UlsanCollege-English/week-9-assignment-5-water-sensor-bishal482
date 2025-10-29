"""
HW05 — Water Sensor: Streaming Median

Implement streaming_median(nums) -> list
"""

def streaming_median(nums):
    # TODO:
    # Maintain two heaps: low (max-heap via negatives) and high (min-heap).
    # Invariants: all low <= all high; len(low) >= len(high) and difference ≤ 1.
    # After each insert, append current median (float for even).
    raise NotImplementedError
