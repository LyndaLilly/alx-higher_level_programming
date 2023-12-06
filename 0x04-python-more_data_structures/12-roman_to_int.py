#!/usr/bin/python3
def ytract(c):
    y = 0
    x = max(c)

    for n in c:
        if x > n:
            y += n

    return (x - y)


def roman_to_int(roman_string):
    if not roman_string:
        return 0

    if not isinstance(roman_string, str):
        return 0

    z = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    a = list(z.keys())

    num = 0
    b= 0
    c = [0]

    for ch in roman_string:
        for r_num in a:
            if r_num == ch:
                if z.get(ch) <= last_rom:
                    num += ytract(c)
                    c = [z.get(ch)]
                else:
                    c.append(z.get(ch))

                b= z.get(ch)
    num += ytract(c)

    return (num)
