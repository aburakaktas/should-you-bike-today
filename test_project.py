from project import decide_result, Result
from weather import Weather

def test_decide_result():
    assert decide_result(23, "Clear", 12, "New York") == "Is it cycling weather in New York?\n- Yes! It is 23 degrees and weather type is: Clear.\nShould I care about wind?\n- Yes. Wind speed is 12 km/h."
    assert decide_result(13, "Rainy", 5, "Chicago") == "Is it cycling weather in Chicago?\n- No. It is 13 degrees and weather type is: Rainy.\nShould I care about wind?\n- No! Wind speed is 5 km/h."