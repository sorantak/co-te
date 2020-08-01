def med3(a, b, c):
    if a >= b:
        if b >= c:
            return b
        elif a <= c:
            return a
        else:
            return c
    elif a > c:
        return a
    elif b > c:
        return c
    else:
        return b

print('Get median from 3 numbers.')
a = int(input('Input integer a.: '))
b = int(input('Input integer b.: '))
c = int(input('Input integer c.: '))

print(f'Median is {med3(a, b, c)}.')