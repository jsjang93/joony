# db04.py
import sqlite3
학생들 = {5:'Hong',6:'Sophia',7:'King'}
dbcon = sqlite3.connect('test01.db')
cursor = dbcon.cursor()
###########################################


for i in 학생들:
    sql = '''Insert Into T1 values({},"{}")'''.format(i,학생들[i])
    cursor.execute(sql)
dbcon.commit()

###########################################
cursor.close()
dbcon.close()


