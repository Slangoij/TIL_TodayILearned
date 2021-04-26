## 06. 모델 저장
- 학습 끝난 후 저장
  - 파라미터만 저장
  - 모델 전체 저장
- 학습 중간 저장
  - callback함수 사용

### 1. 학습 끝난 후 저장방식
- 텐서플로 파일 타입
  - checkpoint: 파라미터 저장용
    - 형식: Tensorflow checkpoint(Dafault), HDF5
  - SavedModel: 모델 구조 + 파라미터 저장용
- ex) 코랩 사용환경 가정
```python
# 파라미터 저장할 경로 생성
import os
base_dir = "/content/drive/MyDrive/Colab Notebooks/Playdata/saved_models" # 모델/파라미터들을 저장할 root
weight_dir = os.path.join(base_dir, 'mnist', 'weights')
print(weight_dir)
if not os.path.isdir(weight_dir):
  os.makedirs(weight_dir, exist_ok=True) # exist_ok=False(default): 이미 경로가 있으면 예외발생, True: 예외발생 없음
weight_path = os.path.join(weight_dir, 'mnist_cnn_weights.ckpt') # 저장할 디렉토리 + 파일명
# 파라미터 저장
model.save_weights(weight_path)
# model.save_weights(weight_h5_path, save_format='h5') # hdt5 형식 저장시

# 모델 저장경로 생성
model_dir = os.path.join(base_dir, 'mnist', 'models', 'saved_model')
if not os.path.isdir(model_dir):
  os.makedirs(model_dir, exist_ok=True)
# 모델 저장
model.save(model_dir) # SaveModel 형식으로 저장시 디렉토리 지정
```

### 2. 학습 중간 저장방식
- Callback: 학습 도중 특정 이벤트 발생시 호출할 수 있는 다양한 함수 제공
- `ModelCheckpoint`: 지정한 평가지표가 가장 좋을 때 모델, 파라미터 저장
- `EarlyStopping`: 지정한 평가지표가 지정한 epoch동안 좋아지지 않을 경우 학습 중단
```python
# 중간 결과 저장할 경로 생성
callback_dir = os.path.join(base_dir, 'mnist', 'models', 'callback')
if not os.path.isdir(callback_dir):
  os.makedirs(callback_dir, exist_ok=True)
callback_path = os.path.join(callback_dir, 'save_model_{epoch:02d}.ckpt') # {epoch:02d} - 포멧문자열. 몇번 쨰 에폭의 저장포인트인지

# ModelCheckpoint callback 생성
mc_callback = keras.callbacks.ModelCheckpoint(filepath=callback_path, # 학습 도중 모델/파라미터 저장할 경로
                                              save_weights_only=True, # True: 가중치 저장, False(default): 모델+가중치 저장
                                              save_best_only=True, # True: 가장 성능이 좋았을 당시에만 저장. False(default): 매 에폭마다 저장.
                                              monitor='val_loss', # save_best_only=True 일 때 성능확인할 평가지표
                                              verbose=1 # 저장할 때마다 로그 출력
                                              )

# EarlyStopping callback 생성
es_callback = keras.callbacks.EarlyStopping(monitor='val_loss',
                                            patience=5) # 5 에폭 학습하는 동안 val_loss가 개선되지 않으면 학습 중단)

# 아래와 같이 학습시 callbacks 매개변수에 리스트안에 넣어 입력
model2.fit(train_dataset,
          epochs=N_EPOCHS,
          steps_per_epoch=steps_per_epoch,
          validation_data=test_dataset,
          validation_steps=validation_steps,
          callbacks=[mc_callback, es_callback])
```
