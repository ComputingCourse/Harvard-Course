#from TikTacToe import winnable,check_win,get_row,get_collum
import project.project as project

def test_winnable():
    assert winnable(["","x",""],["","x",""],["","",""]) == (2,1)
    assert winnable(["x","",""],["","x",""],["","",""]) == (2,2)
    assert winnable(["","","x"],["","x",""],["","",""]) == (2,0)
    assert winnable(["x","x",""],["","",""],["","",""]) == (0,2)

def test_check_win():
    assert check_win(["","x",""],["","x",""],["","",""]) == False
    assert check_win(["","x",""],["","x",""],["","x",""]) == True
    assert check_win(["o","",""],["o","x",""],["o","x",""]) == True

def test_get_row():
    assert get_row(150) == 0
    assert get_row(300) == 1
    assert get_row(450) == 2

def test_get_collum():
    assert get_collum(150) == 0
    assert get_collum(300) == 1
    assert get_collum(450) == 2