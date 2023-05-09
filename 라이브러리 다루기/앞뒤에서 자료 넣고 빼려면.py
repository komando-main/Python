from collections import deque
a=[1,2,3,4,5]
#2칸 뒤로 밀기
d=deque(a)#.rotate(2) 바로 사용 불가능 하다 에러남
d.rotate(2)
# d.appendleft(x)#왼쪽 에 x값 삽입 리스트보다 빠르며 스레드 환경에서 안전하다
# d.popleft()#왼쪽 첫번째 값 삭재 리스트보다 빠르며 스레드 환경에서 안전하다
result=list(d)
print(result)