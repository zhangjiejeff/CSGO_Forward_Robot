# (QQ群机器人-推送CSGO服务器信息) CSGO_Forward_Robot
> 用于推送CSGO服务器的信息到QQ群，基于ONE-Bot协议的QQ机器人

## 需要下载的Python模块（Related Modulus Download）
> 1. A2S-python https://github.com/Yepoleb/python-a2s
> 其余使用到的模块为内置模块（Other modulus used is built-in python modulus, you may ignore）

## 使用方法 ( How to use )
> 1. 下载基于One-Bot协议的QQ机器人并进行配置，此处推荐cqhttp机器人 https://github.com/Mrs4s/go-cqhttp/releases/tag/v0.9.40
> 2. 配置机器人里的config.hjson文件，需要开启HTTP的监听，机器人http_config里的配置需要和config.json里的vector_bot内保持一致
> "api_root" : "http://127.0.0.1:5700" == 机器人http_config里的 host:port
> "api_token": "apitoken" == 机器人http_config里的 access_token
> 3. 配置Mysql里的服务器列表，以及main.py里的querysentence, 使得其能正确的读出服务器信息，此处写出我的mysqlquery设置
> querysentence = 'select id, modid, shortname, public from vcf_servers where invisible=0 order by id'
> id为序列, modid为模式id(因为搭配其他功能使用，如不需要的可以自行删除并调整数组的索引号), shortname为推送时服务器的名称, public为该服务器IP
> 4. 修改main.py里的content推送的格式，改为自己服务器需要的格式
> 5. 先运行qq机器人，再运行此python脚本即可进行自动推送

## 疑问咨询 ( Questions )
> 有任何关于使用的疑问和建议都可以咨询我 QQ1204601575
