#자료에 이름을 붙이려면
from collections import namedtuple #자료에 이름 붙이지

#사용한 단어의 겟수를 구하자
from collections import Counter #사용한 단어 겟수 구하기 (겹치는 단어 겟수)
import re #정규 표현식을 사용

#딕셔너리 한번에 초기화하는 방법
from collections import defaultdict


# ------------------------------------------------자료에 이름 붙이기----------------------------------------------------------
data = [
    ('홍길동', 23, '01099990001'),
    ('김철수', 31, '01099991002'),
    ('이영희', 29, '01099992003'),
]

cEmployee = namedtuple('Employee', ['name', 'age', 'cellphone'])#라이브러리 선언하기 첫번째 인자의 'Employee'는 튜플의 이름(Key) 라고 보면 된다

# data=[Employee(emp[0],emp[1], emp[2]) for emp in data] #이런식으로도 가능하다

data=[cEmployee._make(emp) for emp in data]#간단한 방법

emp=data[0]#객체 선택 Employee(name='홍길동', age=23, cellphone='01099990001')

new_emp = emp._replace(name='박길동')#선택 되어진 기존의 객체를 바꾸는것이 아닌 새로운 객체를 생성하여 바꾸는거다

print(emp.name)
print(new_emp) #Employee(name='박길동', age=23, cellphone='01099990001') 새로운 객체 생성

print(emp.age)

print(emp.cellphone)
# --------------------------------------------end-------------------------------------------------


# ------------------------------------------사용한 단어의 겟수 확인--------------------------------
data ="""
산에는 꽃이 피네
꽃이 피네
갈 봄 여름 없이
꽃이 피네

산에
산에
피는 꽃은
저만치 혼자서 피어 있네

산에서 우는 작은 새여
꽃이 좋아
산에서
사노라네

산에는 꽃 지네
꽃이 지네
갈 봄 여름 없이
꽃이 지네
"""
words = re.findall(r'\w+', data) # r은 정규표현식이 원시 문자열(raw string)임을 알려주는 문자
counter = Counter(words)
print(counter)
print(counter.most_common(1))#.most_common(1) 겹치는 단어중 많이 겹치는 단어 위주로 튜플 반환한다 ******배열의 인덱스 번호 아님******
print(counter.most_common(2))
print(counter.most_common(3))
# ----------------------------------------------------end-----------------------------------------------------------

# ---------------------------------------------------------딕셔너리 한번에 초기화하는 방법--------------------------------------
text = "Life is too short, You need pytnon."

#방어적 코드
d=dict()
for key in text:
    if key not in d:
        d[key]=0 #d 바인드에 대한 초기화 포문 돌때마다 초기화 함으로 비효율적이다
    d[key]+=1
print(d)
#결과물 {'L': 1, 'i': 2, 'f': 1, 'e': 3, ' ': 6, 's': 2, 't': 3, 'o': 5, 'h': 1, 'r': 1, ',': 1, 'Y': 1, 'u': 1, 'n': 3, 'd': 1, 'p': 1, 'y': 1, '.': 1}


#초기화 하는법
a= defaultdict(int) #정수 타입으로 초기화 한다
for key in text:
    a[key]+=1 #초기화 없이 쓸경우 오류 난다
print(a)
#결과물: defaultdict(<class 'int'>, {'L': 1, 'i': 2, 'f': 1, 'e': 3, ' ': 6, 's': 2, 't': 3, 'o': 5, 'h': 1, 'r': 1, ',': 1, 'Y': 1, 'u': 1, 'n': 3, 'd': 1, 'p': 1, 'y': 1, '.': 1})

print(a['s'])
#결과물: 2