from lib.how_to import best_three, has_special_chars, is_valid_title
from lib.weather import is_valid_city
from lib.history import save_question, get_history, clear_history

LINES = [
    "how to boil an egg | Put the egg in boiling water.",
    "how to make tea | Boil water and add a tea bag.",
    "how to take a screenshot | Press Win + Shift + S.",
]


def test_best_three_finds_the_right_answer():
    answers = best_three("boil egg", LINES)
    assert answers[0][1] == LINES[0]


def test_best_three_returns_nothing_for_unknown_question():
    assert best_three("fly to the moon", LINES) == []


def test_has_special_chars():
    assert has_special_chars("how to?") is True
    assert has_special_chars("how to make tea") is False


def test_is_valid_title():
    assert is_valid_title("how to make coffee") is True
    assert is_valid_title("make coffee") is False


def test_is_valid_city():
    assert is_valid_city("New York") is True
    assert is_valid_city("L0nd0n!") is False


def test_history_save_and_clear(tmp_path):
    db = str(tmp_path / "test.db")
    save_question("boil egg", path=db)
    assert get_history(path=db)[0][0] == "boil egg"
    clear_history(path=db)
    assert get_history(path=db) == []
