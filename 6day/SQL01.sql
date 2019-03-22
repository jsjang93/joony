-- SQL01.sql
select * 
from emp;

-- 직원들의 이름, 사번, 업무(JOB) 은?
select ename, empno, job
from emp;

-- 부서들의 부서명, 부서위치는?
SELECT dname, loc
from dept;

-- 직원들의 이름, 사번, 급여는?
SELECT 	ename as 이름, 
		empno 사번, 
		sal as 급여, 
		job as 업무
from emp;

SELECT ename || " 의 사번은 " || empno from emp ;

-- 직원들의 업무(Job)은?
SELECT DISTINCT job
from emp;

-- 직원들의 업무(오름차순), 이름(내림차순), 사번은?
SELECT job, ename, empno
from emp
order by job asc, ename desc; -- order by 기본값 asc

-- 직원들의 이름, 사번, 상관의 사번을
-- 상관의 사번 순으로 정렬하세요
select ename, empno, mgr
from emp 
order by mgr;







