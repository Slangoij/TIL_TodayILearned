# 04. Pandas 시각화
- 판다스 자체적으로 matplotlib 기반의 시각화 기능 지원
- Series나 DataFrame에 plot()함수나 plotaccessor를 사용

### 1. plot()
- 막대 그래프
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

tips = pd.read_csv('data/tips.csv')
# 성별: 남성, 여성의 수
# plt.figure(figsize=(10,10))
tips['sex'].value_counts().plot(kind='bar',figsize=(7,7))
# Series.bar(): index가 x축, value가 Y축

plt.title('성별 손님수')
plt.xlabel('손님수')
plt.ylabel('성별')
plt.show()
```
  - 두 개의 분류 별로 그리기
  ```python
  import matplotlib as mpl
  
  # 요일(day)-성별(sex) 손님의 총수(size)
  # DF의 index: ticks - 1차 그룹, columns-각 tick마다 나눠져 나옴 - 2차 그룹
  tips.pivot_table(index='day', columns='sex', values='size', aggfunc='sum').plot.bar() # plot(kind='bar')
  ```
  

- 파이차트
```python
tips['day'].value_counts().plot.pie(figsize=(7,7), autopct='%.2f%%')
```

- 히스토그램, KDE(밀도그래프)
```python
# tips['total_bill'].plot.hist(figsize=(6,6), bins=20)
tips['total_bill'].plot(kind='hist', figsize=(6,6), bins=20)
plt.show()

tips['total_bill'].plot.kde()
plt.show()
```

- Boxplot(상자그래프)
```python
# Series
tips['total_bill'].plot.box()
plt.show()

# DataFrame
tips[['total_bill','tip']].plot(kind='box', figsize=(7,7))
plt.show()
```

- Scatter plot(산점도)
```python
tips.plot(kind='scatter', x='total_bill', y='tip', figsize=(6,6)) # x에 올 컬럼명, y에 올 컬럼명
plt.show()

tips[['total_bill', 'tip']].corr()
```


- 파이썬의 날짜/시간 다루기
  - datetime 모듈
    - datetime 클래스 - 날짜/시간
    - date: 날짜
    - time: 시간
```python
import datetime # module

c = datetime.datetime.now() # 현재일시를 datetime객체로 반환
# 특정 일시
date = datetime.datetime(2000,4,5)

print(date2.year, date2.month, date2.day, date2.hour, date2.minute, date2.second)
print('요일:', date2.weekday()) # 0: 월요일 6: 일요일

date2.isocalendar() # (년도, 주차, 요일) # 요일: 월-1, 일-7

# datetime -> 문자열
# datetime.strftime('format문자열')
# %Y: 4자리 년도, %m: 월, %d: 일, %H: 시간(24), %M: 분, %S: 초
date2.strftime('%Y/%m/%d %H:%M:%S')

# 문자열 -> datetime
# strptime
d = datetime.datetime.strptime("2020/10/20", '%Y/%m/%d')
d.day

# day: 일, hour: 시간, minute: 분, second:초
# week: 주
# dayofweek: 요일(0: 월 ~ 6: 일)
# dayofyear
# isocalendar() - (년, 주차, 요일) 1: 월 ~ 7: 일 => DataFrame

# datetiem 타입의 index를 생성
# pd.date_range(시작날짜, freq='변화규칠', periods='개수') # 규칙적으로 증가/감소하는 datetime값을 가지는 index를 생성

pd.date_range('2000/1/1', freq='M', periods=5) # 2000/1/1부터 1개월씩 증가하는 날짜 5개 생성
pd.date_range('2000/1/1', freq='MS', periods=5)
pd.date_range('2000/1/1', freq='Y', periods=5)
pd.date_range('2000/1/1', freq='YS', periods=5)

# freq - 간격 지정 문자(Y: 년, M: 월, D: 일, H: 시간, T:분, S: 초)
#        YS, MS, HS, TS : 첫번째 날짜/시간. S생략: 마지막
# 문자 앞에 정수: 간격

pd.date_range('2000/1/1', freq='8D', periods=5)
pd.date_range('2000/1/1', freq='-7H', periods=5)
```
