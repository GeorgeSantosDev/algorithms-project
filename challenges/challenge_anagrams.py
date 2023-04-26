def merge(letters, start, mid, end):
    left = letters[start:mid]
    right = letters[mid:end]
    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            letters[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            letters[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            letters[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            letters[general_index] = right[right_index]
            right_index = right_index + 1


def sort_function(letters, start, end):
    if (end - start) > 1:
        mid = (start + end) // 2
        sort_function(letters, start, mid)
        sort_function(letters, mid, end)
        merge(letters, start, mid, end)


def aggregator(word):
    letters_list = [letter.lower() for letter in word]
    sort_function(letters_list, 0, len(letters_list))

    return "".join(letters_list)


def is_anagram(first_string, second_string):
    if first_string == "" and second_string == "":
        return (first_string, second_string, False)

    if first_string == "" or second_string == "":
        return (
            (aggregator(first_string), second_string, False)
            if second_string == ""
            else (first_string, aggregator(second_string), False)
        )

    first = aggregator(first_string)
    second = aggregator(second_string)

    return (first, second, first == second)
