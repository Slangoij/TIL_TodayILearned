# Support Vector Machine(SVM)

### 01. 선형(Linear) SVM
- 딥러닝 이전에 가장 활용도가 높았던 `분류`모델
- 목표: support vector간의 가장 넓은 margin을 갖는 초평면(데이터 구분을 나누는 경계)를 찾기
![다운로드](https://user-images.githubusercontent.com/71580318/112831415-dbc95680-90ce-11eb-9824-84b0d1ed78f9.png)
- 하이퍼파라미터: `C`
  - 기본값 1, 값이 커질수록 과적합 가능성 상승 -> Hard Margin / 작을수록 -> Soft Margin
  ```python
  import numpy as np
  import pandas as pd
  from sklearn.datasets import load_breast_cancer
  from sklearn.model_selection import train_test_split, GridSearchCV
  from sklearn.preprocessing import StandardScaler
  from sklearn.svm import SVC
  from sklearn.metrics import accuracy_score

  X, y = load_breast_cancer(return_X_y=True)
  X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=1)

  # SVM은 선형모델이므로 Scaling 작업이 필요
  scaler = StandardScaler()
  X_train_scaled = scaler.fit_transform(X_train)
  X_test_scaled = scaler.transform(X_test)

  # from sklearn.svm import LinearSVC
  # svc = LinearSVC() => 아래와 같이 선형 SVC 모델
  svc = SVC(kernel='linear',
           C=1.0, # C값이 커질수록 overfitting의 가능성 상승
           random_state=1)
  svc.fit(X_train_scaled, y_train)

  gs = GridSearchCV(svc,
                    param_grid={"C":[(10**i) for i in range(-5,6)]}, 
                    scoring='accuracy',
                    cv=3,
                    n_jobs=-1)
  gs.fit(X_train_scaled, y_train)
  gs_pred_train = gs.predict(X_train_scaled)

  accuracy_score(y_train, gs_pred_train)
  ```
  
### 02. 비선형(Kernel Support Vector Machine)
- 차원을 늘려야 비선형 데이터 분류 가능 -> 늘리면 낮은 차수 다항식의 패턴을 표현하기 힘들어 과소적합, 너무 높은 차수는 과적합 + 느린 모델
- 따라서 방사기저함수(Radial Base Function) 사용
  - 기준점을 여러 개 지정 후 각 샘플이 기준점에서 떨어져 있는 거리로 데이터 차원 늘리는 효과
  - ![다운로드 (2)](https://user-images.githubusercontent.com/71580318/112832640-91e17000-90d0-11eb-89f7-4c28563cbb87.png)
  - 변환 전
  - ![다운로드 (1)](https://user-images.githubusercontent.com/71580318/112832601-82fabd80-90d0-11eb-84e2-3605cbb45fe8.png)
  - 변환 후(gamma=0.3, 기준점:-2,1)
- 하이퍼파라미터
    - C: 오차 허용기준, 클수록 과적합 가능성 상승
    - gamma: 방사기저함수의 `gamma`로 규제의 역할, 클수록 과적합 가능성 상승
```python
rbf_svc = SVC(kernel='rbf', # default: rbf
              C=1, # soft margin ~ hard margin
              gamma=0.01, # rbf의 gamma. 실수, 문자열(scale: 1/(컬럼수*컬럼의분산), auto: 1/컬럼수)
              probability=True, # True로 지정해야 predict_proba() 호출 가능(기본: False)
              random_state=1)
rbf_svc.fit(X_train_scaled, y_train)
pred_train = rbf_svc.predict(X_train_scaled)
pred_test = rbf_svc.predict(X_test_scaled)
accuracy_score(y_train, pred_train), accuracy_score(y_test, pred_test)

# GridSearch로 하이퍼파라미터 비교
param = {
    'kernel':['rbf', 'linear'],
    'C':[0.001, 0.01, 0.1, 1, 10, 100],
    'gamma':[0.001, 0.01, 0.1, 1, 10]
}
svc = SVC(random_state=1, probability=True)
gs_svc = GridSearchCV(svc,
                      param_grid=param,
                      scoring=['accuracy','roc_auc','average_precision'],
                      refit='accuracy',
                      cv=3,
                      n_jobs=2)
gs_svc.fit(X_train_scaled, y_train)
pd.DataFrame(gs_svc.cv_results_).sort_values('rank_test_average_precision').head()
```
