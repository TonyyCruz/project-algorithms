def bubble_sort(string):
    string = list(string.lower())
    length = len(string)

    for ordered_elements in range(length - 1):
        for item in range(0, length - 1 - ordered_elements):
            if string[item] > string[item + 1]:
                current_element = string[item]
                string[item] = string[item + 1]
                string[item + 1] = current_element
    return "".join(string)


print(bubble_sort("DCBA"))
