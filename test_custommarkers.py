import pytest


@pytest.mark.smoke
def test_t1():
    x = 20
    y = 20
    assert x == y


@pytest.mark.regression
def test_t2():
    x = 20
    y = 20
    assert x == y


@pytest.mark.shadaab
@pytest.mark.regression
def test_t3():
    name = "Credence "
    message = "Credence is the best place to work"
    assert name in message


@pytest.mark.smoke
@pytest.mark.regression
def test_t4():
    name = "credence is the best place to work"
    message = "credence is the best place to work"
    assert name is message


@pytest.mark.regression
def test_t5():
    name = "Credence"
    message = "Credence is the best place to work"
    assert name is message
