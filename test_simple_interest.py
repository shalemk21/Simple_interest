from simple_interest import sim_int

def test_sim_int_positive():
    assert sim_int(1000, 2, 5) == 100.0
def test_sim_int_zero():
    assert sim_int(0, 2, 5) == 0.0
def test_sim_int_negative():
    assert sim_int(-1000, 2, 5) == -100.0