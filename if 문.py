money=True
if money:
    print('개임 사자')
else:
    print('돈 벌자')

money=2000
if money >= 3000:
    print('돈은 충분하다')
else:
    print('더 모아야 한다')
card=True
if money >= 3000 or card:
    print('돈은 있다')
else:
    print('카드로 때운다')

a=[1,2,3]
b= 1 in a
print(b)

a=['a','b','c']
b='b' not in a
print(b)

pocket=['poper','cellphone']
card=True
if 'moner' in pocket:
    print('돈내고 사먹자')
elif card:
    print('카드로 사먹자')
else:
    print('굶어라')
    
if 'money' in pocket:
    pass
else:
    print('카드로 때워라')
    
message='돈있다 게임사자' if money >= 6000 else '개임 가격대 2000원 으로'
print(message)