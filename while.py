# 1 에서 5까지 의 총 합 구하기
# i = 1
# j = 0
# while i <= 5:
#     j += i
#     i+=1

# print(j)

# 구구단 3 단 8단 구하기
# i = 1
# j = 1
# while i < 10:
#     while i == 3 and j < 10: #중간에 브래이크를 못 시킴
#         i+=1
#         j+=1
#         print(f"{i} {j}")
#     print(f" while 1번 안  {i}")
#     i+=1

# for i in range(1, 10):
#     for j in range (1,10):
#         if i == 3:
#             print(f"{i} * {j} = {i*j}")
#     for j in range(1, 10):
#         if i == 8:
#             print(f"{i} * {j} = {i*j}")
i = 1

while i < 10:
    j = 1
    if i == 3:
        print(f"====== {i}단 =====")
    elif i == 8:
        print()
        print(f"====== {i}단 =======")

    while i == 3 and j < 10:
        print(f"{i} * {j} = {i*j}")
        j+=1
    while i == 8 and j < 10:
        print(f"{i} * {j} = {i*j}")
        j+=1
    i+=1

i = 20
j = 35
a = 0
while i <= j:
    if i % 3 == 0:
        print(f"{i}")
        a += i
        print(f"3의 배수 더한 값 {a}")
    i+=1