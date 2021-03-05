# 05. DataFrame 합치기

### 1. `join()`
  - `concat()`은 단순히 DF를 합칠 뿐이라 활용도 낮음
  - 구문: `dataframe객체.join(others, how='left', lsuffix='', rsuffix='')`
  - 두 개 이상의 DF를 조인 가능
    - 조인 기준: index가 값은 값끼리 더함, 조인 기본방식: Left outer 방식
  ```python
  # 컬럼명에 suffix(접미어)를 붙인다
  s_2017.add_suffix('_2017').join([
  s_2016.add_suffix('_2016'),
  s_2016.add_suffix('_2018')])
  ```
- - -


### 1. `merge()`
- 구문: `dataframe.merge(합칠dataframe, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False)`
- 조인 기준: 같은 컬럼명 기준(equi-join), 기본방식: inner join
- 매개변수
  - on : 같은 컬럼명이 여러개일때 join 대상 컬럼을 선택
  - right_on, left_on : 조인할 때 사용할 왼쪽,오른쪽 Dataframe의 컬럼명. 
  - left_index, right_index: 조인 할때 index를 사용할 경우 True로 지정 
      - 위의 네 매개변수를 적절히 조합하여 사용
  - how : 조인 방식.  'left', 'right', 'outer', 'inner'. 기본: inner 
  - suffixes: 두 DataFrame에 같은 이름의 컬럼명이 있을 경우 구분을 위해 붙인 접미어를 리스트로 설정
      - 생략시 x, y를 붙인다.
```python
s_info.merge(s_2018_copy, left_on='Symbol', right_index=True, how='inner')
s_info.merge(s_2018_copy, left_on='Symbol', right_index=True, how='left')
s_info.merge(s_2018_copy, left_on='Symbol', right_index=True, how='right')
s_info.merge(s_2018_copy, left_on='Symbol', right_index=True, how='outer')
```
