def is_palindrome_iterative(word):
    initial_index = 0
    final_index = len(word) - 1
    if final_index < initial_index:
        return False

    while initial_index < final_index:
        if word[initial_index] != word[final_index]:
            return False
        initial_index += 1
        final_index -= 1
    return True
