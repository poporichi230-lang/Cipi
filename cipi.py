#!/usr/bin/env python3
"""Cipi — simple text analysis utilities."""

import re
import sys
from collections import Counter


def word_count(text: str) -> int:
    """Return the number of words in text."""
    return len(text.split())


def char_count(text: str, include_spaces: bool = True) -> int:
    """Return the number of characters in text."""
    if include_spaces:
        return len(text)
    return len(text.replace(" ", ""))


def sentence_count(text: str) -> int:
    """Return the number of sentences (split on . ! ?)."""
    sentences = re.split(r"[.!?]+", text)
    return len([s for s in sentences if s.strip()])


# TODO: implement word_frequency — return a Counter of how often each
# lowercased word appears in text, ignoring punctuation.
def word_frequency(text: str) -> Counter:
    words = re.findall(r"[a-zA-Z']+", text.lower())
    return Counter(words)


def summarise(text: str) -> dict:
    """Return a dict with basic stats about text."""
    freq = word_frequency(text)
    most_common = freq.most_common(5) if freq else []
    return {
        "words": word_count(text),
        "characters": char_count(text),
        "characters_no_spaces": char_count(text, include_spaces=False),
        "sentences": sentence_count(text),
        "unique_words": len(freq),
        "top_5_words": most_common,
    }


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: cipi.py <text | ->")
        print("  Pass - to read from stdin.")
        sys.exit(1)

    if sys.argv[1] == "-":
        text = sys.stdin.read()
    else:
        text = " ".join(sys.argv[1:])

    stats = summarise(text)
    print(f"Words            : {stats['words']}")
    print(f"Characters       : {stats['characters']}")
    print(f"Chars (no spaces): {stats['characters_no_spaces']}")
    print(f"Sentences        : {stats['sentences']}")
    print(f"Unique words     : {stats['unique_words']}")
    if stats["top_5_words"]:
        print("Top 5 words      :", ", ".join(f"{w}({n})" for w, n in stats["top_5_words"]))


if __name__ == "__main__":
    main()
