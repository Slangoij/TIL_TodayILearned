# 01. groupby 관련 메소드

### 1. filter()
- 구문: `DataFrameGroupBy.filter(func, dropna=True, *args, **kwargs)`
- 특정 집계 조건을 만족하는 Group의 행들만 조회한다.
    1. DataFrameGroupBy의 group로 DataFrame을 함수에 전달한다.
    2. 함수는 받은 DataFrame을 이용해 집계한 값의 조건을 비교해서 반환한다.(반환타입: Bool) 
    3. 반환값이 True인 Group들의 모든 행들로 구성된 DataFrame을 반환한다.
- 매개변수
    - func: filtering 조건을 구현한 함수
        - 첫번째 매개변수로 Group으로 묶인 DataFrame을 받는다.
    - dropna=True
        - 필터를 통과하지 못한 group의 DataFrame의 값들을 drop, False로 설정하면 NA 처리
    - \*args, \*\*kwargs: filter 함수의 매개변수에 전달할 전달인자값.
  ```python
  import numpy as np
  import pandas as pd

  # cnt1 - 사과: 10대, 귤: 20대, 배: 단단위, 딸기 30이상
  data = dict(fruits=['사과', '사과','사과', '사과','사과','귤','귤','귤','귤','귤','배','배','배','배','배','딸기','딸기','딸기','딸기','딸기']
              ,cnt1=[10, 12, 13, 11, 12, 21, 22, 27, 24, 26, 7, 7, 8, 3, 2, 30, 35, 37, 41, 28]
              ,cnt2=[100,  103, 107, 107,  101,  51,  57, 58,  57, 51,  9, 9,  5,  7,  7,  208, 217, 213, 206, 204]
             )
  df = pd.DataFrame(data)

  # 사용자 정의 함수(람다 함수도 사용 가능)
  def check_cnt1_mean(x):
      """
      [매개변수]
          x: DataFrame (Group별로 나눈 DataFrame)
      [반환값]
          bool : x['cnt1']의 평균이 20이상인지 여부
      """
      return x['cnt1'].mean() >= 20

  df.groupby('fruits').filter(check_cnt1_mean)
  
  # 매개변수 있는 filter함수
  df.groupby('fruits').filter(check_mean, col='cnt1', threshold=30)
  ```

### 2. transform
  함수에 의해 처리된 값으로 원래 값들을 변경 후 반환
  DataFrame에 Group 단위 통계량을 추가시 유용
  - 구문: `DataFrameGroupBy.transform(func, *args)`, `SeriesGroupBy..transform(func, *args)`
      - func: 매개변수로 그룹별로 Series를 받아 Series의 값들을 변환하여 (Series로)반환하는 함수객체
          - DataFrameGroupBy은 모든 컬럼의 값들을 group 별 Series로 전달한다.
      - \*args: 함수에 전달할 추가 인자값이 있으면 매개변수 순서에 맞게 값을 전달한다. (위치기반 argument)
  - transform() 함수를 groupby() 와 사용하면 컬럼의 각 원소들을 자신이 속한 그룹의 통계량으로 변환된 데이터셋을 생성할 수 있다.
  - 컬럼의 값과 통계값을 비교해서 보거나 결측치 처리등에 사용할 수있다.
  ```python
  # 함수 정의
  def func(x):
    """
    [매개변수]
        x: Series - 그룹별 각 컬럼들을 Series로 전달
    [반환값]
        int : max - min
    """
    return x.max() - x.min()
  df.groupby('fruits').transform(func)
  
  # 람다식으로도 함수전달 가능
  df.groupby('fruits').transform(lambda x: x.max() - x.min())
  
  # 그룹별 평균을 transform을 이용해 조회
  cnt1_group_mean = df.groupby('fruits')['cnt1'].transform('mean')
  print(type(cnt1_group_mean))
  cnt1_group_mean
  
  # 결측치 변경(대체)
  # Series.fiilna(대체할 값)
  # 대체값: scalar - 동일한 값으로 대체
  #       : 배열형태(리스트, 시리즈, ndarray) - NA의 index와 동일한 인덱스에 있는 값으로 대체
  ```

### 3. pivot_table()
  엑셀의 pivot table 기능을 제공하는 메소드.    
  분류별 집계(Group으로 묶어 집계)를 처리하는 함수로 group으로 묶고자 하는 컬럼을 행과 열로 위치시키고 집계값을 값으로 보여준다.    
  역할은 groupby() 를 이용한 집계와 같다.

  > pivot() 함수와 역할이 다르다.   
  > pivot() 은 index와 column의 형태를 바꾸는 reshape 함수.

  - 구문: `DataFrame.pivot_table(values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All')`
  - **매개변수**
      - index
          - 문자열 또는 리스트. index로 올 컬럼들 => groupby였으면 묶었을 컬럼
      - columns
          - 문자열 또는 리스트. column으로 올 컬럼들 => groupby였으면 묶었을 컬럼 (index/columns가 묶여서 groupby에 묶을 컬럼들이 된다.)
      - values
          - 문자열 또는 리스트. 집계할 대상 컬럼들
      - aggfunc
          - 집계함수 지정. 함수, 함수이름문자열, 함수리스트(함수이름 문자열/함수객체), dict: 집계할 함수
          - 기본(생략시): 평균을 구한다. (mean이 기본값)
      - fill_value, dropna
          - fill_value: 집계시 NA가 나올경우 채울 값
          - dropna: boolean. 컬럼의 전체값이 NA인 경우 그 컬럼 제거(기본: True)
      - margins/margins_name
          - margin: boolean(기본: False). 총집계결과를 만들지 여부.
          - margin_name: margin의 이름 문자열로 지정 (생략시 All)
  ```python
  # 세로축(index)을 'AIRLINE'으로, 가로축(columns)을 'ORG_AIR'로 하여 'CANCELLED'데이터로 집계
  flights.pivot_table(values='CANCELLED', index='AIRLINE',
                    columns='ORG_AIR', aggfunc='sum')
  ```
  

- - -

# 02. 일괄처리 메소드

### 1. apply() - Series, DataFrame의 데이터 일괄 처리
  데이터프레임의 행들과 열들 또는 Series의 원소들을 일괄 처리가 가능하게 하는 함수
  - 구문: `DataFrame.apply(함수, axis=0, args=())`
      - 인수로 행이나 열을 받는 함수를 apply 메서드의 인수로 넣으면 데이터프레임의 행이나 열들을 하나씩 함수에 전달한다.
      - 매개변수
          - 함수: DataFrame의 행들 또는 열들을 전달할 함수
          - axis: **0-행을 전달, 1-열을 전달 (기본값 0)** G: 0이 행이다...
          - args: 행/열 이외에 전달할 매개변수를 위치기반(순서대로) 튜플로 전달
  - 구문: `Series.apply(함수, args=())`
      - 인수로 Series의 원소들을 받는 함수를 apply 메소드의 인수로 넣으면  Series의 원소들을 하나씩 함수로 전달한다.
      - 매개변수
          - 함수: Series의 원소들을 전달할 함수
          - args: 원소 이외에 전달할 매개변수를 위치기반(순서대로) 튜플로 전달객체.sort_index(axis, ascending=True)`
  ```python
  # 데이터를 처리할 사용자 함수
  def func(x):
    """
    apply()에 적용할 함수
    [매개변수]
        x: DataFrame에 적용시-Series, Series에 적용시-scalar
    [반환값]
        x를 처리한 결과
    """
    print(type(x))
    return x**2
    
  df.apply(func)
  
  # 간단한 함수는 람다식으로도 가능
  df.apply(lambda x: x**2)
  ```
  

### 2. cut()/qcut() - 연속형(실수)을 범주형으로 변환
  - cut() : 지정한 값을 기준으로 구간을 나눠 그룹으로 묶는다.
      - 구문: `pd.cut(x, bins,right=True, labels=None)`
      - 매개변수
          - x: 나눌 대상. 1차원 배열형태의 자료구조
          - bins: 나누는 기준값(구간경계)을 리스트로 전달
          - right: 구간경계의 오른쪽(True)을 포함할지 왼쪽(False)을 포함할지
          - labels: 각 구간의 label을 리스트로 전달
  - qcut() : 데이터를 오름차순으로 정렬한 뒤 데이터 개수가 같도록 지정한 개수만큼의 구간으로 나눈다.
      - 구문: `pd.qcut(x, q, labels)`
      - 매개변수
          - x: 나눌 대상. 1차원 배열형태의 자료구조
          - q: 나눌 개수
  ```python
  ages = pd.Series(np.random.randint(50, size=30))
  ages.shape
  
  bins = [-1,10,20,30,40,51]
  age_cate = pd.cut(ages, bins=bins)
  print(age_cate.shape)
  print(age_cate.value_counts())
  ```
