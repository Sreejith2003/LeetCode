def majorityElement(nums):
    # lst = []
    # nums.sort()
    # l = 0
    # count = 1

    # for r in range(l+1, len(nums)):
    #     if nums[l] == nums[r]:
    #         count += 1
            
    #     if nums[l] != nums[r] or r == len(nums)-1:
    #         lst.append(f"{nums[l]}: {count}")
    #         l = r
    #         r = l + 1 
    #         count = 1
        
    # val = lst[max(lst)]
    # print(val)

    hash_map = {}
    for ele in nums:
        if ele not in hash_map:
            hash_map[ele] = 1
        else:
            hash_map[ele] += 1

    max_val = max(hash_map, key = hash_map.get)

    print(max_val)
nums = [1,1,1,2,2,2,2]       #[1,1,1,2,2,2,2]
majorityElement(nums)
            