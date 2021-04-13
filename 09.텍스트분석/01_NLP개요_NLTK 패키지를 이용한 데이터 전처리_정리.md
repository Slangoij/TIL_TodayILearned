# NLP(Natural Language Processing)
- 자연어: 사람이 사용하는 고유한 언어 <-> 인공언어: 특정 목적을 위해 인위적으로 만든 언어
- 자연어 처리
  - 번역시스템, 문서요약, etc.
- Process
  1. 텍스트 전처리
    - 클렌징: 특수문자, 기호 등 필요없는 문자 제거, 대소문자 통일
    - stop word(분석에 필요없는 토큰)제거
    - 텍스트 토큰화: 분석의 최소단위로 분할
    - 어근 추출(Stemming/Lemmatization)을 통한 텍스트 정규화
  2. Feature vectorization: 문자열비정형 데이터인 텍스트를 숫자타입으로 변환
  3. 머신러닝 모델 수립, 학습, 예측, 평가
```python
# 예제로 쓰기 좋은 파이썬 자체 
import this
```
- - -
# NLTK(Natural Language ToolKit)
- nltk 패키지 설치(기초 패키지만 설치됨)
```python
pip install nltk
# 주피터에서는 `!`를 앞에 붙여 실행
```
- NLTK 추가 패키지(nltk 설치 이후 필요 패키지 추가 설치)
```python
import nltk
nltk.download() # 설치 GUI 프로그램 실행
nltk.download('패키지명')
```

- - -
# 형태소 분석
- 형태소: 일정한 의미가 있는 가장 작은 말의 단위
  - 어간추출(Stemming)
  - 원형(기본형) 복원(Lemmatization)
  - 품사부착(POS(PartOfSpeech) tagging)

### 01. 어간 추출(Stemming)
- **어간**: 활용어에서 변하지 않는 부분 ex) 'painted','paint','painting' => 'paint'
- 어간 추출을 통해 같은 의미를 갖는 단어의 여러가지 활용이 있을 경우 하나로 통일하여 카운트 가능
- 종류: `Porter Stemmer`, `Lancaster Stemmer', 'Snowball Stemmer'
- 메소드: `stemmer객체.stem(단어)
- 완벽하진 않다. new와 news를 같은 new로 처리
```python
from nltk import PorterStemmer, LancasterStemmer, SnowballStemmer
# stemming은 단어들을 모두 소문자로 변환후 처리.
# 대상 단어
words = [
    'Working', 'Works', 'Worked',
    'Painting','Paints','Painted',
    'happy','happier','happiest'
]

# 1. stemmer객체를 생성
# 2. stem(단어)을 호출해 단어별 어간추출 작업 진행
ps = PorterStemmer()
print([ps.stem(word) for word in words])

ls = LancasterStemmer()
print([ls.stem(word) for word in words])

sbs = SnowballStemmer('english')
print([sbs.stem(word) for word in words])
```

### 02. 원형 복원(Lemmatization)
- 단어의 기본형 반환 ex) am, is, are => be
- 단어의 품사 지정시 정확한 복원 가능
- `WordNetLemmatizer객체.lemmatize(단어, [, pos=품사])`
```python
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer

words = ['is', 'are', 'am', 'has', 'had', 'have']
lemm = WordNetLemmatizer()
lemm.lemmatize('are', pos='v')
```

### 03. 품사부착(POS Tagging(Part-Of-Speech))
- 형태소에 품사를 붙이는 작업
- NLTK는 Penn Treebank Tagset 이용
  - 명사 : N으로 시작 (NN-일반명사, NNP-고유명사)
  - 형용사 : J로 시작(JJ, JJR-비교급, JJS-최상급)
  - 동사: V로 시작 (VB-동사, VBP-현재형 동사)
  - 부사: R로 시작 (RB-부사)
- `pos_tag(단어_리스트)`    
  - 단어와 품사를 튜플로 묶은 리스트를 반환
```python
nltk.download('tagsets')
nltk.download('averaged_perceptron_tagger')
# 도움말
nltk.help.upenn_tagset()

from nltk.tag import pos_tag
words = ['Book', 'book', 'car', 'go', 'Korea', 'have','good']
pos_tag(words)
```

### 텍스트 전처리 프로세스 실습
```python
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag

def get_wordnet_postag(pos_tag):
  """
  펜 트리뱅크 태그셋의 품사를 (pos_tag() 반환 형식)을 WordNetLemmatizer(원형복원처리객체)가
  사용하는 품사 형식으로 변환
  - n: 명사, a: 형용사, v: 동사, r: 부사
  """
  if pos_tag.startswith('J'):
    return 'a'
  elif pos_tag.startswith('N'):
    return 'n'
  elif pos_tag.startswith('V'):
    return 'v'
  elif pos_tag.startswith('R'):
    return 'r'
  else:
    return None
        
def tokenize_text2(doc):
  """
  tokenize_text() 함수 + 원형복원을 추가.
  """
  # 소문자 변환
  text = doc.lower()
  # 문장단위 토큰화
  sent_tokens = nltk.sent_tokenize(text)

  # Stopwords 리스트 load
  sw = stopwords.words('english')
  sw.extend(['although','unless']) # stopword 추가

  # WordNetLemmatization객체 생성
  lemm = WordNetLemmatizer()

  result_list = []
  # 단어단위 토큰화
  for sent in sent_tokens:
    tmp_words = nltk.regexp_tokenize(sent, '[a-zA-Z가-힣]+')
    # 불용어(stopword) 제거
    words_list = [word for word in tmp_words if word not in sw]
    # 원형복원
    # 1. pos_tag
    pos_taged = pos_tag(words_list)
    # 2. WordNet이 사용하는 품사태그로 변환
    org_list = [lemm.lemmatize(word, pos=get_wordnet_postag(tag))
                for word, tag in pos_taged if get_wordnet_postag(tag)!=None]

    result_list.append(org_list)

  return result_list
    
tokenize_text2(txt)
```

### 04. 분석을 위한 클래스
1. Text클래스
- 문서 분석에 유용한 메소드 제공
- 생성
  - Text(토큰리스트, [name=이름])
- 주요 메소드
  - count(단어): 매개변수로 전달한 단어의 빈도수
  - plot(N): 빈도수 상위 N개 단어를 선그래프로 시각화
  - dispersion_plot(단어리스트): 매개변수로 전달한 단어들의 문서 내 위치를 시각화
```python
from nltk import Text
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.style.use('seaborn')

word_list = nltk.word_tokenize(txt)
news_words = [word for word_list in news_tokens for word in word_list]
len(news_words)

# Text객체 생성
news_text = Text(news_words, name='손흥민뉴스')
news_text

# text.count(단어): 단어의 빈도수 조회
news_text.count('parent'), news_text.count('son')

# 빈도수 상위 단어들에 대한 선그래프
plt.figure(figsize=(10,7))
news_text.plot(20)
plt.show()

# 문서 내의 해당 단어 위치 개략적 시각화
plt.figure(figsize=(10,7))
news_text.dispersion_plot(['son', 'koean', 'say'])
plt.show()
```

2. FreqDist
- document에서 사용된 토큰의 사용빈도 데이터를 갖는 클래스 => key: 토큰, value: 개수 를 갖는 딕셔너리
- 생성
  - Text객체의 vocab()로 조회
  - 생성자에 토큰리스트를 넣어 직접 생성 가능
- 주요 메소드
  - `B()`: 출연한 고유 단어의 개수
  - `N()`: 총 단어수
  - `get(단어)` or FreqDist['단어']: 특정 단어 출연 빈도수
  - `freq(단어)`: 총 단어수 대비 특정단어 출연비율
  - `most_common()`: 빈도수 순서로 정렬된 리스트 반환
```python
# FreaqDist객체 생성
freq = news_text.vocab()
# 다른 방법
from nltk import FreqDist
freq2 = FreqDist(['a','b','c'])

print("총단어수: {}, 고유단어개수: {}".format(freq.N(), freq.B()))
print("단어 london의 빈도수: {}, {}, {}".format(freq.get('london'), freq['london'], news_text.count('london')))
print("단어 london의 출연비율:{}, {}".format(6/1197, freq.freq('london')))
print(freq.most_common())
```

3. wordcloud
- 단어의 빈도수 시각화, 빈도수가 높으면 크게, 적으면 작게 단어 표현.
```python
# [(f.name, f.fname) for f in fm.fontManager.ttflist if 'malgun' in f.name.lower()]
# 에서 맑은 고딕(한글지원) 폰트 경로 조회
font_path = 'C:\\WINDOWS\\Fonts\\malgun.ttf'

from wordcloud import WordCloud
# 설정
wc = WordCloud(font_path=font_path,
              max_words=200, # 출연단어의 최대 개수
              prefer_horizontal=0.7, # 가로쓰기의 비율
              relative_scaling=0.7, # 0 ~ 1 사이의 실수. 1에 가까울수록 빈도수가 많은 단어와 적은 단어 크기 차이를 크게 한다.)
               min_font_size=1,
               max_font_size=50, # 가장 작은 폰트크기, 가장 큰 폰트크기 지정
               background_color='white'
              )
# WordCloud객체에 데이터 넣기
word_cloud = wc.generate_from_frequencies(freq) # 딕셔너리: {단어: 빈도수, 단어:빈도수, ...}

# matplotlib으로 출력
plt.figure(figsize=(15,15))
plt.imshow(word_cloud)
plt.axis('off')
plt.show()
```

4. ConVectorizer로 TDM 만들기(뒤에서 이어서)
