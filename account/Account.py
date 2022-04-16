# 用户管理
import random

import allure

from login import Login
from util import Utiltool
from util.ApiUtil import api


@allure.step('新增用户')
def test_account_add(jwtToken):
    data = {
        'userName': '新增测试',
        'orgId': 10028,
        'idCard': '440509199904220813',
        'roleIds': '37, 38, 39, 45',
        'phonenumber': '13902748130',
        'account': 'TLCB789',
        'remark': '产品测'+str(random.randint(22, 88)),
        'status': 0,
        'zzdAccount': ''
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.ACCOUNT_ADD, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='用户新增成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='用户新增失败', attachment_type=allure.attachment_type.TEXT)
        assert False

    return result


@allure.step('编辑用户')
def test_account_update(jwtToken):
    data = {
        'userName': '编辑测试',
        'orgId': 10028,
        'idCard': '440509199904220813',
        'roleIds': '37, 38, 39, 45',
        'phonenumber': '13902748130',
        'account': 'TLCB789',
        'remark': '产品测'+str(random.randint(22, 88)),
        'status': 0,
        'userId': 89,
        'zzdAccount': ''
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.ACCOUNT_UPDATE, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='编辑用户成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='编辑用户失败', attachment_type=allure.attachment_type.TEXT)
        assert False

    return result


@allure.step('用户管理-列表')
def test_account_list(jwtToken):
    data = {
        'pageNo': 1,
        'pageSize': 10,
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.ACCOUNT_LIST, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='用户管理列表查询', attachment_type=allure.attachment_type.TEXT)
        # print("数据获取成功-->", result)
        assert result
    else:
        allure.attach(str(result), name='用户管理列表获取失败', attachment_type=allure.attachment_type.TEXT)
        # print("数据获取失败-->", result)
        assert result

    return result


@allure.step('重置密码')
def test_reset_password(jwtToken):
    data = {
        'userId': ''
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api('post', Utiltool.ContUtil.ACCOUNT_RESET, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='重置用户成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='重置用户失败', attachment_type=allure.attachment_type.TEXT)
        assert False

    return result


@allure.step('停用用户')
def test_disable(jwtToken):
    data = {
        'userId': '',
        'status': 1
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api('post', Utiltool.ContUtil.ACCOUNT_DISABLE, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='停用用户成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='停用用户失败', attachment_type=allure.attachment_type.TEXT)
        assert False

    return result
