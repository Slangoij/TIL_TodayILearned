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
      ![img1]C:\Users\inje.jeong\Desktop\1.png
    - 2. 이항 범용함수
      ![img2]C:\Users\inje.jeong\Desktop\2.png
### 1-1. 
- ex)
- ```python
  # boolean indexing을 활용하기 위해 bool변수를 가진 똑같은 shape의 배열을 만들자.
  # 벡터화(연산)
  # 배열 + 배열 : 같은 인덱스의 원소끼리 연산
  a = np.array([1,2,3])
  b = np.array([10,20,30])
  print(a + b)

  arr = np.arange(100)
  np.random.shuffle(arr)
  print(arr)
  
  
  
  
  
  

- - -

# 2. 

- - -

# 3. 
