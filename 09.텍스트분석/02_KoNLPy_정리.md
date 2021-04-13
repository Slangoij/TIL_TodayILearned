# 01. KoNLPy
- 한국어 처리를 위한 파이썬 패키지
- Java, JPype1, koNLPy 모두 설치해야 한다.
- Java설치: https://www.oracle.com/java/technologies/javase-downloads.html
  - 환경변수 설정: `JAVA_HOME` - 설치경로 지정, `Path` - `설치경로\bin` 경로 지정
- JPype1설치: `!pip install JPype1==0.7.0` 버전 설치
- KoNLPy설치: `!pip install konlpy`
- KoNLPy 제공 말뭉치(글로 구성된 문서의 묶음)
  - kolaw: 대한민국 헌법 말뭉치, kobill: 대한민국 국회 의안
```python
from konlpy.corpus import kolaw, kobill
# corpus파일이름 조회
print(kolaw.fileids())
print(kobill.fileids())

constitution = kolaw.open('constitution.txt')
bill = kobill = kobill.open('1809890.txt').read()
```

# 02. 형태소 분석기/사전
- 형내소 사전 내장, 형태소 분석 함수 제공 모듈
- KoNLPy 제공 형태소 분석기: Hannanum, Kkma, Komoran(Shineware에서 개발, 성능 양호), Mecab, Open Korea Text(트위터코리아에서 개발)
- 공통 메소드
  - `morphs(string)`: 형태소 단위로 토큰화
  - `nouns(string)`: 명사만 추출하여 토큰화
  - `pos(string)`: 품사 부착 (분석기마다 품사태그 상이)
  - `tagset`: 분석기가 사용하는 품사태그 설명
```python
from konlpy.tag import Okt, Komoran # Okt: Open Korea Text

# Okt
okt = Okt()
# 형태소 추출
tokens = okt.morphs(txt)
# 명사만 추출
noun_tokens = okt.nouns(txt)
# 품사부착(pot-tagging)
pos_tokens = okt.pos(txt)
okt.tagset
sample = '이것도 되나욬ㅋㅋㅋ'
okt.morphs(sample, norm=True) # 트위터 기반이라 비언어도 언어로

# Komoran
kom = Komoran()
# 형태소 토큰화
tokens = kom.morphs(txt)
kom.tagset
```
