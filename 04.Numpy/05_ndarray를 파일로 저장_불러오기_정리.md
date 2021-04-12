배열의 파일 저장 및 호출
========================

# 1. 바이너리 파일
  - 01. 저장`np.save("파일경로", 배열)`
  - 02. 호출`np.load("파일경로")`
  - 03. 여러개 배열 압축 저장`np.savez("파일경로", 이름=배열[,이름=배열,...])`
  - ex)
    ```python
    import numpy as np
    a = np.arange(10)
    b = np.arange(12).reshape(4,3)
    c = np.arange(24).reshape(4,2,3)

    # 한개의 배열 저장
    np.save('a.npy', a) # 배열 a를 'a.npy' 파일로 저장
    np.save('b', b) # 확장자를 생략해도 npy 확장자는 자동으로 붙는다.
    np.save('c.arr', c)

    a2 = np.load('a.npy')
    print(a2)
    b2 = np.load('b.npy')
    print(b2)
    c2 = np.load('c.arr.npy')
    print(c2)
    ```
  
# 2. 텍스트 파일
  - 01. 저장 `savetxt("파일경로", 배열 [, delimiter='공백'])`
  - 02. 호출 `loadtxt("파일경로" [,dtype=float, delimiter=공백])`
  - 1차원과 2차원 배열만 저장 가능하고, 여러배열 압축 저장은 불가능
      - ex)
      ```python
      # 텍스트 파일로 저장
      np.savetxt('a.txt', a)
      np.savetxt('b.txt', b)
      np.savetxt('b.csv', b, delimiter=',')
      # np.savetxt('c.txt', c) # 1,2차원까지만 가능하므로 불가능

      b4 = np.loadtxt('b.csv', delimiter=',')
      print(b4)
      ```
