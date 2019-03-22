-- SQL02.sql

-- 스미스의 이름, 사번은?
SELECT ename, empno
from emp 
where (ename = 'SMITH');

-- CLERK 업무를 하는 직원들의 이름, 사번, 업무는?
SELECT ename, empno, job
from emp 
where (job = 'CLERK');

-- 급여가 1350 이상인 직원들의 이름, 사번, 급여는?
SELECT ename, empno, sal
from emp 
where (sal >= 1350);

-- 커미션이 없는 직원들의 이름, 사번, 커미션은?
SELECT ename, empno, comm
from emp 
--where not(comm > 0);
where (comm = 0) or (comm is null);

SELECT ename, empno, ifnull(comm,0)
from emp 
where (ifnull(comm,0)==0);

-- 부서번호가 10 인 직원들의 이름, 사번, 업무, 부서번호는 ?
SELECT ename, empno, job, deptno
from emp 
where (deptno = 10);

-- 상관의 사번이 7566 인 직원들의 이름, 사번, 상관의 사번은?
SELECT ename, empno, mgr
from emp 
where (mgr = 7566);




