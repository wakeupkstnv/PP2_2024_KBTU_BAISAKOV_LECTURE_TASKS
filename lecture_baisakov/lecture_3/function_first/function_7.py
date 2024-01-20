def has_33(nums: list) -> bool:
    for index_of_nums in range(len(nums) - 1):
        if nums[index_of_nums] == nums[index_of_nums + 1] == 3:
            return True
    
    return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]) )