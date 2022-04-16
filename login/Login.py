import json

import allure
import requests

from util import Utiltool, Redis
from util.ApiUtil import api


# 登录页
# 获取图形验证码
def verfiy():
    result = api("get", Utiltool.ContUtil().VERIFYCODE_URL, "",
                 headers={'Content-Type': 'application/x-www-form-urlencoded'})
    verifyKey = result["data"]["verifyKey"]
    # print(verifyKey)
    verifyCode = Redis.redisVerfiy().get("OPENSSO:VERIFYCODE:" + verifyKey)
    # print(verifyCode)
    return verifyKey, verifyCode


# 获取ticket票据
def ticket():
    result = api("post", Utiltool.ContUtil.TICKET_URL, "",
                 headers={'Content-Type': 'application/x-www-form-urlencoded'})
    ticket = result['data']['ticket']
    # print(result['data']['ticket'])
    return ticket


# 输入登录信息，进行登录操作
@allure.step('登录')
def test_getjwtToken():
    verf = verfiy()
    tiket = ticket()
    data = {
        'account': Utiltool.AcccountUtil.ACCOUNT,
        'password': Utiltool.AcccountUtil.PASSWORD,
        'userType': 0,
        'verifyCode': verf[1],
        'verifyKey': verf[0],
        'ticket': tiket
    }
    result = api("post", Utiltool.ContUtil.JWTTOKEN_URL, data=data,
                 headers={'Content-Type': 'application/x-www-form-urlencoded'})
    if result['code'] == 0:
        # print("登录成功，接口获取无误！！")
        jwtToken = result['data']['jwtToken']
        allure.attach(jwtToken, name='登录成功', attachment_type=allure.attachment_type.TEXT)
        return jwtToken
        assert True
    else:
        allure.attach("获取接口数据有误，登录异常", name='登录失败', attachment_type=allure.attachment_type.TEXT)
        assert False
        # print("登录失败，接口信息有误！！")


# if __name__ == '__main__':
    # verfiy()
    # ticket()
    # getjwtToken()
