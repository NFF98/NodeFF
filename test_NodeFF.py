from pathlib import Path


def test_nodeff_contains_expected_value():
    value = Path("NodeFF").read_text(encoding="utf-8").strip()
    assert value == "98"
