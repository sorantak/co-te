print('세 정수의 최댓값 구하기')
a = int(input('정수 a의 값: '))
b = int(input('정수 b의 값: '))
c = int(input('정수 c의 값: '))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c

print(f'최댓값은 {maximum}')

# 포맷 문자열 리터럴(간단히 f-문자열이라고도 합니다)은 문자열에 f 또는 F 접두어를 붙이고 표현식을 {expression}로 작성하여 문자열에 파이썬 표현식의 값을 삽입할 수 있게 합니다. 선택적인 포맷 지정자가 표현식 뒤에 올 수 있습니다.
# https://docs.python.org/ko/3/tutorial/inputoutput.html