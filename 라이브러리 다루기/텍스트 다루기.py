#문자열 줄여 표지할때 사용
import textwrap
a=textwrap.shorten("Life is short, you need python.", width=15)
print(f'{a}\n')

b=textwrap.shorten("인생은 짧으니 파이썬이 필요해.", width=15, placeholder='...')
print(f'{b}\n')

#긴 문장 줄 바꿈
long_text='Life is too short, you need python. ' * 10
# result=textwrap.wrap(long_text, width=70)
# print('\n'.join(result))
result=textwrap.fill(long_text, width=70)#1줄에 70자가 넘지 않음
print(result)

#정규 표현식
import re
data = """
홍길동의 주민 등록 번호는 999999-9999999 입니다
그리고 고길동의 주민 등록 번호는 999999-9999999 입니다
그러다면 누가 형님일까요?
"""
# result=[]
# for line in data.split('\n'):
#     word_result = []
#     for word in line.split(" "):
#         if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
#             word=word[:6] + '-' + '*******'
#         word_result.append(word)
#     result.append(' '.join(word_result))
# print("\n".join(result))

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))