
"""
    f = open("./1.txt", "r", encoding="UTF-8")

    # print(f.read())
    print('\n\n')
    print(f.readline())


    f.close()
"""

f = open("./2.txt", "a", encoding="UTF-8")
f.write("새로운 글이 작성되었습니다.")
f.close()