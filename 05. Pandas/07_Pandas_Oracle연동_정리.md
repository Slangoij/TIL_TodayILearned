# 07. Pandas, Oracle간 연동

### 1. DataBase 연동모듈: `cx_Oracle` 모듈
  - 이전에 진행한 파이썬-오라클 연동과 같은 방식
  - Connection : DB 연결정보를 가진 객체
      - connection() 함수를 이용해 연결
  - Cursor
      - SQL 문 실행을 위한 메소드 제공
      - Connection.cursor() 함수를 이용해 조회
  ```python
  # 연결
  # username, password, host
  conn = cx_Oracle.connect('c##scott', 'tiger', 'localhost:1521/XE') # 'c##scott/tiger@localhost:1521/XE'
  print('연결완료')
  
  # Cursor생성
  cursor = conn.cursor()
  
  # sql 실행
  cursor.execute('select * from emp')
  result = cursor.fetchall()
  
  # 연결 끊기
  cursor.close()
  conn.close()
  ```
- - -

### 2. 판다스 오라클 
  - `pd.read_sql("select문", con=connection)` 구문 한방에 끝!
  ```python
  conn = cx_Oracle.connect('c##scott_join/tiger@localhost:1521/XE')
  emp_df = pd.read_sql("select * from emp", con=conn, index_col='EMP_ID')
  ```
