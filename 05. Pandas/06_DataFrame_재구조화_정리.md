# 06. DataFrame 재구성

### 정돈된 데이터(Tidy Data)란?
    - 각 변수(데이터의 속성)는 열을 형성한다.
    - 각 관측값(하나의 데이터)은 행을 형성한다.
    - 각 관측 단위별(데이터 Entity)로 별도의 테이블(표)을 구성한다. => 단일 관측
  - 그렇다면 정돈되지 않은 데이터는 주로?
    1. 열 이름이 변수 이름이 아니라 값인 경우
    1. 열 이름에 복수 개의 변수가 저장된 경우
    1. 변수가 행과 열에 모두 저장된 경우
    1. 같은 테이블에 복수 형식의 관측단위가 저장된 경우
        - 하나의 테이블에 여러 데이터(관측단위)가 병합된 것
    1. 단일 관측 단위가 복수 테이블에 저장된 경우
        - 하나의 데이터의 변수들이 여러 테이블에 나눠 저장된 경우
  
### 1. `stack()`
  - 컬럼명을 index(행명)으로 전환
      - 기존 index가 있으면 하위 레벨로 들어간다. (기존 것이 상위 레벨)
  ```python
  import pandas as pd
  import numpy as np

  state_fruit = pd.read_csv('data/state_fruit.csv', index_col=0)
  s1 = state_fruit.stack()
  
  state_fruit_tidy = state_fruit.stack().reset_index()
  state_fruit_tidy.columns = ['state', 'fruit', 'count']
  
  s2 = s1.rename_axis(['STATE','FRUIT'], axis=0) # 각 축(index/columns)의 이름 지정
  s2.reset_index(name='COUNT') # series.reset_index(name='이름') DF로 변경될 시 value의 컬럼명을 지정
  ```
- - -


### 2. `unstack()`
  - stack() 반대로 index를 컬럼으로 변환한다.
  - 매개변수 
      - level: multi-index일 경우 컬럼으로 만들 레벨을 지정한다. 기본값은 -1 로 가장 안쪽의 index를 이동시킨다.
  ```python
  s = state_fruit_tidy.set_index(['state','fruit'])
  s.unstack() # 가장 안쪽 level의 index가 컬럼으로 변환
  # s.unstack(level=-2)
  
  s2 = s.unstack(level=0)
  
  # droplevel(): multi index에서 하나를 제거할 때 사용
  s2.droplevel(level=0, axis=1)
  ```
- - -

### 3. `melt()`
  - 구문: `DF객체.melt(id_vars=[], value_vars=[], var_name='', value_name='')`
  - id_vars: 값으로 변환하지 않고 그대로 유지하고자 하는 컬럼명(열이름)들의 리스트
      - 지정한 변수(컬럼)은 같은 열에 남게 되지만, value_vars에 전달된 각 열에 대해 반복적으로 나타난다.
  - value_vars: 단일 컬럼의 값으로 변경하고자 하는 컬럼명 리스트
      - value_vars에 지정한 컬럼이 value가 되고 그 컬럼의 값들은 다른 컬럼으로 생성된다.
      - id_vars와 value_vars에 **지정 안된** 컬럼은 제거된다.
          - 제거 되지 않고 **단독 컬럼으로 유지되길 바라는 컬럼은 id_vars**로 지정한다.
  - var_name: value_vars로 단일열이 된 열의 이름 지정(지정 안하면 컬럼명은 **variable**)
  - value_name: value_vars에 지정된 열들의 값들이 변환된 컬럼의 이름 지정(지정안하면 컬럼명은 **value**)
  ```python
  state_fruit.melt(value_vars=['Apple','Orange']) # id_vars나 value_vars에 포함되지 않은 컬럼들은 제거된다.
  ```

- - -

### 4. `pivot()`
  - 구문: `DF객체.melt(id_vars=[], value_vars=[], var_name='', value_name='')`
  - **각 index, columns 매개변수의 값은 단일 문자열로 컬럼명을 준다.**
  - index: 문자열(리스트안됨). 행이름으로 사용할 컬럼 -> 열이 index로 이동하는 형태가 된다.
  - columns: 문자열(리스트안됨). 컬럼명으로 사용할 컬럼
    - **index와 columns 는 여러개 지정 안됨. 오직 하나만 지정 가능**
  - values : Value에 올 컬럼명
  ```python
  state_fruit_melt = state_fruit.melt(id_vars=['State'], value_vars=['Apple','Orange','Banana'], var_name='Fruit', value_name='Count')
  ```
