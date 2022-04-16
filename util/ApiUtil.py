# 定义通用api请求
import requests


def api(method, url, data, headers):
    global results
    try:
        if method == ("post" or "POST"):
            results = requests.post(url, data, headers=headers)
        if method == ("get" or "GET"):
            results = requests.get(url, data, headers=headers)
        response = results.json()
        # code = response.get("code")
        return response
    except Exception as e:
        print("请求失败 %s--->" % e)
