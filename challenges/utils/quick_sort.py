def quick_sort(string, start=0, end=None):
    if end is None:
        end = len(string) - 1
    if start < end:
        p = partition(string, start, end)
        quick_sort(string, start, p - 1)
        quick_sort(string, p + 1, end)


def partition(string, start, end):
    pivot = string[end]
    delimiter = start - 1

    for index in range(start, end):
        if string[index] <= pivot:
            delimiter = delimiter + 1
            string[index], string[delimiter] = string[delimiter], string[index]

    string[delimiter + 1], string[end] = string[end], string[delimiter + 1]

    return delimiter + 1
