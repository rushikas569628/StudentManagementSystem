import pytest
import Source.calculator as a

def test_add_positive():
    assert a.add(12,3)==5

def test_add_negative():
    assert a.add(-2,-3)==-5

def test_add_zero():
    assert a.add(0,0)==0