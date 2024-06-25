from fastapi import APIRouter
from schemas import words

router = APIRouter()


@router.post("/vowel_count")
async def vowel_count(request: words.VowelCount):
    vowel_count_dict = {}
    for word in request.words:
        vowel_count = 0
        for letter in word:
            if letter.lower() in ["a", "e", "i", "o", "u"]:
                vowel_count += 1
        vowel_count_dict[word] = vowel_count
    return vowel_count_dict


@router.post("/sort")
async def sort_words(request: words.WordsSort):
    return sorted(request.words)
