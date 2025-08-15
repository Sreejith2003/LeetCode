def minimumOperations(nums):
        count = 0
        while True:
            non_zero = [x for x in nums if x != 0]
            if not non_zero:
                break
            x = min(non_zero)
            
            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] -= x
            count += 1
        return count

nums = [1,5,0,3,5]
print(minimumOperations(nums))