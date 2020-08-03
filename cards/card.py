from typing import List, NamedTuple, Optional

import string

from cards.constants import IGNORE_TEXT, NOTE_DELIMETER


class Card(NamedTuple):
    kana: str
    romaji: str
    definition: str


def maybe_create_card(line: str) -> Optional[Card]:
    """
    Create a card if the input line satisfies the following conditions:
    * Line does not contain ignore text
    * Line contains expected number of delimeters separating romaji, kana, english

    We accept either of the following formats:
    1. かな - romaji - definition
    2. romaji - かな - definition
    """
    if any(ignore in line for ignore in IGNORE_TEXT):
        return
    if line.count(NOTE_DELIMETER) != 2:
        return

    w1, w2, definition = line.split(" - ")

    # Check for empty notes
    if not all([w1, w2, definition]):
        print(f"Blank note found, {w1, w2, definition}")
        return

    if w1[0] in string.ascii_lowercase:
        # First word is romaji
        romaji, kana = w1, w2
    else:
        # First word is kana
        kana, romaji = w1, w2

    return Card(kana, romaji, definition)


def filter_duplicate_kana(cards: List[Card]) -> List[Card]:
    seen_kana = set()
    filtered_list = []

    for card in cards:
        if card.kana in seen_kana:
            print(f"Found duplicate: {card}")
        else:
            filtered_list.append(card)
            seen_kana.add(card.kana)
    return filtered_list