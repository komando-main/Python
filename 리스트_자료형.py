a=[]
b=[0,1,2,3,4]
c=['Life', 'is', 'too', 'short']
d=[1,2, 'Lift', 'is']
e=[1,2,['Life', 'is']]
print(a)
print(b)
print(c)
print(d)
print(e[2][1])
print(b[2]+b[1])
print(e[-1])
print(e[-1][0])
print(b[:2])
print(b[2:])
print(b[1:3])
z=[5,6,7,8,9]
f=b+z
print(f)
a=b+[0,1,2,3,4]
print(a)
a=b*3
print(a)
print(len(a))
w=str(100)+" "+c[3]
print(w)
w='{0} {1}'.format(100, c[3])
print(w)
num=100
w=f'{num} {c[3]}'
print(w)
b[3]=10
print(b)
del b[3]
print(b)
b.append(3)
print(b)
b.sort()#문자열에도 사용 가능
print(b)
del b[0]
print(f"is 가 있는 배열 번호:{c.index('is')}, 참고로 배열은 0부터 시작하고 값이숫자인 경우도 배열번호 찾는다")
a=[0,1,2,4,5]
a.insert(3,3)
print(a)
a.remove(5)
print(a)
a.pop()
print(a)
a.pop(0)
print(a)
a.pop(1)
print(a)
a=[1,2,3,4,5]
b=[5,6,7,8,9]
a.extend(b)
print(a)
print(f'리스트 안에 5가 몇 개 있는지 {a.count(5)}')