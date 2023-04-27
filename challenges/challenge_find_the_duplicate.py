def find_duplicate(nums):
    duplicates = set()

    nums.sort()

    for index in list(range(0, len(nums) - 1)):
        if isinstance(nums[index], str) or nums[index] < 0:
            return False

        if nums[index] == nums[index + 1]:
            duplicates.add(nums[index])

    duplicate_list = list(duplicates)

    if len(duplicate_list) == 1:
        return duplicate_list[0]

    return False
