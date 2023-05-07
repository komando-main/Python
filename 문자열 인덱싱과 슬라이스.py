a = 'Life is short, You need Python'
print(a[0])
print(a[3])
print(a[12])
print(a[-0])
print(a[-2])
print(a[-5])
print(a[:4])
print(a[8:13])
print(a[0:0])
print(a[:])
print(a[0:1])
print(a[-1])
print(a[24:])
a = '20010331Rainy'
date=a[:8]
year=a[:4]
day=a[4:8]
weather=a[8:]
print(date)
print(year)
print(day)
print(weather)
a=a[:4]+'-'+a[4:6]+'-'+a[6:8]+'-'+a[8:]
print(a)
a = '2001%c03%c31%cRainy' %('-','-','-')
print(a)
a='성공 확율 %0.3f%% 여도 도전한다' %0.12345
print(a)
number=10
no='없다'
a='이 상자에 %d개의 감자가 %s' %(number, no)
print(a)
a='이 상자에 {0}개의 감자가 {1}'.format(number, no)
print(a)
a="'{0:<10}'".format('hi')
print(a)
a="'{0:>10}'".format('hi')
print(a)
a="{asd}".format(asd=111)
print(a)
a="{{and}}".format()
print(a)
num=38
a=f'나는 올해 만으로 {num} 이고 다음 연도에는 {num+1} 이다'
print(a)
a={'name':'고민재', 'age':39}
b=f'My name {a["name"]} My age {a["age"]}'
print(b)
a=f'"{"hi":<10}"'
print(a)
a=f'"{"hi":>10}"'
print(a)
a=f'"{"hi":=^10}"'
print(a)
a=f'{"hi":!<10}'
print(a)
a=f'{"hi":!>10}'
print(a)
y=3.14159
a=f'{y:0.2f}'
print(a)
a=f'{{}}'
print(a)
print('2001%c03%c31%cRainy' %('-','-','-'))
print('%d' % 5)  