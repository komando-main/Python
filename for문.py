test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a=[(1,2), (3,4), (5,6)]
for (first, last) in a:
    print(first + last)

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number+=1
    if mark >= 60:
        print(f'{number}번 학생은 {mark}점으로 합격 입니다')
    else:
        print(f'{number}번 학생은 {mark}점으로 탈락 입니다')

add=0
for i in range(1,11):
    add+=i
    
print(add)

for num in range(len(marks)):
    if marks[num] < 60:
        continue
    print(f'{num+1}학생은 {marks[num]}점으로 합격입니다')

add=0
for i in range(1,101):
    add+=i
print(add)

for i in range(2,10):
    for j in range(1,10):
        print(f'{i} * {j} = {i*j}')

a=[1,2,3,4]
result = []
for num in a:
    result.append(num*3)
print(result)

a=[1,2,3,4]
result = [num*3 for num in a]
print(result)

a=[1,2,3,4]
result=[num * 3 for num in a if num % 2 == 0]
print(result)

result=[x*y for x in range(2,10)
            for y in range(1,10)]
print(result)