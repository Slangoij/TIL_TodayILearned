# OpenCV
- C++로 작성됨, OS 및 언어에 상관없이 동작
- 이미지 입출력, 동영상 입출력 처리 가능

## 01. 이미지
- `cv.imread(filename[, flag])` 메소드 사용하여 ndarray 형식 반환
  - filename: 파일경로, flag: 읽기 모드 - cv2.IMREAD_XXXX 상수 이용(default: IMREA_COLOR)
- 색공간 변환
  - `cv2.cvtColor(src, code)`
    - src: 원본소스(ndarray)
    - code: 변환시킬 색공간 타입 지정(cv2.COLOR_XXX2YYY) - ex) cv2.COLOR_BGR2HSV (BGR -> HSV)
    - HSV: Hue(색상), Saturation(채도), Value(밝기)
- 이미지 출력
  - `cv2.imshow(winname, mat)
    - winname: 창 이름, mat: 출력이미지(ndarray)(dtype을 uint8로 변환해야 정상 출력)
  - `cv2.imwrite(filename, img)`: bool
    - filename: 파일경로, img: 저장할 이미지(ndarray), 반환값: 저장성공시 True
```python
import cv2
import numpy as np

# 이미지 읽기
lenna = cv2.imread('./images/lenna.bmp')#, cv2IMREAD_GRAYSCALE)

# opencv메소드로 창으로 출력
cv2.imshow("lenna",lenna) # "window이름", ndarray(이미지배열)
cv2.waitKey(0) # 키보드 입력을 기다린다. (0: 입력될 떄까지 기다린다. 양수=ms(밀리초))
cv2.destroyAllWindows() # 모든 창(window)를 종료

# matplotlib으로 주피터노트북에 출력
import matplotlib.pyplot as plt
plt.figure(figsize=(10,10))
# plt.imshow(lenna)
plt.imshow(lenna[:, :, ::-1]) # height, width는 그대로 갖고오며 color channel은 역순으로 갖고와 RGB로 변형하여 전달
plt.axis('off')
plt.show()

# BGR->RGB 색공간 변환
lenna_rgb = cv2.cvtColor(lenna, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10,10))
plt.imshow(lenna_rgb)
plt.axis('off')
plt.show()

# 특정 키를 클릭했을때 종료
cv2.imshow('img', lenna)
while True:
    if cv2.waitKey(0) == 27: # 27: esq키 # ord('q'): # q를 입력할 때만 종료
        break
cv2.destroyAllWindows()

# 파일로 저장
import os
if not os.path.isdir('output'):
    os.mkdir('output')
```

## 02. 동영상
- VideoCapture 클래스 사용
  - 객체생성: `VideoCapture(filename)`
    - filename: 동양상파일인 경우 파일 경로, 웹캠영상인 경우 웹캠ID
  - 주요 메소드
    - isOpened(): bool - 대상에 연결 여부 반환
    - read(): (bool, img) - Frame 이미지로 읽기
      - bool: 읽었는지 여부, img: 읽은 이미지
  - 동영상 저장
    - `cv2.VideoWriter(filename, codec, fps, size)`
      - filename: 저장경로
      - codec: VideoWriter_fourcc(codec종류) 이용(문자열은 문자를 낱개로 각각 전달해야 한다.
      - fps, size: size는 영상의 width, height 순서로 대입
    - `cv2.VideoWriter().write(img)
      - Frame 
```python
# 웹캠
# VideoCapture(정수): 웹캠 연동
cap = cv2.VideoCapture(0)
# 연동 성공여부
if not cap.isOpened():
    print("웹캠 연결 실패")
    exit(1) # 프로그램 실행 종료 1: 비정상 종료
    
while True:
    # 웹캠으로부터 영상이미지(Frame)을 읽기
    ret, img = cap.read() # ret: boolean, img: ndarray-이미지
    if not ret:
        print("이미지 캡처 실패")
        break
    # 캡처한 이미지 화면에 출력
    img = cv2.flip(img, 1) # 양수: 수평반전, 0:수직반전, 음수: 수평+수직반전
    cv2.imshow('Frame', img)
    
    if cv2.waitKey(1) == ord('q'): # q를 입력받으면 웹캠 이미지 읽기(capture) 종료
        break
        
cap.release() # 웹캠연결 종료
cv2.destroyAllWindows() # 출력창 종료

# 동영상 파일
cap = cv2.VideoCapture("images/wave.mp4")

if not cap.isOpened():
    print("영상과 연결 실패")
    exit(1) # 프로그램 실행 종료 1: 비정상 종료
    
FPS = cap.get(cv2.CAP_PROP_FPS) # 영상의 fps값 조회
delay_time = int(np.round(1000/FPS)) # 1000밀리초(1초)/FPS
print(FPS, delay_time)

cnt = 0    
while True:
    # 웹캠으로부터 영상이미지(Frame)을 읽기
    ret, img = cap.read() # ret: boolean, img: ndarray-이미지
    if not ret:
        print("이미지 캡처 실패")
        break
    # 캡처한 이미지 화면에 출력
    img = cv2.flip(img, 1) # 양수: 수평반전, 0:수직반전, 음수: 수평+수직반전
    cv2.imshow('Frame', img)
    # 파일로 저장
    cv2.imwrite("test/output_{}.jpg".format(cnt), img)
    cnt += 1
    
    if cv2.waitKey(delay_time+500) == ord('q'): # q를 입력받으면 웹캠 이미지 읽기(capture) 종료
        break
        
cap.release() # 동영상연결 종료
cv2.destroyAllWindows() # 출력창 종료


codec = cv2.VideoWriter_fourcc(*"MJPG") # = ('M','J','P','G')
# VideoWriter 생성
writer = cv2.VideoWriter('output/webcam_output.avi', codec, fps, (width, height)) # shape메소드로 받아올 때의 순서 바꿔서 전달
if not writer.isOpened():
    print("동영상파일로 출력할 수 없습니다.")
    exit(1)
    
# while 문제 영상 저장 코드만 추가
# While True:
img = cv2.flip(img, 1)
writer.write(img)
```
