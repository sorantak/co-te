print('입력한 수만큼 1부터 정수의 합을 구합니다.')
n = int(input('Input a number: '))

sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print(f'1부터 {n}까지 합은 {sum}입니다.')