def find_duplicate(nums):
    numbers_count = dict()

    if nums == None:
        return False

    for number in nums:
        if isinstance(number, str) or number < 0:
            return False
        elif number in numbers_count:
            numbers_count[number] += 1
        else:
            numbers_count[number] = 1

    numbers_count_list = list(numbers_count.items())

    duplicate_numbers = []

    for numb, counter in numbers_count_list:
        if counter > 1:
            duplicate_numbers.append(numb)

    if len(duplicate_numbers) == 1:
        return duplicate_numbers[0]

    return False
