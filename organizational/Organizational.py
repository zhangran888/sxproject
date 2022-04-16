# 机构管理
import random

import allure

from login import Login
from util import Utiltool
from util.ApiUtil import api

# 机构管理列表


@allure.step('新增机构')
def test_organizational_add(jwtToken):
    data = {
        'orgId': '',
        'orgProvinceId': '330000',
        'orgProvince': '浙江省',
        'orgCity': '丽水市',
        'orgArea': '缙云县',
        'orgStreet': '新建镇',
        'orgLatitude': '30.344444',
        'orgLongitude': '123.232333',
        'creditFlag': '1',
        'orgDetail': '测试区',
        'organizationName': '测试',
        'orgSimpleName': '测试',
        'uscId': '91340000762794062H',
        'rootOrgId': '10049',
        'orderNum': '1',
        'parentId': '8888',
        'status': '0',
        'remark': '测试',
        'orgCityId': '331100',
        'orgAreaId': '331122',
        'orgStreetId': '33112206'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.ORGANIZATIONAL_ADD, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='新增机构成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='新增机构失败', attachment_type=allure.attachment_type.TEXT)
        assert False


@allure.step('修改机构')
def test_organizational_update(jwtToken):
    data = {
        'orgId': '10063',
        'orgProvinceId': '330000',
        'orgProvince': '浙江省',
        'orgCity': '丽水市',
        'orgArea': '缙云县',
        'orgStreet': '新建镇',
        'orgLatitude': '30.344444',
        'orgLongitude': '123.232333',
        'creditFlag': '1',
        'orgDetail': '测试区',
        'organizationName': '测试'+str(random.randint(12, 55)),
        'orgSimpleName': '测试',
        'uscId': '91340000762794062H',
        'rootOrgId': '10049',
        'orderNum': '1',
        'parentId': '8888',
        'status': '0',
        'remark': '测试',
        'orgCityId': '331100',
        'orgAreaId': '331122',
        'orgStreetId': '33112206'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.ORGANIZATIONAL_UPDATE, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='修改机构成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='修改机构失败', attachment_type=allure.attachment_type.TEXT)
        assert False


@allure.step('机构管理-列表')
def test_organizational_list(jwtToken):
    data = {
        'pageNo': 1,
        'pageSize': 10,
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.ORGANIZATIONAL_LIST, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='机构管理列表查询', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='机构管理列表-获取失败', attachment_type=allure.attachment_type.TEXT)
        assert False

    return result

