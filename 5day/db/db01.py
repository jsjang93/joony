# db01.py

#커넥션 연결, 커서 연결, 처리, 커서해제, 커넥션 해제
import sqlite3
dbcon = sqlite3.connect('test01.db')
cursor = dbcon.cursor()              #  <-- 이동용 판넬
###########################################
#처리


sql = '''SELECT * FROM T1;'''
rows = cursor.execute(sql)                # 이동용 판넬에 sql 태움
for r in rows: print(r)                   # Tuple형태의 List였음

print()

cursor.execute(sql)
rows1 = cursor.fetchall()
for r in rows1: print(r)

print()

cursor.execute(sql)
rows2 = cursor.fetchmany(2)
for r in rows2: print(r)
###########################################
cursor.close()
dbcon.close()


# schema 어떤 용어, 시스템 등에 대한 사전 지식




