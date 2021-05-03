##### 내용이 길어 핵심만 정리, 코드는 주피터 참고

# 01. GAP
- output으로 나온 Feature map의 개수가 충분히 많을 시, 계산의 효율을 위해서 각 채널별 평균값을 추출하는 방식
- `model.add(keras.layers.GlobalAveragePooling2D())`


# 02. Transfer learning(전이학습)
- 데이터셋을 미리 학습한 pre-trained Model의 weigth(가중치)를 이용하여 새로운 데이터셋을 예측하는 방식
- 이를 이용해 VGG16 모델과 ResNet(pre-trained model)에 적용하려 한다.
  - ILSVRC(ImageNet Scale Visual Recognition Challenge, 2010~2017) 대회에서 수상한 SOTA(State-Of-The-Art) 모델들
  - VGG16: 14년 2등한 모델, 기존의 5x5 필터를 3x3 필터 2개로 대체하여 파라미터 수를 줄여준 모델
  - ResNet: 15년 우승, shortcut connection 기법을 이용해 layer수를 획기적으로 늘린 CNN모델
  - ` H(x) = F(x) + x`
  - x: input, H(x): output, F(x): layer통과값 에서 F(x)를 0으로 만드는 방향으로 학습. F(x)는 잔차(Residual)이라고 한다.

- 전이학습 방식
  - pretrained Model(conv_base로 칭함)을 `tensorflow.keras.applications`패키지를 통해 전이학습
  - 생성자 매개변수:
    - weights: 모델의 학습된 가중치, default-'imagenet'
    - include_top: FC(Fully Connected layer) 포함 여부
    - input_shape: 입력 텐서(3D), dafault: (224,224,3)
- 특성 추출 방식: 빠른 추출방식, 받아온 특성 layer를 이용해 새로운 모델 구현하는 방식
  - 빠른 추출방식은 `conv_base`에 입력하여 나온 출력값을 새로 학습할 모델의 입력값으로 전달해주는 식
  - 후자는 conv_base에 바로 layer를 더해 전체 모델을 다시 학습 => conv_base의 가중치는 학습되지 않도록 고정하지만 데이터가 다시 거치기 때문에 느림.
  - 전자만 data augmentation 사용가능


# 03. Fine-tuning(미세조정)
- pre-trained Model을 다시 특정 custom dataset에 재학습
- 전략
  - 1. train dataset의 양이 많고, 기존 dataset과 custom dataset의 class간 유사성이 낮은 경우
    => 전체 모델 재학습 (거의 새로운 데이터이므로)
    
  - 2. train dataset의 양이 많고, 기존 dataset과 custom dataset의 class간 유사성이 높은 경우
    => pre-train 모델 top layer일부 재학습 (비슷한 데이터지만 새로운 데이터도 많으니 일부 학습)
    
  - 3. train dataset의 양이 적고, 기존 dataset과 custom dataset의 class간 유사성이 낮은 경우
    => pre-train 모델 top layer일부 재학습 (새로운 데이터지만 전부 학습시키기엔 양이 적으니)
    
  - 4. train dataset의 양이 적고, 기존 dataset과 custom dataset의 class간 유사성이 높은 경우
    => classifier만 재학습 (같은 데이터이며 학습도 시킬 수 없다)
