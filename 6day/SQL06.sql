-- SQL06.sql

-- SMITH의 이름, 급여, 급여등급은?
SELECT e.ename, e.sal, s.grade
from emp e, salgrade s
where (e.sal BETWEEN s.losal and s.hisal)
 and  (e.ename = 'SMITH');
 
-- 3등급의 급여등급을 가지고 있는 직원들의 이름, 급여, 급여등급은?
SELECT e.ename, e.sal, s.grade
from salgrade s, emp e
where (e.sal BETWEEN s.losal and s.hisal)
 and  (s.grade = 3);

-- 급여가 1401 ~ 2000 인 직원들의 이름, 급여,급여등급,부서명은?
SELECT e.ename, e.sal, s.grade, d.dname
from emp e, salgrade s, dept d
where (e.sal BETWEEN s.losal and s.hisal)
 and  (e.deptno = d.deptno)
 and  (e.sal BETWEEN 1401 and 2000);


-- 시카고에서 근무하는 직원들의 이름, 부서명, 위치, 급여,급여등급은 ?
SELECT e.ename, d.dname, d.loc, e.sal, s.grade
from dept d, emp e, salgrade s
where (d.deptno = e.deptno)
 and  (e.sal BETWEEN 1401 and 2000)
 and  (d.loc = 'CHICAGO');
 
-- SMITH의 이름, 사번, 상관의 이름, 사번은?
SELECT ee.ename, ee.empno, em.ename, em.empno 
from emp em, emp ee
where (em.empno = ee.mgr)
 and  (ee.ename = 'SMITH');

-- SMITH의 이름, 사번,부서명, 상관의 이름, 사번,부서명은?
SELECT ee.ename, ee.empno,de.dname, em.ename, em.empno,dm.dname
from emp ee, dept de, emp em, dept dm
where (ee.deptno = de.deptno)
 and  (ee.mgr = em.empno)
 and  (em.deptno = dm.deptno)
 and  (ee.ename = 'SMITH');
 
-- SMITH의 이름, 사번,급여,급여등급, 상관의 이름, 사번,급여,급여등급은?
SELECT ee.ename, ee.empno,ee.sal,se.grade, 
		em.ename, em.empno,em.sal,sm.grade 
from emp ee, salgrade se, emp em , salgrade sm
where (ee.sal BETWEEN se.losal and se.hisal)
 and  (ee.mgr = em.empno)
 and  (em.sal BETWEEN sm.losal and sm.hisal)
 and  (ee.ename = 'SMITH');


-- SMITH의 이름, 사번,급여등급,부서명, 상관의 이름,사번,급여등급,부서명은?
SELECT ee.ename, ee.empno,ee.sal,se.grade, de.dname,
		em.ename, em.empno,em.sal,sm.grade, dm.dname 
from emp ee, salgrade se, dept de, emp em, salgrade sm, dept dm
where (ee.sal BETWEEN se.losal and se.hisal)
 and  (ee.deptno = de.deptno)
 and  (ee.mgr = em.empno)
 and  (em.sal BETWEEN sm.losal and sm.hisal)
 and  (em.deptno = dm.deptno)
 and  (ee.ename = 'SMITH');




