import pytest
import sys


@pytest.mark.skip #unconditional
def test_t1():
    x = 10
    y = 20
    assert x == y


@pytest.mark.skipif(sys.version_info <= (3, 7), reason="Credence is the best IT training institute")
def test_t2():
    x = 20
    y = 20
    assert x == y


@pytest.mark.xfail
def test_t3():
    x = 30
    y = 20
    result = x + y
    assert result == 50


def test_5():
    x = 30
    y = 20
    result = x + y
    assert result == 50


def test_4():
    x = 30
    y = 20
    result = x + y
    assert result == 50



