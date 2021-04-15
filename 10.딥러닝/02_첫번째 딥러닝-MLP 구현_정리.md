# MLP(Multi-Layer Perceptron)
- Keras를 사용한 개발 과정
  1. 입력(X), 출력(y) 텐서로 이뤄진 훈련 데이터 정의 (ML과 같다)
  2. 입력과 출력 연결하는 Layer(층)으로 이뤄진 모델 정의
    - Sequential 방식: 순서대로 layer 쌓아올려 생성
    - Functional API 방식: 다양한 구조의 네트워크를 함수형으로 생성
    - Subclass 방식: 네트워크 정의하는 클래스로 구현
  3. 모델 컴파일: 학습시 필요한 손실함수, 최적화기법, 평가지표 설정
  4. 훈련: 모델의 fit메소드에 훈련데이터 입력하여 훈련
  ![다운로드](https://user-images.githubusercontent.com/71580318/114862383-6cbb6400-9e29-11eb-96dc-131436be5ef6.png)
  
실습: MNIST 이미지 분류
- 싸이킷런의 예제보다 조금 더 고해상도의 숫자샘플
- 샘플 개수: train: 60,000 / test: 10,000
- 샘플 데이터 시각화
```python
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.figure(figsize=(15,5))
# 5개 이미지를 확인
for i in range(5):
    plt.subplot(1,5, i+1)
    plt.imshow(X_train[i], cmap='gray')
    plt.title(y_train[i])
    plt.axis('off')
    
# plt.colorbar()
plt.show()
```

### 실예제
```python
import tensorflow as tf
from tensorflow import keras

# 싸이킷런과 데이터 받아오는 순서 다름에 유의
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()
```

##### 1. 신경망 구현
```python
# 모델 생성
model = keras.Sequential()
# 층(Layer)를 모델에 추가
model.add(keras.layers.Input((28,28)))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(256, activation='relu'))
model.add(keras.layers.Dense(128, activation='relu'))
model.add(keras.layers.Dense(10, activation='softmax'))

# 모델 개요 확인
model.summary()
```

##### 2. 컴파일
- 모델에 추가 설정 - 손실함수/최적화함수/평가지표
```python
model.compile(optimizer='adam', # Optimizer 등록
             loss='categorical_crossentropy', # Loss Function 등록
             metrics=['accuracy']) # 평가지표 - Training 도중 validation 결과를 확인
```

##### 3. 데이터 준비
- X: 0 ~ 1 사이의 값으로 정규화 / y: 원핫인코딩(1tensorflow.keras.utils.to_categorical()1 이용)
```python
X_train = X_train/255.
X_test = X_test/255.

y_train = keras.utils.to_categorical(y_train)
y_test = keras.utils.to_categorical(y_test)
```

##### 4. 학습
- epoch: 전체 데이터를 몇 번 학습시킬지
- batch_size: 전체 데이터를 몇 개의 샘플로 나눠 학습할지
```python
model.fit(X_train, y_train,
         epochs=10, # epoch: 전체 train dataset을 한번 학습 - 1 epoch
         batch_size=100, # 파라미터 업데이트(최적화)를 100개마다 처리
         validation_split=0.2)
```

##### 5. 평가
- predict()
  - 각 클래스 별 확률 반환 => 머신러닝의 predict_proba 역할
- 이진 분류(binary classification)
  - `numpy.argmax(model.predict(x) > 0.5).astype("int32")`
- 다중클래스 분류(multi-class classification)
  - `numpy.argmax(model.predict(x), axis=-1)`
```python
# 추론 => class별 확률
pred = model.predict(X_test[:10])
model.predict_classes(X_test[:10])
```
