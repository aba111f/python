def spy_game(nums):
    for i in range(1, len(nums) - 1):
        if nums[i-1] == 0 and nums[i] == 0 and nums[i+1] == 7:
            return True
    return False



print(spy_game([1,2,4,0,0,7,5]) )
print(spy_game([1,0,2,4,0,5,7]) )
print(spy_game([1,7,2,0,4,5,0]) )