import a2s  # 模块(sourcemod a2s query)
import time  # 模块(获取时间等)
from connecting import write_log  # 错误记录函数


# 通过mysql句柄进行对应的query处理，如报错则通过write_log函数记录
def fetch_and_return(mysql_conn, query):
    # 初始化数组
    try:
        with mysql_conn.cursor() as cursor:
            cursor.execute(query)
            select_result = cursor.fetchall()
            return_array = list(select_result)
    except Exception as e:
        write_log(
            ("[Error][" + ipaddress + ":" + str(e) + "]" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '\n'))
        return []
    return return_array


# 根据对应给出的ip地址进行服务器信息的获取，如报错则通过write_log函数记录
def get_server_info(ipaddress):
    ipport = ipaddress.split(':')
    server_address = (ipport[0], int(ipport[1]))

    try:
        info = str(a2s.info(server_address))
    except Exception as e:
        write_log(
            ("[Error][" + ipaddress + ":" + str(e) + "]" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '\n'))
        return "服务器暂未开放", 0, 0

    # 切出地图信息
    pos_start = info.find("map_name='") + 10
    pos_end = info.find("', folder", pos_start)
    map_name = str(info[pos_start:pos_end])

    # 切出当前玩家信息
    pos_start = info.find("player_count=") + 13
    pos_end = info.find(", max_players", pos_start)
    player_count = str(info[pos_start:pos_end])

    # 切出最大玩家信息
    pos_start = info.find("max_players=") + 12
    pos_end = info.find(", bot_count", pos_start)
    max_player = str(info[pos_start:pos_end])

    # 用于重复验证，但加重负担先不考虑
    # if player_count == 0 and not check:
    # time.sleep(5)
    # return get_server_info(ipaddress, True)

    return map_name, player_count, max_player
