from tic_tac_toe import winner
import pytest
value=[1 , 2, 3, 4, 5, 6, 7, 8, 9]
def test_winner():
    if  value[0] == "x" and value[1]  == "x" and  value[2] == "x" or value[0] == "o" and value[1]  == "o" and  value[2] == "o":
        return True
    assert winner() == True

pytest.main(["-v", "--tb=line","-rN","test_tic_tac_toe.py"])
