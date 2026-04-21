from app.constants.mapping import LETTER_VALUES, MASTER_NUMBERS
from app.constants.meanings import NUMBER_MEANINGS
from app.schemas.numerology import LetterValue, NumerologyResponse
from app.utils.normalize import normalize_text
from app.utils.reduction import reduce_number


class NumerologyServiceError(Exception):
    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.message = message


class NumerologyService:
    def build_reading(self, text: str) -> NumerologyResponse:
        normalized = normalize_text(text)
        if not normalized:
            raise NumerologyServiceError("invalid_input_text", "Input must contain at least one valid letter.")

        letters = self.map_letters(normalized)
        total = self.calculate_sum([item.value for item in letters])
        reduced = reduce_number(total)
        return NumerologyResponse(
            input=text,
            normalized=normalized,
            letters=letters,
            sum=total,
            reduced=reduced,
            is_master=reduced in MASTER_NUMBERS,
            meaning=self.get_meaning(reduced),
        )

    def map_letters(self, text: str) -> list[LetterValue]:
        return [LetterValue(char=char, value=LETTER_VALUES[char]) for char in text]

    def calculate_sum(self, values: list[int]) -> int:
        return sum(values)

    def get_meaning(self, number: int) -> str:
        return NUMBER_MEANINGS[number]