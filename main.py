# -*- coding: utf-8 -*-
# --------------- import ------------------------

import yaml
import requests
from requests.exceptions import Timeout

# ---------------- import ------------------------

# 打开并提取文件
with open("sub.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

with open("status.txt", "w", encoding="utf-8") as status_file:
    for i in config:
        name = i["name"]
        url = i["url"]
        try:
            # 发送 GET 请求并设置超时时间
            response = requests.get(url, timeout=5)
            states = response.status_code
            if states == 200:
                status_line = f"{name} 状态正常"
            else:
                status_line = f"{name} 状态异常，状态码：{states}"
            # 写入状态信息到文件
            status_file.write(status_line + "\n")
            # 打印状态信息到控制台（可选）
            print(status_line)
        except Timeout:
            # 捕获超时异常并处理
            status_line = f"{name} 请求超时，状态码：408"
            status_file.write(status_line + "\n")
            print(status_line)
        except Exception as e:
            # 捕获其他异常并处理
            status_line = f"{name} 发生错误: {e}"
            status_file.write(status_line + "\n")
            print(status_line)
