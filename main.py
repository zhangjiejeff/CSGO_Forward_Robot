import json  # 模块(处理json相关格式)
import time  # 模块(获取时间等)
import requests  # 模块(HTTP协议处理)
import config  # 读取配置相关的函数
import connecting as conn  # 链接服务器等相关的函数
import csgoserverinfo as csgo  # 对于服务器信息的处理相关函数


# 机器人将服务器信息推送至群，推送间隔为forward_sep
def group_forward(bot_setting, mysql_config):
    while True:
        # 检查是否在可发送的小时内
        forward_hours = str(bot_setting['forward_hour']).split(',')
        if str(time.strftime("%H")) in forward_hours:
            # 此处为通过mysql查询需要获取查询的主页服务器信息
            querysentence = 'select id, modid, shortname, public from vcf_servers where invisible=0 order by id'

            group_array = str(bot_setting['groups']).split(',')

            mysql_handle = conn.try_and_except(conn.connect_mysql, mysql_config)
            if mysql_handle is not None:
                result = csgo.fetch_and_return(mysql_handle, querysentence)
                mysql_handle.close()
                final_result = []

                for i in range(len(result)):
                    current_map, current_players, max_players = csgo.get_server_info(result[i][3])
                    if current_map != "服务器暂未开放":
                        result_line = result[i][2], current_map, current_players, max_players
                        final_result.append(result_line)

                content = "*********************************************************************" + '\n'
                content = content + "*************** 当 前 时 间 : " + time.strftime("%Y-%m-%d %H:%M:%S") + " ***************" + '\n'
                content = content + "********************** V E 社 区 为 您 播 报 **********************" + '\n'
                for server in final_result:
                    content = content + server[0] + "  当前地图:" + server[1] + "  玩家:" + server[2] + "/" + server[3] + '\n'
                content = content + "*********************************************************************" + '\n'
                content = content + "进入服务器请从官网：www.ve-club.net 首页跳转进入" + '\n'
                content = content + "友情提示：使用国服登录器-perfectword会有额外积分奖励哦！" + '\n'
                content = content + "*********************************************************************"

                headers = {'Content-Type': 'application/json'}
                http_url = bot_setting['api_root'] + "/send_group_msg?access_token=" + bot_setting['api_token']

                for group in group_array:
                    data = json.dumps({"group_id": group, "message": content})
                    requests.post(http_url, data=data, headers=headers)

                    # 报错提示，暂时不使用
                    # if rev.text['status'] != "ok":
                    # csgo.write_log(("[Bot][Fail:Forward]" + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '\n'))

                    # 记录在窗口上
                    print('[Bot_forward]已成功完成对群(' + group + ')的服务器推送, 时间: ' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '\n')

                    # 每个群间隔几秒发送以防止被封号，推荐为5秒
                    time.sleep(bot_setting['group_sep'])
            else:
                print('[Bot_forward]因Mysql连接失败, 服务器推送失败, 时间: ' + str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())) + '\n')

        # 机器人推送间隔
        time.sleep(bot_setting['forward_sep'])


# 读取各类信息和配置
mysql_server, bot_config = config.load_config()
group_forward(bot_config, mysql_server)