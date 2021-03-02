# DataFrame 정렬
================

### 1. Indea명/컬럼명 기준 정렬
  - 구문: `DF객체.sort_index(axis, ascending=True)`
    - axis
      - index명 기준 정렬(행) : 'index' 또는 0 (기본값)
      - columnm 명 기준 정렬(열) : 'columns' 또는 1
    - ascending
      - 정렬방식
      - True(기본): 오름차순, False: 내림차순
    - inplace
      - 원본에 적용 여부
      - False(기본): 변경한 복사본 반환 
      - True : 원본을 변경
  ```python
  # 문자열 : 특수문자 < 숫자 < 대문자 < 소문자 < 외국어
  movie_df.sort_index(ascending=False) # 내림차순

  movie_df.sort_index(axis=1, ascending=False) # 컬럼명 기준 정렬

  movie_df2
  movie_df2['A':'B'] # index가 sorting된 경우 부분값을 가지고 slicing가능. stop은 포함 안함.
  ```

### 2. 컬럼 값 기준 정렬
  - 구문: `DF객체.sort_values(by, ascending, inplace)`
  ```python
  movie_df.sort_values('director_name', ascending=False)
  # 결측치는 방식(오름/내림차순)과 관계없이 마지막에 나온다.

  # duration으로 정렬하고 duration값이 같은 것끼리는 imdb_score값으로 정렬(둘다 오름차순)
  movie_df.sort_values(['duration', 'imdb_score'])[['duration', 'imdb_score']].head(20)
  ```
    
### 3. 기술통계함수를 이용한 데이터 집계
  - 01. 구문: `DF객체.sort_values(by, ascending, inplace)`
  - ![image](https://user-images.githubusercontent.com/71580318/109632959-ea355880-7b8a-11eb-82b8-d849e08dfeb4.png)
    - DataFrame에 적용할 경우 컬럼별로 계산
    - sum(), max(), min(), idxmax(), idxmin(), unique(), nunique(), count()는 문자열에 적용가능
    - 기본적으로 결측치(NA)는 제외하고 처리하며 제외하지 않으려면 `skipna=False`로 설정
  ```python
  flights.mean() # mean(), std(), var()은 숫자형 컬럼만 계산
  ```
  - 02. aggregate
    - 구문: `aggregate(func, axis=0, \*args, \*\*kwargs) 또는 agg(func, axis=0, \*args, \*\*kwargs)`
    - 집계함수를 DataFrame의 열 별로 처리해주는 함수, 사용자 정의 집계함수나 열 별로 각기 다른 집계를 할 때 사용
    - 매개변수
        - func
            - 집계 함수 지정
                - 문자열/문자열리스트 : 집계함수의 이름. 여러 개일 경우 리스트. 판다스 제공 집계함수는 문자열로 함수명만 제공가능
                - 딕셔너리 : {집계할컬럼 : 집계함수[, 컬럼:집계함수]}
                - 함수 객체 : 사용자 정의 함수의 경우 함수이름 전달
        - axis
            - 0 또는 'index' (기본값): 컬럼 별 집계
            - 1 또는 'columns': 행 별 집계
        - \*args, \**kwargs 
            - 함수에 전달할 매개변수. 
            - 집계함수는 첫번째 매개변수로 Series를 받는다. 그 이외의 매개변수가 있는 경우.
    ```python
    #AIRLINE : 최빈값-mode, DEP_DELAY: 평균-mean, 표준편차-std
    flights.agg({'AIRLINE':'mode', 'DEP_DELAY':['mean', 'std']})
    ```
  - 03. Groupby
    - 구문: `DF.groupby('그룹으로묶을기준컬럼')['집계할 컬럼'].집계함수()`
      - 집계 컬럼은 Fancy인덱싱 가능
    - 복수열 기준 Grouping
      - groupby의 매개변수에 그룹으로 묶을 컬럼들의 이름을 리스트로 전달
    ```python
    # flights.groupby('AIRLINE')['ARR_DELAY', 'DEP_DELAY'].mean()
    flights.groupby('AIRLINE')[['ARR_DELAY', 'DEP_DELAY', 'AIR_TIME']].agg(['mean', 'std'])
    # result = flights.groupby('AIRLINE')[['ARR_DELAY', 'DEP_DELAY', 'AIR_TIME']].agg(['mean', 'std'])
    # result['ARR_DELAY', 'mean'] # multi index 조회법
    
    # 복수열 Grouping시 구문이 복잡하므로 주로 변수로 따로 저장 후 조회
    result = flights.groupby(['AIRLINE', 'MONTH'])[['DEP_DELAY', 'ARR_DELAY']].agg(['mean','sum'])
    result.loc['AA', 1]
    ```
  - 04. 사용자 정의 집계함수 이용
    - # max와 min값의 차이를 반환하는 사용자정의 집계함수
    ```python
    def max_min_diff(x):
      """
      max와 min값의 차이를 반환하는 사용자정의 집계함수
      [매개변수]
          x: 통계량을 구할 Series
      [반환값]
          max()-min()
          Series x의 타입이 object(문자열)이면 None을 반환
      """
      if x.dtype == 'object':
          return None
      return x.max() - x.min()
          
    print(flights['ARR_DELAY'].agg(max_min_diff))
    print(max_min_diff(flights['ARR_DELAY'])) # 사용자정의 집계함수 객체를 매개변수로 전달.
    ```
