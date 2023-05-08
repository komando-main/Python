# a=input('숫자를 입력하세요:')
# print(a)

# print("a" "b" "c" "d")
# print("a"+"b"+"c"+"d")
# print("aa", "bb", "cc", "dd")

# for i in range(10):
#     print(i, end=' ')

# open("생성 및 읽을 파일", "옵션") 옵션에는 3가지 r=읽기모드 w=쓰기모드(기존 파일 열면 전부 사라진다 주의) a=추가모드(마지막 열에 데이터추가)
# f=open('안녕.txt', 'w')
# f.close()

# f=open('c:/kmj/참 쉬운대.txt', 'w')
# for i in range(1,11):
#     data = f'{i}번째 줄 입니다\n'
#     f.write(data)#들여쓰기 하고 안하고 차이가 있내.. 들여쓰기 안하면 마지막 1번 출력 하고 만다
# f.close()

# f=open('c:/kmj/참 쉬운대.txt', 'r')
# while True:
#     line = f.readline()#1줄씩 객체로 받는다
#     if not line: break
#     print(line)
# f.close()

# f= open('c:/kmj/참 쉬운대.txt', 'r')
# date = f.readlines()#리스트로 받는다
# f.close()
# print(date)

# f=open('c:/kmj/참 쉬운대.txt', "r")
# data= f.read()#전채 내용 읽기
# f.close()
# print(data)

# f=open("c:/kmj/참 쉬운대.txt", "a")
# for i in range(11, 20):
#     data = f'{i}번째 줄 입니다\n'
#     f.write(data)
# f.close()
# user=input("저장할 내용을 입력 하세요:")
# with open('c:/kmj/잼있다1.txt', 'w') as f:
#     f.write(user+'\n')
with open('c:/kmj/잼있다3.txt', 'w') as f:
    f.write('안녕하세요~!')