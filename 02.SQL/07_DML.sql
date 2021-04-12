/* *********************************************************************
DML - 데이터(값)을 다루는 SQL문
    - insert: 삽입 (Create)
    - select: 조회 (Read,Retrieve): DQL(query)
    - update: 수정 (Update)
    - delete: 삭제 (Delete)
********************************************************************* */


/* *********************************************************************
INSERT 문 - 행 추가
구문
 - 한행추가 :
   - INSERT INTO 테이블명 (컬럼 [, 컬럼]) VALUES (값 [, 값[])
   - 모든 컬럼에 값을 넣을 경우 컬럼 지정구문은 생략 할 수 있다.

 - 조회결과를 INSERT 하기 (subquery 이용)
   - INSERT INTO 테이블명 (컬럼 [, 컬럼])  SELECT 구문
	- INSERT할 컬럼과 조회한(subquery) 컬럼의 개수와 타입이 맞아야 한다.
	- 모든 컬럼에 다 넣을 경우 컬럼 설정은 생략할 수 있다.
	
  
************************************************************************ */
desc    demp; -- 테이블 구성 확인
insert into dept (dept_id, dept_name, loc) values (1000, '기획부', '서울');
insert into dept values (1100, '구매부', '부산');
commit;

-- commit 후 실수한 부분
insert into dept (dept_id, dept_name, loc) values (1100, '기획부', '서울');
insert into dept (dept_id, dept_name, loc) values (1200, '기획부', '서울');
insert into dept (dept_id, dept_name, loc) values (1300, '기획부', '서울');
commit; --commit을 하기 전까지는 임시로 처리된 상태 -> commit으로 최종 처리
rollback; --insert/update/delete하기 전 상태로 돌려라

select * from dept order by dept_id desc;

desc emp;

insert into emp values(1000, '홍길동', 'FI_ACCOUNT', 100, '2017/10/20', 5000, 0.1, 20);
insert into emp (emp_id, emp_name, hire_date, salary) values(1100, '이순신', '2000/01/05', 6000);
insert into emp values(1200, '박영희', 'FI_ACCOUNT', null, '2020/01/02', 7000, null, 10);
insert into emp values(1300, '박영희', 'FI_ACCOUNT', null, to_date('2020/01', 'yyyy/mm'), 7000, null, 10);

insert into emp values(1000,'김영수','FI_ACCOUNT',100,'2021/01/06',1000,0.1,20); --이미 있는 PK값을 insert하면 오류 발생
insert into emp values(1500,null,'FI_ACCOUNT',100,'2021/01/06',1000,0.1,20); --not null 컬럼에 null 삽입 불가
insert into emp values(1000,'김영수','회게',100,'2021/01/06',1000,0.1,20); --emp의 job_id는 FK컬럼 -> 부모컬럼에 있는 PK컬럼에 존재하는 값만 가능

--컬럼의 데이터 타입의 크기보다 더 큰 값을 넣는 경우 오류
insert into emp values(1000,'김영수김영수김영수','FI_ACCOUNT',100,'2021/01/06',1000,0.1,20);
insert into emp values(1000000,'김영수','FI_ACCOUNT',100,'2021/01/06',1000,0.1,20);

commit;

select * from emp order by emp_id desc;

create table emp_copy(
    emp_id number(6),
    emp_name varchar2(20),
    salary number(7,2)
);

/*
select  emp_id,
        emp_name,
        salary
from    emp
where   dept_id = 100;

--기존의 테이블을 조회한 결과를 다른 테이블에 삽입하는 구문
insert into emp_copy (emp_id, emp_name, salary)
select  emp_id,
        emp_name,
        salary
from    emp
where   dept_id = 10;

select * from emp_copy;
*/

--TODO: 부서별 직원의 급여에 대한 통계 테이블 생성. 
--      조회결과를 insert. 집계: 합계, 평균, 최대, 최소, 분산, 표준편차
create table salary_stat(
    dept_id number(6),
    salary_sum number(15,2),
    salary_avg number(10, 2),
    salary_max number(7,2),
    salary_min number(7,2),
    salary_var number(20,2),
    salary_stddev number(7,2)
);

/* 전체 컬럼 삽입하기에 컬럼명 생략 가능
insert into salary_stat (
    dept_id,
    salary_sum,
    salary_avg,
    salary_max,
    salary_min,
    salary_var,
    salary_stddev
)
*/
insert into salary_stat
select  dept_id,
        sum(salary),
        round(avg(salary), 2),
        max(salary),
        min(salary),
        round(variance(salary), 2),
        round(stddev(salary), 2)
from    emp
group by dept_id
order by dept_id;

ROLLBACK;
select * from salary_stat;

/* *********************************************************************
UPDATE : 테이블의 컬럼의 값을 수정

구문
UPDATE 테이블명
SET    변경할 컬럼 = 변경할 값  [, 변경할 컬럼 = 변경할 값]
[WHERE 제약조건]

 - UPDATE: 변경할 테이블 지정
 - SET: 변경할 컬럼과 값을 지정
 - WHERE: 변경할 행을 선택.
************************************************************************ */


-- 직원 ID가 200인 직원의 급여를 5000으로 변경 (변경 전: 4400)
select * from emp where emp_id = 200;

update emp
set salary = 5000
where emp_id = 200;
rollback;
select * from emp;

-- 직원 ID가 200인 직원의 급여를 10% 인상한 값으로 변경.
select * from emp where emp_id = 200;

update  emp
set     salary = salary * 1.1
where   emp_id = 200;

-- 부서 ID가 100인 직원의 커미션 비율을 0.2로 salary는 3000을 더한 값으로, 상사_id는 100 변경.
select * from emp where emp_id = 100;
update  emp
set     comm_pct = 0.2,
        salary = salary + 3000,
        mgr_id = 100
where   emp_id = 100;
commit;

-- TODO: 부서 ID가 100인 직원들의 급여를 100% 인상
select * from emp where dept_id = 100;
update  emp
set     salary = salary*2
where   dept_id = 100;
rollback;

-- TODO: IT 부서의 직원들의 급여를 3배 인상
select  *
from    emp e left join dept d on e.dept_id = d.dept_id
where   dept_name = 'IT';

update  emp
set     salary = salary*2
where   dept_id = (select dept_id from dept where dept_name = 'IT');
rollback;

-- TODO: EMP 테이블의 모든 데이터를 MGR_ID는 NULL로 HIRE_DATE는 현재일시로 COMM_PCT는 0.5로 수정.
update  emp
set     mgr_id = null,
        hire_date = sysdate,
        comm_pct = 0.5;
        
select * from emp;

-- TODO: COMM_PCT 가 0.3이상인 직원들의 COMM_PCT를 NULL 로 수정.
update  emp
set     comm_pct = null
where   comm_pct >= 0.3;

select * from emp;

-- TODO: 전체 평균급여보다 적게 받는 직원들의 급여를 50% 인상.
select  * from emp
where salary < (select  avg(salary) from emp);

update  emp
set     salary = salary * 1.5
where   salary < (select  avg(salary) from emp);

/* *********************************************************************
DELETE : 테이블의 행을 삭제

구문 
DELETE FROM 테이블명 [WHERE 제약조건]
 
   - WHERE: 삭제할 행을 선택
************************************************************************ */
delete from emp;
select * from emp;
rollback;

-- 부서테이블에서 부서_ID가 200인 부서 삭제
select * from dept;
delete from dept where dept_id = 200;

-- 부서테이블에서 부서_ID가 10인 부서 삭제
select * from emp where dept_id = 10;
select * from emp where dept_id in (200, 1200, 1300);
delete from dept where dept_id = 10;
rollback;

--delete from emp, dept; --한 테이블 단위로만 처리 가능

-- TODO: 부서 ID가 없는 직원들을 삭제
select * from emp where dept_id is null;

delete from emp where dept_id is null;

-- TODO: 담당 업무(emp.job_id)가 'SA_MAN'이고 급여(emp.salary) 가 12000 미만인 직원들을 삭제.
select * from emp where job_id = 'SA_MAN' and salary < 12000;

delete from emp where job_id = 'SA_MAN' and salary < 12000;

-- TODO: comm_pct 가 null이고 job_id 가 IT_PROG인 직원들을 삭제
select * from emp where comm_pct is null and job_id = 'IT_PROG';

delete from emp where comm_pct is null and job_id = 'IT_PROG';

-- TODO: job_id에 CLERK가 들어간 업무를 하는 직원들 삭제
select * from emp where job_id like '%CLERK%';

delete from emp where job_id like '%CLERK%';