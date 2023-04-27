
fruits = ['apple', 'banana', 'strawberry']


try :
    fruits[3]
except:
    print("인덱스를 참조할 수 없습니다.")
else:
    print("정상 수행")
finally:
        print("명령 수행")
        