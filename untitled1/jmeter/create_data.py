import pymysql,random




for i in range(1,10001):
    number = random.randint(1, 100000)
    num = i
    con = pymysql.connect("localhost", "root", "123456", "data")  # 链接数据库
    cur = con.cursor()  # 创建游标ec
    #sql = "delete from try"
    sql = "insert into try values('%d','裙子%d','12','包装厂','重庆')"%(num,number)
    cur.execute(sql)
    con.commit()

