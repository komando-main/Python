#중복을 허용하지 않는다
#순서가 없다
s1=set([1,2,3])
print(s1)
s2={1,2,3}
print(s2)
st1='hello'
s3=list(set(st1))
print(s3)
l1=[1,2,3,4,5]
l2=[3,4,5,6,7]
ss1=set(l1)
print(ss1)  
ss2=set(l2)
print(ss2)
ss3=list(ss1 & ss2)
print(ss3)
ss4=list(ss1|ss2)
print(ss4)
ss5=list(ss1-ss2)
print(ss5)
ss6=list(ss2-ss1)
print(ss6)
ss11=list(ss1.difference(ss2))
print(ss11)
ss22=list(ss2.difference(ss1))
print(ss22)
ss11=set(ss11)
ss11.add(3)
print(ss11)
ss11.update([4,5,6])
print(ss11)
ss11=list(ss11)
ss11=set(ss11)
ss11.remove(4)
print(ss11)
ss11=list(ss11)#.pop(2) #호 좀 틀리내 선택된 인덱스 값을 1개만 반환 한다
ss11.pop(1)#선택 된 인덱스 1개만 지운다
print(ss11)