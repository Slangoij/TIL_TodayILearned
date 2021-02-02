-- 한줄 주석
/*
block 주석
테이블: 회원(member)
속성
id: varchar2(10), primary key
password: varchar2(10) not null
name: nvarchar2(50) not null(not null로 하지 않으면 nullable)
point: number(7) -9999999 ~ +9999999 nullable
join_date: date not null
*/
-- 실행: control + enter
create table member(
    id varchar2(10) primary key,
    password varchar2(10) not null,
    name nvarchar2(50) not null,
    point number(7),
    join_date date not null
);
select * from tab;
-- 테이블 제거
drop table member;

-- 한 행의 값을 추가 - insert
-- 문자열: ' '으로 감싼다.
-- date: '년/월/일' - 월/일이 한자리일 경우 앞에 0을 붙인다. 05 03 이런식으로
insert into member (id,password,name,point,join_date) values ('id-1','abcde','홍길동',10000,'2020/10/05');
-- 모든 컬럼에 값을 전부 넣을 경우 컬럼명은 생략 가능
insert into member values ('id-2','11111','박영희',10000,'2010/05/07');
-- primary key(pk) 컬럼: not null + unique
insert into member values ('id-33333333','11111','장영수',10000,'2013/07/07'); --pk는 기존에 있는 값을 중복하여 넣을 수 없다.
insert into member values ('id-4','11111','박영희',null,'2013/07/07');

select * from member;