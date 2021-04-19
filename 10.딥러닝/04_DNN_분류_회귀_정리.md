# 데이터셋 API
- 데이터 입력 파이프라인을 위한 패키지
- `tf.data` 패키지에서 제공
- `tf.data.Dataset` 추상클래스에서 상속된 여러가지 클래스 객체를 사용, 또는 작성하여 사용

## 데이터 입력 파이프라인
**모델에 공급**되는 데이터에 대한 전처리 작업과 공급을 담당
- 이미지 데이터: 분산 파일시스템으로부터 이미지를 수집 작업, 이미지 변형, 무작위로 데이터를 선택하여 배치데이터를 만드는 작업
- 텍스트 데이터 경우: 원문을 토큰화하는 작업, 임베딩하는 작업, 길이가 다른 데이터를 패딩하여 합치는 작업 


## 데이터셋 API 사용 순서
1. 데이터셋 생성
  - from_tensor_slices(), from_generator() 클래스 메소드, tf.data.TFRecordDataset 클래스로 메모리/파일데이터를 데이터소스로 변환
  - from_tensor_slices(): 리스트 넘파이배열, 텐서플로 자료형에서 데이터 생성
2. 데이터셋 변형: map(), filter(), batch() 등 메소드로 데이터 소스 변형
3. for 반복문에서 iterate를 통해 데이터셋 사용

## Dataset의 주요 메소드
- map(함수) : dataset의 각 원소들을 함수로 처리
- shuffle(크기): dataset의 원소들 셔플. 크기는 섞는 공간의 크기로  **데이터보다 크거나 같으면** 완전셔플, **적으면 일부만 가져와서 섞어** 완전셔플이 안된다<br/>
=>데이터가 너무 많으면 적게 주기도 한다.)
- batch(size) : 반복시 제공할 데이터 수. 지정한 batch size만큼 data를 꺼내준다.

### 회귀 데이터셋 예시 - Boston Housing Dataset
```python
import numpy as np
import tensorflow as tf
from tensorflow import keras

# random seed
np.random.seed(1)
tf.random.set_seed(1)

# 데이터셋 로딩
(X_train, y_train), (X_test, y_test) = keras.datasets.boston_housing.load_data()
X_train.shape, X_test.shape

# 하이퍼파라미터 값들을 설정
LEARNING_RATE = 0.001 # 학습률
N_EPOCHS = 200 # 에폭 횟수
N_BATCHS = 32 # # batch_size. 32개 데이터셋마다 가중치 업데이트

N_TRAIN = X_train.shape[0] # train set의 개수
N_TEST = X_test.shape[0] # test set의 개수
N_FEATURES = X_train.shape[1] # input data의 feature(컬럼) 개수

# Dataset 생성
# drop_remainder=True: 마지막에 batch size보다 제공할 데이터가 적으면 학습시 버림
# repeat(): epoch을 반복할 때마다 계속 데이터를 제공하게 하기 위해
train_dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))\
.shuffle(N_TRAIN).batch(N_BATCHS, drop_remainder=True).repeat()
val_dataset = tf.data.Dataset.from_tensor_slices((X_test, y_test)).batch(N_BATCHS)

# 모델 생성 함수화
def create_model():
    model = keras.Sequential()
    # 입력 Layer를 따로 정의.
    # 첫번째 Layer를 만들 때 input_shape(입력데이터 1개의 형태)를 지정시 입력 Layer층이 자동 생성
    model.add(keras.layers.Dense(units=16, activation='relu', input_shape=(N_FEATURES,)))
    model.add(keras.layers.Dense(units=8, activation='relu'))
    # 출력 Layer
    model.add(keras.layers.Dense(units=1)) # 회귀의 출력층: units수는 1, activation 함수 사용
    
    # 모델 컴파일
    model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=LEARNING_RATE), # optimizer의 하이퍼파라미터를 기본값으로 쓸 경우 문자열로 "adam"으로 선언.
                 loss="mse") # 회귀의 Loss 함수: mse
    return model
    
# 모델 생성
model = create_model()

# 1 step: 한번 가중치를 업데이트. batch size
# 1 epoch: 전체 train 데이터를 한번 학습
steps_per_epoch = N_TRAIN // N_BATCHS # 학습데이터개수 // 배치수
validation_steps = int(np.ceil(N_TEST / N_BATCHS))

# 모델 학습과 동시에 학습 데이터 저장
history = model.fit(train_dataset, # train dataset (X_train, y_train)
         epochs=N_EPOCHS,
         steps_per_epoch=steps_per_epoch, # 1 에폭당 step 수
          validation_data=val_dataset, # 검증 Dataset 지정
          validation_steps=validation_steps
         )
         
# epoch당 loss와 val_loss 변화에 대해 선그래프 작성
import matplotlib.pyplot as plt
plt.figure(figsize=(10,7))

plt.plot(range(1, N_EPOCHS+1), history.history['loss'], label='Train loss')
plt.plot(range(1, N_EPOCHS+1), history.history['val_loss'], label='Validation loss')

plt.xlabel('Epochs')
plt.ylabel('Loss(MSE)')
plt.ylim(0, 100)
plt.legend()
plt.grid(True)
plt.show()
```
