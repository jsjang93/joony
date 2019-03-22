-- SQL03.sql

select 1 + 1;
select 'he' || 'llo';

-- 급여가 1500 이상이고, 2990 이하인 직원들의 이름, 사번, 급여는?
SELECT ename, empno, sal
FROM emp
WHERE (sal BETWEEN 1500 AND 2990) ;
--WHERE (sal >= 1500) AND (sal <= 2990) ;

-- 업무가 CLERK 이고, 급여가 1000 미만인 직원들의 이름, 사번, 업무, 급여는?
SELECT ename, empno, job, sal
FROM emp
WHERE(job = 'CLERK') and (sal < 1000);

-- 부서번호가 10 이 아닌 직원들의 이름, 사번, 부서번호는 ?
SELECT ename, empno, deptno
from emp
where (deptno <> 10);
--where not(deptno = 10);
--where (deptno != 10);

-- A 로 시작하는 이름을 가진 직원들의 이름, 사번은?
SELECT  ename, empno
from emp
where (ename like 'A%'); -- % 여러칸에 아무글자, _ 한칸에 아무글자

-- 이름 두번째 위치에 A가 들어가는 직원들의 이름, 사번은?
SELECT  ename, empno
from emp
where (ename like '_A%');
-- 뒤에서 두번째 위치에 E가 들어가는 직원들의 이름, 사번은?
SELECT  ename, empno
from emp
where (ename like '%E_');

-- 급여가 1100 이거나 1600 이거나 3000 인
-- 직원들의 이름, 급여는?
SELECT ename, sal
from emp
where (sal in (1100,1600,3000));
--where (sal = 1100) or (sal = 1600) or (sal = 3000);












