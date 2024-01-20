def spy_game(nums: list) -> bool:
    need_numbers, index = [0, 0, 7], 0
    
    for index_of_nums in range(len(nums)):
        if need_numbers[index] == nums[index_of_nums]:
            index += 1
        if index == 3:
            return True
    
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0])) 