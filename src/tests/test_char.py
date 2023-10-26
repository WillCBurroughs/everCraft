from classes.char import Char

charactor = Char("jett", "lga")

def test_make_name():
    assert charactor.name is not None
    
def test_Alignment():
    assert charactor.alignment is not None

def test_Health():
    assert charactor.hp is 5

def test_Armor():
    assert charactor.ac is 10