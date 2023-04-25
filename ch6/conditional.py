# 조건문

if True:
    print("True")



"""
    value = input("값을 입력해주세요: ")

    if int(value) > 10:
        print("a")
    else:
        print("b")
"""

"""
    value = input("값을 입력해 주세요.")

    value = value.upper()

    if value == "INFP":
        print("INFP")
    else:
        print("nothing")
"""

day = input("요일을 입력해주세요(0~6): ")
# 다중조건문
if day == "0":
    print("휴무")
elif day == "6":
    print("단축영업")
else:
    print("정상영업")
    
