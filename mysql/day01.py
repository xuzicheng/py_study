import pymysql
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='zse123579', db='python_day01')
cur = conn.cursor()
cur.execute('insert into book values (55,"qeeee","哈哈哈")')
conn.commit()
cur.close()
conn.close()
