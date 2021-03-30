# Voting
- 종류:
  1. `hard voting`: 다수의 추정기가 결정한 예측값들 최빈값 선택하는 방식
  ![다운로드](https://user-images.githubusercontent.com/71580318/112966533-4937be80-9185-11eb-95b8-2b0e4835b8af.png)
  2. `soft voting`: 다수 예측값 중 확률의 평균값이 가장 큰 값 선택
  ![다운로드 (1)](https://user-images.githubusercontent.com/71580318/112966582-548aea00-9185-11eb-86b6-24326008ef39.png)
- 일반적으로 소프트 보팅의 성능이 더 우수
- 보팅은 성향이 다르며 비슷한 성능의 모델을 결합시 가장 우수한 성능 발휘
- `VotingClassifier` 이용
  - estimators : 앙상블할 여러 모델 설정.  `("추정기이름", 추정기)`의 튜플 리스트로 묶어 전달
  - voting: voting 방식. `hard(기본값)`, `soft`  지정
```python
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline

# wine data
wine = pd.read_csv('data/wine.csv')
X = wine.drop('color', axis=1)
y = wine['color']

# 원핫인코딩
ohe = OneHotEncoder()
quality = ohe.fit_transform(np.array(X['quality']).reshape(-1,1)).toarray()
quality
X = pd.concat([X, pd.DataFrame(quality, columns=ohe.get_feature_names())], axis=1)
X.drop('quality', axis=1, inplace=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=1)
from sklearn.pipeline import make_pipeline

knn = KNeighborsClassifier(n_neighbors=5)
svc = SVC(C=1.0, gamma=0.1, probability=True)
rf = RandomForestClassifier(n_estimators=200)

# estimators = [('knn', knn),
#               ('random forest', rf),
#               ('svm', svc)]

# knn, svc는 Scaling을 처리. RF는 처리x
knn_pipe = make_pipeline(StandardScaler(), knn)
svc_pipe = make_pipeline(StandardScaler(), svc)

estimators = [('knn', knn_pipe),
              ('random forest', rf),
              ('svm', svc_pipe)]

voting = VotingClassifier(estimators)

# 다수의 지표 동시에 확인할 함수 작성
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
def print_metrics(y, y_pred, title=None):
    if title: # title != None
        print(title)
    metrics = f"""정확도:{accuracy_score(y, y_pred)}, 재현율:{recall_score(y, y_pred)},\n정밀도:{precision_score(y, y_pred)}, f1점수:{f1_score(y, y_pred)}"""
    print(metrics)
    
voting.fit(X_train, y_train) # estimators에 등록할 모든 모델을 학습시킴
pred_train = voting.predict(X_train)
pred_test = voting.predict(X_test)

print_metrics(y_test, pred_test, "Test 데이터셋-Hard Voting")

# soft voting: class별 확률의 평균으로 결정
voting_soft = VotingClassifier(estimators,
                              voting='soft') # default: "hard"
                              
voting_soft.fit(X_train, y_train)
pred_train_soft = voting_soft.predict(X_train)
pred_test_soft = voting_soft.predict(X_test)
print_metrics(y_train, pred_train_soft, "TrainSet-Soft Voting")
print_metrics(y_test, pred_test_soft, "TestSet-Soft Voting")
```
  
