#!usr\bin\python3

# python3中MySQL数据操作,使用mysql-connector-python数据模块

import mysql.connector


def db_connect():
    # 创建数据库连接
    db = mysql.connector.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        passwd="root123456"  # 数据库密码
    )
    print(db)
    # 创建该连接的游标
    cursor = db.cursor()
    # 创建数据库
    cursor.execute('DROP DATABASE IF EXISTS Tibet_db')
    cursor.execute("CREATE DATABASE Tibet_db")
    # 查询数据库
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        print(x)
    db.close()
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root123456",
        database="Tibet_db"
    )
    cursor = db.cursor()
    # 创建一个名为 sites 的数据表
    cursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
    # 查询表
    cursor.execute("SHOW TABLES")
    for x in cursor:
        print(x)
    # 添加id为主键
    cursor.execute("ALTER TABLE sites ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
    # 直接建表添加主键
    # cursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")
    # 插入单条数据
    sql_one = "INSERT INTO sites (name, url) VALUES (%s, %s)"
    val_one = ("RUNOOB", "https://www.runoob.com")
    cursor.execute(sql_one, val_one)
    db.commit()  # 数据表内容有更新，必须使用到该语句
    print(cursor.rowcount, "记录插入成功。")
    sql_many = "INSERT INTO sites (name, url) VALUES (%s, %s)"
    val_many = [
        ('Google', 'https://www.google.com'),
        ('Github', 'https://www.github.com'),
        ('Taobao', 'https://www.taobao.com'),
        ('stackoverflow', 'https://www.stackoverflow.com/')
    ]
    cursor.executemany(sql_many, val_many)
    db.commit()  # 数据表内容有更新，必须使用到该语句
    print(cursor.rowcount, "记录插入成功。")
    # 获取最后一条记录的id
    print("最后一条记录, ID:", cursor.lastrowid)
    # 查询表中所有信息
    cursor.execute("SELECT * FROM sites")
    my_result = cursor.fetchall()  # fetchall() 获取所有记录，fetchone() 获取一条记录
    for x in my_result:
        print(x)
    # 查询表中指定元素特定条件的信息，DESC降序，没有升序
    cursor.execute("SELECT * FROM sites WHERE url LIKE '%oo%' ORDER BY name")
    result = cursor.fetchall()
    for x in result:
        print(x)
    # LIMIT查询限制条数，OFFSET从第几条开始
    cursor.execute("SELECT * FROM sites LIMIT 3 OFFSET 1")  # 0 为 第一条，1 为第二条，以此类推
    result_all = cursor.fetchall()
    for x in result_all:
        print(x)
    # 删除
    sql = "DELETE FROM sites WHERE name = %s"
    na = ("stackoverflow",)
    cursor.execute(sql, na)
    db.commit()
    print(cursor.rowcount, " 条记录删除")
    # 修改
    sql = "UPDATE sites SET name = %s WHERE name = %s"
    val = ("Zhihu", "ZH")
    cursor.execute(sql, val)
    db.commit()
    print(cursor.rowcount, " 条记录被修改")
    # 删除表
    sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites
    cursor.execute(sql)


def main():
    db_connect()


if __name__ == '__main__':
    main()
