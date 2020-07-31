

def add_nums(nums, indices, target):
    try:
        num1 = nums[indices[0]]
        num2 = nums[indices[1]]
    except IndexError:
        return "None of these numbers add up to " + str(target)
    if num1 + num2 == target:
        return indices[0], indices[1]
    return add_nums(nums, [indices[0], indices[1] - 1], target)

nums = [1, 2, 22, 2]
target = 9

print(add_nums(nums, [0, len(nums) - 1], target))
