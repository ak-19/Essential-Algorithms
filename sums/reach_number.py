#addition is progressed from 1 to k, add 1 , 2, ...... k
#until target number is reached

# 1. either target is reached summing naively or
# 2. target-sum is bigger and even so changing sign to some number of even number can lower sum to target
# 3. move k while target-sum is not even

#approach number 1
def reach_number1(target):
    i = cum_sum = 0
    target = abs(target)
    
    while cum_sum < target:
        i += 1
        cum_sum += i            
        if cum_sum == target: return i
        
    while (cum_sum - target) % 2:
        i += 1
        cum_sum += i            
    
    return i 

#approach number 2
def reach_number2(target):
    k, target = 0, abs(target)
    
    while target > 0: 
        k += 1
        target -= k 
                        
    return k if target % 2 == 0 else k + 1 + k % 2