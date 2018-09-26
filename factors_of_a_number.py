def factor(num):
    nums = []
    
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
    
    return nums
    
print(factor(-9))
print(factor(36))
print(factor(0))
