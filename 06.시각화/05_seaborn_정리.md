# 5. Seaborn
- matplotlib을 기반으로 한 다양한 테마 및 그래프 지원하는 파이썬 시각화 패키지
- 아나콘다에 기본적으로 포함
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('seaborn')

# tips = pd.read_csv('data/tips.csv') # 이것 대신
tips = sns.load_dataset('tips')
tips
```
- 그래프 종류
  - rugplot, kdeplot, distplot : 1차원 연속형 값 분포
  - boxplot, violinplot, swamplot : 연속형 데이터 분포
  - countplot : 막대(범주형)
  - scatterplot, lmplot, jointplot, pairplot : 산점도
  - heatmap : 값들의 상관성 2차원
  - lineplot : 시계열

### 01. rugplot
- 각 데이터들의 위치를 보여준다.
```python
plt.figure(figsize=(6,6))
sns.rugplot('total_bill', data=tips)
plt.show()
# 컬럼명: 문자열
# data: DataFrame객체
```

### 02. kdeplot
- 히스토그램을 부드러운 곡선 형태로 표현한다. 
- KDE(Kernel Density Estimation) : 확률밀도추정
```python
plt.figure(figsize=(6,6))
# sns.kdeplot(tips['total_bill'])
sns.kdeplot('total_bill', data=tips)
plt.show()
```

### 03. distplot
- 히스토그램에 kdeplot, rugplot 한번에 그린다.(default: kdeplot만)
```python
plt.figure(figsize=(7,7))
sns.distplot(tips['total_bill'],
            hist=True,
            kde=True,
            rug=True)
plt.show()
# distplot은 dataframe과 컬럼을 나눠서 지정하는 구문 불가
```

### 04. boxplot
- 히스토그램에 kdeplot, rugplot 한번에 그린다.(default: kdeplot만)
```python
plt.figure(figsize=(6,6))
plt.subplot(1,2,1)
sns.boxplot(y=tips['total_bill']) # 수직
plt.title('수직 boxplot')
plt.subplot(1,2,2)
sns.boxplot(x=tips['total_bill'])
plt.title('수평 boxplot')
plt.show()

plt.figure(figsize=(7,7))
sns.boxplot(y='total_bill', x='smoker', hue='sex',  data=tips)
# x(y)축: 분포를 보려는 연속형 값의 컬럼, y(x)축: 그룹을 나누려는 범주형 컬럼
plt.show()
```


### 05. violinplot
- boxplot 위에 분포 밀도(kernel density)를 좌우 대칭으로 덮어쓰는 방
```python
# 요일(day)별 tip의 분포
plt.figure(figsize=(10,7))
sns.violinplot(y='tip', x='day', hue='smoker', data=tips) # 요일-흡연여부
plt.show()
```

### 06. swarmplot
- swarmplot은 실제 값이 있는 위치에 점을 찍으므로 정확한 위치 파악에 용이
```python
plt.figure(figsize=(5,5))

sns.boxplot(x='smoker', y='tip', data=tips)
sns.swarmplot(x='smoker', y='tip', data=tips, color='black')

plt.show()
```

### 07. countplot
- 막대그래프(bar plot)을 그리는 함수
- 범주형 변수의 고유값의 개수를 표시
- matplotlib의 bar()
```python
# 요일별-흡연여부별로
plt.figure(figsize=(7,7))

sns.countplot(x='day', hue='smoker', data=tips)

plt.show()
```

### 08. scatterplot
- 막대그래프(bar plot)을 그리는 함수
- 범주형 변수의 고유값의 개수를 표시
- matplotlib의 bar()
```python
# 성별로 나눠서 확인
plt.figure(figsize=(6,6))
sns.scatterplot(x='total_bill', y='tip', hue='sex', data=tips, palette='cool')
# colormap 지정: matplotlib/pandas - cmap, seaborn - palette
plt.show()
```

### 09. implot(lm-Linear Model)
- 선형회귀 적합선을 포함한 산점도를 그린다.
```python
sns.lmplot(x='total_bill', y='tip', hue='smoker', data=tips, height=7)
plt.show()
```

### 10. jointplot
- scatter plot 과 각 변수의 히스토그램을 같이 표기, DataFrame만 사용 가능
```python
sns.jointplot(x='total_bill', y='tip', data=tips)
plt.show()
```

### 11. pairplot
- 다변수(다차원) 데이터들 간의 산점도를 보여준다. 
- 데이터프레임을 인수로 받아 그리드(grid) 형태로 각 변수간의 산점도 표기
- 같은 변수가 만나는 대각선 영역에는 해당 데이터의 히스토그램 표기
```python
sns.pairplot(tips)
plt.show()
```

### 12. heatmap
- 값들의 상관관계 2차원 자료로 색으로 구현
```python
sns.heatmap(tips.corr(), annot=True, cmap='Blues')
```

### 13. lineplot
- 선그래프
- 시간의 흐름에 따른 값의 변화(시계열 데이터) 시각화에 유용
```python
index = pd.date_range('2021/1/1', freq='D', periods=10)
value = np.random.randint(1,100,size=(10,3))
df = pd.DataFrame(value, index=index, columns=list('ABC'))

plt.figure(figsize=(10,5))
sns.lineplot(x=df.index, y='A', data=df)
plt.xticks(df.index, rotation=45)
plt.show()
```
