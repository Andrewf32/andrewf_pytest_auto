from pytest import fixture, mark
from selenium import webdriver


@fixture(scope='function')
def car_condition(condition):
    yield condition


@fixture(scope='function')
def part_condition(p_condition):
    if p_condition == 'Faulty':
        return p_condition
    elif p_condition == 'Clean':
        return p_condition


@fixture(scope='session')
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser
    print("\n\nTearing down browser")