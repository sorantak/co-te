print('입력한 수만큼 1부터 정수의 합을 구합니다.')
n = int(input('Input a number: '))

sum = 0
for i in range(1, n + 1):
    sum += i

print(f'1부터 {n}까지 합은 {sum}입니다.')