from app.service import process_data

def test_process_data():
    data = [
        {"value": 10, "divider": 2},
        {"value": 20, "divider": 0},  # ❌ will cause crash
        {"value": 30, "divider": 3},
    ]

    result = process_data(data)
    assert result == 10


def test_empty_case():
    data = [
        {"value": 10, "divider": 0},
        {"value": 20, "divider": 0},
    ]

    result = process_data(data)
    assert result == 0
