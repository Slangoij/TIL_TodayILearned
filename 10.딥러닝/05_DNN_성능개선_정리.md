# DNN(Deep Neural Networks) 성능개선 기법
- 최적화, 일반화
  - 최적화: train data에서 최고의 성능을 얻기 위한 모델 조정과정
  - 일반화: 훈련된 모델의 처음 보는 데이터에 대한 판단 성능
- 과소적합: Epoch를 진행해도 train, test loss 모두 나아지지 않는 경우 => 복잡한 모델 or 튜닝 필요
- 과(대)적합: Epoch가 진행 되며 train loss는 감소하지만 test loss가 증가(훈련 데이터셋에만 특화) => 단순한 모델 사용

=> 보통 딥러닝 쯤 되면 과소보단 과대적합 발생
### 과적합 방지 방법
- 더 많은 data를 수집하는 것은 현실적으로 어려움 => 모델을 간단히 만드는 방법 주로 선택
- 따라서 모델의 layer나 unit수를 조정

## 01. Dropout Layer 추가
- 학습시 일부의 노드를 임의로 선정, 누락하여 학습 => train set에서
- 일반적으로 0.2 ~ 0.5 사이의 값 지정

## 02. Batch Normalization(배치정규화)
- 각 layer에서 출력된 값을 표준정규화하여 각 layer의 입력분포를 균일화한다.
- 딥러닝의 대부분이 그렇듯 공학적이기보단 실험적으로 검증된 방법
- 효과
  - 랜덤하게 생성되는 초기 가중치에 대한 영향 완화
  - 학습 도중의 과적합 규제 효과
  - Gradient Vanishing, Gradient exploding 완화

## 03. Learning Rate Decay(학습률 조절)
- Adam이나 RMSProp 등의 optimizer는 가중치에 대한 Loss의 변화율을 구하는 것이고 그 앞에 더해지는 변화율은 우리가 조절할 수 있는 하이퍼파라미터

## 성능개선 방법 정리
- Hyper parameter 조절
  - Hidden layer 수
  - Hidden unit(nodes) 수
  - activation function 종류
  - minibatch size
  - epoch 수
  - Optimizer 종류
  - learning rate
  - regulation - dropout, batch norm 등)
