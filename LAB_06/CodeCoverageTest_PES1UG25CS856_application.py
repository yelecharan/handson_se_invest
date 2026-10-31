import pytest

from bowling_alley import lane_cost, frame_score, lane_assignment


# LANE COST TESTS

def test_weekday_booking():
    assert lane_cost("weekday", 2, 4, 2, False) == 900


def test_weekend_booking():
    assert lane_cost("weekend", 2, 5, 1, True) == 1160


def test_invalid_day_type():
    with pytest.raises(ValueError):
        lane_cost("holiday", 2, 4, 1, False)


def test_invalid_booking():
    with pytest.raises(ValueError):
        lane_cost("weekday", 0, 4, 1, False)


def test_invalid_players():
    with pytest.raises(ValueError):
        lane_cost("weekday", 2, 7, 1, False)


def test_too_many_shoe_rentals():
    with pytest.raises(ValueError):
        lane_cost("weekday", 2, 3, 4, False)


def test_league_member_discount():
    assert lane_cost("weekday", 1, 4, 0, True) == 320


# FRAME SCORE TESTS

def test_open_frame():
    assert frame_score(3, 4, []) == 7


def test_strike():
    assert frame_score(10, 0, [5, 3]) == 18


def test_spare():
    assert frame_score(6, 4, [5]) == 15


def test_invalid_roll():
    with pytest.raises(ValueError):
        frame_score(-1, 4, [])


def test_invalid_frame():
    with pytest.raises(ValueError):
        frame_score(8, 5, [])


# LANE ASSIGNMENT TESTS

def test_no_lanes_available():
    assert lane_assignment(4, False, 0) == "wait"


def test_bumper_lane():
    assert lane_assignment(4, True, 2) == "bumper lane"


def test_two_lanes():
    assert lane_assignment(8, False, 2) == "two lanes"


def test_wait_for_two_lanes():
    assert lane_assignment(8, False, 1) == "wait"


def test_standard_lane():
    assert lane_assignment(4, False, 2) == "standard lane"