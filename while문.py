# 1

prompt = '''
1.Add
2.Del
3.List
4.Quit
Enter number:'''
numder = 0
while numder != 4:
    print(prompt)
    numder=int(input())


# money=0
# coffee=5
# while coffee != 0:
#     if money < 300:
#         c=int(input(f'\n남은 커피{coffee}\n\n돈을 지불하세요\n현재 금액 {money}원 필요금액 300원\n투입:'))
#         money+=c
#     elif money >= 300:
#         coffee-=1
#         print(f'\n커피가 나옵니다.\n거스름 돈 {money-300}원\n')
#         money=0

# a=0
# while a < 10:
#     a+=1
#     if a % 2 == 0:
#         continue
#     print(a)

# while True:
#     print('Ctrl+C를 눌러야 while문을 빠저나갈 수 있습니다')