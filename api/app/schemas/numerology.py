from pydantic import BaseModel, Field


class NumerologyRequest(BaseModel):
    text: str = Field(..., min_length=1, description="Nome de pessoa, empresa ou qualquer string.")


class LetterValue(BaseModel):
    char: str
    value: int


class NumerologyResponse(BaseModel):
    input: str
    normalized: str
    letters: list[LetterValue]
    sum: int
    reduced: int
    is_master: bool
    meaning: str