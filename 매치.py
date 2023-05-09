a=15

match (a%2, a%4, a%5):#조건식
    case (0,0,0):#비교
        print(f'0번{a}')
    case (0,_,_):
        print(f'1번{a}')
    case (_,0,_):
        print(f'2번{a}')
    case (_,_,0):
        print(f'3번{a}')
    case (_,_,_):
        print(f'4번{a}')