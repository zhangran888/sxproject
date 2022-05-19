import difflib
import random

import allure
import pytest

from login import Login
from util import Utiltool
from util.ApiUtil import api
import re


# author: zhangran
# createTime: 2022-4-8
# describe:机构分类

@allure.step('机构分类管理-列表')
def test_institu(jwtToken):
    data = {
        'pageNo': 1,
        'pageSize': 100,
        'orgTypeLevel': 2,
        'orgTypeName': '',
        'startTime': '',
        'endTime': ''
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api("post", Utiltool.ContUtil.INSTITUTIONAL_LIST, data=data, headers=headers)
    if result['code'] == 0:
        inlist = str(result)
        allure.attach(inlist, name='机构分类列表查询成功', attachment_type=allure.attachment_type.TEXT)
        assert True
    else:
        allure.attach(str(result), name='机构分类列表查询失败', attachment_type=allure.attachment_type.TEXT)
        # print("数据获取失败-->", result)
        assert False

    return result


@allure.step('新增机构分类')
def test_add_institutional(jwtToken):
    data = {
        'parentId': 20,
        'orgTypeName': 'test'+str(random.randint(50, 99)),
        'orgTypeNo': random.randint(50, 99),
        'remark': '测试'
    }
    # # 用于报错
    # data = {}
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'jwtToken': jwtToken
    }
    result = api('post', Utiltool.ContUtil.INSTITUTIONAL_ADD, data=data, headers=headers)
    if result is None:
        with allure.step('异常'):
            allure.attach('接口异常', name='新增机构分类失败', attachment_type=allure.attachment_type.TEXT)
            assert False
    else:
        if result['code'] == 0:
            msg = str(result)
            allure.attach(msg, name='新增机构分类成功', attachment_type=allure.attachment_type.TEXT)
            assert True
        else:
            allure.attach(result['msg'], name='新增机构分类失败', attachment_type=allure.attachment_type.TEXT)
            assert False


@allure.step('修改机构')
def test_inst_update(jwtToken):
    result = test_institu(jwtToken)
    for name in result['data']['records']:
        # print(name['orgTypeName'])
        if re.match('test', name['orgTypeName']):
            # print(name['id'])
            data = {
                'id': name['id'],
                'parentId': 20,
                'orgTypeName': 'test' + str(random.randint(50, 99)),
                'orgTypeNo': random.randint(101, 199),
                'remark': '修改' + str(random.randint(101, 199))
            }
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'jwtToken': jwtToken
            }
            apirestult = api('post', Utiltool.ContUtil.INSTITUTIONAL_UPDATE, data=data, headers=headers)
            msg = str(apirestult)
            if apirestult is None:
                with allure.step('异常'):
                    allure.attach('接口异常', name='修改机构分类失败', attachment_type=allure.attachment_type.TEXT)
                    assert False
            else:
                if apirestult['code'] == 0:
                    allure.attach(msg, name='修改机构分类接口请求成功', attachment_type=allure.attachment_type.TEXT)
                    assert True
                else:
                    allure.attach(msg, name='修改机构分类失败', attachment_type=allure.attachment_type.TEXT)
                    assert False


@allure.step('删除机构-分类')
def test_delete_institu(jwtToken):
    result = test_institu(jwtToken)
    for name in result['data']['records']:
        # print(name['orgTypeName'])
        if re.match('aaa', name['orgTypeName']):
            # print(re.match('test', name['orgTypeName']).string)
            # print(name['id'])
            data = {
                'id': name['id']
            }
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
                'jwtToken': jwtToken
            }
            resultup = api('post', Utiltool.ContUtil.INSTITUTIONAL_DELETE, data=data, headers=headers)
            msg = str(resultup)
            if resultup is None:
                with allure.step('异常'):
                    allure.attach('接口异常', name='删除机构接口异常', attachment_type=allure.attachment_type.TEXT)
                    assert False
            else:
                if resultup['code'] == 0:
                    allure.attach(msg, name='删除机构分类接口请求成功', attachment_type=allure.attachment_type.TEXT)
                    assert True
                else:
                    allure.attach(msg, name='删除机构分类失败', attachment_type=allure.attachment_type.TEXT)
                    assert False
