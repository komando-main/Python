#튜플은 한번 지정하면 값을 변경 및 삭재가 불가능하다
#리스트와 다루는 법이 비슷하다
a=()
b=(1,)
c=(1,2)
d=(1,2,3,'a', 'b', 'c')
e=1,2,3
f=('a','b',('as', 'qw'))
print(c[1])
print(f[2][0])
print(d[2:])
print(e+c)
print(c*5)
print(len(f), len(f[2]))
print()
num=[1,2,3]
print(num)
q2=2,3,4
qq=(num,q2)
num[0]=3
num.append(5)
num.pop(0)
print(qq)
print(qq[0][2])
print(num)