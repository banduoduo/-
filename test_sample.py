"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/4/8 8:13 下午'
"""
import pytest


def func(x):
    return x + 1


@pytest.mark.login
def test_answer():
    assert func(4) == 5
