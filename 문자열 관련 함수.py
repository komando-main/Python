a="hobby"
print(a.count('b'))

a="Python is the best choice"
print(a.find('b'))
print(a.find('k'))

a=","
print(a.join('abcd'))

a=","
print(a.join(['asd', 'qwe', 'zxc', 'qaz']))

a='hi'
print(a.upper())

a='HI'

print(a.lower())

a=' asd'
print(a, len(a))
b=a.lstrip()
print(b, len(b))

a='asd '
print(a, len(a))
b=a.rstrip()
print(b, len(b))

a=' a s d f g a '
print(len(a))
b=a.strip()
print(b, len(b))

a=' a s d f g a '
print(len(a))
b=a.replace(" ", "")
print(b, len(b))

a=' a s d f g a '
b=a.replace(" ", "띄어쓰기")
print(b, len(b))

a='Lift is too short'
b=a.split()
print(b)

a='Lift / is / too / short'
b=a.replace(" ", "").split("/")
print(b)