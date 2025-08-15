def moveZeroes(nums):

    # hash_map = {}
    
    # left = 0
    
    # right = 0
    
    # while right < len(nums):

    #     curr_ele = nums[left]
    #     count = 0

    #     while right < len(nums) and nums[right] == curr_ele:
    #         count += 1
    #         if nums[right] == curr_ele:
    #             right += 1  
    #     hash_map[curr_ele] = count

    #     if count > 2:
    #         while count > 2:
    #             nums.remove(nums[left])
    #             count -= 1
    #     if len(nums) == right:
    #         return nums
        
    #     left = right - 1
    #     right = left
 
    # return nums

    hash_map = {}

    for ele in nums:
        if ele in hash_map:
            hash_map[ele] += 1
        else:
            hash_map[ele] = 1
        
        for ele, count in hash_map.items():
            while count > 2:
                if count > 2:
                    nums.remove(nums[ele])
                    count -= 1 
                    
            
        
    return nums


nums = [0,0,1,1,1,2,2,3,3,4]
print(moveZeroes(nums))