import sys

print("Welcome to mean_median_mode!\n")

def find_mean(nums): # add option for decimals
    sum = 0
    decimal_places = int(input("How many decimal places would you like to round to? >> "))
    
    for num in nums:
        sum += num
    
    if decimal_places == 0:
        return int(sum / len(nums))
    else: 
        return round(sum / len(nums), decimal_places)

def find_median(nums):
    nums.sort() 
    if len(nums) % 2 == 1: 
        return nums[int((len(nums) - 1) / 2)]
    else:
        return nums[0:int(len(nums) / 2)][-1], nums[int(len(nums) / 2):][0]
        
def find_mode(nums):
    current_highest = 1
    result = []
    for num in nums:
        if nums.count(num) >= current_highest and num not in result: 
            result.append(num)
            current_highest = nums.count(num)
    return result
                       
nums_str = input("\nEnter numbers seperated by commas (ex. 1, 2, 33, 4) >> ")
nums = [int(num) for num in nums_str.split(',')]

print("\nMean = {}\n".format(str(find_mean(nums))))
print("Median = {}\n".format(str(find_median(nums))))
print("Mode = {}\n".format(str(find_mode(nums))))
