import lab.ahs_lab01 as l

def test_q1():
    assert l.falling(6, 3) == 120
    assert l.falling(4, 3) == 24
    assert l.falling(4, 1) == 4
    assert l.falling(4, 0) == 1