# Iris 예측모델(결정Tree 모델)
- 머신러닝계의 `HelloWorld!`
- 용어
  - 속성(Feature) : 입력데이터(X), 독립변수, 학습해야 하는 값들
  - 레이블(Label)[=타겟(Target)] : 출력데이터(Y), 종속변수, 지도학습시 정답데이터(분류의 경우 레이블을 구성하는 고유값을 클래스(Class)라 한다.

- scikit-learn 내장 데이터셋 호출
```python
from sklearn.datasets import load_iris
import numpy as np
iris = load_iris()
```
- 내장 데이터셋 구성
> **target_names**: 예측하려는 값(class)을 가진 문자열 배열
> **target**: Label(출력데이터)
> **data**: Feature(입력변수)
> **feature_names**: 입력변수 각 항목의 이름
> **DESCR**: 데이터셋에 대한 설명

- 데이터셋 데이터프레임으로 변환
```python
import numpy as np
import pandas as pd
# 기존 데이터셋 활용
iris_df = pd.DataFrame(iris['data'], columns=iris['feature_names'])
iris_df['species'] = iris['target']
# 파일 직접 읽어오기
iris_tmpdf = pd.read_csv(r'파일위치', header=0)
iris_tmpdf.columns = ['꽃받침 길이', '꽃받침 너비', '꽃잎 길이', '꽃잎 너비', '품종']
iris_tmpdf
```

### 01. 결정Tree 알고리즘을 이용한 분류
- 독립 변수의 조건에 따라 종속 변수를 분리(Y/N 형식, 이진으로 갈리도록 질문 구성)
- 장점: 머신러닝의 몇 안되는 White box 모델 / 단점: 과적합 빈번
- 절차
> 1. import 모델
> 2. 모델 생성
> 3. 모델 학습시키기
> 4. 예측
```python
# 1. import 모델
from sklearn.tree import DecisionTreeClassifier
# 2. 모델 생성
tree = DecisionTreeClassifier()
# 3. 모델 학습시키기(Train)
tree.fit(iris['data'], iris['target']) # input_data(feature), output_data(label)
# 4. 예측
pred = tree.predict([[5, 3.5, 1.4, 0.25]]) # 예측할 대상을 전달. 전달값을 Feature, 2차원 배열. 반환: label
print(pred)

# 예측할 결과는 동시에 여러 값을 예측할 수 있으므로 갯수에 무관하게 2차원 배열로 입력
tmp_iris = [
    [5, 3.5, 1.4, .25],
    [6, 7, 1.5, 2.3],
    [2, 3, 5, 7]
]
pred2 = tree.predict(tmp_iris)
iris['target_names'][pred2]
```

> 5. 검증
- 검증하기 위해 기존의 데이터를 분할하여 훈련데이터셋과 평가데이터셋으로 분할
- 보통 비율은 훈련, 평가 순으로 8:2, 7:3 정도, 데이터셋이 충분시엔 6:4로도
- 각 클래스가 같은 비율로 나뉘어야 함
- 머신러닝 평가지표 함수들은 sklearn.metrics 모듈에 있다.
  - accuracy(정확도)
    - 전체 데이터셋 중 맞춘 개수의 비율
  - 혼동행렬 (Confusion Matrix)
    - 예측 한 것이 실제 무엇이었는지를 표로 구성한 평가 지표
    - 분류의 평가 지표로 사용된다.
    - axis=0: 실제, axis=1: 예측
```python
from sklearn.model_selection import train_test_split # DataSet을 Train dataset과 Test dataset으로 분할하는 함수
# input, output(target)
X_train, X_test, y_train, y_test = train_test_split(iris['data'], # input dataset
                                                    iris['target'], # output dataset,
                                                    test_size=0.2, # test set의 비율(0 ~ 1). default: 2.5
                                                    stratify = iris['target'], # class들을 원본 데이터셋과 같은 비율로 분할
                                                    random_state=1) # random의 seed값 정의
```


- 전체 절차 코드
```python
# 모델 생성
tree = DecisionTreeClassifier()

# 모델 학습
tree.fit(X_train, y_train)

# 모델 평가
pred_train = tree.predict(X_train)

from sklearn.metrics import accuracy_score # 정확도 검증 함수
acc_train_score = accuracy_score(y_train, pred_train) # (정답, 예측결과)
acc_test_score = accuracy_score(y_test, pred_test)

print("Train Set 정확도:", acc_train_score)
print("Test Set 정확도:", acc_test_score)

from sklearn.metrics import confusion_matrix
cm_train = confusion_matrix(y_train, pred_train)
cm_test = confusion_matrix(y_test, pred_test)
print("평가 by 혼동행렬:", cm_train)
```
