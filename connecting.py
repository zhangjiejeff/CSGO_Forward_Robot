import pymysql  # 模块(mysql相关函数)
import time  # 模块(时间相关函数)


# 错误记录函数
def write_log(log_info):
    file = open("log.txt", 'a')
    file.write(log_info)
    file.close()


def connect_mysql(dbconfig):
    mysql_conn = pymysql.connect(
        host=dbconfig['host'],
        port=dbconfig['port'],
        user=dbconfig['username'],
        password=dbconfig['password'],
        db=dbconfig['database'])
    return mysql_conn


def try_and_except(func, config):
    try:
        rt = func(config)
    except Exception as e:
        write_log("[Error][" + config['host'] + ":" + str(config['port']) + "|" + str(e) + "]" + str(
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '\n')
        return None
    return rt
