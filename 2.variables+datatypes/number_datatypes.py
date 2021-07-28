# 숫자 자료형
# 정수형
a = 154
print(type(a))
a = 0
print(type(a))
a = -25
print(type(a))

# 실수형
b = 181.34
print(type(b))
b = -22.22
print(type(b))

# 복소수형
c = 1 + 4j
print(type(c))
print(c.real)
print(c.imag)
print(c.conjugate())
print(abs(c)) # 루트(1 + 4*4 = 17) = 4.12

# 예제 : 스스로 사칙연산을 활용해가며 확인해보자
a = 5
b = 3.14
c = 3 + 4j
print(10*a + 3*b + c)
