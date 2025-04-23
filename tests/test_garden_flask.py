from garden.garden_flask import happy_earth_day

def test_index():
    expected = '<p>Happy Earth Day!</p>'
    out = happy_earth_day()
    assert expected == out
    