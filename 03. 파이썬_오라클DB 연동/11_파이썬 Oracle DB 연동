파이썬-오라클 DB 연동
==================

네트워크의 구성
-------------

- `네트워크`의 구성은 간단히 보자면 `서버`와 `클라이언트로 구성이 되어있다.
- `Oracle`도 하나의 서비스 이므로 서버와 클라이언트로 구성이 되어잇는데, 수업상에서는 `오라클서비스XE` 서버 프로그램과\
`오라클오라DB홈리스너` 클라이언트 프로그램을 모두 내 컴퓨터에서 사용하므로 따로 구성할 필요가 없다.
- 이때, 서버와 클라이언트틑 연결할 시
  - 1. ip 주소
  - 2. port번호
  - 3. 유저 아이디
  - 4. 유저 비밀번호
  - 5. (오라클에 한하여) SID : 목표 DB 지정
가 필요하다. 이때 배를 항구에 정박하는 것을 네트워크로 비유하자면, 아이피 주소는 목표 국가, 포트번호는 항구로 비유할 수 있다.

DB와 파이썬과의 연동
-----------------
- 현재 수업 상에서 활용하는 프로그래밍 언어인 `Pyhon`과 `Oracle`을 연동하기 위해서는 연동 모듈인 `cx_Oracle` 모듈이 필요하다.

다음은 파이썬으로 해당 모듈을 호출하고 이전에 작업했던 'emp' 테이블과 연동시키는 방법이다.

**1. CREATE/INSERT**
```sql
create_sql = 'create table test(id varchar2(10), name varchar2(100), age number(3))'
insert_sql = 'INSERT INTO test VALUES (:1, :2, :3)'

with cx_Oracle.connect('c##scott_join/tiger@localhost:1521/XE') as conn:
    with conn.cursor() as cursor:
        try:
            cursor.execute(create_sql) # 테이블 생성
        except Exception as e:
            print(e)
        # insert
        cursor.execute(insert_sql, [1, '이름1', 20])
        cursor.execute(insert_sql, [2, '이름2', 30])
        cursor.execute(insert_sql, [3, '이름3', 40])
        conn.commit() # commit
```

**2. DELETE**
```sql
delete_sql = "DELETE FROM test WHERE name=:1"
with cx_Oracle.connect('c##scott_join/tiger@localhost:1521/XE') as conn:
    with conn.cursor() as cursor:
        cursor.execute(delete_sql, ['이름1'])
        conn.commit()
```

**3. UPDATE**
```sql
update_sql = "UPDATE test SET name=:1"
with cx_Oracle.connect('c##scott_join/tiger@localhost:1521/XE') as conn:
    with conn.cursor() as cursor:
        cursor.execute(update_sql, ['새이름'])
        conn.commit()
```

**4. SELECT**
```sql
select_sql = "select * from test"
with cx_Oracle.connect('c##scott_join/tiger@localhost:1521/XE') as conn:
    with conn.cursor() as cursor:
        cursor.execute(select_sql)
        pprint(cursor.fetchall())
```
