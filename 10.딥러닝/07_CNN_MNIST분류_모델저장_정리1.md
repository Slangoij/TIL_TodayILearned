# 케라스 이용하여 MINST를 이용한 실제 CNN 구현

## 00.(코랩 환경설정)
![2021-04-26 18;10;35](https://user-images.githubusercontent.com/71580318/116058358-b8d49700-a6ba-11eb-90b1-842f5990d94b.PNG)

## 01. 결과 그래프 출력 함수 생성
```python
import matplotlib.pyplot as plt
# 학습결과 그래프 함수
def plot_history(history):
  # Loss
  plt.subplot(1,2,1)
  plt.plot(history.history['loss'], label='Train loss')
  plt.plot(history.history['val_loss'], label='Validation loss')
  plt.title('Loss')
  plt.xlabel('epoch')
  plt.ylabel('loss')
  
  plt.subplot(1,2,2)
  plt.plot(history.history['accuracy'], label='Train accuracy')
  plt.plot(history.history['val_accuracy'], label='Validation accuracy')
  plt.title('Accuracy')
  plt.xlabel('epoch')
  plt.ylabel('accuracy')
  
  plt.legend()
  plt.show()
```

## 02. 데이터셋, 하이퍼파라미터 설정
```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
# from tensorflow.keras.layers import Dense, Conv2D, MaxPool2D, Flatten, Input
import numpy as np

np.random.seed(1)
tf.random.set_seed(1)

# 하이퍼파라미터 설정
LEARNING_RATE = 0.001
N_EPOCHS = 20
N_BATCHS = 100
N_CLASS = 10

# 데이터셋 로드
(train_image, train_label), (test_image, test_label) = keras.datasets.mnist.load_data()
train_image.shape, train_label.shape, test_image.shape, test_label.shape

# 추가 변수 설정
N_TRAIN = train_image.shape[0]
N_TEST = test_image.shape[0]

# 전처리: 이미지 - 정규화(0 ~ 1)
#         label - onehotencoding(생략-loss: sparse_categorical_crossentropy)
X_train, X_test = train_image/255., test_image/255.
X_train, X_test  = X_train[..., np.newaxis], X_test[..., np.newaxis] # channel 축 추가 작업(기존 흑백데이터라 channel 미존재)
y_train, y_test = train_label, test_label

# dataset 구성(셔플링, 배치나누기, repeat(데이터 입력반복))
train_dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train)).shuffle(N_TRAIN).batch(N_BATCHS, drop_remainder=True).repeat()
test_dataset = tf.data.Dataset.from_tensor_slices((X_test, y_test)).batch(N_BATCHS)
```

## 03. 모델 구성
```python
# convolution layer의 filter 개수는 적은 개수에서 점점 늘려간다.
# 모델 생성 함수화

def create_model():
  model = keras.Sequential()
  model.add(layers.Input((28,28,1))) # Input shape
  # Convolution layer: Conv2D -> MaxPool2D
  model.add(layers.Conv2D(filters=32, # Filter 개수
                          kernel_size=(3,3), # Filter(kernel)의 height, width, h/w가 같은 경우에는 정수
                          padding='same', # Padding방식: 'valid', 'same' - 대소문자 무관
                          strides=(1,1), # Strides 설정: (상하). 상하/좌우 같을 시 정수
                          activation='relu'))
  # Max Pooling layer => MaxPool2D
  model.add(layers.MaxPool2D(pool_size=(2,2), # 영역 height,width 크기 지정, h/w 같을 시 정수. default=(2,2)
                             strides=(2,2), # dafault: None => pool_size를 사용, 두개 값이 같을 시 정수
                             padding='same')) # "valid" - 뒤에 남는 것은 버린다
  model.add(layers.Conv2D(filters=64,
                          kernel_size=3,
                          padding='same',
                          strides=1,
                          activation='relu'))
  model.add(layers.MaxPool2D(padding='same')) # pool_size, strides: dafault 값으로 설정

  # Classification Layer -> Fully Connected Layer
  # Conv 거친 Feature map은 3차원 형태
  model.add(layers.Flatten())
  model.add(layers.Dense(256, activation='relu'))

  # 출력
  model.add(layers.Dense(N_CLASS, activation='softmax'))

  return model
  
# 모델 생성 및 개요 확인
model = create_model()
model.summary()
# 모델 구성 그림으로 확인
keras.utils.plot_model(model, show_shapes=True)
# 모델 컴파일
model.compile(optimizer=keras.optimizers.Adam(learning_rate=LEARNING_RATE),
              loss='sparse_categorical_crossentropy', # sparse_catetorical_crossentropy: y가 one hot encoding이 안된 경우 사용
              metrics=['accuracy'])
```
## 04. 모델 학습
```python
# 훈련 변수 설정
steps_per_epoch = N_TRAIN // N_BATCHS # 에폭당 스텝(배치 한번 입력 후 파라미터 업데이트 과정단위)
validation_steps = int(np.ceil(N_TEST / N_BATCHS))
# 히스토리 남기며 학습 
history = model.fit(train_dataset,
                    epochs=N_EPOCHS,
                    steps_per_epoch=steps_per_epoch,
                    validation_data=test_dataset,
                    validation_steps=validation_steps)
```

## 05. 학습 결과 확인
```python
model.evaluate(test_dataset)

# 새로운 데이터 추론
pred = model.predict(X_test[:10])
pred_class = np.argmax(pred, axis=-1)
# 에러 발생한 예제 확인
pred = model.predict(X_test)
pred_class = np.argmax(pred, axis=-1)
pred_class[:10]

# 틀린 것 10개 확인
plt.figure(figsize=(15,10))
for i in range(10):
  err = error_idx[i]
  plt.subplot(2,5, i+1)
  plt.imshow(test_image[err], cmap='gray')
  plt.title(f'label:{y_test[err]}, pred:{pred_class[err]}')
  plt.axis('off')
plt.tight_layout()
plt.show()
```
