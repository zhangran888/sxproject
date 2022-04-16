# 机构产品权限
import allure

from login import Login
from util import Utiltool
from util.ApiUtil import api

# author: zhangran
# createTime: 2022-4-8
# describe:机构产品权限列表


@allure.step('新增机构产品权限')
def test_authortity_add(jwtToken):
    data = {
        'insertFlag': 'true',
        'orgId': '10048',
        'platformIds': '0, 1, 2'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.AUTHORITY_ADD, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='新增机构产品权限成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='新增机构产品权限失败', attachment_type=allure.attachment_type.TEXT)
        assert False


@allure.step('编辑机构产品权限')
def test_authortity_update(jwtToken):
    data = {
           'insertFlag': 'false',
           'orgId': '8888',
           'platformIds': '0, 1, 2'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.AUTHORITY_UPDATE, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='修改机构产品权限成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='修改机构产品权限失败', attachment_type=allure.attachment_type.TEXT)
        assert False


@allure.step('机构产品权限-列表')
def test_authortity_list(jwtToken):
    data = {
        'pageNo': 1,
        'pageSize': 10,
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.AUTHORITY_LIST, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='机构产品权限列表查询', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='机构产品权限列表-查询失败', attachment_type=allure.attachment_type.TEXT)
        assert False

    return result


@allure.step('删除机构产品权限')
def test_authortity_del(jwtToken):
    data = {
        'orgId': 10048
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.AUTHORITY_DELETE, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='删除机构产品权限成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='删除机构产品权限-失败', attachment_type=allure.attachment_type.TEXT)
        assert False

