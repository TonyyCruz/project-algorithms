def sort_function(string, index=0, end=False):
    end = end or len(string)

    if type(string) is str:
        string = list(string.lower())
    if index >= end - 1:
        return "".join(string)
    for i in range(1, end):
        if string[i - 1] > string[i]:
            string[i - 1], string[i] = string[i], string[i - 1]
    return sort_function(string, index + 1, end)
