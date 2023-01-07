from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    if target > nums[-1] or target < nums[0]:
        return len(nums) if target > nums[-1] else 0
    else:
        if target in nums:
            return nums.index(target)
        else:
            count = 0
            while len(nums) > 1:
                index = len(nums) // 2
                left = nums[:index]
                right = nums[index:]
                if target < left[-1]:
                    nums = left
                elif target > right[0]:
                    count += len(left)
                    nums = right
                else:
                    count += len(left)
                    break
            return count






print(searchInsert([1, 3, 5, 6], 5), '=> 2')
print(searchInsert([1, 3, 5, 6], 2), '=> 1')
print(searchInsert([1, 3, 5, 6], 7), '=> 4')
print(searchInsert([1, 2, 3, 3, 4, 4, 5, 5, 7, 8, 9, 10], 6), '=> 8')