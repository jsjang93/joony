-- SQL05.sql

-- SMITH 의 부서명은?
SELECT ename, dname
from emp, dept 
where(emp.deptno = dept.deptno)
 and (ename = 'SMITH');
 
-- SALES 부서의 직원 이름, 사번은?
SELECT dname, ename, empno
from emp , dept 
where (dept.deptno = emp.deptno) 
 and  (dname ='SALES');

-- CLERK 업무를 하는 직원들의 이름,사번,부서명,부서위치는?
SELECT ename,empno,dname,loc
from emp, dept
where (dept.deptno = emp.deptno)
 and  (job = 'CLERK');
 
-- DALLAS 에서 일하는 직원들의 부서명, 부서위치, 부서번호,이름,사번은?
SELECT d.dname, d.loc, d.deptno, e.ename, e.empno
from dept d, emp e
where (d.deptno = e.deptno)
 and  (d.loc = 'DALLAS');
 
-- 급여가 1500 ~ 2500 사이인 직원들의 이름, 부서명, 급여는?
SELECT e.ename, d.dname, e.sal
FROM emp e, dept d 
where (e.deptno = d.deptno)
 and   (sal BETWEEN 1500 and 2500);

-- 부서별 직원들의 평균급여, 최소급여, 최대급여, 급여합산은? 
-- 부서이름은 내림차순으로 정렬
SELECT d.dname,round(avg(e.sal)), min(e.sal), max(e.sal), sum(e.sal)
from dept d, emp e 
where (e.deptno = d.deptno)
group by d.dname
order by d.dname desc;

-- 업무별 급여합산액이 6000 이상인 업무와 급여합산액은?
SELECT job, sum(sal)
from emp 
group by job
having (sum(sal) >= 6000);

-- 업무별 인원수가 3명 미만인 업무와 인원수는?
SELECT job, count(empno)
from emp 
group by job 
HAVING(count(empno)<3);

-- 부서별 급여최대값 3000 이하인 부서와 급여합산액은?
SELECT d.dname, max(sal)
from dept d, emp e
where (d.deptno = e.deptno)
group by d.dname
having (max(sal) <= 3000);

SELECT ename, sal, comm, sal*12,(sal*12) + ifnull(comm,0)
from emp;

-- 직원들 중 1년 수입이 20000 이 넘는 직원들의 이름, 부서명, 1년 수입은?
-- 1년 수입 : 12개월 급여 + 커미션
SELECT e.ename, d.dname, ((sal*12) + ifnull(comm,0)) as "1년 수입"
from emp e, dept d
where (e.deptno = d.deptno)
 and  (((sal*12) + ifnull(comm,0)) > 20000);

-- 부서별 평균 1년 수입금액이 25000 이 넘는 부서별 평균 1년 수입금액은?
-- 1년 수입 : 12개월 급여 + 커미션
SELECT d.dname, round(avg((sal*12) + ifnull(comm,0))) as "평균 1년 수입"
from dept d, emp e 
where (d.deptno=e.deptno)
group by d.dname
having (round(avg((sal*12) + ifnull(comm,0))) > 25000);









 