# DataFrame(데이터프레임)
=======================

### 1. DataFrame 개요
  - 판다스 클래스 중 표를 다루는 클래스
  - 많은 테이블을 다루는 포맷(`CSV, Excel, DB` 등)과 호환 가능

### 2. 생성
  - `pd.DataFrame(data [, index=None, columns=None])`
    - data 
        - DataFrame을 구성할 값을 설정
            - Series, List, ndarray를 담은 2차원 배열
            - 열이름을 key로 컬럼의 값 value로 하는 딕셔너리(사전)
    - index
        - index명으로 사용할 값 배열로 설정
    - columns
        - 컬럼명으로 사용할 값 배열로 설정
    ```python
    import pandas as pd
    import numpy as np

    data_dict = {
        'id':['id-1', 'id-5', 'id-2', 'id-4', 'id-3'],
        'korean':[100, 50, 70, 60, 90],
        'english':[90, 80, 100, 50, 100]
    }
    grade = pd.DataFrame(data_dict)
    print(grade)
    print(grade.shape) # (행 수, 열 수)
    grade
    ```

- - -


### 3. 파일호환
  - 01. 읽어오기
    - `DataFrame객체.to_csv(파일경로,sep=',', index=True, header=True, encoding)`
      - 텍스트 파일로 저장
      - 파일경로: 저장할 파일경로(경로/파일명)
      - sep : 데이터 구분자
      - index, header: 인덱스/헤더 저장 여부
      - encoding
          - 파일인코딩
          - 생략시 운영체제 기본 encoding 방식
    - `DataFrame객체.to_excel(파일경로, index=True, header=True)`
        - 엑셀파일로 저장
    ```python
    # csv: text파일
    grade.to_csv('data/grade2.csv', index=False, header=False)
    grade.to_csv('data/grade4.csv', index=False, sep='\t')

    # excel 포맷
    grade.to_excel('data/grade1.xls', index=False)

    # pickle (객체를 binary로 저장)
    grade.to_pickle('data/grade.pkl')

    # json (딕셔너리 형태)
    grade.to_json('data/grade.json') # text
    ```
  - 02. 파일로 저장
    - `pd.read_csv(파일경로, sep=',', header, index_col, na_values, encoding)`
      - 파일경로 : 읽어올 파일의 경로
      - sep
        - 데이터 구분자. 
        - 기본값: 쉼표
      - header=정수
        - 열이름(컬럼이름)으로 사용할 행 지정
        - 기본값: 첫번째 행
          - None 설정: 첫번째 행부터 데이터로 사용하고 header(컬럼명)는 0부터 자동증가하는 값을 붙인다.
      - index_col=정수,컬럼명
        - index 명으로 사용할 열이름(문자열)이나 열의 순번(정수)을 지정.
        - 생략시 0부터 자동증가하는 값을 붙인다.
      - na_values
        - 읽어올 데이터셋의 값 중 결측치로 처리할 문자열 지정.
        - NA, N/A, 빈 값 => 결측치로 자동인식
      - encoding
        - 파일 인코딩
        - 생략시 운영체제 기본 encoding 방식
    ```python
    # CSV파일 읽기
    g2 = pd.read_csv('data/grade2.csv', header=None)
    g2 # pandas는 주피터노트북에서 따로 지원하므로 그냥 호출할 때 표를 장식하여 표현해준다.
    
    # 엑셀파일 읽기
    g5 = pd.read_excel('data/grade.xls')
    g5
    ```
    
- - -


### 4. 주요 메소드, 속성
  ![1](https://user-images.githubusercontent.com/71580318/109127255-8f1df300-7791-11eb-83e4-ae74e2449bae.PNG)
  ![2](https://user-images.githubusercontent.com/71580318/109127268-9218e380-7791-11eb-973e-2631fed0cf9b.PNG)
  - 관례적으로 데이터프레임 속성 확인
    ```python
    # 데이터프레임 생성 - movie.csv
    df = pd.read_csv('data/movie.csv')
    # shape
    print(df.shape) # -> 행: 4916, 열: 28 -> 영화개수: 4916, 영화속성: 28
    # 데이터 일부를 확인
    print(df.head(10))
    print(df.tail(10))
    # DataFrame 정보 -> 행, 열에 대한 상세정보
    # #:번호, Column: 컬럼명, Non-Null Count: 값이 몇개 있는지(NA제외), Dtype: 데이터타입(object: 문자열)
    print(df.info())
    
    # 결측치 확인
    print(df.isnull()) # 원소단위
    print(df.isnull().sum()) 
    print(df.isnull().sum().sum())
    ```
  ##### 01) 컬럼이름/행이름 조회 및 변경
    - `DataFrame객체.columns`
      - 컬럼명 조회
      - 컬럼명은 차후 조회를 위해 따로 변수에 저장하는 것이 좋다.
    - `DataFrame객체.index`
      - 행명 조회
    - 01. 컬럼이름/행이름 변경
      - 컬럼과 인덱스는 불변의 성격을 가짐
      - columns와 index 속성으로는 통째로 바꾸는 것은 가능하나 index로 하나씩 바꾸는 것은 안된다.
        - `df.columns = ['새이름','새이름', ... , '새이름']`
        - `df.columns[1] = '새이름'` # 이 구문으로는 불가능

    - 02. 컬럼이름/행이름 변경 관련 메소드    
      - `DataFrame객체.rename(index=행이름변경설정, columns=열이름변경설정, inplace=False)`
      - `DataFrame객체.rename(mapper=행/열이름변경설정, axis=축번호, inplace=False)` : axis=0-index, axis=1-columns
        - 개별 컬럼이름/행이름 변경 하는 메소드
        - 변경한 DataFrame을 반환
        - 변경설정: 딕셔너리 사용
          - {'기존이름':'새이름', ..}
          - inplace: 원본을 변경할지 여부(boolean)
      - `DataFrame객체.set_index(컬럼이름, inplace=False)`
        - 특정 컬럼을 index명으로 사용/ 해당 컬럼은 Data Set 에서 제거된다.
      - `DataFrame객체.reset_index(drop=False, inplace=False)`
        - index를 첫번째 컬럼으로 복원
        - drop=True: index명을 제거하고 순번으로 변경
    ```python
    grade.columns = ['ID', 'Korean', 'English'] # 원본을 변경
    grade
    
    # Korean=>국어, English=>영어 / 컬럼명 일괄변경
    d = {
        "Korean":"국어",
        "English":"영어"
    }
    grade.rename(columns=d)
    
    # ID컬럼의 값들을 index로 지정
    grade.set_index('ID', inplace=True)
    grade
    ```
  ##### 02) 컬럼/행 삭제
    - `DataFrame객체.drop(columns, index, inplace=False)`
    - `DataFrame객체(label=삭제할컬럼/index이름, axis=삭제할 축)`
      - columns : 삭제할 열이름 또는 열이름 리스트
      - index : 삭제할 index명 또는 index 리스트
      - inplace: 원본을 변경할지 여부(boolean)
    ```python
    # 행/열 
    grade.drop(columns=['Korean','English'])
    grade.drop(labels=['Korean','English'], axis=1)
    grade.drop(index=['id-1','id-2'])
    grade.drop(labels=['id-1','id-2'], axis=0)
    # 다만 행/열 제거시 순번은 사용 불가
    # grade.drop(index=[0,3]) -> 불가
    ```
  ##### 03) 컬럼/행 추가
    - 새로운 열을 지정 후 값을 대입하면 새로운 열을 추가할 수 있다.
      - 보통 파생변수를 만들 때 사용한다.
    - df['새열명'] = 값
      - 마지막 열로 추가된다.
      - 하나의 값을 대입하면 모든 행에 그 값이 대입된다.
      - 다른 값을 주려면 배열에 담아서 대입한다.
    - 기존 열들의 값을 이용한 새로운 열 생성
      - 벡터 연산을 이용하여 값 대입
      - df[‘새열이름‘] = 기존 열들을 이용한 연산
    ```python
    grade['math'] = 80 # math 컬럼(없는 컬럼)을 추가, 값은 전부 80 대입
    grade
    
    # 전체 컬럼의 평균을 새로운 컬럼으로 추가
    grade['total'] = grade['Korean'] + grade['English'] + grade['math']
    grade['mean'] = grade['total'] / 3
    ```
    
  ##### 04) 컬럼/행별 값 조회
    - 01. 열 조회
      - df['컬럼명']
      - df.컬럼명
      - 팬시 indexing
        - 여러 개의 컬럼을 조회할 경우 컬럼명들을 담은 리스트/튜플로 조회
      - 주의
        - df[컬럼index] 구문은 불가
        - df[0:3] 슬라이싱은 행 조회다.
        - 만약 indexing이나 slicing을 이용해 컬럼값 조회하려면 columns 속성을 이용
          - `df[df.columns[:3]]`
      - 조회결과
        - 한 개 컬럼조회: Series로 반환 (행명을 index명으로, 조회값을 값으로 가지는 Series)
        - 여러 개 컬럼조회: DataFrame으로 반환
      ```python
      # 컬럼 조회시
      grade[grade.columns[3]]
      # DataFrame의 컬럼명들을 변수에 넣어서 사용.
      cols = grade.columns
      grade[cols[1:5]] # 주로 이런식의 구문 사용
      ```
    - 02. 열 조회 메소드
      - `select_dtypes(include=[데이터타입,..], exclude=[데이터타입,..])`
        - 전달한 데이터 타입의 열들을 조회. 
        - include : 조회할 열 데이터 타입
        - exclude : 제외하고 조회할 열 데이터 타입
      - `filter (items=[], like='', regex='')`
       - 매개변수에 전달하는 열의 이름에 따라 조회
        - 각 매개변수중 하나만 사용할 수 있다.
        - items = [ ] 
          - 리스트와 일치하는 열들 조회
          - 이름이 일치 하지 않아도 Error 발생안함.
        - like = “ “ 
          - 전달한 문자열이 들어간 열들 조회
          - 부분일치 개념
        - regex = “ ”
          - 정규 표현식을 이용해 열명의 패턴으로 조회
      ```python
      # grade[['Korean', 'eng']] # 없는 컬럼으로 조회시 Exception 발생
      grade.filter(items=['korean','eng']) # 없는 아이는 빼고 있는 아이만 조회
      
      grade.insert(1, 'korean3', 70)
      grade.filter(regex='.+\d')
      
      # 해당 타입만 조회
      grade.select_dtypes(include=['int64', 'bool'])
      ```
    - 03. 행 조회
      - 두가지 방법이 있다. `loc`으로 index명으로 조회/ 또는 `iloc`으로 행순번으로 조회
      - 1) `loc`: 행이름으로 조회
        - `DF.loc[ index이름 ]`
            - 한 행 조회.
            - 조회할 행 index 이름(레이블) 전달
            - 이름이 문자열이면 " " 문자열표기법으로 전달. 정수이면 정수표기법으로 전달한다.
        - `DF.loc[ index이름 리스트 ]`
            - 여러 행 조회. 
            - 팬시 인덱스
            - 조회할 행 index 이름(레이블) 리스트 전달
        - `DF.loc[시작index이름 : 끝index이름: step]`
            - 슬라이싱 지원
            - 끝index이름의 행까지 포함한다.
        - `DF.loc[index이름 , 컬럼이름]`
            - 행과 열 조회
            - 둘다 이름으로 지정해야 함.
      - 2) `iloc` : 행 순번으로 조회
        - `DF.iloc[행번호]`
            - 한 행 조회.
            - 조회할 행 번호 전달
        - `DF.iloc[ 행번호 리스트 ]`
            - 여러 행 조회.
            - 조회할 행 번호 리스트 전달
        - `DF.iloc[start 행번호: stop 행번호: step]`
            - 슬라이싱 지원
            - stop 행번호 포함 안함.
        - `DF.iloc[행번호 , 열번호]`  
            - 행과 열 조회
            - 행열 모두 순번으로 지정
    - 04. Boolean indexing 조회
      - 다중조건의 경우 `()`로 묶는다
      - 파이썬과 달리 `&`, `|`, `~`의 논리연산자 사용
      - 구문: `DataFrame객체[조건], DataFrame객체.loc[조건]` - 조건이 True인 행만 조회
        - 열까지 선택시 `DataFrame객체[조건][열]` 또는 `DataFrame객체.loc[조건, 열]` 로 조회
      ```python
      # 국어 또는 영어가 80점 이상
      grade.loc[(grade['korean']>=80) | (grade['english']>=80)]
      ```
