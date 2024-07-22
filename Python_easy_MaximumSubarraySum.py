# Easy: Find the Maximum Subarray Sum (Kadane's Algorithm)
# Problem: Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.


def max_subarray_sum(nums):
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))