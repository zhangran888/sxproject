# 角色管理
import allure

from login import Login
from util import Utiltool
from util.ApiUtil import api


# author: zhangran
# createTime: 2022-4-8
# describe:角色管理


@allure.step('角色新增')
def test_role_add(jwtToken):
    data = {
            'roleId': '',
            'roleName': 'test',
            'orgIds': '',
            'userType': 0,
            'platformId': 0,
            'parentId': -1,
            'orgTypeLevels': '[{"orgTypeId": "1008", "orgLevels": [1, 2, 3]}]',
            'parentOrgTypeId': 20
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api('post', Utiltool.ContUtil.ROLE_ADD, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='新增角色成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='新增角色失败', attachment_type=allure.attachment_type.TEXT)
        assert False

    return result


@allure.step('角色修改')
def test_role_update(jwtToken):
    data = {
            'roleId': 41,
            'roleName': 'test',
            'orgIds': '',
            'userType': 0,
            'platformId': 0,
            'parentId': -1,
            'orgTypeLevels': '[{"orgTypeId": "1008", "orgLevels": [1, 2, 3]}]',
            'parentOrgTypeId': 20
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api('post', Utiltool.ContUtil.ROLE_UPDATE, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='编辑角色成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='编辑角色失败', attachment_type=allure.attachment_type.TEXT)
        assert False

    return result


@allure.step('删除角色')
def test_role_del(jwtToken):
    data = {
            'roleId': ''
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api('post', Utiltool.ContUtil.ROLE_UPDATE, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='删除角色成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='删除角色失败', attachment_type=allure.attachment_type.TEXT)
        assert False

    return result


@allure.step('角色管理-列表')
def test_role_list(jwtToken):
    data = {
        'pageNo': 1,
        'pageSize': 10,
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.ROLE_LIST, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='角色列表查询', attachment_type=allure.attachment_type.TEXT)
        # print("数据获取成功-->", result)
        assert True
    else:
        # print("数据获取失败-->", result)
        assert False

    return result
