# 1. **컬럼 type 변경**
> - 이 친구들 범주형에서 연속형으로
> - ~~education_level~~
> - ~~last_new_job~~
> - ~~experience~~
> - ~~enrolled_university~~
> - `category_feature = ['city','gender','relevent_experience','major_discipline','company_size','company_type']`
> - `numeric_feature = ['city_development_index','training_hours','education_level','last_new_job','experience','enrolled_university']`
------------
### 1-1. education_level type change to integer
> - 4 : Phd
> - 3 : masters
> - 2 : graduate
> - 1 : high school
> - 0 : primary school
------------
### 1-2. last_new_job type change to integer
> - `'>4' = 5`, `'never' = 0`
------------
### 1-3. experience type change to integer
> - `'>20' = 21`, `'<1' = 0`
------------
### 1-4. enrolled_university type change to integer
> - 2 : Full time course
> - 1 : Part time course
> - 0 : no_enrollment
------------
# 2. **컬럼별 결측치 처리**
> - ~~**null**값이 500 이하인 행 KNN 처리~~
> - ~~**gender** : 결측치를 반반 남, 녀 나눠주기~~
> - ~~**major_discipline** : 결측치를 최빈값에 합친다.~~
> - ~~**company_size . type** : unkown이라는 새로운 컬럼에 정의~~
------------
### 2-1. 전체 데이터의 결측치가 3%이하인 결측치 처리
> - knn으로 변환
------------
### 2-2. gender 결측치 처리
> - 결측치를 반으로 나누어 반은 Male, 반은 Female로 분배
------------
### 2-3. major_discipline 결측치 처리
> - 결측치는 최빈값에 넣어준다.(최빈값 = 'STEM' == 데이터과학자과?)
> - 데이터관련학과의 value는 STEM 한개이고(major) 나머지는 비전공으므로 non_major로 명시
------------
### 2-4. company_size, type 결측치 처리
> - 결측치의 양이 많으므로 unknown으로 정의
