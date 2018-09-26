def factor(num):
    
    nums = []
    
    for i in range(2, num + 1):
        if i == num:
            print("{} is a prime number.".format(num))
        elif (num % i) == 0:
            break   
    
    if num == 0:
        return nums
    
    if num > 0:
        for i in range(1, num + 1):
            if num % i == 0:
                nums.append(i)
    
    if num < 0:
        rng = range(num - 1, abs(num) + 1)
        for i in rng:
            if i == 0:
                continue
            elif num % i == 0:
                nums.append(i)        
        
    nums.sort()
    nums = [str(n) for n in nums]
    return ', '.join(nums)
    
num = input("Enter a number >> ")
print(factor(int(num)))
