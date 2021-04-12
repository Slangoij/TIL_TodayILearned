Numpy
=====

# 넘파이의 데이터구조
  - 스칼라: 하나의 숫자로 이루어진 데이터
  - 벡터: 여러 개의 숫자를 특정한 순서대로 배열시켜 놓은 데이터
  - 행렬: 여러 개의 벡터들을 모아놓은 데이터 집합
  - 텐서: 여러 개의 같은 크기의 행렬/텐서를 모아놓은 데이터 집합(벡터와 행렬도 저차원의 텐서라고 봐도 무방하다.)
  
### 넘파이 데이터 구조 관련 용어
    - 축: 값들의 나열 방향(차원과 동일한 개념)
    - 랭크: 축의 개수
    - 형태/형상: 각 축 내에서의 데이터의 개수
    - 크기: 데이터 내 원소의 총 개수

- - -

# 넘파이 관련 데이터 생성 메소드
### 1. zeros(shape, dtype)
- 영벡터(행렬)(원소를 0으로 채운 배열)
  - shape : 형태(크기, 개수) 지정
  - dtype : 요소의 개수 지정
```python
z1 = np.zeros(10) # size가 10인 vector(1d array)
print(z1.shape)

z2 = np.zeros([3,5]) # 3 x 5 행렬
print(z2.shape)
print(z2)
print(z2.dtype)

z3 = np.zeros((5,3,2,5,6), dtype=np.float32)
print(z3.shape)
print(z3.dtype)
print(z3)
```

### 2. ones(shape, dtype)
- 1벡터(행렬)(원소를 1로 채운 배열)
  - shape : 형태(크기, 개수) 지정
  - dtype : 요소의 개수 지정
```python
o1 = np.ones(10) # shape 정수: 1차원 배열
print(o1.shape)
print(o1.ndim)
print(o1.dtype)

o2 = np.ones((10,5))
print(o2.shape)
o2
```

### 3. full(shape, fill_value, dtype))
-원소들을 원하는 값으로 채운 배열 생성
  - shape : 형태(크기, 개수) 지정
  - fill_vlaue : 채울 값
  - dtype : 요소의 개수 지정
```python
f1 = np.full(10, 5)
print(f1)

f2 = np.full(shape=(5,3), fill_value=7, dtype=np.int)
print(f2.shape)
print(f2.dtype)
```

### 4. xxx_like(배열)
- zeros_like(), ones_like()
- 매개변수로 받은 배열과 같은 shape의 0 또는 1로 값을 채운 배열을 생성.
-원소들을 원하는 값으로 채운 배열 생성
```python
a = np.array([1,2,3,4,5])
a_1 = np.ones_like(a)
print(a.shape, a_1.shape)
print(a_1)
```

### 5. arange(start, stop, step, dtype)
- start에서 stop 범위에서 step의 일정한 간격의 값들로 구성된 배열 리턴 
  - start : 범위의 시작값으로 포함된다.(생략가능 - 기본값: 0)
  - stop : 범위의 끝값으로 **포함되지 않는다.** (필수)
  - step : 간격 (생략가능 - 기본값: 1)
  - dtype : 요소의 타입
  - 1차원 배열만 생성가능
```python
a1 = np.arange(10, 0, -1) # 감수: 10 ~ 0+1, -1씩 증가
print(a1)

a2 = np.arange(0, 1, .1) # 0 ~ 1-0.1, 0.1씩 증가
print(a2)
```

### 6. linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
- 시작과 끝을 균등하게 나눈 값들을 가지는 배열을 생성 
  - start : 시작값
  - stop : 종료값
  - num : 나눌 개수. 기본-50, 양수 여야한다.
  - endpoint : stop을 포함시킬 것인지 여부. 기본 True
  - retstep : 생성된 배열 샘플과 함께 간격(step)도 리턴할지 여부. True일경우 간격도 리턴(sample, step) => 튜플로 받는다.
  - dtype : 데이터 타입
```python
a = np.linspace(1, 100, num=10, retstep=True)
print(a3)
```

### 7. eye(N, M=None, k=0, dtype=<class 'float'>) / 8. identity(N)
- 항등행렬 생성 / 단위 행렬 생성
  - N : 행수
  - M : 컬럼수
  - k : 대각선이 시작할 index (첫행의 index를 지정한다. ) 기본값 : 0
> ##### 대각행렬
>    - 행과 열이 같은 위치를 대각(diagnonal) 이라고 하며 그 대각에만 값이 있고 비대각은 0으로 채워진 행렬.    
>
> ##### 항등행렬/단위행렬
>    - 대각의 값이 1인 정방행렬로 $E$나 $I$ 로 표현한다.
>    - 단위행렬은 행렬에서 곱셈의 항등원이다
>    - 행렬곱셈(내적)에대해서 교환법칙이 성립한다.
>         - $A\cdot E = A$
```python
i = np.identity(3) # 3 X 3의 항등행렬
print(i.shape)
print(i)

e1 = np.eye(5, 3) # 5 x 3
print(e1)

e2 = np.eye(5, 3, k=-1)
print(e2)
```
