def roman_to_int(roman_string:str):
    if roman_string is None or type(roman_string) != str:
        return 0
    lists = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = [lists[p] for p in roman_string] + [0]
    y = 0

    for m in range(len(res) - 1):
        if res[m] >= res[m+1]:
            y += res[m]
        else:
            y -= res[m]

    return y
