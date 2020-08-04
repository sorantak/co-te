print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('Input a: '))
b = int(input('Input b: '))

# 숫자 크기를 오름차순으로 정렬
# 우변에 튜블 (b, a)가 생성됨 -> 대입할때 튜플이 풀어져 각각을 a, b에 대입함
if a > b:
    a, b = b, a

sum = 0
for i in range(a, b + 1):
    sum += i

print(f'{a}부터 {b}까지 합은 {sum}입니다.')