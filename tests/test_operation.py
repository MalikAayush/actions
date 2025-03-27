from src.math_opertaion import add,sub

def test_add():
    assert add(2,3)==5
    assert add(5,6)==11
    assert add(4,5)==9

def test_sub():
    assert sub(5,2)==3
    assert sub(5,6)==-1
    assert sub(3,3)==0