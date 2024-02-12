def unique(nums):
    new_list =[]
    for i in range(0, len(nums)-1):
        if nums[i] != nums[i+1]:
             new_list.append(nums[i])
            

    return new_list

print(unique([1,1,3,1,6,3,2]))
