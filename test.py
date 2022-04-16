import re

import allure


@allure.severity(allure.severity_level.BLOCKER)
def test_BLOCKER():
    print('BLOCKER')


@allure.severity(allure.severity_level.CRITICAL)
def test_CRITICAL():
    print('CRITICAL')


@allure.severity(allure.severity_level.MINOR)
def test_MINOR():
    print('MINOR')


@allure.severity(allure.severity_level.TRIVIAL)
def testTRIVIAL():
    print('TRIVIAL')