# 함수형 API, 순차적 API
- 순차적(Sequential) API: 각 층의 입력, 출력이 하나씩이므로 한정적이지만 모델 작성 쉬움.
```python
seq_model = keras.Sequential()
seq_model.add(layers.Input(shape=(32,32,3)))
seq_model.add(layers.Conv2D(filters=64, kernel_size=3, padding='same', activation='relu'))
seq_model.add(layers.Flatten())
seq_model.add(layers.Dense(units=256, activation='relu'))
seq_model.add(layers.Dense(units=10, activation='softmax'))
```
- 함수형(Functional) API: 작성은 어렵지만 다중입출력을 다루기 가능
```python
input_tensor = layers.Input(shape=(32,32,3))
conv_tensor = layers.Conv2D(filters=64, kernel_size=3, padding='same', activation='relu')(input_tensor)
pool_tensor = layers.MaxPool2D(padding='same')(conv_tensor)

flatten_tensor = layers.Flatten()(pool_tensor)

dense_tensor = layers.Dense(units=256, activation='relu')(flatten_tensor)
dense_tensor2 = layers.Dense(units=128)(dense_tensor)

bn_tensor = layers.BatchNormalization()(dense_tensor2)
relu_tensor = layers.ReLU()(bn_tensor)

output_tensor = layers.Dense(units=10, activation='softmax')(relu_tensor)

fn_model = models.Model(input_tensor, output_tensor) # (입력텐서, 출력텐서)

fn_model.summary()
```

- 레이어 합치는 함수
  - `concatenate(list, axis=-1)`: 합칠 레이어를 list에 묶어 전달, axis는 합칠 기준 축
  - add(list), substract(list), multyply(list): 같은 index의 값들은 계산하여 하나의 레이어로 만든다.
  - 예시: residual block
  ```python
  # Residual block
  input_tensor = layers.Input((32,32,3))
  x = layers.Conv2D(64, kernel_size=3, padding='same', activation='relu')(input_tensor)
  x1 = layers.Conv2D(64, kernel_size=3, padding='same')(x)
  b1 = layers.BatchNormalization()(x1)
  add1 = layers.add([x, b1])
  r = layers.ReLU()(add1)

  r_block_model = models.Model(input_tensor, r)
  ```
