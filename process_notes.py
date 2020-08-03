# Python 3
from typing import List

import csv
import fileinput
import string

from card import Card, maybe_create_card, filter_duplicate_kana


def make_cards() -> List[Card]:
    with open("nihongo_notes.txt", "rb") as notes_in:
        cards = [
            maybe_create_card(line.decode("utf-8"))
            for line in notes_in.read().splitlines()
        ]
        cards = filter_duplicate_kana(filter(None, cards))
        cards.sort(key=lambda x: x[0])
        return cards


def process_notes() -> None:
    cards = make_cards()
    with open("process_notes_out.tsv", "w", newline="", encoding="utf-8") as file_out:
        csv_out = csv.writer(file_out, delimiter="\t")
        for card in cards:
            csv_out.writerow(card)


if __name__ == "__main__":
    process_notes()
