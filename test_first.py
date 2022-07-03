import pytest


def test_t1():
    x = 10
    y = 20
    assert x == y

def test_t2():
    x = 20
    y = 20
    assert x == y


def test_t3():
    x = 30
    y = 20
    result = x + y
    assert result == 50



def some_test(): # invalid name
    x = 30
    y = 20
    result = x + y
    assert result == 50


def test_4():
    x = 30
    y = 20
    result = x + y
    assert result == 50
