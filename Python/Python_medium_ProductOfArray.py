# Medium: Product of Array Except Self
# Problem: Given an array 'nums' of 'n' integers where n > 1, return an array output such that output[i] is equal to the product of all the elements of 'nums' except nums[i].

def product_except_self(nums):
    length = len(nums)
    output = [1] * length

    left_product = 1
    for i in range(length):
        output[i] = left_product
        left_product *= nums[i]
    
    right_product = 1
    for i in range(length - 1, -1, -1):
        output[i] *= right_product
        right_product *= nums[i]
    
    return output

# Test
nums = [1, 2, 3, 4]
print(product_except_self(nums))  # Output: [24, 12, 8, 6]