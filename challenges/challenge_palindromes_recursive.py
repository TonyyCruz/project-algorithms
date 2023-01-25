def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    while high_index > low_index <= len(word) // 2:
        if word[low_index] != word[high_index]:
            return False
        else:
            return (
                True
                and is_palindrome_recursive(
                        word,
                        low_index + 1,
                        high_index - 1
                    )
            )
    return True
