from copy import copy
a = [1,2,3]
print(id(a))
a1 = a
print(id(a1))
b = a1
print(id(b))
c = id(a)==id(b)==id(a1)
print(c)
d = a is b is a1
print(d)
e=a[:]
f=copy(a)
a1[0]=5
#e=a[:] #위치에따른 값이 변화가 있다 정확히는 a1[0]=5 실행되기 전 후 에 따라 값이 바뀌고 안바뀌고 한다
print(id(e))
print(e)
print(b[0])
print(e is a)
# f=copy(a) #위와 동일하게 a1[0]=5 전 후로 값이 바뀌고 안바뀌고 한다
print(f)
print(f is a1)
a, b=('qwe','asd')
print(a)
print(b)
(c, d)= 'zxc', 'qaz'
print(c)
print(d)
(w,a)=('asd','qwe')
print(w)
print(a)
[r,q]=['asd','zxc']
print(r)
print(q)
r=t=y='lll'
print(r)
print(t)
print(y)
l=3
o=6
print(l,o)
l,o=o,l
print(l,o)