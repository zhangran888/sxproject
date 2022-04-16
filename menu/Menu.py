# 菜单管理
import allure

from login import Login
from util import Utiltool
from util.ApiUtil import api


# author: zhangran
# createTime: 2022-4-8
# describe:菜单列表


@allure.step('新增菜单')
def test_menu_add(jwtToken):
    data = {
        'menuName': '测试',
        'url': '12',
        'menuType': 'M',
        'platformId': 0
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api('post', Utiltool.ContUtil.MENU_ADD, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='新增菜单成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='新增菜单失败', attachment_type=allure.attachment_type.TEXT)
        assert False


@allure.step('修改菜单')
def test_menu_update(jwtToken):
    data = {
        'menuName': '测试',
        'orderNum': 0,
        'path': '#',
        'pathId': '',
        'icon': '',
        'url': 12,
        'visible': 0,
        'menuType': 'M',
        'parentId': '',
        'platformId': 0,
        'menuId': 5730
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api('post', Utiltool.ContUtil.MENU_UPDATE, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='修改菜单成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='修改菜单失败', attachment_type=allure.attachment_type.TEXT)
        assert False


@allure.step('菜单管理-列表')
def test_menu_list(jwtToken):
    data = {
        'pageNo': 1,
        'pageSize': 10,
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.MENU_LIST, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='菜单配置-列表获取成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='菜单配置-列表获取失败', attachment_type=allure.attachment_type.TEXT)
        assert False

    return result


@allure.step('删除菜单')
def test_menu_del(jwtToken):
    data = {
        'menuId': 5730
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.MENU_DELETE, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='菜单删除成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='菜单删除失败', attachment_type=allure.attachment_type.TEXT)
        assert False
