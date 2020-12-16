from day_4 import solve_both


def test_solve_first():
    assert solve_both('day_4_sample.txt') == (2, 2)
    # 290 total
    assert solve_both('day_4_my_input.txt') == (216, 150)
