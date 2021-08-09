def task_1(nums):
    count = 0
    for i in range(len(nums)):
        if(is_prime(nums[i])):
            count +=1
        else:
            continue
    return count

def is_prime(n):
    for i in range(2,(n//2)+1):
        if(n % i ==0):
            return False
    return True

