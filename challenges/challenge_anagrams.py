# from challenges.utils.sort_function import sort_function
# from challenges.utils.bubble_sort import bubble_sort
from challenges.utils.quick_sort import quick_sort


def is_anagram(first_string, second_string):
    first_str_list = list(first_string.lower())
    second_str_list = list(second_string.lower())

    quick_sort(first_str_list)
    quick_sort(second_str_list)

    first_str_sorted = "".join(first_str_list)
    second_str_sorted = "".join(second_str_list)
    string_is_anagram = first_str_sorted == second_str_sorted

    response = (
        first_str_sorted,
        second_str_sorted,
        string_is_anagram
    )

    if not first_string or not second_string:
        return tuple((first_str_sorted, second_str_sorted, False))

    return response
