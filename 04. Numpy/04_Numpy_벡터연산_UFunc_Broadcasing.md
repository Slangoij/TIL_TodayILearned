벡터의 연산
==========
- 기본적으로 스칼라와 연산하거나, 같은 shape의 벡터와만 연산 가능하다.

# 1. 내적(Dot product)
  - `@` 연산자 또는 `numpy.dot(벡터, 벡터)` 함수 사용
  - 조건: 앞 벡터의 열 개수와 뒤 벡터의 행 개수가 같아야 한다.
  - ex)
  ```python
  A = np.arange(1,7).reshape(2,3)
  B = np.arange(1,7).reshape(3,2)
  C = np.arange(1,7).reshape(2,3)

  print(B, B.shape)
  print(A @ B)
  print(np.dot(A,B))

  # print(A @ C)
  # (2,3), (2,3) 앞의 열수와 뒤의 행수가 다르므로 연산 불가
  ```
  
# 2. 범용함수(Ufunc, Universal Function)
  - 벡터화를 지우너하는 넘파이 연산 함수들
  - 반복문으로 직접 짜는 것보다 범용함수를 사용하는 것이 속도가 훨씬 빠르다.
  - 주요함수
    - 1. 단항 범용함수
      ![1](https://user-images.githubusercontent.com/71580318/108481567-b3825700-72db-11eb-9518-a1a50911a735.PNG)
      - ex)
      ```python
      import numpy as np
      a = np.array([10,100,1000])
      print(np.sqrt(a))
      print(np.square(a))
      print(np.modf(np.sqrt(a))) # 첫번째배열: 실수부, 두번째배열: 정수부

      # 넘파이에서 NaN => np.nan
      b = np.array([10, np.nan, 20, 30, np.nan])
      print(np.isnan(b))
      # b에서 nan의 개수
      print(np.sum(np.isnan(b)))
      ```
    - 2. 이항 범용함수
      ![2](https://user-images.githubusercontent.com/71580318/108481709-dd3b7e00-72db-11eb-8442-b0d53fd7f9e9.PNG)
      - ex)
      ```python
      a = np.array([1,2,3])
      b = np.array([10,20,30])
      c = np.array([100, np.nan, -100])

      print(a + b)
      print(np.add(a,b))
      print(np.power(b, a))
      print(np.maximum(a,b))
      print(np.maximum(b,c))
      print(np.add(b,c))
      print(np.fmax(b,c))
      ```
    - 연산결과 출력 지정
      - `np.유니버셜함수.(배열, 배열, out = 담을 대상 배열)` 이렇게 하면 해당 배열에 결과가 담긴다.
    - 누적연산함수
      - 1. reduce()
        - 해당 축을 기준으로 그 축 내에서 모든 결과를 연산하여 하나로 만들어 결과 배열 반환
      - 2. accumulate()
        - reduce와 마찬가지지만 축방향으로 진행하며 결과를 누적해가며 연산.
    - ex>
    ```python
    # 연산결과 출력 지정
    a = np.arange(11,20).reshape(3,3)
    b = np.arange(21,30).reshape(3,3)
    print(a.shape,b.shape)

    out = np.zeros((3,3))
    print(out, out.shape)
    print(np.add(a,b,out=out)) # 연산결과를 out에 담아준다
    
    # 누적 연산함수 - reduce
    x = np.arange(1,13).reshape(3,4)
    print(x)
    print(np.add.reduce(x)) # axis 생략시 기본값 0
    print(np.add.reduce(x, axis=1))
    print(np.add.reduce(x, axis=None)) # axis=None시 전체 계산
    
    # 누적 연산함수 - accumulate
    # 행(0축): 일자별 팔린 개수
    # 열(1축): 0:사과, 1:배, 2:귤
    l = [
        [10,5,30],
        [20,10,2],
        [7,10,3],
        [20,20,3]
    ]
    count = np.array(l)
    print(np.add.accumulate(count, axis=0))
    print(np.add.accumulate(count, axis=1))
    print(np.multiply.accumulate(count, axis=1))
    ```
