# from 에는 폴더 명과 파일명까지 적어 줘야 한다 impotr 모듈에 정의되어진 것들을 불러온다
from module.mod_test import *
from module.asd.test import * #모듈에 정의 된거 저부 불러오기
# from module.asd.test import name as asd #함수 이름 바꾸기
# from module.asd.test import a as myName #변수 이름 바꾸기
from module.asd.test import name as asd, a as myName
print(sub(4,1))
print(asd('고'))
print(name(myName))