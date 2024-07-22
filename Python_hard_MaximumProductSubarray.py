# Hard: Maximum Product Subarray
# Problem: Given an integer array 'nums', find the contiguous subarray within an array (containing at least one number) which has the largest product.


def max_product(nums):
    if not nums:
        return 0
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for num in nums[1:]:
        if num < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(num, max_product * num)
        min_product = min(num, min_product * num)
        
        result = max(result, max_product)
    
    return result

# Test
nums = [2, 3, -2, 4]
print(max_product(nums))  # Output: 6
