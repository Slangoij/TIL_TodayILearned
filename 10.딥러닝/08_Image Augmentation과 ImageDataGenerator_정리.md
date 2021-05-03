# ImageDataGenerator
- 학습시 모델에 부족한 image dataset을 조금씩 조작하여 제공
```python
# 이미지 다운로드
# 'https://drive.google.com/uc?id=공유파일_ID
import gdown

url = 'https://drive.google.com/uc?id=1nBE3N2cXQGwD8JaD0JZ2LmFD-n3D5hVU'
fname = 'cats_and_dogs_small.zip'

gdown.download(url, fname, quiet=False) # url, 저장할 경우

# 리눅스 명령어로 디렉토리 생성
!mkdir data
# 압축풀기 -q: 로그 출력 ㄴㄴ, -d: 압축을 풀 디렉토리 지정
!unzip -q cats_and_dogs_small.zip -d data/cats_and_dogs_small
```

## 01. ImageDataGenerator()
- 매개변수
  - fill_mode(채우기): 사진의 이동이나 회전시 생기는 빈 공간을 채우는 방법
    - nearest-가장 가까운 픽셀로 채우기 / reflect: 경계면에 대칭하여 채움 / constant: 지정값으로 채움, dafault값은 0
  - Normalization: 
    - rescale-지정한 값을 각 픽셀에 곱하기
    - feature_center=True: channel별 평균을 기준으로 표준화
    - featurewise_std_normalization=True: channel 별로 표준화
  - 반전: horizontal_flip=True: 좌우반전 / vertical_flip_flip=True: 상하반전
  - 회전: rotation_range: 입력값의 반대 부호값부터 해당값까지 랜덤값으로 회전
  - 이동: width_shift_range: 좌우이동 / height_shift_range: 상하이동
  - Zoom_range: 1미만-축소 / 1초과-확대
  - 전단변환(shear): shear_range-각도 지정
  - 명암: brightness_range-리스트(범위), 1미만-어두움 / 1초과-밝음

```python
# 임의의 모델 생성 후

# ImageDataGenerator 생성 => Augmentation, 입력 pipeline
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# train, validation, test 디렉토리별로 데이터 저장되어 있어야
train_dir = '/content/data/cats_and_dogs_small/train'
validation_dir = '/content/data/cats_and_dogs_small/validation'
test_dir = '/content/data/cats_and_dogs_small/test'

# 1. ImageDataGenerator - No Augmentation
train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

# Gen.flow_from_directory() 이용해 iterator 생성
train_iterator = train_datagen.flow_from_directory(directory=train_dir, # 이미지가 존재하는 디렉토리
                                                   target_size=(IMAGE_SIZE, IMAGE_SIZE), # Resize 크기(height,width)
                                                   class_mode='binary', # dog/cat => binary
                                                   batch_size=N_BATCHS)

validation_iterator = test_datagen.flow_from_directory(directory=validation_dir,
                                                      target_size=(IMAGE_SIZE, IMAGE_SIZE),
                                                      class_mode='binary',
                                                      batch_size=N_BATCHS)

test_iterator = test_datagen.flow_from_directory(directory=test_dir,
                                                target_size=(IMAGE_SIZE, IMAGE_SIZE),
                                                class_mode='binary',
                                                batch_size=N_BATCHS)
                                                                                             
# 이미지 generator로 만들어진 dataset 전달
history = model.fit(train_iterator,
                    epochs=N_EPOCHS,
                    steps_per_epoch=len(train_iterator),
                    validation_data=validation_iterator,
                    validation_steps=len(validation_iterator))
                    
# 2. ImageDataGenerator - Augmentation 사용
train_datagen = ImageDataGenerator(rescale=1./255,
                                   rotation_range=40,
                                   width_shift_range=0.2,
                                   height_shift_range=0.2,
                                   zoom_range=0.2,
                                   brightness_range=(0.7,1.3),
                                   horizontal_flip=True,
                                   fill_mode='constant')
# validation, test용
test_datagen = ImageDataGenerator(rescale=1./255)
```
  
## 02. ImageDataGenerator에 dataset을 제공하는 메소드
  ### 1. flow_from_directory()
  - 주요 매개변수
    - directory: 이미지 저장경로(해당 디렉토리 하위에 클래스 별로 디렉토리, 그 밑에 이미지 저장되있어야)
    - target_size: 해당 이미지 크기로 변환하여 전달
    - color_mode: grayscale-흑백, rgb-컬러(default), rgb-컬러+투명도
    - class_mode: 분류 종류 지정, binary / category(onehotencoding된 경우) / sparse(안된 경우)/ None(하위 디렉토리로 추론)
    - batch_size: 미니배치사이즈 지정(Default:32)
  - 반환값
    - DirectoryIterator: batch size만큼 image와 label 제공
  - class조회: `DirectoryIterator객체.class_indices.keys()`

  ### 2. flow_from_dataframe()
  - 파일의 경로, label을 DataFrame으로 생성하여 이를 이용하여 데이터셋 전달
  - from directory와 다른 매개변수
    - DataFrame
    - x_col: 이미지 경로 컬럼명
    - y_col: 라벨 컬럼명

  ### 3. flow()
  - ndarray 타입의 이미지를 매개변수로
  - 매개변수: x(input data), y(label), batch_size

```python
import gdown

url = 'https://drive.google.com/uc?id=17ejPJw42TgTv0jCPMMlVTHwF57XYE2kb'
fname = 'cats_and_dogs_unions.zip'
gdown.download(url, fname, quiet=True)

!mkdir data
!unzip -q ./cats_and_dogs_unions.zip -d ./data/cats_and_dogs
```
