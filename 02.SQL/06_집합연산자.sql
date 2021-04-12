/* **********************************************************************************************
집합 연산자 (결합 쿼리)
- 둘 이상의 select 결과를 가지고 하는 연산.
- 구문
 select문  집합연산자 select문 [집합연산자 select문 ...] [order by 정렬컬럼 정렬방식]

-연산자
  - UNION: 두 select 결과를 하나로 결합한다. 단 중복되는 행은 제거한다. (합집합)
  - UNION ALL : 두 select 결과를 하나로 결합한다. 중복되는 행을 포함한다. (합집합)
  - INTERSECT: 두 select 결과의 동일한 결과행만 결합한다. (교집합)
  - MINUS: 왼쪽 조회결과에서 오른쪽 조회결과에 없는 행만 결합한다. (차집합)
   
 - 규칙
  - 연산대상 select 문의 컬럼 수가 같아야 한다. 
  - 연산대상 select 문의 컬럼의 타입이 같아야 한다.
  - 연산 결과의 컬럼이름은 첫번째 select문의 것을 따른다.
  - order by 절은 구문의 마지막에 넣을 수 있다.
  - UNION ALL을 제외한 나머지 연산은 중복되는 행은 제거한다.
*************************************************************************************************/
select * from emp where dept_id in (10,20,30,40)
union all
select * from emp where salary > 15000
order by 1; --order by절은 최종결과에 대해서 정렬

--중복 허용
select * from emp where dept_id in (10,20)
union all
select * from emp where dept_id in (20,30);  

--중복 미허용 -> 만약 두 개 조회결과가 자체적으로 중복이 없을 시 union all을 쓰는게 낫다.
-- -> 효율성 제고 위해
select * from emp where dept_id in (10,20)
union
select * from emp where dept_id in (20,30);

--교집합
select * from emp where dept_id in (10,20)
intersect
select * from emp where dept_id in (20,40);

--차집합(앞의 조회결과가 기본)
select * from emp where dept_id in (10,20)
minus
select * from emp where dept_id in (20,40);



-- emp 테이블의 salary 최대값과 salary 최소값, salary 평균값 조회
select max(salary), min(salary), avg(salary) from emp;

select 'MAX' "Label", to_char(max(salary),'999,999.00') "급여집계" from emp
union all
select 'MIN', to_char(min(salary),'999,999.00') from emp
union all
select 'AVG', to_char(round(avg(salary), 2),'999,999.00') from emp
order by 2;

-- emp 테이블에서 업무별(emp.job_id) 급여 합계와 전체 직원의 급여합계를 조회.
select  decode(grouping(job_id), 0, job_id, '총계') job_id,
        sum(salary)
from    emp
group by rollup(job_id);

select  job_id,
        sum(salary)
from    emp
group by job_id
union all
select '총계', sum(salary)
from    emp;

--한국 연도별 수출 품목 랭킹
drop table export_rank;
create table export_rank(
    year char(4) not null,
    ranking number(2) not null,
    item varchar2(60) not null
);
insert into export_rank values(1990, 1, '의류');
insert into export_rank values(1990, 2, '반도체');
insert into export_rank values(1990, 3, '가구');
insert into export_rank values(1990, 4, '영상기기');
insert into export_rank values(1990, 5, '선박해양구조물및부품');
insert into export_rank values(1990, 6, '컴퓨터');
insert into export_rank values(1990, 7, '음향기기');
insert into export_rank values(1990, 8, '철강판');
insert into export_rank values(1990, 9, '인조장섬유직물');
insert into export_rank values(1990, 10, '자동차');

insert into export_rank values(2000, 1, '반도체');
insert into export_rank values(2000, 2, '컴퓨터');
insert into export_rank values(2000, 3, '자동차');
insert into export_rank values(2000, 4, '석유제품');
insert into export_rank values(2000, 5, '선박해양구조물및부품');
insert into export_rank values(2000, 6, '무선통신기기');
insert into export_rank values(2000, 7, '합성수지');
insert into export_rank values(2000, 8, '철강판');
insert into export_rank values(2000, 9, '의류');
insert into export_rank values(2000, 10, '영상기기');

insert into export_rank values(2018, 1, '반도체');
insert into export_rank values(2018, 2, '석유제품');
insert into export_rank values(2018, 3, '자동차');
insert into export_rank values(2018, 4, '평판디스플레이및센서');
insert into export_rank values(2018, 5, '합성수지');
insert into export_rank values(2018, 6, '자동차부품');
insert into export_rank values(2018, 7, '철강판');
insert into export_rank values(2018, 8, '선박해양구조물및부품');
insert into export_rank values(2018, 9, '무선통신기기');
insert into export_rank values(2018, 10, '컴퓨터');

--년도별 수입 품목 랭킹
drop table import_rank;
create table import_rank(
    year char(4) not null,
    ranking number(2) not null,
    item varchar2(60) not null
);
insert into import_rank values(1990, 1, '원유');
insert into import_rank values(1990, 2, '반도체');
insert into import_rank values(1990, 3, '석유제품');
insert into import_rank values(1990, 4, '섬유및화학기계');
insert into import_rank values(1990, 5, '가죽');
insert into import_rank values(1990, 6, '컴퓨터');
insert into import_rank values(1990, 7, '철강판');
insert into import_rank values(1990, 8, '항공기및부품');
insert into import_rank values(1990, 9, '목재류');
insert into import_rank values(1990, 10, '계측제어분석기');

insert into import_rank values(2000, 1, '원유');
insert into import_rank values(2000, 2, '반도체');
insert into import_rank values(2000, 3, '컴퓨터');
insert into import_rank values(2000, 4, '석유제품');
insert into import_rank values(2000, 5, '천연가스');
insert into import_rank values(2000, 6, '반도체제조용장비');
insert into import_rank values(2000, 7, '금은및백금');
insert into import_rank values(2000, 8, '유선통신기기');
insert into import_rank values(2000, 9, '철강판');
insert into import_rank values(2000, 10, '정밀화학원료');

insert into import_rank values(2018, 1, '원유');
insert into import_rank values(2018, 2, '반도체');
insert into import_rank values(2018, 3, '천연가스');
insert into import_rank values(2018, 4, '석유제품');
insert into import_rank values(2018, 5, '반도체제조용장비');
insert into import_rank values(2018, 6, '석탄');
insert into import_rank values(2018, 7, '컴퓨터');
insert into import_rank values(2018, 8, '정밀화학원료');
insert into import_rank values(2018, 9, '자동차');
insert into import_rank values(2018, 10, '무선통신기기');

commit;


--TODO:  2018년(year) 수출(export_rank)과 수입(import_rank)을 동시에 많이한 품목(item)을 조회
-- 양쪽에 있는 것. intersect
select item from export_rank where year = 2018;
intersect
select item from import_rank where year = 2018;

--TODO:  2018년(export_rank.year) 주요 수출 품목(export_rank.item)중 2000년에는 없는 품목 조회
-- 2018-2000
select item from export_rank where year = 2018
minus
select item from export_rank where year = 2000;

--TODO: 1990 수출(export_rank)과 수입(import_rank) 랭킹에 포함된  품목(item)들을 합쳐서 조회.
--      중복된 품목도 나오도록 조회
--union all
select item from export_rank where year = 1990
union all
select item from import_rank where year = 1990;

--TODO: 1990 수출(export_rank)과 수입(import_rank) 랭킹에 포함된 품목(item)들을 합쳐서 조회.
--      중복된 품목은 안나오도록 조회
--union
select item from export_rank where year = 1990
union
select item from import_rank where year = 1990;

--TODO: 1990년과 2018년의 공통 주요 수출 품목(export_rank.item) 조회
-- intersect
select item from export_rank where year = 1990
intersect
select item from export_rank where year = 2018;

--TODO: 1990년 주요 수출 품목(export_rank.item)중 2018년과 2000년에는 없는 품목 조회
--1990 - 2018 - 2000
select item from export_rank where year = 1990
minus
select item from export_rank where year = 2018
minus
select item from export_rank where year = 2000;

--TODO: 2000년 수입품목중(import_rank.item) 2018년에는 없는 품목을 조회.
-- 2000 - 2018
select item from import_rank where year = 2000
minus
select item from import_rank where year = 2018;

