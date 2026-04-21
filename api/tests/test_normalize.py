from app.utils.normalize import normalize_text
from app.utils.reduction import reduce_number


def test_normalize_text_removes_accents_spaces_and_symbols():
    assert normalize_text("Nitai Embrás") == "NITAIEMBRAS"


def test_normalize_text_ignores_non_letters():
    assert normalize_text("A B-C_123") == "ABC"


def test_reduce_number_preserves_master_numbers():
    assert reduce_number(11) == 11
    assert reduce_number(22) == 22
    assert reduce_number(33) == 33


def test_reduce_number_reduces_until_single_digit():
    assert reduce_number(52) == 7