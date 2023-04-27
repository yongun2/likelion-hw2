# 리스트(lists)
mbti = ['INFP', 'ENFP', 'ISTJ', 'ESTP',]
print(mbti)


mbti[0] = 'INFJ'
print(mbti)



my_list = [123, 'apple']
print(my_list)


colors = ['red', 'blue', 'green']
print(colors)

"""
    colors[2] = 'black'
    print(colors)
"""

"""
    colors.append('purple')
    print(colors)
"""

"""
    colors.insert(1, 'yellow')
    print(colors)
"""

"""
    del colors[0]
    print(colors)
"""

"""
    colors.pop(0)
    print(colors)
"""

colors.remove('blue')
print(colors)


# 리스트 정ㅕ
colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']
print(colors)
# 정렬 1
# colors.sort()
# print(colors)

# 역순으로 정렬 1
colors.sort(reverse=True)
print(colors)

# 정렬 2
after = sorted(colors)
print(colors,"\n", after)

# 길이 - 요소의 갯수
print(len(colors))


print('\n\n')
# 리스트 슬라이싱
colors = ['blue', 'red', 'gray', 'black', 'yellow', 'orange']

print(colors[1:5])
print(colors[:4])
print(colors[2:5])
print(colors[-5:])

print('\n\n')

# 같은 공간을 참조하게됨
colors_2 = colors

colors_2.pop()
print(colors)
print('\n\n')


scores = [88, 100, 96, 43, 65, 78]
for score in scores:
    print(score)

print('\n\n')

scores = [88, 100, 96, 43, 65, 78]
max_val = max(scores)
min_val = min(scores)
sum_val = sum(scores)

print(max_val, min_val, sum_val)



    