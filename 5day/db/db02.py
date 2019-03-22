# db02.py

#커넥션 연결, 커서 연결, 처리, 커서해제, 커넥션 해제
import sqlite3
dbcon = sqlite3.connect('test01.db')
cursor = dbcon.cursor()              #  <-- 이동용 판넬
###########################################
#처리


sql = '''insert into T1 values(40, 'James')'''
cursor.execute(sql)
dbcon.commit() # commit


###########################################
cursor.close()
dbcon.close()


# schema 어떤 용어, 시스템 등에 대한 사전 지식




