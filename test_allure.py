import allure
import pytest


class Test_all():
    @allure.step(title="allure通过注解方式完成内容的展示，setp表示测试步骤1...")
    def test_setup(self):
        print("我就是打酱油的setup")

    @allure.step(title="run就是一个正常的方法.")
    def test_run(self):
        allure.attach("自定义描述1", "描述内容，自定义")
        print("我要运行")
        assert True

    def test_skip(self):
        print("我要跳过")

