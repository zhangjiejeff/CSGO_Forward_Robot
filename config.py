import json  # 模块(处理json相关格式)


def load_config():
    with open('config.json', 'r') as f:
        data = json.load(f)
        mysql_config = data['mysql_server']
        bot_config = data['vector_bot']

    return mysql_config, bot_config
