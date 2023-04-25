# 숫자(numbers)

import struct


a = 2
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)

print("\n\n\n\n")
# 제곱
print(a ** b)
print("\n\n\n\n")

print((a + b) * b)
print("\n\n\n\n")

print(a + b * b)

print("\n\n\n\n")

print(a // b) # 몫
print("\n\n\n\n")

print(a % b) # 나머지
print("\n\n\n\n")



# 실수(Float) - 십진 부동 소수점
x = 0.1
y = 0.2

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print("\n\n\n\n")
print(x + y == 0.3)
print("\n\n\n\n")

# 수치가 큰 데이터 가독성 좋게 하기
price = 12_349_000_000_000
print(price)
print("\n\n\n\n")

# 상수(constant)
PI = 3.141592

PI = 1.23
print(PI)
print("\n\n\n\n")


# 문자열 - 숫자 간 변환
a = 100
b = "100"

# 숫자 -> 문자열로 변환하기
a = str(a)
print(type(a))
print("\n\n\n\n")


# 문자 -> 숫자로 변환하기
b = int(b)

print(type(b))


