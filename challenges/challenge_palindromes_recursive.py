def is_palindrome_recursive(word, low_index, high_index):
    if (
        word == ""
        or low_index == (len(word) // 2) + 1
        or len(word) == 1
        or word[low_index] != word[high_index]
    ):

        return (
            True
            if low_index == (len(word) // 2) + 1 or len(word) == 1
            else False
        )
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
