# --------------- import ------------------------

import yaml
import requests
from requests.exceptions import Timeout

# ---------------- import ------------------------

# 打开并提取文件
with open("sub.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

for i in config:
    name = i["name"]
    url = i["url"]
    try:
        # 发送 GET 请求并设置超时时间
        response = requests.get(url, timeout=5)
        states = response.status_code
        if states == 200:
            print(f"{name} 状态正常")
        else:
            print(f"{name} 状态异常，状态码：{states}")
    except Timeout:
        # 捕获超时异常并处理
        print(f"{name} 请求超时，状态码：408")
    except Exception as e:
        # 捕获其他异常并处理
        print(f"{name} 发生错误: {e}")
