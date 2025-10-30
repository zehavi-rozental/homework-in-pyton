# 1
def analyze_list(lst):
    unique_numbers = set(lst)
    average = sum(lst) / len(lst) if lst else 0
    minimum = min(lst) if lst else None
    maximum = max(lst) if lst else None

    return {
        'unique_numbers': unique_numbers,
        'average': average,
        'min': minimum,
        'max': maximum
    }


numbers = [1, 2, 3, 4, 4, 5, 5, 6]
result = analyze_list(numbers)
print(result)

2
d = {
    "dan": 35,
    "gad": 55,
    "ron": 35,
    "bob": 39,
    "gon": 88
}


def filter_dict(d, threshold):
    s = []
    for key, value in d.items():
        if value > threshold:
            s.append(key)

    return s


print(filter_dict(d, 36))
