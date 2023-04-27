def is_palindrome_iterative(word):
    length = len(word)

    if word == "":
        return False

    if length == 1:
        return True

    for index in list(range(0, (length // 2) + 1)):
        if not word[index] == word[length - 1 - index]:
            return False

    return True
