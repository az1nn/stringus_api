from pydantic import BaseModel


class VowelCount(BaseModel):
    words: list[str]


class WordsSort(BaseModel):
    words: list[str]
