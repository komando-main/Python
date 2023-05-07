# result=0
# i=0
# while i <= 1000:
#     if i % 3 == 0:
#         result+=i
#     i+=1
    
# print(result)

# i=0
# while i < 5:
#     i+=1
#     print(" "*(5-i)+"*"*i+"*"*i)

# a="*"
# b=" "
# f=0
# c=5

# while f < 5:
#     print((b*c)+(a*f)+(a*f)+(a))
#     c-=1
#     f+=1
# while c < 6:
#     print((b*c)+(a*f)+(a*f)+(a))
#     c+=1
#     f-=1

# i=0
# while True :
#     i+=1
#     if i > 5 :break
#     print("*"*i)

# for i in range(1, 101):
#     print(i)

a=[70,60,55,75,95,90,80,80,85,100]
total=0
# print(len(a))
for score in a:
    total+=score

average= total / len(a)
print(f'{average:0.2f}')

numbers=[1,2,3,4,5]
result=[num * 2 for num in numbers]
print(result)