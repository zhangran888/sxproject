# 首页
import allure

from login import Login
from util import Utiltool
from util.ApiUtil import api


@allure.step('辖内机构数显示')
def test_home_xn(jwtToken):
    print(jwtToken)
    allure.attach(jwtToken, name='jwtToken数据获取', attachment_type=allure.attachment_type.TEXT)
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("get", Utiltool.ContUtil.HOME_INSTITUTION_NUMBER, "", headers=headers)
    if result['code'] == 0:
        strname = '辖内机构数--> ' + str(result['data']['normalNum']) + '停用账号共计--> ' + str(result['data']['stopNum'])\
              + '正常账号共计--> ' + str(result['data']['totalNum'])
        allure.attach(strname, name='辖内机构数', attachment_type=allure.attachment_type.TEXT)
        print("数据获取成功-->", result)
        assert True
    else:
        print("数据获取失败-->", result)
        assert False

    return result


@allure.step('本机构用户数显示')
def test_home_local(jwtToken):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("get", Utiltool.ContUtil.HOME_LOACAL_INST_NUMBER, "", headers=headers)
    if result['code'] == 0:
        strname = '本机机构数--> ' + str(result['data']['totalNum']) \
                  + '停用账号共计--> ' + str(result['data']['lockedNum']) \
                  + '正常账号共计--> ' + str(result['data']['normalNum'])\
                  + '冻结账号共计--> ' + str(result['data']['blockedNum'])
        allure.attach(strname, name='本机构用户数', attachment_type=allure.attachment_type.TEXT)
        print("数据获取成功-->", result)
        assert True
    else:
        print("数据获取失败-->", result)
        assert False

    return result


@allure.step('用户基本信息')
def test_home_information(jwtToken):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.HOME_USER_INFORMATION, "", headers=headers)
    if result['code'] == 0:
        info = '账号--> ' + str(result['data']['account']) + '姓名--> ' + str(result['data']['userName'])\
                        + '角色--> ' + str(result['data']['roleNames'])
        allure.attach(info, name='用户基本信息', attachment_type=allure.attachment_type.TEXT)
        print("数据获取成功-->", result)
        assert result
    else:
        print("数据获取失败-->", result)
        assert result

    return result


@allure.step('用户登录信息')
def test_home_log(jwtToken):
    data = {
        'businessType': 4,
        'pageNo': 1,
        'pageSize': 10
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.HOME_LOG, data=data, headers=headers)
    if result['code'] == 0:
        logger = str(result)
        allure.attach(logger, name='用户基本信息', attachment_type=allure.attachment_type.TEXT)
        print("数据获取成功-->", result)
        assert True
    else:
        print("数据获取失败-->", result)
        assert False

    return result

# if __name__ == '__main__':
#     home_log()