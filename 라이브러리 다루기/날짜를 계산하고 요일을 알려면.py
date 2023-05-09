#두 날짜의 차이 구하기
import datetime
day1=datetime.date(2019, 12, 14)
print(day1)
day2=datetime.date(2021, 6, 5)
print(day2)
diff = day2-day1
print(diff.days)#days는 ()가 없어야 오류가 안나다


#요일 확인 하기
day=datetime.date(2019, 12, 14)
print(day.isoweekday()) #1~7으로 표기 하며 1번 월요일 ~ 7번 일요일

#두 날자의 차이 계산 하기
today = datetime.date.today()#오늘 날자 불러오기
diff_day = datetime.timedelta(days=100)
print(today+diff)
print(today-diff)

#윤년 확인하기 그레고리력 2월29일
import calendar #이모듈은 윤년을 확이하는 모듈이다
# def is_leap_year(year):
#     match (year % 400, year % 100, year % 4):
#         case (0, _, _):
#             print("윤년")
#         case (_, 0, _):
#             print("평년")
#         case (_, _, 0):
#             print("윤년")
#         case (_):
#             print(year)
print(calendar.isleap(0))
print(calendar.isleap(1))
print(calendar.isleap(4))
print(calendar.isleap(1200))
print(calendar.isleap(700))
print(calendar.isleap(2020))