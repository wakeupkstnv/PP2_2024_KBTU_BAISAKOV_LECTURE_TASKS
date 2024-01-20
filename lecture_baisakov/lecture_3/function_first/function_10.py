def unique(nums: list) -> list:
    hash_table = {}
    for _ in nums:
        hash_table[_] = 1

    return [key for key, value in hash_table.items()]

print(unique([1, 2, 3, 2, 1, 3, 1]))