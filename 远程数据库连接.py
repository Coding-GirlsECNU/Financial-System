import psycopg2

# 替换为你的PostgreSQL数据库的配置信息
host = '47.95.213.242'          # 阿里云的PostgreSQL服务器地址
port = '5433'          # 通常是5432
database = 'al'  # 数据库名称
user = 'postgres'          # 数据库用户名
password = 'zzh0117.'  # 数据库密码

try:
    # 建立数据库连接
    connection = psycopg2.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )

    # 创建一个游标对象
    cursor = connection.cursor()

    # 执行一个SQL查询
    cursor.execute("SELECT version();")

    # 获取查询结果
    db_version = cursor.fetchone()
    print(f"PostgreSQL数据库版本: {db_version}")

    # 关闭游标和连接
    cursor.close()
    connection.close()

except Exception as error:
    print(f"连接到PostgreSQL数据库时出错: {error}")
