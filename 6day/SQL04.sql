-- SQL04.sql

-- 직원들의 수는?
select count(empno)
from emp;

select job,count(empno)
from emp
group by job;

-- 업무(job) 의 개수는?
SELECT count(DISTINCT job)
from emp;

-- 커미션을 받는 직원들의 수는?
SELECT count(comm)
from emp
where (comm > 0);

-- 직원들의 평균급여, 최소급여, 최대급여, 급여합산은?
SELECT round(avg(sal)),min(sal),max(sal),sum(sal)
from emp;

SELECT job,count(empno),round(avg(sal)),min(sal),max(sal),sum(sal)
from emp
group by job;

-- 부서번호별 인원수와 최대급여는?
SELECT deptno, count(empno), max(sal)
from emp 
group by deptno;




