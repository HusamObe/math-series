import pytest
from math_series.series import fibonacci
from math_series.series import lucas
from math_series.series import sum_series



def test_one():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected
    
def test_two():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected
    
def test_three():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected
    
def test_four():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected
    
def test_five():
    actual = fibonacci(-9)
    expected = 34
    assert actual == expected
    
def test_one_lucas():
    actual = lucas(0)
    expected = 2
    assert actual == expected
    
def test_two_lucas():
    actual = lucas(1)
    expected = 1
    assert actual == expected
    
def test_three_lucas():
    actual = lucas(4)
    expected = 7
    assert actual == expected

def test_four_lucas():
    actual = lucas(7)
    expected = 29
    assert actual == expected
    
def test_five_lucas():
    actual = lucas("10")
    expected = 123
    assert actual == expected
    
def test_sum_series_one():
    actual = sum_series(5)
    expected = 5
    assert actual == expected  
    
def test_sum_series_two():
    actual = sum_series(7,2,1)
    expected = 29
    assert actual == expected
    

def test_sum_series_three():
    actual = sum_series(-7)
    expected = 13
    assert actual == expected