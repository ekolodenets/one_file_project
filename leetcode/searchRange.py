from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    if not nums or target not in nums:
        return [-1, -1]
    else:
        total = [i for i in range(len(nums)) if nums[i] == target]
        return [min(total), max(total)]


print(searchRange([5, 7, 7, 8, 8, 10], 8), '=> [3, 4]')
print(searchRange([5, 7, 7, 8, 8, 10], 6), '=> [-1, -1]')
print(searchRange([], 0), '=> [-1, -1]')
