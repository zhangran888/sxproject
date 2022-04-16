# 零级机构配置
import allure

from login import Login
from util import Utiltool
from util.ApiUtil import api

# 零级机构列表


@allure.step('新增-零级')
def test_zero_add(jwtToken):
    data = {
        'organizationName': '32',
        'uscId': '232332332332232333',
        'orgUniformName': '23',
        'orgParentTypeId': '20',
        'orgTypeId': '21',
        'abbreviation': 'test',
        'orderNum': '23',
        'serveTel': '',
        'orgId': '',
        'file': ''
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.ZERO_ADD, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='新增零级机构成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='新增零级机构-失败', attachment_type=allure.attachment_type.TEXT)
        assert False


@allure.step('修改零级机构')
def test_zero_update(jwtToken):
    data = {
        'organizationName': '1',
        'uscId': '231312312323333333',
        'orgUniformName': '11',
        'orgParentTypeId': '10',
        'orgTypeId': '1004',
        'abbreviation': '22',
        'orderNum': '1',
        'serveTel': '121',
        'orgId': '10053'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.ZERO_UPDATE, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='修改零级机构成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='修改零级机构失败', attachment_type=allure.attachment_type.TEXT)
        assert False

    return result


@allure.step('零级-列表')
def test_zero_list(jwtToken):
    data = {
        'pageNo': 1,
        'pageSize': 10,
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.ZERO_LIST, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='零级列表查询', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='零级列表查询-失败', attachment_type=allure.attachment_type.TEXT)
        assert False

    return result


@allure.step('删除零级机构')
def test_zero_delete(jwtToken):
    data = {
        'orgId': 10062
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.ZERO_DELETE, data=data, headers=headers)
    if result['code'] == 0:
        allure.attach(str(result), name='删除零级机构成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='删除零级机构失败', attachment_type=allure.attachment_type.TEXT)
        assert False

