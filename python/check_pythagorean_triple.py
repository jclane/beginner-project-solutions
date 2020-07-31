from math import pow as p

def check_pythagorean_triple(nums):
    nums = nums.split(' ')
    nums = [int(num) for num in nums]
    
    if p(nums[0], 2) + p(nums[1], 2) == p(nums[2], 2): return True
    if p(nums[1], 2) + p(nums[2], 2) == p(nums[0], 2): return True
    if p(nums[2], 2) + p(nums[0], 2) == p(nums[1], 2): return True
    
    return False
    
while True:
    nums = input("\nEnter three numbers seperated by a space [3 4 5] >>  ")
    
    if nums.lower() != 'q':
        print("\n" + str(check_pythagorean_triple(nums)))
    else:
        break

