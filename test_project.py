from project import decide_result, extract_time, find_time_zone

def test_decide_result():
    assert decide_result(23, "Clear", 12, "New York") == "Is it cycling weather in New York?\n- Yes! It is 23 degrees and weather type is: Clear.\nShould I care about wind?\n- Yes. Wind speed is 12 km/h."
    assert decide_result(13, "Rainy", 5, "Chicago") == "Is it cycling weather in Chicago?\n- No. It is 13 degrees and weather type is: Rainy.\nShould I care about wind?\n- No! Wind speed is 5 km/h."
    
    
def test_extract_time():
    assert extract_time("2023-05-26 20:12:59.163581+02:00") == "20:12"
    assert extract_time("2023-05-26 19:27:22.828515+03:00") == "19:27"
    
    
def test_find_time_zone():
    assert find_time_zone(48, 11) == "Europe/Berlin"
    assert find_time_zone(35, 139) == "Asia/Tokyo"