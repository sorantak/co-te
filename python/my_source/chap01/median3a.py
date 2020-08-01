def med3(a, b, c):
    if (b >= a and c <= a) or (b <= a and c >= a):
        return a
    elif (a > b and c < b) or (a < b and c > b):
        return b
    return c

    
print('Get median from 3 numbers.')
a = int(input('Input integer a.: '))
b = int(input('Input integer b.: '))
c = int(input('Input integer c.: '))

print(f'Median is {med3(a, b, c)}.')
