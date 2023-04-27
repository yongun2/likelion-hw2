# 함수(Functions)

def print_name(name):
    print(name)

print_name("김멋사")
print_name("이멋사")

print("\n\n")

def print_ex_string():
    print("예시 문자열입니다.")

print_ex_string()
print('\n\n')


def order_coffee(qty, option='hot'):
    print(f"{qty}잔 / {option}")

order_coffee(3, "iced")
order_coffee(3)
print("\n\n")

order_coffee(option="iced", qty=5)
print("\n\n")

def get_id(email:str) -> str:
    
    email_id = email.removesuffix("@test.com")
    print(email_id)

    return email_id

get_id("user@test.com")
