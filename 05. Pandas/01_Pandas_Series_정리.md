판다스
======

# 1. 판다스 개요
  - 데이터 분석과 관련된 다양한 기능을 제공하는 파이썬 패키지(아나콘다에 내장)
  - 특히 표 형태의 데이터에 특화
  - 주요 데이터 형식
    - `Series`: 1차원 자료구조를 표현(행 또는 열)
    - `DataFrame`: 행렬의 표를 표현(행렬)

- - -

# 2. `Series`
  - DataFrame의 한 행이나 열을 표현
  - 각 원소는 index로 접근 가능 및 벡터화 연산 지원
    - 01. 생성
      ```python
      # 판다스 모듈 import
      import pandas as pd
      # 보통은 데이터 분석 시 넘파이와 매트플롯라이브러리 모두 import하고 시작
      import numpy as np
      import matplotlib.pyplot as plt
      
      pd.Series([10,20]) # 이처럼 리스트, 또는 튜플, 넘파이배열 모두 매개변수로 활용하여 시리즈 생성가능
      ```
    - 02. 원소 접근
      - Indexing
        - index 순번으로 조회
          - Series[순번]
          - Series.iloc[순번] - iloc indexer
        - index 이름으로 
          - Series[index명]
          - Series.loc[index명] - loc indexer
          - Series.index명
              - index명이 문자열일 경우 `. 표기법` 사용가능
          - index명이 문자열이면 문자열(" ") 로, 정수이면 정수로 호출
              - s['name'], s[2], s.loc['name'], s.loc[2]
        - Fancy 인덱싱 가능( 리스트로 묶어서 인덱스 전달)
      - Slicing
        - `Series[start index :  end index : step]`
            - end index
                - index 순번일 경우는 포함 하지는다.
                - index 명의 경우는 포함한다.
        - Slicing의 결과는 원본의 참조(View)를 반환(얉은 복사)
      - ex)
      ```python
      # 영어 - index(명)
      print(s3['영어'], s3.loc['영어'], s3.영어)

      # .표기법(s3.영어) : index명이 숫자로 시작하는 경우, 변수이름으로 불가능한 글자가 있는 경우 사용 불가
      s5 = pd.Series([10,20,30], index=['국어 점수','영어#점수','2영어 점수'])
      # print(s5.국어 점수)

      s6 = pd.Series([10,20,30], index=[100,200,300])
      print(s6)
      
      # fancy indexing - 한번에 여러 값 조회
      print(s3[[1,2,3]])
      print(s3[['영어','수학']])
      
      # 시리즈(데이터프레임)의 index명은 중복 가능
      s8 = pd.Series(np.arange(5), index=['a','b','c','d','d'])
      print(s8)
      print(s8['d'])

      s9 = pd.Series(np.arange(6), index=['k','r','c','d','s','d'])
      # print(s9['k':'d']) # 동일한 이름이 모여있으면 상관없지만 다른 문자가 껴있으면 에러
      ```
        
    - 03. Indexing, Slicing을 통해 값 변경시 조심스러우면 `.copy()`를 통해 깊은 복사 후 진행
    - 04. Boolean 인덱싱
      - Series 의 indexing 연산자에 boolean 리스트를 넣으면 True인 index의 값들만 조회한다.
    - 05. 주요 메소드
