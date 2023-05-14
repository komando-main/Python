#딕셔너리는 키값이 중복되면 기존키의 value 삭재되고 나중에 들어온 value로 저장된다
#키값은 튜플()로 가능하나 리스트[]는 불가능하다
a={'name':'민', 'phone':'0123456789', 'day':'1212'}
b={1:'qwe', 2:'qwe', 3:'zxc'}
c={'qwe':1, 'asd':2, 'zxc':3}
d={'qwe':[1,2,3], 'asd':[4,5,6]}
print(a[next(iter(a))])
print(a['name'])
print(b[1])
print(d['qwe'][0])
print(d['asd'][2])
a[3]='와웅'
a['우와']=123
aa='qq'
bb=11
a[bb]=aa
print(a)
qwe=11
print(a[qwe])
cc=123, 'asd'
ll=456
a[cc]=ll
print(a)
print(a[cc])
print(a[123,'asd'])#키가 튜플이면 튜블로 불러와야 한다
#print(a[123])
#print(a['asd'])
a[cc]=123
print(a)
print(a.keys())
print(a.values())
uu=list(a.values())
print(uu)
print(uu[3])
gg=list(a.keys())
print(gg)
print(gg[6][0])
ee=list(c.keys())
print(ee)
print(a.items())
print(a.get(gg[6]))
print(a.get('day','어서업쎠'))
print(a.get('어서업쎠','없는 키'))
print('어서업쎠' in a)
a.clear()
print(a)