# CNN - 합성곱 신경망(Convolutional Neural Network)
- 얀르쿤(Yann Lecun)이 1989 LeNet 모델을 만들면서 제안한 딥러닝 구조
- 주로 컴퓨터 비전에서 사용됨
- 사용영역(컴퓨터비전)
- Image Classification(이미지분류): 입력된 이미지를 분류
- Object Detection(객체 탐지): 이미지 내 물체의 위치 정보를 찾아 표기(하나의 물체일 경우 Localization, 여러 개일 경우 Object Detection
- Image Segmentation: 이미지 내의 특정 물체와 관련된 픽셀을 하나로 묶어 표기
- Image Captioning: 이미지에 대한 설명문 자동으로 생성
- Super Resolution: 저해상도의 이미지를 고해상도의 이미지로 변환
- Neural Style Transfer: 입력이미지와 스타일 이미지를 합쳐 새로운 스타일의 이미지 생성
- Text Detection & OCR: text detection-이미지 내 텍스트영역을 찾아 표시, OCR: 해당 영역의 글자들이 어떤 문자인지 해석
- Human Pose Estimation: 인간의 특정 신체부위를 탐지하여 포즈 예측

## 이미지 인식이 어려운 이유
- 컴퓨터가 입력받는 이미지는 0~255의 숫자로 이뤄진 매트릭스이므로
- 이외 배경과 대상이 비슷한 경우, 같은 종류 대상에 매우 많은 다른 형태 존재, 가려져 있는 대상일 경우 등 다양한 이유로

## 기존 이미지 처리 방식과 딥러닝의 차이
- 기존 방식 - Handcrafted Feature
  - 사람이 이미지의 특징을 직접 찾아 학습
- 딥러닝 - End to End learning
  - 이미지 특징 추출부터 분류까지 모두 컴퓨터가 학습

## CNN 구성
- 이미지로부터 특정 위치의 특성을 추출하는 Feature Extraction layer(Convolution layer)와 Classification layer(Dense layer)로 나뉜다.
- 기존의 Fully Connected Layer는 유닛의 수에 따라 학습할 weight의 수가 상당히 커지기 때문에 메모리 부족 현상, 그리고 이미지의 공간적 구조학습에 대한 어려움 존재

### 01. Filter
- 주로 3,3의 shape을 가진 매트릭스 input이미지에 갖다 대어 각 부분의 특성을 추출
- ![numerical_no_padding_no_strides](https://user-images.githubusercontent.com/71580318/116053815-0a2e5780-a6b6-11eb-9f8c-cb93d11cbae2.gif)
- 이렇게 부분적 특징을 찾아내는 방식의 층을 여러겹 쌓으면 뒤로 갈수록 더욱 전체적이고 추상적인 개념을 추출
- filter의 크기는 (height, width, channel)로 컬러이미지는 3, 흑백은 1의 채널이 필요
- 이러한 필터 k개를 거쳐 나오는 output은 'same' padding 적용시, (기존이미지 height, 기존이미지 width, k)개의 형식을 가진 feature map이다.
- padding: 이미지의 가장 자리 픽셀이 연산에 적게 반영되는 것을 방지하는 방법
  - option으로 'same'시 output의 이미지 크기가 filtering 되기 전과 똑같이 유지
  - 'valid'시 padding하지 않음
- strides: filter가 한번 연산후 이동하는 간격, 보통 1지정

### 02. MaxPooling
- 부분적 특징을 그 중 최대값만 뽑아내어 한 영역의 특징을 조금 더 개략화한다. 일반적으로 size, strides를 같이 주어 subsampling 효과

### 참고: filter류 input, ouput 크기 계산 수식
![2021-04-26 17;49;55](https://user-images.githubusercontent.com/71580318/116056196-790cb000-a6b8-11eb-83c5-6a9c8839831f.PNG)


### 보통 위의 Conv layer와 pooling layer를 충분히 거쳐 특징을 추출했다면, 마지막에 FC layer를 거쳐 분류 
