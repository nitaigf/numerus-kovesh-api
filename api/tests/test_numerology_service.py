import pytest

from app.services.numerology_service import NumerologyService, NumerologyServiceError


def test_build_reading_for_nitai():
    service = NumerologyService()

    result = service.build_reading("NITAI")

    assert result.normalized == "NITAI"
    assert [item.value for item in result.letters] == [5, 9, 2, 1, 9]
    assert result.sum == 26
    assert result.reduced == 8
    assert result.is_master is False
    assert result.meaning == "Poder"


def test_build_reading_rejects_input_without_letters():
    service = NumerologyService()

    with pytest.raises(NumerologyServiceError) as exc_info:
        service.build_reading("123 !!!")

    assert exc_info.value.code == "invalid_input_text"