import os

import allure
import pytest

from Role import Role
from account import Account
from authority import Authortity
from institutional import Institutional
from login import Login, Home

# @allure.title('系统设置模块')
# def test():
#     with allure.step('登录步骤一'):
#         jwtToken = Login.test_getjwtToken()
#     with allure.step('首页辖内'):
#         Home.test_home_xn(jwtToken)
#     with allure.step('首页本级'):
#         Home.test_home_local(jwtToken)
# @allure.title('登录')
# def test_jwtoken():
#     jwtToken = Login.test_getjwtToken()
#     return jwtToken
#
#
# @allure.title('首页')
# def test_home():
#     jwtToken = test_jwtoken()
#     Home.test_home_xn(jwtToken)
#     Home.test_home_local(jwtToken)
#
#
# @allure.title('机构分类管理')
# def test_fl():
#     jwtToken = test_jwtoken()
#     Institutional.test_institu(jwtToken)
from menu import Menu
from organizational import Organizational
from zero import Zero

jwtToken = None


@allure.feature('管理后台-登录-首页')
class Test_login:
    @allure.title('登录模块')
    def test_login(self):
        global jwtToken
        jwtToken = Login.test_getjwtToken()

    @allure.title('首页模块')
    def test_home(self):
        Home.test_home_xn(jwtToken)
        Home.test_home_local(jwtToken)
        Home.test_home_information(jwtToken)
        Home.test_home_log(jwtToken)


@allure.feature('系统设置-机构分类')
class Test_institutional:
    @allure.title('机构分类列表')
    def test_fl(self):
        Institutional.test_institu(jwtToken)

    @allure.title('新增机构分类')
    def test_a(self):
        Institutional.test_add_institutional(jwtToken)

    @allure.title('修改机构分类')
    def test_up(self):
        Institutional.test_inst_update(jwtToken)

    @allure.title('删除机构分类')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_del(self):
        Institutional.test_delete_institu(jwtToken)


@allure.feature('系统设置-零级机构')
class Test_zero:
    @allure.title('零级配置-列表')
    def test_zer(self):
        Zero.test_zero_list(jwtToken)

    @allure.title('新增-零级')
    def test_zer_add(self):
        Zero.test_zero_add(jwtToken)

    @allure.title('修改-零级')
    def test_zer_update(self):
        Zero.test_zero_update(jwtToken)

    @allure.title('删除-零级')
    def test_zer_del(self):
        Zero.test_zero_delete(jwtToken)


@allure.feature('系统设置-机构管理')
class Test_organ:
    @allure.title('机构列表')
    def test_zation(self):
        Organizational.test_organizational_list(jwtToken)

    @allure.title('新增-机构')
    def test_zation_add(self):
        Organizational.test_organizational_add(jwtToken)

    @allure.title('修改-机构')
    def test_zation_update(self):
        Organizational.test_organizational_update(jwtToken)


@allure.feature('系统设置-机构产品权限')
class Test_author:
    @allure.title('机构权限配置')
    def test_tity(self):
        Authortity.test_authortity_list(jwtToken)

    @allure.title('新增机构权限')
    def test_tity(self):
        Authortity.test_authortity_add(jwtToken)

    @allure.title('修改权限')
    def test_tity(self):
        Authortity.test_authortity_update(jwtToken)

    @allure.title('删除机构权限')
    def test_tity(self):
        Authortity.test_authortity_del(jwtToken)


@allure.feature('系统设置-角色管理')
class Test_role:
    @allure.title('角色列表')
    def test_ro_list(self):
        Role.test_role_list(jwtToken)

    @allure.title('新增角色')
    def test_ro_add(self):
        Role.test_role_add(jwtToken)

    @allure.title('修改角色')
    def test_ro_update(self):
        Role.test_role_update(jwtToken)

    @allure.title('删除角色')
    def test_ro_del(self):
        Role.test_role_del(jwtToken)


@allure.feature('系统设置-用户管理')
class Test_acunt:
    @allure.title('用户列表')
    def test_coun_list(self):
        Account.test_account_list(jwtToken)

    @allure.title('新增用户')
    def test_ac_add(self):
        Account.test_account_add(jwtToken)

    @allure.title('修改用户')
    def test_ac_update(self):
        Account.test_account_update(jwtToken)

    @allure.title('停用用户')
    def test_ac_disable(self):
        Account.test_disable(jwtToken)

    @allure.title('重置密码')
    def test_ac_rst(self):
        Account.test_reset_password(jwtToken)


@allure.feature('系统设置-菜单管理')
class Test_me:
    @allure.title('菜单列表')
    def test_mnu(self):
        Menu.test_menu_list(jwtToken)

    @allure.title('新增菜单')
    def test_mnu_add(self):
        Menu.test_menu_add(jwtToken)

    @allure.title('修改菜单')
    def test_mnu_add(self):
        Menu.test_menu_update(jwtToken)

    @allure.title('删除菜单')
    @allure.severity(allure.severity_level.BLOCKER)
    def test_mnu_add(self):
        Menu.test_menu_update(jwtToken)



if __name__ == '__main__':
    pytest.main(["-s", "-v", "--alluredir", "./report"])