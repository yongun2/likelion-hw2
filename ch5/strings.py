# 문자열(Strings) = 문자의 나열

city = "seoul"
print(city)

# 대문자로 변경
print(city.upper())

#소문자로 변경
city = city.upper()

city = city.lower()
print(city)

occupation = "developer    "
print(occupation)

print(occupation.rstrip())

occupation = "    developer"
print(occupation)

print(occupation.lstrip())

occupation = "    developer    "
print(occupation)

print(occupation.strip())

print("INFP\nENFP\nISTJ\nESTJ\n")

# prefix 제거하기
score = "점수:90"
print(score.removeprefix("점수:"))

# suffix 제거하기
score_2 = "75점"
print(score_2.removesuffix("점"))


# 문자열 포맷팅
city = "서울 중구"
print(city.replace("서울", "서울시"))

si_1 = "용인"
gu_1 = "기흥"

si_2 = "서울"
gu_2 = "종로"

# 서울시 종로구
# 용인시 기흥구
# (시의 이름)시 (구의 이름)구
print(f"{si_1}시 {gu_1}구")
print(f"{si_2}시 {gu_2}구")

address_1 = f"{si_1}시 {gu_1}구"
print(address_1)
